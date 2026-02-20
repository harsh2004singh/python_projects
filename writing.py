from PIL import Image, ImageDraw, ImageFont

# Your text
text = """My mother is the best person in the world.
She loves me unconditionally and supports me always."""

# Create blank white image
img = Image.new("RGB", (1000, 600), color="white")
draw = ImageDraw.Draw(img)

# Load handwriting font (make sure file exists)
font = ImageFont.truetype(
    r"C:\Users\Harsh\python projects\handwriting.ttf",40)

# Write text
draw.multiline_text((50, 100), text, fill=(0, 0, 138), font=font, spacing=10)

# Save image
img.save("mother_poem.png")

print("✅ Handwriting image created successfully!")