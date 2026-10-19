# Day18.py
# AI/ML Primer + Agentic AI Fundamentals Glossary

glossary = {
    "AI (Artificial Intelligence)": "Machines performing tasks that normally require human intelligence. Example: ChatGPT answering questions.",
    
    "ML (Machine Learning)": "A subset of AI where systems learn from data. Example: Email spam detection.",
    
    "LLM (Large Language Model)": "A model trained on large amounts of text to understand and generate language. Example: GPT-4.",
    
    "Agent": "An AI system that can make decisions and perform tasks. Example: An AI assistant that books meetings.",
    
    "Tool": "External functionality used by an agent. Example: A weather API used to fetch weather information.",
    
    "Memory/State": "Information retained during interactions. Example: Remembering a user's preferred language.",
    
    "Workflow": "A sequence of steps to complete a task. Example: Receive query → Search data → Generate response."
}

print("\n=== AI/ML & Agentic AI Glossary ===\n")

for term, definition in glossary.items():
    print(f"{term}")
    print(f"  {definition}\n")