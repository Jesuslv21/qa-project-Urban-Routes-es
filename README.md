# 🚕 Urban Routes – Web Test Automation Project

<img width="1536" height="1024" alt="ChatGPT Image 4 mar 2026, 06_45_04 p m" src="https://github.com/user-attachments/assets/b9a7a828-16f2-458f-9a38-07ad7ba5221e" />



## 📌 Project Overview

This repository contains the **Web Test Automation process** performed for Urban Routes, a ride-hailing web application.

The project automates a complete end-to-end user flow using **Selenium WebDriver** and **pytest**, validating core booking functionality and user interactions within the platform.

The main objective was to automate functional testing scenarios while applying structured test design principles and the Page Object Model (POM).

---

## 🎯 Project Goals

- Automate end-to-end ride booking flow  
- Validate UI elements and user interactions  
- Handle dynamic content using explicit waits  
- Integrate SMS code retrieval via API  
- Apply Page Object Model for maintainability  
- Execute structured automated tests using pytest  

---

## 🛠 Tech Stack

- **Language:** Python  
- **Automation Tool:** Selenium WebDriver  
- **Testing Framework:** pytest  
- **Design Pattern:** Page Object Model (POM)  
- **Browser:** Google Chrome  
- **Wait Strategy:** WebDriverWait (Explicit Waits)  

---

## 📁 Project Structure

```
qa-project-urban-routes/
│
├── data.py
├── retrieve_code.py
├── urban_routes_page.py
├── urban_routes_tests.py
└── README.md
```

---

## 🧪 Automated Test Flow

The automated script performs the following actions:

1. Set origin and destination addresses  
2. Select the **Comfort** fare  
3. Enter a phone number  
4. Retrieve and enter the SMS verification code  
5. Add a credit card  
6. Write a custom message to the driver  
7. Request blanket and tissues  
8. Order two ice creams  
9. Confirm the ride  
10. Wait until driver information appears  

This validates the complete booking workflow from start to confirmation.

---

## 🔎 Testing Approach

### 🧩 Page Object Model (POM)

- UI elements and methods are separated into `urban_routes_page.py`
- Improves readability and maintainability
- Encourages scalable automation structure

---

### ⏳ Explicit Wait Strategy

- Implemented using `WebDriverWait`
- Avoids unstable `time.sleep()` usage
- Handles dynamic loading elements properly

---

### 🔐 SMS Code Retrieval

- SMS verification code is retrieved using an API helper (`retrieve_code.py`)
- Enables fully automated authentication process

---

## ⚙️ Requirements

- Python 3.9+  
- Google Chrome installed  
- ChromeDriver (compatible with your Chrome version)  

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/qa-project-urban-routes.git
cd qa-project-urban-routes
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate   # Mac
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Tests

From the project directory:

```bash
pytest urban_routes_tests.py
```

Or run directly from PyCharm by right-clicking on:

```
urban_routes_tests.py → Run 'pytest in urban_routes_tests.py'
```

---

## ⚠️ Important Note

Make sure to update the base URL in `data.py` with the server-generated URL provided in the platform before running the tests.

If the URL is not updated, the automation script will not execute correctly.

---

## 📊 Results

- Complete ride booking flow automated  
- SMS verification integrated into automation  
- Dynamic content handled using explicit waits  
- Stable execution without hard-coded delays  
- Structured and maintainable test architecture  

---

## 🚀 Skills Demonstrated

- Web Automation with Selenium  
- End-to-End Test Automation  
- pytest Framework Usage  
- Page Object Model Implementation  
- Explicit Wait Handling  
- API Integration for Authentication  
- UI Element Interaction  
- Test Structure & Maintainability  

---

## 📌 Conclusion

This project demonstrates my ability to:

- Design and implement structured web automation  
- Automate complex user workflows  
- Apply scalable test architecture (POM)  
- Integrate API logic into UI automation  
- Deliver stable and maintainable automated tests  
