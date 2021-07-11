from PIL import Image, UnidentifiedImageError
from os import listdir, remove as os_remove

from utils import mkpath


search_path = "../icons1000"
verify_size = (1000, 1000)

delete_damaged = False  # Warning!!!


print("Starting verification...")

for filename in listdir(mkpath(search_path)):
    try:
        image = Image.open(mkpath(search_path, filename))

        if image.size != verify_size:
            print("Image \"{}\" is wrong size".format(filename))

        image.close()

        # print(filename)

    except (IOError, SyntaxError, UnidentifiedImageError):
        print("Image \"{}\" is damaged".format(filename))

        if delete_damaged:
            os_remove(mkpath(search_path, filename))
