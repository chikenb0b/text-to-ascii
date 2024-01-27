# stuff to import
from PIL import Image
import numpy as np

# Sets paramiters of the final ascii art
imageselection = input("What Image Would You Like to Use (Note: it theimage has to be in the same directory. And have the exact name (case sensitive)): ")
target_width = input("Wow Wide Would You Like Your Image to be: ")
target_width = int(target_width)
target_height = input("How Long Would You Like Your Image to be (Note: it should be a dividend number of the width of you image I like halfing the width): ")
target_height = int(target_height)

asciibright = (["@", "&", "#", "*", "+", "=", "-", ":", "<"])

# Open the image and convert it to grayscale
img = Image.open(imageselection).convert('L') # to change it put a image in the same folder as this and change the name to your file I have tried with .jpg and .png with no trouble

# Resize the image, specifying the target width and height
greyscaleimg = img.resize((target_width, target_height))

# Get the pixel values as an array
grayscaleimgdata = np.asarray(greyscaleimg)

# Create bins to cover the entire range of pixel values
bins = np.linspace(0, 256, len(asciibright) + 1)

# Digitize the image using the bins
grayscaleimgdatalist = np.digitize(grayscaleimgdata, bins)

# Map digitized values to ASCII characters
ascii_chars = np.array(asciibright)
ascii_img = ascii_chars[grayscaleimgdatalist - 1]  # Subtract 1 to match 0-based indexing

# Reshape the ASCII array to match the resized image size
ascii_img = ascii_img.reshape((target_height, target_width))

# Print the ASCII art
for row in ascii_img:
    print(''.join(row))