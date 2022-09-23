import pandas as pd
from glob import glob
import chardet
from collections import Counter
import os
from tqdm import tqdm
from bs4 import BeautifulSoup

# load the data
categories = sorted(glob('/categories/*'))

# check encoding types of files
# code influenced by:
# https://stackoverflow.com/questions/3323770/character-detection-in-a-text-file-in-python-using-the-universal-encoding-detect
def read_file(filename):
    with open(filename, 'rb') as infile:
        contents = infile.read()
    return contents

d = {}
test = []
for category in categories:
    for path, dirs, files in os.walk(category):
        d[basename(category)] = {}
        for file in tqdm(files):
            data = chardet.detect(read_file(os.path.join(path,file)))
            test.append(data['encoding'])

# source code: https://www.geeksforgeeks.org/python-get-unique-values-list/
# Function to get unique values from list
def unique(list1):
    # Print directly by using * symbol
    print(*Counter(list1))

# unique(test)

def read_file(filename):
    try:
        with open(filename, encoding='utf-8') as infile:
            contents = infile.read()
    except:
        try:
            with open(filename, encoding='Windows-1252') as infile:
                contents = infile.read()
        except:
            try:
                with open(filename, encoding='Windows-1254') as infile:
                    contents = infile.read()
            except:
                try:
                    with open(filename, encoding='TIS-620') as infile:
                        contents = infile.read()
                except:
                    with open(filename, encoding='ISO-8859-1') as infile:
                        contents = infile.read()
    return contents

# create dictionary of categories and files, and read files (saved as soup)
d = {}
for category in categories:
    for path, dirs, files in os.walk(category):
        d[basename(category)] = {}
        for file in tqdm(files):
            contents = read_file(os.path.join(path,file))
            soup = BeautifulSoup(contents, 'html') # transform into a BS4 object
            d[basename(category)][file] = soup
            
# Extract the data from the stored HTML files

def metadata(attr):
    return value.find('meta', attrs={'property': attr})

def metadata_content(attr):
    return value.find('meta', attrs={'property': attr})['content']

data = {}
for category, html_dict in d.items():
    data[category] = {}
    for key, value in html_dict.items():
        data[category][key] = {}
        if metadata('og:title'):
            data[category][key]['title'] = metadata_content('og:title')
            data[category][key]['title'] = data[category][key]['title'].replace(' | PBS', '')
        else:
            data[category][key]['title'] = ''

        if metadata('og:description'):
            data[category][key]['description'] = metadata_content('og:description')
        else:
            data[category][key]['description'] = ''

        if metadata('og:image'):
            data[category][key]['image'] = metadata_content('og:image')
        else:
            data[category][key]['image'] = '' 

# save data as dataframe
df_categories = []
htmls = []
titles = []
descriptions = []
images = []
#tokens = []
for key, value in data.items():
    for html, values in value.items():
        df_categories.append(key)
        htmls.append(html)
        for label, text in values.items():
            if label == 'title':
                titles.append(text)
            elif label == 'description':
                descriptions.append(text)
            elif label == 'image':
                images.append(text)
df = pd.DataFrame()
df['Category'] = df_categories
df['html'] = htmls
df['Title'] = titles
df['Description'] = descriptions
df['Image-URL'] = images
#df['Tokens'] = tokens
# df['Cluster'] = kmeans.labels_ # this line of code was added after calculating the kmeans clusters, found below

# replace empty images
df['Image-URL'] = [str(x).replace('None?focalcrop=1200x630x50x10&format=auto',
'https://i1.wp.com/www.fryskekrite.nl/wordpress/wp-content/uploads/2017/03/No-image-available.jpg') for x in df['Image-URL']]
# save dataframe as csv file
df.to_csv('.csv')
