from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def summarize_text(text):
    short_text = text[:1500]  # limit size (VERY IMPORTANT)

    prompt = f"""
    Summarize this research abstract in 3-4 simple lines:
    {short_text}
    """

    return llm.invoke(prompt)
def answer_question(context, question):
    prompt = f"""
    You are a helpful medical assistant.

    Based on this research abstract:
    {context}

    Answer this question clearly:
    {question}

    Keep answer simple and precise.
    """

    return llm.invoke(prompt)