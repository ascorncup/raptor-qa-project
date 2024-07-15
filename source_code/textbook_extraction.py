import PyPDF2
import json
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

#processing the textbooks
def process_textbooks(textbook_paths):
    extracted_texts = {}
    for path in textbook_paths:
        book_name = Path(path).stem
        print(f"Extracting text from {book_name}...")
        extracted_texts[book_name] = extract_text_from_pdf(path)
    return extracted_texts

if __name__ == "__main__":
    textbook_paths = [
        '../textbooks/Introduction to Information Retrieval.pdf',
        '../textbooks/Natural Language Processing with Python.pdf',
        '../textbooks/Reinforcement Learning Introduction.pdf'
    ]

    extracted_texts = process_textbooks(textbook_paths)

    # Save extracted texts
    with open('extracted_texts.json', 'w') as f:
        json.dump(extracted_texts, f)

    print("Extraction complete. Texts saved to extracted_texts.json")