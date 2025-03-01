# Text to Handwriting

This is a simple Python project that converts a given text into a handwritten-like image using the **Pillow** library. You can use a custom handwriting-style font to enhance the handwritten effect.

## Features
- Converts text to a handwritten-style image.
- Uses a customizable handwriting font.
- Generates a `.png` image of the handwritten text.

## Prerequisites
Make sure you have Python installed on your system. You also need the following Python libraries:

- Pillow

Install it using pip:
```bash
pip install pillow
```

## Usage
1. Clone this repository:
```bash
git clone https://github.com/dishapawarkhausi/python-projects.git
```

2. Navigate to the project directory:
```bash
cd Text_To_Handwriting
```

3. Ensure you have a handwriting-style font file (e.g., `SweetGetawayDemoRegular-2XyK.ttf`) in the project directory. You can download fonts from websites like [Google Fonts](https://fonts.google.com/) or [DaFont](https://www.dafont.com/).

4. Run the Python script:
```bash
python main.py
```

## Example Code
```python
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
    draw.text((x, y), line, fill=(0, 0, 138), font=font)  # Text color
    y += line_spacing

image.save("handwriting.png")
print("Handwritten-like image saved as 'handwriting.png'")
```

## Output
Running the script generates an image `handwriting.png` in the project directory. It contains the provided text in a handwriting-style font.

## Project Structure
```
Text_To_Handwriting/
│
├── main.py          # Python script
├── handwriting.png  # Output image (generated after running the script)
├── SweetGetawayDemoRegular-2XyK.ttf  # Handwriting-style font file
└── README.md        # Project documentation
```

## Notes
- Replace `SweetGetawayDemoRegular-2XyK.ttf` with any handwriting-style font of your choice.
- Ensure the font file is in the project directory, or update the `font_path` variable with the correct location.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository and contribute by submitting a pull request.
