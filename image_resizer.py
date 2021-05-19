from PIL import Image
import os

# where the full sized images are kept relative to the repository
PATH = '../images/images/'

# list artists/folders
artists = os.listdir('../images/images/')

for artist in artists:
    # make destination directory if doesn't exist
    os.makedirs('../100x100/' + artist, exist_ok=True)
    # get all filenames for that artist/folder
    image_names = os.listdir(PATH + artist)
    # for each image, save in desitnation folder
    # a resized version to 100x100 pixels
    for image_name in image_names:
        location = PATH + artist + '/' + image_name
        image = Image.open(location)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.resize((100, 100)).save('../100x100/' + artist +
                                      '/' + image_name)
        image.close()
