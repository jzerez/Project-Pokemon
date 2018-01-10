from bs4 import BeautifulSoup
import requests
import os

'''
Jonathan Zerez
January 2018

The purpose of this script is to obtain .png files of pokemon sprites from
https://pokemondb.net/sprites/
'''

#array of all links to each pokemon's page
pokemon_urls = []
generation = 'sun-moon'
home_url = 'https://pokemondb.net/sprites/'

#creates a soup object from a given url for processing
def make_soup(home_url):
    html = requests.get(home_url)
    soup = BeautifulSoup(html.content, "lxml")
    return soup


page_main = make_soup(home_url)

for link in page_main.find_all('a'):
    url = link.get('href')
    #look for links that lead to sprites
    split = url.split('/sprites/')
    #if the link leads to a sprite page for a specific pokemon, store the link
    if len(split) > 1:
        pokemon_urls.append(home_url + split[1])

for pokemon in pokemon_urls:
    page = make_soup(pokemon)
    for image in page.find_all('img'):
        #get original data from each image for downloading
        source = image.get('data-original')
        split = source.split('/')
        #check for correct generation
        if len(split) > 4 and split[4] == generation:
            #filename structure: <SHINY-STATUS>-<POKEMON>
            filename = split[-2] + '-' + split[-1]
            print(filename + " downloaded!")
            url = requests.get(source)
            #open/create a new file and copy content from response object to it
            open('Training/' + filename, 'w').write(url.content)
