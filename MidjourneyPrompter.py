import random
import os
import re
import streamlit as st
from langchain_nvidia_ai_endpoints import ChatNVIDIA

# Set environmental variables

os.environ["NVIDIA_API_KEY"] = "YOUR_NVIDIA_API_KEY"
nvidia_api_key = os.environ["NVIDIA_API_KEY"]

# Initialize ChatNVIDIA for text generation
client = ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",
    api_key=nvidia_api_key,
    temperature=0.5,
    top_p=0.85,
    max_tokens=80
)

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
phrases_file = os.path.join(script_dir, "phrases.txt")

# Read phrases from the text file
with open(phrases_file, "r") as f:
    lines = f.readlines()

def clean_response(response_text):
    # Join the response list into a single string
    response_end = " ".join(response_text).strip()

    # Replace multiple spaces with a single space
    response_end = re.sub(r'\s+', ' ', response_end)  # Collapses multiple spaces into one

    # Attempt to fix improper word splitting only
    # This regex finds single-letter space single-letter cases more precisely and joins them
    response_end = re.sub(r'(\b\w)\s+(\w\b)', r'\1\2', response_end, flags=re.UNICODE)

    response_end = re.sub(r'\s*([,.!?])\s*', r'\1 ', response_end)

    # Remove any extraneous newlines or extra spaces left over
    response_end = response_end.replace("\n", " ").replace("  ", " ")

    # Trim any leading or trailing spaces
    response_end = response_end.strip()
    
    return response_text

def generate(starting_text):
    for count in range(6):
        seed = random.randint(100, 1000000)
        random.seed(seed)
    
        # If the text field is empty
        if starting_text == "":
            starting_text = lines[random.randrange(0, len(lines))].strip()
            starting_text = re.sub(r"[,:\-–.!;?_]", '', starting_text)
    
        # Format messages for the client
        messages = [
            {"role": "system", "content": "Create a vivid and imaginative MidJourney prompt for image generation. Focus on descriptive language, colors, and setting to evoke a specific visual scene. Avoid storytelling; focus on visual elements."},
            {"role": "user", "content": starting_text}
        ]

        # Stream response from LLaMA
        response = client.stream(messages)

        # Buffer to accumulate response chunks
        buffer = []
        for chunk in response:
            if chunk.content:
                resp = chunk.content.strip()
                if resp != starting_text:
                    buffer.append(resp)

        # Join the buffered chunks into a single string
        response_text = " ".join(buffer).strip()

        # Clean up the response text
        response_end = clean_response(response_text)

        # Print only the final response if it's not empty
        if response_end != "":
            return response_end

# Streamlit UI
st.title("Generate Sci-fi/Space-themed MidJourney Prompts")

user_input = st.text_input("Enter a short text or just press 'Generate Prompt' to use our space-themed RAG to get space-themed prompt:")

if st.button("Generate Prompt"):
    generated_prompt = generate(user_input)
    st.write("**MidJourney Prompt:**")
    st.write(generated_prompt)