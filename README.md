

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?style=flat&logo=streamlit)
![OpenAI](https://img.shields.io/badge/Powered%20by-GPT_API-orange?style=flat&logo=openai) 

 # 🚀 AI-Powered Coding Assistant

A smart, interactive coding environment built with **Python** and **Streamlit**. This application acts as your personal "Co-pilot," utilizing OpenAI's GPT models to generate, explain, and debug code in real-time within a syntax-highlighted editor.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Key Features

The application is organized into three intuitive workflows:

* **✨ Auto-Complete / Generate:** Describe your task in plain English (e.g., *"Create a Python function to check for palindromes"*), and the AI generates clean, ready-to-use code.
* **🧐 Explain Code:** Paste complex code snippets, and the AI will break down the logic step-by-step to help you understand it.
* **🐛 Debug & Fix:** Paste broken code along with an error message. The AI analyzes the issue, provides a corrected version, and explains the fix.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Code Editor:** [Streamlit-Ace](https://github.com/okld/streamlit-ace) (Monaco-style editor)
* **AI Model:** OpenAI API (GPT-4 / GPT-3.5)
* **Environment Mgmt:** Python Dotenv

## 📋 Prerequisites

* Python 3.8+
* An OpenAI API Key (See [OpenAI Platform](https://platform.openai.com/))

## ⚙️ Installation

1.  **Clone the repository** (if applicable):
    ```bash
    git clone [https://github.com/your-username/ai-coding-assistant.git](https://github.com/your-username/ai-coding-assistant.git)
    cd ai-coding-assistant
    ```

2.  **Install required dependencies:**
    ```bash
    pip install streamlit streamlit-ace openai python-dotenv
    ```

## 🔑 Configuration

You need an OpenAI API Key to run the AI features.

**Recommended Method (`.env` file):**
1.  Create a file named `.env` in the root folder.
2.  Add your key inside:
    ```text
    OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
    ```

**Alternative Method (UI):**
If no `.env` file is detected, the application will provide a secure input field in the sidebar to enter your key manually.

## 🚀 Usage

Run the application using Streamlit:

```bash
streamlit run app.py


