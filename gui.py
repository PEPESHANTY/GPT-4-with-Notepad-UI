import tkinter as tk
from tkinter import Menu
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Setup prompt and model
template = """
{context}
User: {question}
AI:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# GUI
class NotepadClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Set Notepad icon
        try:
            self.root.iconbitmap("notepad_icon.ico")
        except Exception as e:
            print("Icon not set:", e)

        self.context = ""

        # Add Menu bar (File, Edit, View)
        menubar = Menu(self.root)
        menubar.add_command(label="File")
        menubar.add_command(label="Edit")
        menubar.add_command(label="View")
        self.root.config(menu=menubar)

        # Editable area like Notepad
        self.text_area = tk.Text(
            self.root, wrap=tk.WORD, font=("Consolas", 11), bg="white", fg="black", undo=True
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus()

        self.text_area.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        event.widget.mark_set("insert", "insert-1c")
        last_input = self.get_last_user_input()
        if last_input.strip() == "":
            return "break"

        self.context += f"User: {last_input}\n"
        response = chain.invoke({"context": self.context, "question": last_input})
        self.context += f": {response}\n"
        self.text_area.insert(tk.END, f"\nAI: {response}\n")
        self.text_area.see(tk.END)
        return "break"

    def get_last_user_input(self):
        all_text = self.text_area.get("1.0", tk.END).strip()
        lines = all_text.split("\n")
        return lines[-1] if lines else ""

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadClone(root)
    root.mainloop()
