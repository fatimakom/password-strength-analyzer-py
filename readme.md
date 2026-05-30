# 🔐 Password Strength Analyzer

> A cybersecurity tool that analyzes how strong your password is — built with Python & vanilla HTML/JS.

---

## ✨ Features

- 🔍 Real-time password strength analysis
- 📊 Score from 0 to 100 with visual bar
- ⏱️ Estimated crack time (based on 10 billion guesses/second)
- 🧮 Entropy calculation (how unpredictable your password is)
- ✅ 10 security checks (length, uppercase, symbols, sequences...)
- 💡 Smart suggestions to improve your password
- ✨ Strong password generator built in
- 📋 Copy to clipboard in one click
- 🖥️ Terminal (CLI) version + 🌐 Web version

---

## 📸 Preview

| Web App | Terminal |
|---|---|
| Beautiful real-time UI with score bar and checks | Clean CLI with color indicators |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/password-analyzer.git
cd password-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the CLI app

```bash
python password_analyzer.py
```

### 4. Run the Web app

Just open `index.html` in your browser — no server needed!

---

## 🗂️ Project Structure

```
password-analyzer/
├── password_analyzer.py   # Python CLI app
├── index.html             # Web app (HTML + CSS + JS)
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

---

## 🔍 How the Score Works

| Score | Strength |
|---|---|
| 0 – 39 | ❌ Weak |
| 40 – 59 | ⚠️ Fair |
| 60 – 79 | ✅ Strong |
| 80 – 100 | 💪 Very Strong |

---

## ✅ The 10 Security Checks

| Check | What it means |
|---|---|
| 8+ characters | Minimum safe length |
| 12+ characters | Recommended length |
| Uppercase letters | A-Z present |
| Lowercase letters | a-z present |
| Numbers | 0-9 present |
| Special characters | !@#$%... present |
| Not a common password | Not in top 1000 weak passwords |
| No repeated characters | No "aaa" or "111" |
| No sequential characters | No "abc" or "123" |
| 3+ character types | Good variety |

---

## 🧮 What is Entropy?

Entropy measures how unpredictable your password is, in bits.

```
Entropy = password_length × log2(charset_size)
```

| Entropy | Security Level |
|---|---|
| Below 28 bits | Very weak |
| 28 – 35 bits | Weak |
| 36 – 59 bits | Reasonable |
| 60+ bits | Strong |
| 128+ bits | Very strong |

---

## ⏱️ Crack Time Explained

The crack time is calculated assuming an attacker uses a modern GPU capable of **10 billion guesses per second** — the industry standard for threat modeling.

```
combinations = charset_size ^ password_length
crack_time   = combinations / 10,000,000,000
```

---

## 🛠️ Tech Stack

- **Python 3.10+** — CLI version
- **Vanilla HTML / CSS / JS** — Web version (no frameworks)
- No external APIs needed — 100% offline

---

## 💡 Tips for a Strong Password

- Use **16+ characters**
- Mix uppercase, lowercase, numbers, and symbols
- Never use your name, birthday, or common words
- Use a **passphrase**: `Horse$Battery!Staple99`
- Never reuse passwords across websites
- Use a password manager (Bitwarden, 1Password)

---

## 🙋 Author

Built by **Fatima Koumayha** — junior developer passionate about cybersecurity.

- GitHub: [@fatima koumayha](https://github.com/fatimakom/password-strength-analyzer-py.git)
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

---
## App Preview

![Preview](assets/screenshots/app-preview.png)

## Live Demo

https://password-check-app.netlify.app/

## 📄 License

MIT — free to use and modify.