Space-Themed MidJourney Prompt Generator
This application uses a combination of Random Access Generation (RAG) and a pre-trained language model from NVIDIA to generate vivid and imaginative MidJourney prompts focused on sci-fi and space themes. Users can either provide their own input to guide the prompt creation or let the app use its RAG component to generate a prompt automatically.

How It Works
User Input or RAG: The app offers a simple interface where users can enter a short text to start the prompt generation process. If no input is provided, the app utilizes a RAG approach, selecting a random phrase from a predefined set of space-themed phrases stored in a text file (phrases.txt). These phrases serve as the starting point for generating creative and context-rich prompts.

Prompt Generation: The app uses the ChatNVIDIA model, specifically trained for generating high-quality text, to produce MidJourney prompts. The model is configured with specific parameters (e.g., temperature, top_p) to ensure that the generated prompts are creative, engaging, and aligned with the sci-fi and space theme.

Text Cleaning and Formatting: To maintain the quality of the output, the app includes a text-cleaning process that ensures the generated prompt is well-formatted and free of unnecessary spaces or improper word splits.

Streamlit Interface: The app is built with Streamlit, providing a user-friendly interface. Users can input text directly into the interface or simply click a button to generate a prompt based on the RAG component.

Features
Random Access Generation (RAG): Automatically generates space-themed prompts when no user input is provided, drawing inspiration from a list of predefined phrases.
NVIDIA-Powered LLM: Utilizes NVIDIA's ChatNVIDIA model for generating high-quality text, making use of advanced NLP techniques.
Sci-fi and Space Focused: All prompts are themed around sci-fi and space, ideal for users looking to create MidJourney prompts for imaginative and otherworldly scenes.
Simple and Interactive: Streamlit provides an easy-to-use interface where users can input their own text or generate a random prompt with a single click.
Usage
Enter a short piece of text to guide the prompt generation, or leave the input blank to let the app use its RAG component.
Click the "Generate Prompt" button to create a space-themed MidJourney prompt.
The generated prompt will appear on the screen, ready for use in creative projects.
Note
Ensure that you have set up the necessary API keys and environment variables for NVIDIA services before running the application. 
