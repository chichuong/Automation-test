# 📘 DEMOQA Automation Tests

This project is an automated test suite for the [DEMOQA ](https://demoqa.com)

---

**Login**
**Logout**
**Search books** by keyword
**Verify** search results contain the keyword

---

---

## Tech Stack

- Python 3.8+
- Selenium
- Pytest
- WebDriver Manager
- Page Object Model (POM)

---

---

Create Virtual Environment

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

---

---

Install Dependencies
pip install -r requirements.txt

---

---

Running Tests
Test: Login & Logout
python -m pytest tests/test_login_logout.py -v

Test: Search Books
python -m pytest tests/test_search_book.py -v -s

---

---

Browser Setup
Default browser: Chrome
To switch to Firefox, change the value in conftest.py:
@pytest.fixture(params=["firefox"])

---
