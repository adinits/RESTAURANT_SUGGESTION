# 🍽️ AI Restaurant Name & Cuisine Suggester

This is my first AI-based project built from scratch using Python.
The application generates **creative restaurant names and cuisine suggestions** based on user input using the OpenAI API.

---

## 🚀 Features

* Generate unique and creative restaurant names
* Suggest relevant cuisines based on user ideas
* AI-powered recommendations using OpenAI API
* Simple and beginner-friendly Python implementation
* Environment variable support for secure API key usage

---

## 🛠️ Tech Stack

* Language: Python
* Libraries: OpenAI, dotenv
* Tools: VS Code, Git

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/RESTURANT_SUGGESTION.git
cd RESTURANT_SUGGESTION
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

1. Get your API key from OpenAI
2. Create a `.env` file in the root directory
3. Add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Never commit your `.env` file to GitHub.

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Example input:

```
Enter a theme: Indian street food
```

Example output:

```
Restaurant Name: Spice Junction
Cuisine: Indian Street Food
```

---

## 📂 Project Structure

```
project-folder/
│── app.py
│── requirements.txt
│── .env
│── README.md
```

---

## 🌱 Future Improvements

* Add a web interface using Flask or FastAPI
* Improve prompt engineering for better results
* Add multiple suggestions instead of one
* Deploy the project online

---

## 🙋‍♂️ Author

Aditya Chaudhary

* GitHub: https://github.com/adinits

---

## ⭐ Acknowledgements

* OpenAI for providing the API
* Built as part of my AI learning journey

