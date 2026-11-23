# 🔐 File Integrity Monitoring System

A Python-based cybersecurity automation project that monitors file integrity using SHA-256 hashing and sends automated email alerts whenever a monitored file is modified.

## 📌 Overview

File Integrity Monitoring (FIM) helps identify unauthorized or unexpected changes to files.

This project automates file monitoring by periodically calculating the SHA-256 hash of a file and comparing it with its previously calculated hash.

If a modification is detected, an email notification is automatically sent.

## ✨ Features

- 🔍 Automated file monitoring
- 🔐 SHA-256 hash calculation
- 🚨 File modification detection
- 📧 Automated email notifications
- ⏱️ Continuous monitoring at 5-second intervals
- 🛡️ Secure Gmail SMTP connection using SSL

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| hashlib | SHA-256 hashing |
| smtplib | Email notifications |
| ssl | Secure email connection |
| csv | Credential management |
| time | Monitoring intervals |

## ⚙️ How It Works

1. The program calculates the initial SHA-256 hash of the monitored file.
2. It waits for 5 seconds.
3. It calculates the file's current hash.
4. It compares the current hash with the previous hash.
5. If the hashes differ, an email alert is sent.
6. The new hash becomes the reference for the next comparison.
7. The process continues until monitoring is stopped.

## 📂 Project Structure

```text
File-Integrity-Monitoring/
│
├── main.py
├── security.log
├── README.md
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd File-Integrity-Monitoring
```

### 3. Configure email credentials

Create a local `mailPass.csv` file containing:

```csv
your_email@gmail.com,your_g