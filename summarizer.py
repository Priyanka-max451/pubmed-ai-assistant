from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def summarize_text(text):
    short_text = text[:800]

    prompt = f"""
    Summarize this medical abstract in 3-4 simple bullet points:

    {short_text}
    """

    return llm.invoke(prompt)


def answer_question(context, question):
    short_text = context[:800]

    prompt = f"""
    Based on this research abstract:

    {short_text}

    Answer clearly:
    {question}
    """

    return llm.invoke(prompt)