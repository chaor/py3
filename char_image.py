"""
This scripts convert a color image into a gray image, then replaces each pixel
with an ASCII character based on its gray-scale value. In this way,
you can see the picture in your text editor or terminal :)

Usage: python char_image.py path/to/image_file

If the image size is large, zoom out to see the effect!
"""
import sys
from pathlib import Path

from PIL import Image


def get_gray_value_to_gray_char_mapping():
    # gray value range is [0, 255], 0 is black and 255 is white
    # get a dictionary to map gray value to gray char
    gray_char = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
    return {
        i: gray_char[int(i / 256 * len(gray_char))] for i in range(256)
    }


def image_file_to_gray_char(image_file_path):
    gray_value_to_gray_char = get_gray_value_to_gray_char_mapping()
    char_image = ''

    with Image.open(image_file_path) as img:
        # convert color image to black and white image
        gray_img = img.convert(mode='L')
        width, height = gray_img.size
        for i in range(height):
            one_line = ''.join(
                gray_value_to_gray_char[gray_img.getpixel((j, i))] for j in range(width)
            )
            char_image += one_line + '\r\n'

    return char_image


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python char_image.py path/to/image_file\n')
        sys.exit(1)

    image_file = Path(sys.argv[1])
    if not image_file.is_file():
        print(f"Image file path {sys.argv[1]} doesn't exist")
        sys.exit(1)

    print(image_file_to_gray_char(image_file_path=sys.argv[1]))
