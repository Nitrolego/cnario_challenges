# 🧪 Cnario Test Automation Framework (Playwright + Python)

This repository contains an automated end-to-end testing framework for **cnario.com** challenges, built using **Python** and **Playwright**.

---

## 📌 Tech Stack

- **Python 3.10+**
- **Playwright for Python**
- **Pytest**
- **Pytest-Playwright**

---

## Install Dependencies
```
pip install -r requirements.txt
playwright install
```

Key for tests:
LF = Login Flow
PLP = Product listing & pagination
PF = Profile filtering
SDL = Shadow DOM login
SSE = Simple Search Engine

---

## Running the Tests
Run all tests:
```
pytest
```

Run in headed mode:
```
pytest --headed
```

Run a specific test file:
```
pytest test_example.py
```