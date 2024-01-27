# text to ascii
 it converts images to ascii charecters


# whats needed
 this project requires numpy & pillow

 # how to use
Maybe in a bit I will make it eaiser to use. But what you do is you put your images that you want to convert in the same directory as main.py, then you go in main.py and you change the line: img = Image.open('Meatball.JPG').convert('L') to img = Image.open('example.jpg').convert('L') execpt you change example to what ever image you want

# compatibility
It works with .jpg and .png. But it might support more but I dont know

# how to change the resolution
you change line's 9 and 10 from 150 and 75 to what ever value you want. the bigger the more "pixels" (charecters) it will have but at a certain point it might become difficult to see.