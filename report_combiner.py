from PyPDF2 import PdfMerger
from PIL import Image
import tempfile
import os

def combine_reports(uploaded_files):
    """
    Combines multiple uploaded PDFs and images into a single PDF.
    """
    temp_dir = tempfile.mkdtemp()
    pdf_paths = []

    # Convert all files to PDF (if not already)
    for file in uploaded_files:
        file_ext = file.name.lower().split(".")[-1]
        temp_pdf = os.path.join(temp_dir, f"{os.path.splitext(file.name)[0]}.pdf")

        if file_ext in ["jpg", "jpeg", "png"]:
            image = Image.open(file).convert("RGB")
            image.save(temp_pdf)
        elif file_ext == "pdf":
            temp_pdf = os.path.join(temp_dir, file.name)
            with open(temp_pdf, "wb") as f:
                f.write(file.read())
        else:
            continue

        pdf_paths.append(temp_pdf)

    # Merge all PDFs into one
    merger = PdfMerger()
    for pdf in pdf_paths:
        merger.append(pdf)

    output_pdf = os.path.join(temp_dir, "combined_report.pdf")
    merger.write(output_pdf)
    merger.close()

    return output_pdf
