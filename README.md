# 🛡️ Docker-Based Hacking Lab

![Docker](https://img.shields.io/badge/Docker-🐳-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/herson/hackinglab?style=social)
![Docker Pulls](https://img.shields.io/docker/pulls/hersoncruz/hackinglab-kali?label=kali%20pulls)
![Docker Pulls](https://img.shields.io/docker/pulls/hersoncruz/hackinglab-dvwa?label=dvwa%20pulls)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)

A containerised security training environment for penetration testing, vulnerability research, and CTF practice. One `docker compose` command spins up 20+ tools and deliberately vulnerable applications in an isolated network — no host pollution, fully reproducible across machines.

**Landing page at `http://localhost:8080` lists every service with live status indicators.**

---

## Table of Contents

- [Quick Start](#quick-start)
- [Profiles](#profiles)
- [Services](#services)
- [Labs](#labs)
- [Contributing](#contributing)
- [Sponsoring](#sponsoring)
- [License](#license)

---

## Quick Start

**Prerequisites:** [Docker Desktop](https://docs.docker.com/get-docker/) (or Docker Engine + Compose plugin), Git.

```bash
git clone https://github.com/herson/hackinglab.git
cd hackinglab
cp .env.example .env

# Start everything
docker compose --profile full up -d

# Open the dashboard
open http://localhost:8080
```

---

## Profiles

Use profiles to start only the subset you need — helpful on machines with limited RAM.

| Profile | What starts | RAM (approx) |
|---|---|---|
| *(none)* | Landing page only | < 100 MB |
| `web-apps` | All vulnerable web applications | ~3 GB |
| `api` | All vulnerable APIs + crAPI infrastructure | ~2 GB |
| `scanners` | ZAP + OpenVAS | ~2 GB |
| `tools` | Kali, Metasploit, Nmap, Wireshark, Burp Suite | ~4 GB |
| `full` | Everything | ~8 GB |

```bash
# Web application targets only
docker compose --profile web-apps up -d

# API security targets only
docker compose --profile api up -d

# Mix profiles freely
docker compose --profile web-apps --profile api up -d

# Stop everything
docker compose --profile full down
```

---

## Services

### Landing Page

| Service | Port | URL |
|---|---|---|
| Homer Dashboard | 8080 | `http://localhost:8080` |

### Vulnerable Web Applications (`--profile web-apps`)

| Service | Port | URL | Covers |
|---|---|---|---|
| DVWA | 2580 | `http://localhost:2580` | SQLi, XSS, CSRF, File Upload, Command Injection |
| WebGoat | 2581 | `http://localhost:2581/WebGoat` | OWASP Top 10 interactive lessons |
| bWAPP | 2583 | `http://localhost:2583` | 100+ vulnerability categories |
| OWASP Juice Shop | 3000 | `http://localhost:3000` | OWASP Top 10, gamified challenges |
| Mutillidae II | 2584 | `http://localhost:2584` | Adjustable security levels |
| OWASP WrongSecrets | 2585 | `http://localhost:2585` | Secrets mismanagement |
| DVNA | 2586 | `http://localhost:2586` | Node.js-specific vulnerabilities |
| Vulnerable WordPress | 2587 | `http://localhost:2587` | CMS plugin/theme exploits |
| NodeGoat | 4000 | `http://localhost:4000` | Secure Node.js coding lessons |

### Vulnerable APIs (`--profile api`)

| Service | Port | URL | Covers |
|---|---|---|---|
| crAPI | 2590 | `http://localhost:2590` | OWASP API Security Top 10 |
| crAPI Mailbox | 2592 | `http://localhost:2592` | Email flows for crAPI |
| VAmPI | 6000 | `http://localhost:6000` | OWASP API Security Top 10 |
| Vulnerable API | 2500 | `http://localhost:2500` | Injection, auth bypass |

### Security Scanners (`--profile scanners`)

| Service | Port | URL |
|---|---|---|
| OWASP ZAP | 2582 | `http://localhost:2582` |
| OpenVAS | 9392 | `https://localhost:9392` |

### CLI / GUI Tools (`--profile tools`)

| Service | Access |
|---|---|
| Kali Linux | `docker compose --profile tools exec kali /bin/bash` |
| Metasploit | `docker compose --profile tools exec metasploit msfconsole` |
| Nmap | `docker compose --profile tools exec nmap nmap <target>` |
| Wireshark | X11 forwarding — `docker compose --profile tools exec wireshark wireshark` |
| Burp Suite | X11 forwarding — `docker compose --profile tools exec burpsuite burpsuite` |

---

## Labs

Step-by-step guided scenarios in the [`labs/`](./labs/) directory:

| Lab | Target | Topics |
|---|---|---|
| [01 — SQL Injection Fundamentals](./labs/01-sqli-dvwa.md) | DVWA | Union-based, blind, sqlmap, defence |
| [02 — API Security: OWASP API Top 10](./labs/02-api-owasp-top10-vampi.md) | VAmPI | BOLA, broken auth, mass assignment, function-level auth |
| [03 — Cross-Site Scripting](./labs/03-xss-juice-shop.md) | Juice Shop | DOM, reflected, stored XSS, filter bypass |

---

## Common Commands

```bash
# View logs for a specific service
docker compose logs -f dvwa

# Shell into a running container
docker compose --profile web-apps exec dvwa /bin/bash

# Rebuild a custom image after Dockerfile changes
docker compose --profile web-apps build dvwa
docker compose --profile web-apps up -d dvwa

# Stop and remove containers + volumes (full reset)
docker compose --profile full down -v
```

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to add a new service, write a lab scenario, or fix a bug.

Bug reports and feature requests: use the [issue templates](.github/ISSUE_TEMPLATE/).

---

## Sponsoring

If this lab saves you time or helps your learning, consider sponsoring:

- **GitHub Sponsors** — [github.com/sponsors/herson](https://github.com/sponsors/herson)
- **Ko-fi** — [ko-fi.com/herson](https://ko-fi.com/herson)
- **Buy Me a Coffee** — [buymeacoffee.com/herson](https://buymeacoffee.com/herson)
- **Crypto (OpenNode)** — [checkout.opennode.com/p/0871796a-f309-4e95-82c7-ec8e606e4c45](https://checkout.opennode.com/p/0871796a-f309-4e95-82c7-ec8e606e4c45)

Sponsor funds go towards maintaining images, writing new lab content, and keeping the project up to date with emerging vulnerability classes.

---

## License

MIT — see [LICENSE](./LICENSE).

**Disclaimer:** This lab is for educational purposes only. Always obtain proper written authorisation before testing any system you do not own.

---

**Herson Cruz** · [@hersoncruz](https://twitter.com/hersoncruz) · [github.com/herson/hackinglab](https://github.com/herson/hackinglab)
