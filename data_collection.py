import os
import random
import csv
import uuid
from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

def generate_times_new_roman_images(
    output_dir='times_new_roman_dataset_with_precision', 
    text_samples=None,
    padding=10,
    num_samples=60
):
    os.makedirs(output_dir, exist_ok=True)
    
    csv_path = os.path.join(output_dir, 'labelsReg.csv')
    csv_file = open(csv_path, 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['filename', 'font', 'text', 'font_size', 'text_color'])
    
    font_name = 'Times New Roman'
    try:
        font_path = fm.findfont(fm.FontProperties(family=font_name))
    except Exception as e:
        print(f"Could not find font {font_name}: {e}")
        return
    
    for _ in range(num_samples):
        font_size = round(random.uniform(10, 60), 2)  # Random size with 2 decimal places
        font = ImageFont.truetype(font_path, int(font_size))
        
        text = random.choice(text_samples)
        
        dummy_image = Image.new('RGB', (1, 1))
        draw = ImageDraw.Draw(dummy_image)
        text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]
        
        image = Image.new('RGB', (text_width + 2 * padding, text_height + 2 * padding), 'white')
        draw = ImageDraw.Draw(image)
        draw.text((padding, padding), text, font=font, fill='black')
        
        filename = f'{font_name.replace(" ", "")}{font_size}px_{uuid.uuid4().hex[:6]}.png'
        image_path = os.path.join(output_dir, filename)
        image.save(image_path)
        
        csv_writer.writerow([filename, font_name, text, font_size, 'black'])
    
    csv_file.close()

# Example usage
text_samples = ["Sample text 1", "Sample text 2", "Sample text 3"]
generate_times_new_roman_images(text_samples=text_samples)