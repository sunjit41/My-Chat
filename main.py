from google import genai
from pydantic import BaseModel

# Automatically reads GEMINI_API_KEY from your environment
client = genai.Client()

# 1. Simple text generation
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain why Docker containers are useful for Python apps in 3 bullet points.",
)
print("--- Basic Response ---")
print(response.text)

# 2. Structured JSON output (Great for GitHub portfolios)
class ProjectIdea(BaseModel):
    title: str
    difficulty: str
    key_libraries: list[str]

structured_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Suggest one Python + AI portfolio project.",
    config={
        "response_mime_type": "application/json",
        "response_schema": ProjectIdea,
    },
)
print("\n--- Structured JSON Output ---")
print(structured_response.text)
