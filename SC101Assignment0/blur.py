"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: initial image
    :return: a new blurred image with averaged RGB value of neighboring pixels on a new canvas
    """
    #creating a new canvas
    canvas = SimpleImage.blank(img.width, img.height)

    for x in range(img.width): # loop over every pixel on the old image
        for y in range(img.height):
            green_sum = 0
            red_sum = 0
            blue_sum = 0
            count = 0
            # look for neighboring pixels
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0: # the initial pixel's RGB values are excluded
                        pass
                    else:
                        altered_x = x + dx
                        altered_y = y + dy
                        # pixel at the edges won't be averaged out by all 8 neighboring pixels
                        if 0 <= altered_x <= img.width-1 and 0 <= altered_y <= img.height -1:
                            altered_pixel = img.get_pixel(altered_x, altered_y)
                            green_sum += altered_pixel.green
                            red_sum += altered_pixel.red
                            blue_sum += altered_pixel.blue
                            count += 1
            canvas_pixel = canvas.get_pixel(x, y)
            canvas_pixel.red = red_sum//count
            canvas_pixel.green = green_sum//count
            canvas_pixel.blue = blue_sum//count


    return canvas

def main():
    """
    Reads original image and blurs it by calling the blur function several times
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()
    print('completed')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
