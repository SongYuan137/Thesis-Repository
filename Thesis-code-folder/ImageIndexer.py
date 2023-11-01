from PIL import Image
import os

"""
    Takes a directory of photos and rename them as numbers to simplify iterating processes.
"""

# Set the directory to search for photos
directory = "test_5/3"
# Set the number that will become the name of the first photo
index = 40

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        photo = Image.open(file)
        photo.save("Processed/" + str(index) + ".png", 'PNG')
        index = index + 1
