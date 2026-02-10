"""
CAT FULL AUTO DOWNLOADER (FINAL 2025 VERSION)
Python 3.11 compatible

Requirements:
    pip install python-docx requests pikepdf tqdm
"""

import re, requests
from pathlib import Path
from docx import Document
import pikepdf
from tqdm import tqdm

PASSWORD = "TIME@pdf"
DOCX_FILE = "CAT Study Material.docx"

ENCRYPTED = Path("encrypted_pdfs")
DECRYPTED = Path("decrypted_pdfs")
ENCRYPTED.mkdir(exist_ok=True)
DECRYPTED.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
}
COOKIES = {
    "hd_user_https": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}

print("\n🔍 STEP 1 — Extracting links from DOCX...")
doc = Document(DOCX_FILE)
text = "\n".join(p.text for p in doc.paragraphs)
links = re.findall(r"https?://[^\s)]+", text)
print(f"📌 {len(links)} links found.\n")


def fix_url(url):
    """Convert viewer stream → direct PDF"""
    if "viewerappp.php?file=" in url:
        return url.replace("viewerappp.php?file=", "")
    return url


def fetch_pdf(url, filepath):
    direct = fix_url(url)

    try:
        r = requests.get(direct, headers=HEADERS, cookies=COOKIES, stream=True, timeout=60)
        if r.status_code == 200 and "pdf" in r.headers.get("Content-Type", "").lower():
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(8192):
                    f.write(chunk)
            return True
    except:
        pass
    return False


print("📥 STEP 2 — Downloading PDFs...\n")
success = 0
fail = []

for url in tqdm(links):
    filename = fix_url(url).split("/")[-1].split("?")[0]
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    filepath = ENCRYPTED / filename

    if fetch_pdf(url, filepath):
        success += 1
    else:
        fail.append(url)

print(f"\n✔ Downloaded: {success}")
print(f"❌ Failed: {len(fail)}\n")


print("🔓 STEP 3 — Removing password from PDFs...")
decrypted = 0

for pdf in tqdm(sorted(ENCRYPTED.iterdir())):
    if pdf.suffix.lower() != ".pdf":
        continue
    out = DECRYPTED / pdf.name
    try:
        with pikepdf.open(pdf, password=PASSWORD) as p:
            p.save(out)
        decrypted += 1
    except:
        pass

print("\n🎯 SUMMARY")
print(f"🔹 Total links      : {len(links)}")
print(f"🔹 Downloaded       : {success}")
print(f"🔹 Decrypted        : {decrypted}")
print(f"\n📁 Locked PDFs   → {ENCRYPTED.resolve()}")
print(f"📁 Unlocked PDFs → {DECRYPTED.resolve()}")

if fail:
    print("\n⚠ Failed downloads:")
    for f in fail:
        print("  →", f)

print("\n✨ DONE — All PDFs downloaded and unlocked automatically!\n")
