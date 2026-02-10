from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from docx import Document

START_PAGE = "https://www.time4education.com/my/cat25classvideohandouts-cls.php"

driver = webdriver.Chrome()
driver.get(START_PAGE)

print("\n🔐 Please LOGIN manually...")
input("➡ After login and when handouts page is fully visible, press ENTER here...\n")

time.sleep(5)

# Scroll so all elements load properly
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(4)

buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'View Material') or contains(text(),'View Solution')]")

print("🔗 Total links detected:", len(buttons))

doc = Document()
extracted = 0

for i, btn in enumerate(buttons):
    try:
        href = btn.get_attribute("href")
        if not href:
            continue
        
        # Open link in new tab to fetch final redirected URL
        driver.execute_script("window.open(arguments[0]);", href)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(4)

        final_url = driver.current_url
        print(f"{i+1}. {final_url}")
        doc.add_paragraph(final_url)
        extracted += 1

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        continue

doc.save("TIME_CAT_MATERIAL_LINKS.docx")
driver.quit()

print("\n📁 Saved to TIME_CAT_MATERIAL_LINKS.docx")
print(f"✨ Extraction completed. Total working URLs: {extracted}")
