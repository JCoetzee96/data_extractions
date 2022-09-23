import os
import socket
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

socket.setdefaulttimeout(5)

# download the images from the url in the dataframe, which are then saved on your local machine
def download_images(df, sample_size=100, output_dir='model'):
    """
    Downloads a sample of N images to a directory
    called 'images'
    """
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    sample = df.sample(frac=1, random_state=42)
    examples_done = 0
    for index, row in tqdm(df.iterrows(), total=sample_size):
        if examples_done >= sample_size:
            break
        if row['url'] != 'na':
            url = row['url']
        else:
            continue
        file_extension = url[url.rfind('.'):]
        if '?' in file_extension:
            file_extension = file_extension[:file_extension.find('?')]
        if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
            outdir_path = '{}/{}{}'.format(output_dir, row['index'], file_extension)
        try:
            if not os.path.exists(outdir_path):
                urlretrieve(url, outdir_path)
            examples_done += 1
        except:
            continue
    for image in os.scandir(output_dir):
        try:
            plt.imread(image.path) # if image can't be opened, delete
        except:
            os.remove(image.path)

download_images(df_urls)
