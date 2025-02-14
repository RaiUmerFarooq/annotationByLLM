import os
import pdfplumber
import pandas as pd
import torch
from tqdm import tqdm

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")


pdf_folder = "NeurIPS_2024"

paper_data = []


def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            first_page = pdf.pages[0]
            return first_page.extract_text()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None


for pdf_file in tqdm(os.listdir(pdf_folder), desc="Extracting PDFs"):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)
        text = extract_text_from_pdf(pdf_path)
        
        if text:
            title = text.split("\n")[0]  # Assuming the title is the first line
            abstract = " ".join(text.split("\n")[1:])  # Rest as abstract
            
            paper_data.append({"Title": title, "Abstract": abstract, "File Name": pdf_file})

df = pd.DataFrame(paper_data)
df.to_csv("extracted_papers.csv", index=False)


from google.colab import files
files.download("extracted_papers.csv")

print("Extraction completed! Download 'extracted_papers.csv'.")
