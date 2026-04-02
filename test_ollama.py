from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

response = llm.invoke("Explain AI in 2 lines")

print("OUTPUT:", response)