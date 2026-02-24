# Contributing to Hacking Lab

Thank you for helping improve this project. Contributions of all kinds are welcome — new services, lab write-ups, bug fixes, and documentation improvements.

---

## Ways to Contribute

| Type | Examples |
|---|---|
| **New service** | Add a vulnerable app or security tool to `docker-compose.yml` |
| **Lab write-up** | Add a step-by-step scenario to `labs/` |
| **Bug fix** | Fix a broken Dockerfile, broken port, or misconfigured service |
| **Documentation** | Improve the README or existing lab content |

---

## Getting Started

1. **Fork** the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/hackinglab.git
   cd hackinglab
   ```

2. **Create a branch** for your change:
   ```bash
   git checkout -b feature/add-webgoat-lab
   ```

3. **Test your change locally** before submitting:
   ```bash
   docker compose --profile <relevant-profile> up -d
   # Verify the service or lab works as described
   docker compose --profile <relevant-profile> down
   ```

4. **Commit** with a clear, imperative message:
   ```bash
   git commit -m "Add WebGoat XXE lab write-up"
   ```

5. **Open a pull request** against `main`.

---

## Adding a New Service

- Add the service definition to `docker-compose.yml` under the appropriate section (Web Apps, APIs, Tools, Scanners).
- Assign the correct profiles: `["<category>", "full"]`.
- Add an entry to the Homer dashboard in `homer/assets/config.yml`.
- Add a row to the services table in `README.md`.
- If the service requires a custom Dockerfile, create it in a subdirectory named after the service.

**Required for pull request acceptance:**
- Service starts cleanly with `docker compose --profile <profile> up -d`
- Service is accessible at the documented port within 60 seconds of startup
- No hardcoded secrets that are not already part of the upstream project's documented defaults

---

## Adding a Lab Write-Up

Labs live in `labs/` and follow this naming convention:

```
labs/<NN>-<short-slug>.md
```

Where `<NN>` is a zero-padded sequential number.

Each lab should include:
- The target service and its URL
- The Compose profile needed to start it
- Clear, numbered steps a beginner can follow
- An explanation of why each technique works
- A defence section summarising the correct fix

---

## Code Style

- YAML: 2-space indentation, double-quoted strings for environment values
- Markdown: ATX headings (`#`), fenced code blocks with language identifiers
- Dockerfile: one `RUN` layer per logical group; clean up package caches in the same layer

---

## Legal and Ethical Notice

All contributions must be for **educational and defensive purposes only**. Do not add:

- Real exploits or malware targeting production systems
- Backdoors, reverse shells, or C2 tooling beyond what is documented and containerised
- Content that facilitates illegal activity

By submitting a pull request you confirm that your contribution complies with the MIT License and this project's educational purpose.
