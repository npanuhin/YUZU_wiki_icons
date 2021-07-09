from skimage import io
from os import listdir, remove as os_remove

from utils import mkpath


search_path = "../icons1000"
verify_size = (1000, 1000)

delete_damaged = False  # Warning!!!


print("Starting...")

for filename in listdir(mkpath(search_path)):
    with open(mkpath(search_path, filename), "rb") as img_file:
        try:
            image = io.imread(img_file)

            if image.shape[:2] != verify_size:
                print("Image \"{}\" is wrong size".format(filename))

        except ValueError:
            print("Image \"{}\" is damaged".format(filename))

            if delete_damaged:
                os_remove(mkpath(search_path, filename))
