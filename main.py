# -*- coding: utf-8 -*-
from PIL import Image
import sys
import numpy as np


def LoadImage(imageToAnalyze):
    for color in range(3):
        pixels = []
        im = Image.open(imageToAnalyze)
        rgb_im = im.convert("RGB")

        for x in range(im.size[1]):
            pixel_row = []
            for y in range(im.size[0]):
                r, g, b = rgb_im.getpixel((y, x))
                if color == 0:
                    pixel_row.append((r, 0, 0))
                elif color == 1:
                    pixel_row.append((0, g, 0))
                else:
                    pixel_row.append((0, 0, b))
            pixels.append(pixel_row)

        array = np.array(pixels, dtype=np.uint8)
        new_image = Image.fromarray(array)
        new_image.save(str(color) + ".png")
        print(color)


LoadImage("test.png")
