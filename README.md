# GPT-4o with Notepad UI 📝

This is a lightweight Notepad-style desktop app built with Python, `tkinter`, and OpenAI's GPT-4o model — designed specifically for generating **MySQL/PL-SQL queries** using natural language input.

> ✨ Looks and behaves like Windows Notepad — but secretly powered by AI.

---

## 🔧 Features

- Notepad-like UI with a minimal Windows-style design  
- Converts plain English into accurate MySQL queries  
- Supports self-joins, PL/SQL, window functions, and best practices  
- Powered by OpenAI GPT-4o using secure `.env` file  
- Outputs only SQL — no comments, markdown, or extra fluff  

---

## 🖼️ Preview

![image](https://github.com/user-attachments/assets/562c79f0-1639-4780-9ce1-38d76d421a8d)

---

## 🚀 Setup Instructions

1. **Clone the repository**

git clone https://github.com/PEPESHANTY/GPT-4-with-Notepad-UI.git
cd GPT-4-with-Notepad-UI
```

2. **Create and activate a virtual environment (Windows)**

python -m venv chatbot
chatbot\Scripts\activate
```

3. **Install required dependencies**


pip install -r requirements.txt
```

4. **Create a `.env` file in the project root**

```env
OPENAI_API_KEY="your-api-key"
```

5. **Run the application**

python gui_gpt.py
```

---

## 📁 Project Structure

| File               | Purpose                                  |
|--------------------|------------------------------------------|
| `gui_gpt.py`       | Main GUI code using `tkinter`            |
| `main.py`          | Terminal-based fallback chatbot          |
| `.env`             | Store your OpenAI key (not committed)    |
| `.gitignore`       | Ensures `.env` and other files are safe  |
| `launch_notepad.bat` | Windows desktop launcher (optional)     |
| `notepad_icon.ico` | Icon used for desktop Notepad styling    |

---


## 🙌 Author

Created with ❤️ by [Shantanu Bhute](https://github.com/PEPESHANTY)

---

## 📜 License

This project is licensed under the MIT License.
