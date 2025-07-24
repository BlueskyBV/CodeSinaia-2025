from smart_agent import SmartAgent
from index_notes import load_notes

# Load notes from your Obsidian vault (adjust path if needed)
notes_context = load_notes("./_Notes/0. Vineri - Setup")

smart_agent = SmartAgent("gemma3:1b", notes_context)

question = input("Enter your question: ").strip()
while question != "/pa":
    if question != "":
        answer_text = smart_agent.chat(question)
        print(answer_text)
    question = input("Enter your question: ").strip()

print(notes_context)