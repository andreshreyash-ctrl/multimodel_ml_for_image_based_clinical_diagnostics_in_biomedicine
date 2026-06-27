# Multimodal Medical AI — Initial Two Modules

## Overview
This project contains two initial modules:
1. AI Healthcare Chatbot (Gemini)
2. Smart Report Generator (upload multiple reports -> OCR -> Gemini summarization -> consolidated PDF)

## Setup (quick)
1. Copy `.env.example` to `.env` and set your `GENAI_API_KEY`.
2. Install system Tesseract:
   - Ubuntu: `sudo apt install -y tesseract-ocr`
   - Windows/Mac: install corresponding Tesseract binaries and ensure they are in PATH.
3. Create a virtualenv and install Python deps:
   - python -m venv venv
   - source venv/bin/activate # Linux/Mac
   - venv\Scripts\activate # Windows
   - pip install -r requirements.txt
4. Run the app:
   - streamlit run app.py


## Notes
- The `google-generativeai` SDK and model names may change; if Gemini calls fail, check the SDK quickstart and update `gemini_client.py`.
- For production use: add authentication, encryption for patient data, and proper logging and error handling.
