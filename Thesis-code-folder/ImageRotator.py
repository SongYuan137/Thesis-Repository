from PIL import Image
import os
import math

"""
    Read a directory of images and save a new rotated version.
    The rotator code is referenced in the rotator() function
"""

# Set debug to true for debugging outputs
debugging = False
# Set the directory to read from
directory = "3"
# Set false if the image is already in MobileNetV3 dimensions, set true if image was not processed.
pre_process = False


def rotator(w, h, angle):
    """
    Reference: https://stackoverflow.com/questions/16702966/rotate-image-and-crop-out-black-borders
    Given a rectangle of size wxh that has been rotated by 'angle' (in
    radians), computes the width and height of the largest possible
    axis-aligned rectangle (maximal area) within the rotated rectangle.
    """
    if w <= 0 or h <= 0:
        return 0, 0
    width_is_longer = w >= h
    side_long, side_short = (w, h) if width_is_longer else (h, w)
    sin_a, cos_a = abs(math.sin(angle)), abs(math.cos(angle))
    if side_short <= 2.*sin_a*cos_a*side_long or abs(sin_a-cos_a) < 1e-10:
        x = 0.5*side_short
        wr, hr = (x/sin_a, x/cos_a) if width_is_longer else (x/cos_a, x/sin_a)
    else:
        cos_2a = cos_a*cos_a - sin_a*sin_a
        wr, hr = (w*cos_a - h*sin_a)/cos_2a, (h*cos_a - w*sin_a)/cos_2a
    return wr, hr


for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        photo = Image.open(file)
        width, height = photo.size
        if debugging:
            # Photo size: 1280 by 1707, difference: 427
            print("The photo dimension is: " + str(width) + ' by ' + str(height))

        # Adjust photo dimensions
        top = int((height - width) / 2)
        bottom = int(height - (height - width) / 2)
        right = int(width)
        left = int(0)

        if debugging:
            print("Image two: " + str(bottom - top))
            break

        if pre_process:
            # Crop image to a square
            newImage = photo.crop((left, top, right, bottom))
        else:
            newImage = photo

        # Rotate image by degrees
        degrees = 180
        newImage = newImage.rotate(degrees)
        oldWidth = right - left
        oldHeight = bottom - top
        newWidth, newHeight = rotator(oldWidth, oldHeight, math.radians(degrees))

        # Adjust photo dimensions
        top = int((oldHeight - newHeight) / 2)
        bottom = int(oldHeight - top)
        left = int((oldWidth - newWidth) / 2)
        right = int(oldWidth - left)

        newImage = newImage.crop((left, top, right, bottom))
        newImage = newImage.resize((224, 224))
        # Do not use this function!!! newImage.show()

        if pre_process:
            # Generate a new filename and save
            newFilename = filename.split()
            newImage.save("Processed/" + "ver" + newFilename[1], 'JPEG')
        else:
            newImage.save("Processed/" + "ver" + filename, 'JPEG')
