# 🍽️ AI Restaurant Name & Cuisine Suggester

An AI-powered Streamlit application that generates **creative restaurant names and menu items** using Groq + LangChain.

---

## 🚀 Features

* Generate unique restaurant names based on cuisine
* Automatically generate menu items
* Built using modern LangChain (LCEL)
* Interactive UI with Streamlit

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/adinits/RESTURANT_SUGGESTION.git
cd RESTURANT_SUGGESTION
```

---

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

1. Get your Groq API key:
   https://console.groq.com

2. Create file or Use Existing file secret_key_example.py by renaming it to secret_key.py:

```
src/restaurant_ai/secret_key.py
```

- Rename secret_key_example.py to secret_key.py and add your API key


3. Add:

```python
key_groq = "your_groq_api_key_here"
```

⚠️ Important:

* Do NOT commit this file
* Add to `.gitignore`

---

## ▶️ Run the Application

```bash
streamlit run /workspaces/RESTURANT_SUGGESTION/src/restaurant_ai/main.py
```

OR (recommended portable version):

```bash
streamlit run src/restaurant_ai/main.py
```

---

## 🌐 Open in browser

```
http://localhost:8501
```

---

## 📂 Project Structure

```
RESTURANT_SUGGESTION/
│── src/
│   └── restaurant_ai/
│       ├── __init__.py
│       ├── main.py
│       ├── generator.py
│       ├── secret_key.py  (not committed)
│
│── .venv/
│── requirements.txt
│── pyproject.toml
│── README.md
|── .gitignore
```

---

## ⚠️ Notes

* Uses **modern LangChain (no deprecated LLMChain)**
* Uses Groq models (fast inference)
* Ensure correct Python version (3.10+)

---

## 🙋‍♂️ Author

Aditya Chaudhary
GitHub: https://github.com/adinits

---

## ⭐ Acknowledgements

* Groq API
* LangChain
* Streamlit
