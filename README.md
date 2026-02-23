# 🧠 Moringa AI Capstone: FastAPI Beginner's Toolkit

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

## 📍 Overview

This repository contains a beginner-friendly toolkit for getting started with **FastAPI**. It was built as part of the Moringa AI Capstone Project to demonstrate how to leverage Generative AI for learning and scaffolding new backend technologies.

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints. This project bypasses the standard "Hello World" to provide a fully functional REST API endpoint demonstrating modern backend capabilities.

---

## 🚀 Features

- ✅ **Minimal Working API:** A functional `GET` endpoint returning JSON data.
- ⚡ **Lightning Fast:** Powered by Uvicorn (an ASGI web server).
- 📚 **Auto-Generated Documentation:** Out-of-the-box Swagger UI integration.

---

## 🛠️ System Requirements

- **OS:** Linux (Ubuntu/Debian recommended), macOS, or Windows (via WSL)
- **Python:** v3.8 or higher
- **Tools:** Terminal, VS Code (or preferred IDE)

---

## 💻 Installation & Setup

Follow these steps in your terminal to clone and run the project locally.

### 1️⃣ Clone the repository

````bash
git clone git@github.com:LARRYKIPKURUI/AI-project.git
cd fastapi-toolkit

## 2️⃣ Create and activate a virtual environment

It is best practice to isolate your Python dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
````

---

## 3️⃣ Install dependencies

Install FastAPI and the Uvicorn server:

```bash
pip install fastapi "uvicorn[standard]"
```

(Optional: If you add a `requirements.txt` later, you can run:)

```bash
pip install -r requirements.txt
```

---

## 🏃‍♂️ Running the API

Once your dependencies are installed and your virtual environment is active, start the development server:

```bash
uvicorn main:app --reload
```

### Explanation

- `main` → Refers to the `main.py` file.
- `app` → Refers to the FastAPI instance created inside `main.py` (`app = FastAPI()`).
- `--reload` → Makes the server restart automatically after code changes (useful for development).

---

## 🌐 Testing the API

### 🔹 Raw JSON Output

Open your web browser and navigate to:

```bash
http://127.0.0.1:8000
```

---

### 🔹 Interactive API Docs (Swagger UI)

FastAPI automatically generates an interactive documentation page. Navigate to:

```bash
http://127.0.0.1:8000/docs
```

Here, you can click **"Try it out"** and execute your endpoints directly from the browser without needing tools like Postman.

---

## 📁 Repository Structure

```plaintext
fastapi-toolkit/
├── main.py             # The main FastAPI application code
├── README.md           # Project documentation and setup guide
└── venv/               # Python virtual environment (ignored in git)
```

---

## 🤖 AI Prompt Journal (Summary)

This project was scaffolded using AI tools (`ai.moringaschool.com`). Key prompts used included:

### Scaffolding

> "Act as a senior backend engineer. Give me a step-by-step guide to initializing a FastAPI project in a Python virtual environment..."

### Development

> "How do I create a GET endpoint in FastAPI that returns a JSON list..."

(See the main Toolkit Document for full reflections and common errors encountered.)

---
