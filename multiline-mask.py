#!/usr/bin/env python3

import os
import argparse
from PIL import Image

def multiline_mask_by_letter(image_path):
	path = os.path.realpath(image_path)
	srcimg = Image.open(path)

	mask = Image.new("RGBA", srcimg.size, (255, 255, 255))
	width, height = srcimg.size

	gray = 0
	inc = int(255/30) # 255/[max letters]

	lineBreaks = [0]

	isGap = True
	for y in range(height):
		isLetter = False

		# detect pixels in a column
		for x in range(width):
			r,g,b,a = srcimg.getpixel((x,y))
			if a>0:
				isLetter = True
				isGap = False

		# if it's a gap, and the last column was a letter
		if isLetter == False and isGap == False:
			lineBreaks.append(y)
			isGap = True

	lineBreaks.append(height)

	base = 0
	lineCount = 0
	for lbreak in lineBreaks:
		if lbreak == 0:
			base = lbreak;
		else:
			gray = lineCount*3*inc # delay timing by line
			isGap = True
			print ("row ", base, "to", lbreak)
			for x in range(width):
				isLetter = False

				# detect pixels in a column
				for y in range(lbreak-base):
					r,g,b,a = srcimg.getpixel((x,y+base))
					if a>0:
						isLetter = True
						isGap = False

				# if it's a gap, and the last column was a letter
				if isLetter == False and isGap == False:
					gray += inc
					isGap = True

				for y in range(lbreak-base):
					mask.putpixel((x,y+base), (gray, gray, gray))
			base = lbreak
			lineCount += 1


	maskFile = os.path.splitext(image_path)[0] + '-mask.png'
	print ('mask: ' + maskFile)
	print('size:', mask.size)
	mask.save(maskFile)


def main():
    parser = argparse.ArgumentParser(description="""
        creates a gradient mask by line and by letter from a PNG w transparency
        """)
    parser.add_argument('image', help='path to image (folder of images)')
    args = parser.parse_args()
    path = os.path.realpath(args.image)
    if os.path.isdir(path):
        for f in os.listdir(path):
            img_path = os.path.join(path,f)
            try:
                multiline_mask_by_letter(img_path)
            except:
                print("Couldn't mask {}".format(img_path))
    else:
        multiline_mask_by_letter(path)

if __name__ == "__main__":
    main()

