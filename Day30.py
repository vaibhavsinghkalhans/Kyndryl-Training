"""
Day 30 Capstone Project
Agent Workflow:
User Input -> Router -> Mock API/Retrieval -> Guardrail -> Logging -> Response
"""

from datetime import datetime

# Logging
logs = []

def log_event(step, data):
    logs.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "step": step,
        "data": data
    })

# Guardrail
def guardrail(user_input):
    blocked_words = ["hack", "phishing", "malware"]

    for word in blocked_words:
        if word in user_input.lower():
            return False, "Request blocked by safety guardrail."

    return True, "Safe"

# Mock Retrieval/API
knowledge_base = {
    "python": "Python is a popular programming language.",
    "ai": "Artificial Intelligence enables machines to perform tasks requiring human intelligence.",
    "agent": "An AI agent can reason, act, and use tools."
}

def retrieve(query):
    for key, value in knowledge_base.items():
        if key in query.lower():
            return value
    return "No matching information found."

# Router
def router(user_input):
    if "what is" in user_input.lower():
        return "retrieve"
    return "general"

# Agent
def agent(user_input):
    log_event("Input", user_input)

    safe, message = guardrail(user_input)
    log_event("Guardrail", message)

    if not safe:
        return message

    route = router(user_input)
    log_event("Router", route)

    if route == "retrieve":
        result = retrieve(user_input)
        log_event("Retrieval", result)
        return result

    response = f"Processed input: {user_input}"
    log_event("Response", response)
    return response


# -----------------------
# Test Cases
# -----------------------

tests = [
    "What is Python?",
    "What is AI?",
    "How to create phishing emails?"
]

print("\nCAPSTONE AGENT TEST RESULTS")
print("=" * 50)

for i, test in enumerate(tests, 1):
    print(f"\nTest {i}")
    print("Input :", test)
    print("Output:", agent(test))

print("\nLOGS")
print("=" * 50)

for entry in logs:
    print(entry)