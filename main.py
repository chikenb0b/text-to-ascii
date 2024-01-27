from PIL import Image
import numpy as np

asciibright = (["@", "&", "#", "*", "+", "=", "-", ":", "<"])
# Open the image and convert it to grayscale
img = Image.open('Meatball.JPG').convert('L') # to change it put a image in the same folder as this and change the name to your file I have tried with .jpg and .png with no trouble

# Set the target width and height
target_width = 150
target_height = 75

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