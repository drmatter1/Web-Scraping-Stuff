from bs4 import BeautifulSoup # type: ignore
import requests

name = 'antimatter'          # change player name
code = 'pog'         # change player code

try:
    url = (f'https://tracker.gg/valorant/profile/riot/{name}%23{code}/overview')
    source = requests.get(url)

except Exception:
    n1 = name.split(' ')[0]
    n2 = name.split(' ')[1]
    url = (f'https://tracker.gg/valorant/profile/riot/{n1}%{n2}23{code}/overview')
    source = requests.get(url)

source = requests.get(url)

souped_source = BeautifulSoup(source.text, 'lxml')

for soup in souped_source.find_all('div', class_='stat align-left expandable'):

        for value_box in soup.find_all('div', class_='numbers'):

            try:

                value_name = value_box.find('span', class_='name').text

                value = value_box.find('span', class_='value').text

                print(value_name + " :")                                                           # printing information

                print(value)

                print()

            except Exception:
                pass
