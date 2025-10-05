#lib
import google.generativeai as genai
import os
# generator_gemini
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-001")

def generate_answer(query: str, context_chunks: list) -> str:
    context = "\n\n".join(context_chunks)
    prompt = f"""
You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question: {query}
Answer:
"""
    response = model.generate_content(prompt)
    return response.text
