#!/usr/bin/env python3

import os
import argparse
from PIL import Image

def pad_image(image_path, padding):
	path = os.path.realpath(image_path)
	srcimg = Image.open(path)

	width, height = srcimg.size
	pad = Image.new("RGBA", (width+padding*2, height+padding*2), (255, 255, 255, 0))

	for x in range(width):
		for y in range(height):
			pad.putpixel((x+padding,y+padding), srcimg.getpixel((x,y)))


	padFile = os.path.splitext(image_path)[0] + '-padded.png'
	print(image_path, '\n', srcimg.size, '>', pad.size)
	pad.save(padFile)


def main():
    parser = argparse.ArgumentParser(description="""
        adds padding to an image
        """)
    parser.add_argument('image', help='path to image (folder of images)')
    parser.add_argument('padding', help='padding to add')
    args = parser.parse_args()
    path = os.path.realpath(args.image)
    _padding = int(args.padding)
    if os.path.isdir(path):
        for f in os.listdir(path):
            img_path = os.path.join(path,f)
            try:
                pad_image(img_path, _padding)
            except:
                print("Couldn't pad {}".format(img_path))
    else:
        pad_image(path, _padding)

if __name__ == "__main__":
    main()

