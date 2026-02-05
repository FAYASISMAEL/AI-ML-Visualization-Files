import pandas as pd
import numpy as np
import re
import string

from collections import defaultdict
from pprint import pprint

FILE_PATH = "D:\\MyWorks\\python\\businessCard.txt"

# labels 
IGNORE_LABELS = {"tag"}

rows = []
with open(FILE_PATH, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) < 3:
            continue
        img, token, label = parts[0], parts[1], parts[-1]
        rows.append((img, token, label))

# tokens
grouped = defaultdict(list)
for img, token, label in rows:
    grouped[img].append((token, label))

# training data
TRAINING_DATA = []

for img, tokens in grouped.items():
    text = ""
    entities = []

    cursor = 0
    for token, label in tokens:
        if token == "O":
            continue

        if text and not text.endswith(" "):
            text += " "
            cursor += 1

        start = cursor
        text += token
        end = cursor + len(token)

        if label != "O":
            norm_label = re.sub(r'^[BI]-', '', label, flags=re.I).lower()
            if norm_label in IGNORE_LABELS:
                continue
            entities.append((start, end, label))

        cursor = end

    if entities:
        TRAINING_DATA.append(
            (text, {"entities": entities})
        )

pprint(TRAINING_DATA[:2])
