# report_analyzer.py
from config import load_gemini
from PyPDF2 import PdfReader
import io

def extract_text_from_pdf(pdf_path):
    """Extracts text content from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

def analyze_medical_report(pdf_path):
    """Analyzes a combined medical report using Gemini model."""
    model = load_gemini()
    extracted_text = extract_text_from_pdf(pdf_path)

    if not extracted_text:
        return "⚠️ Unable to extract text from the report. Please ensure it's a readable PDF."

    prompt = f"""
You are an experienced **AI Medical Report Analyst**.
You are given the text extracted from a patient's combined medical report.

Your task:
1. Identify key tests, parameters, and values mentioned.
2. Explain what each major test result indicates in simple, layman-friendly language.
3. If possible, infer potential health issues (e.g., high cholesterol, low hemoglobin, etc.).
4. Provide 3–5 personalized health recommendations or precautions based on the report.
5. Do not make any medical diagnosis or prescribe medications.

Here is the report text:
----------------------------------------
{extracted_text}
----------------------------------------

Now generate a well-structured and concise analysis under these headings:
- 🩺 Summary of Report
- 📊 Key Observations
- ⚠️ Possible Health Issues (if any)
- 💡 Recommendations & Precautions
"""

    response = model.generate_content(prompt)
    return response.text.strip()
