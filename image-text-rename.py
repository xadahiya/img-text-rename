import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


def get_text(dir, path):
    """ Extract text from image using Google Vision API. """
    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        dir + "/" + path)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    ## Detects text from image using google vision API
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return " ".join(texts[0].description.split("\n"))

def rename(path, new_path):
    """ Rename file from path to new_path. """
    os.rename(path, new_path)

def get_dir_files(dir):
    """ Returns a list of files present in dir. """
    return os.listdir(dir)


if __name__ == "__main__":
    ## Directory name containing images
    dir = 'tests'

    for file in get_dir_files(dir):
        try:
            text = get_text(dir, file).lower()
            print(text)
            rename(dir + "/" + file, dir + "/" + text)
        except:
            pass
