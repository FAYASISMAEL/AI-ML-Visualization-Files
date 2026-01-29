import cv2
import pytesseract
import os
import pandas as pd

image_folder = r"D:\MyWorks\python\1_BusinessCardNER\Selected"
data = []

for filename in os.listdir(image_folder):

    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(image_folder, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Failed to read image: {filename}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        data.append({
            "image_name": filename,
            "extracted_text": text.strip()
        })

    
df = pd.DataFrame(data)
print(df)
