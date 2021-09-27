import requests
from bs4 import BeautifulSoup

host = 'https://www.emuparadise.me/roms/search.php'

search = input('Search a ROM\n')

request = requests.get(host + '?query=' + search + '&section=all')

if request.status_code == 200:
  soup = BeautifulSoup(request.text, 'lxml')
  roms_list = soup.find_all('div', class_='roms')
  for index, rom in enumerate(roms_list):
    print('[' + str(index) + ']', rom.text)
  
  option = input('Select an option\n')

  print(roms_list[int(option)].text)