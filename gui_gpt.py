import tkinter as tk
from tkinter import Menu
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load .env file for OpenAI key
load_dotenv()

# GPT-4o setup (you can switch back to "gpt-4o-mini" if needed)
model = ChatOpenAI(model="gpt-4o")

# Prompt template optimized for SQL-only answers
template = """
You are a SQL expert assistant.

If the user provides a database question and the table structure (schema) is either mentioned in the question itself or has been provided earlier, directly generate a clean, well-formatted MySQL SQL query.

schema can either be provided or you can assume the standard schema based on your knowledge from your experience and give soluton,

don't do very long greeting if required keep it short

Use self-joins where simpler than traditional joins.
Focus on accurate MySQL and PL/SQL syntax, and include window functions when helpful.
Never explain your output. Do not include any markdown, formatting, or prefix like 'sql:' or '```'.

Respond with the raw SQL query only.

{context}
User: {question}
SQL:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Notepad-style UI
class NotepadSQL:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        try:
            self.root.iconbitmap("notepad_icon.ico")
        except Exception:
            pass

        self.context = ""

        # Menubar
        menubar = Menu(self.root)
        menubar.add_command(label="File")
        menubar.add_command(label="Edit")
        menubar.add_command(label="View")
        self.root.config(menu=menubar)

        # Text area
        self.text_area = tk.Text(
            self.root, wrap=tk.WORD, font=("Consolas", 11),
            bg="white", fg="black", undo=True
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus()

        self.text_area.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        user_input = self.get_last_user_input()
        if user_input.strip() == "":
            return "break"
        
        self.text_area.insert(tk.END, "\n")

        self.context += f"User: {user_input}\n"
        response = chain.invoke({"context": self.context, "question": user_input})
        self.context += f"SQL: {response.content}\n"

        # Insert formatted response with prefix and spacing
        self.text_area.insert(tk.END, f": {response.content.strip()}\n\n")
        #self.text_area.insert(tk.END, "")  # Move cursor to blank new line
        self.text_area.see(tk.END)

        return "break"



    def get_last_user_input(self):
        all_text = self.text_area.get("1.0", tk.END).strip()
        lines = all_text.split("\n")
        for line in reversed(lines):
            if line.strip() and not line.strip().startswith(":"):
                return line
        return ""

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadSQL(root)
    root.mainloop()
