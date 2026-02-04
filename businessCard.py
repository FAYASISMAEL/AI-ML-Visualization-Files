import numpy as np
import pandas as pd
import string
import re

# Read text file
with open(r"D:\MyWorks\python\businessCard.txt", mode='r', encoding='utf-8', errors='ignore') as file:
    text = file.read()

# Convert text to DataFrame
data = [line.split('\t') for line in text.split('\n') if line.strip()]
df = pd.DataFrame(data[1:], columns=data[0])

# Cleaning setup
whitespace = string.whitespace
punctuation = '!#$%&\'()*+:;<=>?[\\]^`{|}~'

tableWhitespace = str.maketrans('', '', whitespace)
tablePunctuation = str.maketrans('', '', punctuation)

# Clean text function (FIXED)
def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.translate(tableWhitespace)
    text = text.translate(tablePunctuation)
    return text

# Apply cleaning
df['text'] = df['text'].apply(clean_text)

dataClean = df[df['text'] != ""]
dataClean.dropna(inplace=True)
# index adjustment
# dataClean.index = dataClean.index - 2

# Output
print(dataClean.head(10))
