"""
Day 22 - Prompting: Clear Instructions First

Practice:
Write 3 versions of the same prompt:
1. Vague
2. Improved
3. Structured

Done When:
Reusable prompt template with goal, context,
constraints, and output format.
"""

# ----------------------------------------------------
# SAME TASK: Explain Python to a beginner
# ----------------------------------------------------

vague_prompt = """
Tell me about Python.
"""

improved_prompt = """
Explain Python programming for a beginner.
Include:
- Definition
- Main features
- Common use cases

Keep the answer under 150 words.
"""

structured_prompt = """
Goal:
Help a beginner understand Python.

Context:
The learner has no programming experience and is preparing
for a technical interview.

Constraints:
- Use simple language
- Maximum 150 words
- Include one real-world example
- Avoid advanced jargon

Output Format:
1. Definition
2. Key Features
3. Real-World Example
4. Summary
"""

print("========== VAGUE PROMPT ==========")
print(vague_prompt)

print("\n========== IMPROVED PROMPT ==========")
print(improved_prompt)

print("\n========== STRUCTURED PROMPT ==========")
print(structured_prompt)

# ----------------------------------------------------
# REUSABLE PROMPT TEMPLATE
# ----------------------------------------------------

reusable_template = """
Goal:
[What should the AI accomplish?]

Context:
[Background information]

Input:
[Data, question, or task]

Constraints:
- Length:
- Tone:
- Required points:
- Restrictions:

Output Format:
1.
2.
3.
4.
"""

print("\n========== REUSABLE TEMPLATE ==========")
print(reusable_template)