# NeurIPS Paper Processor

A Python pipeline for processing NeurIPS conference papers, including scraping, text extraction, and AI-based classification.

## Features
- **Web Scraping**: Downloads PDFs from NeurIPS proceedings
- **Text Extraction**: Extracts titles and abstracts from PDFs
- **AI Classification**: Classifies papers using Google's Gemini API

## Requirements
- Python 3.8+
- Required packages:
  - requests
  - beautifulsoup4
  - pdfplumber
  - pandas
  - tqdm
  - google-generativeai

## Usage

1. **Scrape Papers**:
   ```bash
   python scrapping.py
   ```

2. **Extract Text**:
   ```bash
   python convetingTocsv.py
   ```

3. **Classify Papers**:
   ```bash
   python LLM-model.py
   ```

## File Descriptions
- **scrapping.py**: Web crawler for downloading NeurIPS papers
- **convetingTocsv.py**: Extracts text from PDFs and saves to CSV
- **LLM-model.py**: Classifies papers using AI

## Output
- `extracted_papers.csv`: Contains paper titles and abstracts
- `annotated_papers.csv`: Contains classified papers with categories

## Notes
- Requires Google Gemini API key
- Configure max_downloads in scrapping.py to control number of papers downloaded
