# Study Material Auto Downloader 📚

Automates extraction, download, and password removal of study material PDFs from the a study portal.

## ✨ Features
- Extracts material links automatically after login
- Bulk PDF downloading
- Converts viewer links to direct PDFs
- Removes password protection
- Progress tracking with download summary

## 🛠 Tech Used
- Python
- Selenium
- Requests
- python-docx
- pikepdf
- tqdm

## ⚙ Installation

bash
pip install -r requirements.txt


---

## 📂 Project Structure


cat-study-material-downloader/

│
├── cat_auto_downloader.py # Main downloader & password remover

├── scrape_cat_links.py # Extracts links after login

├── links.txt # Optional sample list of URLs

├── requirements.txt

└── README.md

## 📁 Output Folders
encrypted_pdfs/   → original downloads
decrypted_pdfs/   → password removed PDFs


## 🎯 Learning Outcomes

This project demonstrates:

Web automation

Authenticated scraping

Handling redirects

File downloading & streaming

PDF security processing

End-to-end workflow automation

## 👩‍💻 Author 

Tanvi Utreja
B.Tech Student
