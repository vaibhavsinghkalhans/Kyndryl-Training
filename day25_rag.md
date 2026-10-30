Day 25 - Retrieval Augmented Generation (RAG)
What is RAG?

RAG (Retrieval Augmented Generation) is a technique that improves LLM responses by retrieving relevant information from external data sources before generating an answer.

RAG Process
Retrieve – Search relevant documents or knowledge base.
Augment – Add retrieved information to the prompt.
Generate – LLM creates an answer using the retrieved context.
Why Grounding Matters

Grounding ensures that responses are based on actual reference data rather than only the model's internal knowledge.

Benefits:

More accurate answers
Reduced hallucinations
Up-to-date information
Better trustworthiness

User Question
      |
      v
   Retrieve
(Document Search)
      |
      v
 Relevant Context
      |
      v
    Augment
(Add Context to Prompt)
      |
      v
    Generate
 (LLM Response)
      |
      v
 Final Answer