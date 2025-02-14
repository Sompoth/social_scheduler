import openai
import os

# Set OpenAI API Key (Replace with your actual API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_caption(topic: str) -> str:
    """Generate a catchy social media caption based on a topic."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Generate a catchy social media caption for the given topic."},
            {"role": "user", "content": topic}
        ]
    )
    return response["choices"][0]["message"]["content"]

def generate_image(prompt: str) -> str:
    """Generate an AI image using DALL·E based on user input."""
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    return response["data"][0]["url"]
