from PIL import Image, ImageDraw, ImageFont

txt = ''' Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility.
It was created by Guido van Rossum and first released in 1991. 
Python is designed to be easy to learn and use, making it a popular choice for both beginners and experienced programmers.'''

image = Image.new('RGB', (1000, 1000), color=(255, 255, 255)) 
draw = ImageDraw.Draw(image)

font_path = "Text_To_Handwriting\SweetGetawayDemoRegular-2XyK.ttf" 
try:
    font = ImageFont.truetype(font_path, 50)
except IOError:
    print("Font file not found. Please use a handwriting font.")
    font = ImageFont.load_default()

x, y = 10, 10  
line_spacing = 30  
for line in txt.split('\n'):
    draw.text((x, y), line, fill=(0, 0, 138), font=font) 
    y += line_spacing

image.save("handwriting.png")
print("Handwritten-like image saved as 'handwriting.png'")
