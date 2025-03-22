from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define prompt template for conversation
template = """
Answer the question below.

Here is the conversation history:
{context}

Question: {question}

Answer:
"""

# Load the local LLaMA3 model
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("SQL QUESTIONS\n")

    while True:
        user_input = input(": ")
        if user_input.strip().lower() == "exit":
            print(":::")
            break

        result = chain.invoke({"context": context, "question": user_input})
        print(f": {result}\n")

        # Update context for continuity
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
