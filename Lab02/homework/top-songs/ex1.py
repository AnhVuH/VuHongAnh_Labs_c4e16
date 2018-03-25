from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'

html_content = urlopen(url).read().decode('utf8')


soup = BeautifulSoup(html_content,'html.parser')

section = soup.find('section', 'chart-grid')

li_list = section.find_all('li')


top_songs =[]

for li in li_list:
    rank = li.strong.string
    name = li.h3.a.string
    artist = li.h4.a.string
    top_songs.append({"Ranks": rank,"Names": name, "Artist": artist})

pyexcel.save_as(records = top_songs, dest_file_name = 'top_songs.xlsx')

options = {
        'default_search' :'ytsearch',
        'max_download' : 1,
        'format': 'bestaudio/mp3'
}
dl = YoutubeDL(options)
list_download =[]
for song in top_songs:
    list_download.append(song["Names"] + song['Artist'])
# print(*list_download, sep ='\n')
dl.download(list_download)
