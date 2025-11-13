# 🌟 Step 1: Install required libraries
# Run this once in your terminal or notebook
# !pip install -U llama-index llama-index-llms-groq python-dotenv

# 🌟 Step 2: Import what we need
import os
from dotenv import load_dotenv  # To load environment variables from .env file
from llama_index.llms.groq import Groq        # To use Groq’s AI models
from llama_index.core import PromptTemplate   # To create and fill text templates

# 🌟 Step 3: Load API key securely
# Make sure you have a .env file with this line inside:
# GROQ_API_KEY=your_actual_groq_api_key
load_dotenv()

# Connect to the Groq LLM
llm = Groq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")   # ✅ Secure: reads from environment variable
)

# 🌟 Step 4: Define functions to ask questions

# --- Zero-Shot Prompting ---
def zero_shot_prompt(asked_question):
    """Ask the question directly (no examples given)."""
    template = PromptTemplate("Answer the following question clearly:\n{question}")
    final_prompt = template.format(question=asked_question)
    response = llm.complete(final_prompt)
    return response.text


# --- Few-Shot Prompting ---
def few_shot_prompt(asked_question):
    """Give 2–3 examples first to show how answers should look."""
    examples = """
    Q: What is machine learning?
    A: It is a field of AI where computers learn patterns from data.

    Q: What is a neural network?
    A: It is a group of connected algorithms that recognize patterns,
       similar to how the human brain works.
    """

    template = PromptTemplate("""
    Follow the same Q&A style shown in the examples below.

    {examples}

    Now answer the next question in the same short and clear format.
    Q: {question}
    A:
    """)

    final_prompt = template.format(examples=examples, question=asked_question)
    response = llm.complete(final_prompt)
    return response.text


# 🌟 Step 5: Try it out!
asked_question = "Explain what a Large Language Model is in simple terms."

print("🧠 Zero-shot answer:\n", zero_shot_prompt(asked_question))
print("\n🎯 Few-shot answer:\n", few_shot_prompt(asked_question))
