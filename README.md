# 🛡️ Docker-Based Hacking Lab 🛡️

![Docker](https://img.shields.io/badge/Docker-🐳-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/herson/hackinglab?style=social)

Welcome to the **Docker-Based Hacking Lab**! This repository offers a comprehensive, containerized environment tailored for penetration testing, vulnerability assessment, and security research. Utilizing Docker Compose, this lab integrates a suite of essential security tools, ensuring an isolated and reproducible setup suitable for both beginners and seasoned professionals.

---

## 📜 Table of Contents

- [🛡️ Docker-Based Hacking Lab 🛡️](#-docker-based-hacking-lab-)
  - [📜 Table of Contents](#-table-of-contents)
  - [🔍 Overview](#-overview)
  - [🚀 Features](#-features)
  - [🛠️ Prerequisites](#️-prerequisites)
  - [⚙️ Installation](#️-installation)
  - [📦 Services Included](#-services-included)
    - [🖥️ Kali Linux](#️-kali-linux)
    - [🔴 Metasploit](#-metasploit)
    - [🕵️‍♂️ Nmap](#️-nmap)
    - [📡 Wireshark](#-wireshark)
    - [🕷️ OWASP ZAP](#️-owasp-zap)
    - [💀 DVWA (Damn Vulnerable Web Application)](#-dvwa-damn-vulnerable-web-application)
    - [🔰 WebGoat](#️-webgoat)
    - [🦠 bWAPP](#-bwapp)
    - [🛡️ Vulnerable API](#️-vulnerable-api)
  - [📈 Usage](#️-usage)
  - [🌐 Accessing the Services](#-accessing-the-services)
  - [🤝 Contributing](#-contributing)
  - [📄 License](#-license)
  - [📫 Contact](#-contact)

---

## 🔍 Overview

The **Docker-Based Hacking Lab** is engineered to provide a versatile and secure environment for security enthusiasts to practice and enhance their skills. By containerizing each tool, the lab ensures that your host system remains unaffected, offering a safe playground for testing various security scenarios.

---

## 🚀 Features

- **Isolated Environment:** Each tool operates in its own container, preventing conflicts and ensuring system integrity.
- **Scalable Setup:** Easily add or remove services as your needs evolve.
- **Reproducible Builds:** Docker Compose guarantees consistent environments across different machines.
- **Comprehensive Toolset:** Integrates industry-standard tools for a holistic security assessment experience.
- **Cross-Platform Compatibility:** Supports both `linux/amd64` and `linux/arm64/v8` architectures with platform specifications.

---

## 🛠️ Prerequisites

Before setting up the hacking lab, ensure you have the following installed on your system:

- **Docker:** [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose:** [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Git:** [Install Git](https://git-scm.com/downloads)

*Ensure Docker is running and you have the necessary permissions to execute Docker commands.*

---

## ⚙️ Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/herson/hackinglab.git
   cd hackinglab
   ```

2. **Configure Environment Variables:**

   Create a `.env` file in the project root to define any necessary environment variables.

   ```bash
   cp .env.example .env
   nano .env
   ```

   *Adjust the variables as needed.*

3. **Build and Deploy the Containers:**

   ```bash
   docker compose up --build -d
   ```

   *This command builds the Docker images and starts the containers in detached mode.*

---

## 📦 Services Included

### 🖥️ Kali Linux

**Description:** A Debian-based Linux distribution crafted for digital forensics and penetration testing.

**Features:**

- Comprehensive suite of security tools
- Customizable environment for various testing scenarios

### 🔴 Metasploit

**Description:** An advanced open-source platform for developing, testing, and executing exploit code against remote targets.

**Features:**

- Extensive exploit database
- Supports a wide range of payloads
- Integration with other security tools

### 🕵️‍♂️ Nmap

**Description:** A network scanning tool used to discover hosts and services on a computer network.

**Features:**

- Host discovery
- Port scanning
- OS detection
- Scripting engine for automation

### 📡 Wireshark

**Description:** A network protocol analyzer that lets you capture and interactively browse the traffic running on a computer network.

**Features:**

- Deep inspection of hundreds of protocols
- Live capture and offline analysis
- Rich display filters

### 🕷️ OWASP ZAP

**Description:** An open-source web application security scanner, ideal for finding vulnerabilities in web applications.

**Features:**

- Automated scanners
- Passive and active scanning
- Integration with CI/CD pipelines

### 💀 DVWA (Damn Vulnerable Web Application)

**Description:** A PHP/MySQL web application that is damn vulnerable, designed for security training.

**Features:**

- Multiple vulnerability levels
- Simulates real-world attack scenarios
- Educational purpose for learning web vulnerabilities

### 🔰 WebGoat

**Description:** A deliberately insecure application maintained by OWASP designed to teach web application security lessons.

**Features:**

- Interactive lessons on various vulnerabilities
- Supports multiple attack vectors
- Community-driven content

### 🦠 bWAPP

**Description:** A free and open-source deliberately insecure web application for security training.

**Features:**

- Over 100 web vulnerabilities
- Compatible with multiple platforms
- Regular updates with new vulnerabilities

### 🛡️ Vulnerable API

**Description:** A sample API designed with intentional vulnerabilities for practicing API security testing.

**Features:**

- Common API vulnerabilities like SQL Injection, XSS, etc.
- RESTful endpoints for testing
- Educational purpose for API security

---

## 📈 Usage

1. **Start All Services:**

   ```bash
   docker compose up -d
   ```

2. **Stop All Services:**

   ```bash
   docker compose down
   ```

3. **View Logs:**

   ```bash
   docker compose logs -f
   ```

4. **Access a Specific Service:**

   ```bash
   docker compose exec <service_name> /bin/bash
   ```

   *Replace `<service_name>` with the name of the service (e.g., `kali`, `metasploit`).*

---

## 🌐 Accessing the Services

| **Service**          | **Port Mapping** | **URL**                                      |
|----------------------|------------------|----------------------------------------------|
| **Kali Linux**       | N/A              | Access via Docker CLI or SSH                 |
| **Metasploit**       | 2588:80          | `http://localhost:2588` (if web interface)    |
| **Nmap**             | 2582:8080        | Use CLI tools within the container           |
| **Wireshark**        | 2584:80          | `http://localhost:2584`                       |
| **OWASP ZAP**        | 2582:8080        | `http://localhost:2582`                       |
| **DVWA**             | 2580:80          | `http://localhost:2580`                       |
| **WebGoat**          | 2581:8080        | `http://localhost:2581`                       |
| **bWAPP**            | 2583:80          | `http://localhost:2583`                       |
| **Vulnerable API**   | 2500:5000        | `http://localhost:2500`                       |

*Ensure that the ports are not being used by other services on your host machine.*

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork the Project**
2. **Create Your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📫 Contact

**Herson Cruz** – [@hersoncruz](https://twitter.com/hersoncruz)

Project Link: [https://github.com/herson/hackinglab](https://github.com/herson/hackinglab)

---

## 🔗 Useful Links

- **Docker Documentation:** [https://docs.docker.com/](https://docs.docker.com/)
- **Docker Compose Documentation:** [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- **OWASP ZAP:** [https://www.zaproxy.org/](https://www.zaproxy.org/)
- **Metasploit Framework:** [https://metasploit.help.rapid7.com/](https://metasploit.help.rapid7.com/)
- **DVWA:** [http://www.dvwa.co.uk/](http://www.dvwa.co.uk/)
- **WebGoat:** [https://owasp.org/www-project-webgoat/](https://owasp.org/www-project-webgoat/)
- **bWAPP:** [http://www.itsecgames.com/](http://www.itsecgames.com/)
- **Nmap:** [https://nmap.org/](https://nmap.org/)
- **Wireshark:** [https://www.wireshark.org/](https://www.wireshark.org/)

---

## 💡 Tips & Tricks

- **Persisting Data:** Ensure that important data is persisted using Docker volumes to prevent data loss upon container restarts.
- **Security Best Practices:** Regularly update your Docker images to incorporate the latest security patches.
- **Resource Management:** Monitor container resource usage to ensure optimal performance of your host machine.
- **Networking:** Leverage Docker networks to simulate complex network topologies for advanced testing scenarios.

---

> **Disclaimer:** This hacking lab is intended for educational purposes only. Ensure you have proper authorization before conducting any security assessments or penetration testing on systems you do not own.