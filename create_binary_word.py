from PIL import Image, ImageDraw, ImageFont

def create_binary_art_default_font(text, size=10):
    # Use a default font
    font = ImageFont.load_default()

    # Determine size required for the text; this is a bit trickier with the default font,
    # so we might need to adjust the size manually
    image_size = (len(text) * size, size * 2)  # Rough estimation

    image = Image.new("1", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Draw the text onto the image
    draw.text((0,0), text, fill="black", font=font)

    # Convert the image to binary representation (1s and 0s)
    pixels = list(image.getdata())
    width, height = image.size
    binary_art = ["0" if pixel == 255 else "1" for pixel in pixels]

    # Format the binary representation into lines
    binary_lines = ["".join(binary_art[i*width:(i+1)*width]) for i in range(height)]

    return "\n".join(binary_lines)

# Generate binary art for "HI" using a default font
binary_art_default_font = create_binary_art_default_font("FUCK")

# Print the result
print(binary_art_default_font)
