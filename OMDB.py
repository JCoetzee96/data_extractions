!pip install omdb

import omdb

# link to get api key from omdb:
# https://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0oCxKYG7xaZwy2ktIrVmWGdWzxj%2FDhHQaAqqFYTiRTDE%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU%2BO86JjTqdg0yhuGR2tBukmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulHLL4j%2B3qCcW3ReXhfb4KKsSs3zlQ%2B48KY6Qzm7wzZbR&at=freeAcct&Email=
omdb.set_default('apikey', "YOUR_API_KEY") # note that free omdb key has limit of 1000 requests per day

# collect metadata and save these in a newly created DataFrame
df_omdb = pd.DataFrame()
titles = []
languages = []
releases = []
directors = []
awards = []
actors = []
countries = []
ratings = []
votes = []
for video in tqdm(df.Title):
    obj = omdb.title(video)
    try:
        titles.append(obj['title'])
    except:
        titles.append('')
    try:
        languages.append(obj['language'])
    except:
        languages.append('')
    try:
        releases.append(obj['released'])
    except:
        releases.append('')
    try:
        directors.append(obj['director'])
    except:
        directors.append('')
    try:
        awards.append(obj['awards'])
    except:
        awards.append('')
    try:
        actors.append(obj['actors'])
    except:
        actors.append('')
    try:
        countries.append(obj['country'])
    except:
        countries.append('')
    try:
        ratings.append(obj['imdb_rating'])
    except:
        ratings.append('')
    try:
        votes.append(obj['imdb_votes'])
    except:
        votes.append('')

df_omdb['Title'] = titles
df_omdb['Language'] = languages
df_omdb['Release Date'] = releases
df_omdb['Director'] = directors
df_omdb['Awards'] = awards
df_omdb['Actors'] = actors
df_omdb['Country'] = countries
df_omdb['IMDb Rating'] = ratings
df_omdb['IMDb votes'] = votes
# save the dataframe as a csv file
df_omdb.to_csv('.csv')
