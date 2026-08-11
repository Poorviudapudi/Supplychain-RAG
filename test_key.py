import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
key = os.environ.get("OPENAI_API_KEY")
print(f"Loaded key starts with: {key[:14] if key else 'None'}")

try:
    model = ChatOpenAI(model="gpt-4o", temperature=0)
    res = model.invoke("say hi")
    print("OpenAI connection successful! Response:", res.content)
except Exception as e:
    print("Error connecting to OpenAI:", e)
