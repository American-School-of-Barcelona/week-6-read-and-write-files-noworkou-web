import sys
from PIL import Image, ImageOps


def main():
    # Check number of arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Valid extensions
    valid_ext = [".jpg", ".jpeg", ".png"]

    # Get extensions
    in_ext = get_ext(input_file)
    out_ext = get_ext(output_file)

    # Check extensions
    if in_ext not in valid_ext:
        sys.exit("Invalid input")
    if out_ext not in valid_ext:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    # Try opening input image
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # Open shirt
    shirt = Image.open("shirt.png")

    # Resize and crop input image to match shirt
    image = ImageOps.fit(image, shirt.size)

    # Paste shirt onto image
    image.paste(shirt, shirt)

    # Save result
    image.save(output_file)


def get_ext(filename):
    return filename.lower()[filename.rfind("."):]


if _name_ == "_main_":
    main()