import google.generativeai as genai

# Paste your Gemini API key here
GEMINI_API_KEY = "AIzaSyCTZepXxJVjR4MtfanqYhUroD8CCZh74eg"

def load_gemini():
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
    return model

