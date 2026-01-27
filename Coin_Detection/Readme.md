🪙 Project: Coin Diameter Measurement Using OpenCV Only

🎯 What This Project Does
Uses camera to scan coins
Detects multiple coins
Measures diameter in real-world units (mm)
Displays diameter on live video

📌 Uses one reference coin with known diameter.

📁 Folder Structure
coin_diameter_opencv/
│
└── main.py

🧠 Core Technique Used
Task	                     Method
Coin detection	             Hough Circle Transform
Measurement	                 Pixel → mm scaling
Camera	                     OpenCV
Language	                 Python

📌 Important Notes (Explain in Viva)
1. Exact measurement requires a reference object
2. Camera must be perpendicular to surface
3. Lighting must be uniform
4. First detected coin is used as reference

🎓 What to Say in Viva (Short)
This project detects coins using the Hough Circle Transform, measures their diameters in pixels, converts them to millimeters using a known reference coin, and displays the real-world size in real time.

🚀 Possible Improvements (Bonus)
Automatic reference coin detection
Noise reduction using adaptive threshold
Perspective correction
Coin classification (₹1, ₹5, ₹10)
Batch image processing

<!-- If you want, I can:
Improve accuracy
Add coin classification
Prepare project report + PPT
Convert this to industrial-grade demo
Just tell me 👍 -->