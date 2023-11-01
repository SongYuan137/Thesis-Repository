from PIL import Image
import os

"""
    Takes a 1280 by 1707 photo and separate it into three square images.
    Then set the resolution to 224, 224 (dimension of MobileNet)
"""

# Set true for debugging
debugging = False
# Set directory to search for photos
directory = "SilverBeet_new"

# Get all photos in directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        photo = Image.open(file)
        width, height = photo.size
        if debugging:
            # Photo size: 1280 by 1707, difference: 427
            print("The photo dimension is: " + str(width) + ' by ' + str(height))

        # Adjust photo dimensions
        top_1 = int(0)
        top_2 = int((height - width) / 2)
        top_3 = int((height - width))
        bottom_1 = int(height - (height - width))
        bottom_2 = int(height - (height - width) / 2)
        bottom_3 = int(height)
        right = int(width)
        left = int(0)

        if debugging:
            print("Image one: " + str(bottom_1 - top_1))
            print("Image two: " + str(bottom_2 - top_2))
            print("Image three: " + str(bottom_3 - top_3))
            break

        # Crop image to a square
        newImage_1 = photo.crop((left, top_1, right, bottom_1))
        newImage_2 = photo.crop((left, top_2, right, bottom_2))
        newImage_3 = photo.crop((left, top_3, right, bottom_3))
        newImage_1 = newImage_1.resize((224, 224))
        newImage_2 = newImage_2.resize((224, 224))
        newImage_3 = newImage_3.resize((224, 224))
        # Do not use this function!!! newImage.show()

        # Generate a new filename and save
        newFilename = filename.split()
        newImage_1.save("Processed/" + "ver_1" + newFilename[1], 'JPEG')
        newImage_2.save("Processed/" + "ver_2" + newFilename[1], 'JPEG')
        newImage_3.save("Processed/" + "ver_3" + newFilename[1], 'JPEG')


