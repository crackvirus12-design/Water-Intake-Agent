
# Water Intake Agent 💧

A portable Python-based personal water intake tracking agent designed to monitor daily hydration habits, send reminders, record user acknowledgements, and generate daily consumption reports.

## 🎯 Project Objectives

- Track water consumption between 6 AM and 7 PM.
- Send hourly water drinking reminders.
- Allow users to acknowledge consumption through Telegram.
- Record YES, NO, and missed acknowledgements.
- Store consumption history in SQLite.
- Generate daily water intake reports at 7 PM IST.
- Support Windows and Linux environments.
- Provide a modular and reusable architecture.

## 🏗️ Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Database | SQLite |
| Scheduler | APScheduler |
| Notifications | Telegram Bot API |
| Reporting | Python / HTML |
| Testing | Pytest |
| Version Control | GitHub |

## 📁 Project Architecture

```text
Water-Intake-Agent/
├── agent/
├── config/
├── data/
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
├── run.py
└── README.md
```

## 🚀 Development Roadmap

- [ ] Phase 1: Core agent and database foundation
- [ ] Phase 2: Telegram notifications and acknowledgements
- [ ] Phase 3: Daily reporting and analytics
- [ ] Phase 4: Windows and Linux deployment
- [ ] Phase 5: AI-powered hydration insights

## ⚙️ Supported Platforms

- Windows
- Linux
- macOS (planned)

## 🔐 Security

- Telegram credentials stored in environment variables.
- No credentials committed to GitHub.
- Local SQLite database for user consumption records.

## 📊 Reporting

The agent will generate a daily report containing:

- Total confirmed water consumption.
- Number of successful acknowledgements.
- Missed reminders.
- Explicit NO responses.
- Progress against daily intake target.

## 👨‍💻 Maintainer

crackvirus12-design

---

**Project Status:** Initial Development
