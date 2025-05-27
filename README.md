# 🌦️ Pytest Weather API Mock

This is a simple Python project that shows how to **mock external API calls** using [`pytest`](https://docs.pytest.org/) and `unittest.mock`. It simulates getting weather data from an API and covers various test cases like ✅ success, ❌ failure, and ⚠️ missing data.

---

## 📁 Project Structure
```bash
weather_project/
├── weather_api.py # Function that fetches weather data
├── test_weather_api.py # Tests using pytest and mock
```

---

## 🔧 What It Does

- Mocks a call to a weather API (`requests.get`)
- Handles:
  - ✅ Successful API response with temperature
  - ❌ Failed API response (like HTTP 404)
  - ⚠️ Response without temperature data

---

## ▶️ How to Run

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/pytest-weather-api-mock.git
cd pytest-weather-api-mock
```

2️⃣ Install dependencies
Make sure you have Python 3 installed. Then install pytest:
```bash
pip install pytest
```

---

## 🧪 Run the tests
```bash
pytest
```
You’ll see output showing the result of the 3 test cases.

---

## 📄 Sample Output
```bash
==================== test session starts ====================
platform win32 -- Python 3.10.3, pytest-8.3.5, pluggy-1.6.0
rootdir: C:\Users\ADITHYA\PycharmProjects\TestProject\pytest
collected 3 items                                                                                                                                                                   

weather_project\test_weather_api.py ...                                                                                                                                      [100%] 



===================== 3 passed in 0.03s =====================
```

---

## 📚 Learning Goals
Understand how to use unittest.mock.patch with requests

Learn how to test external APIs without making real network calls

Practice clean, isolated unit testing in Python 🧼

---

## 📜 License
This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

---

Made with 💻 and ☕ by Adithya
