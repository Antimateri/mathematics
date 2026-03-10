from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image
import os

INPUT_PDF = "renderer.pdf"
OUTPUT_FOLDER = "rendered.webp"

def remove_background(image):

    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2RGBA)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

   # Detect dark pixels (background)
    threshold = 40
    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    # Set alpha channel
    img[:, :, 3] = mask

    out = Image.fromarray(img)
    w, h = out.size
    return out.crop((0, 0, w, h - 1))


# Convert PDF pages to images
page = convert_from_path(INPUT_PDF, dpi=300)[0]


processed = remove_background(page)

output_file = "rendered.webp"

processed.save(output_file)

print("Saved:", output_file)

print("Done!")