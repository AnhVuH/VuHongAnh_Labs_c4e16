from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url ='http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'

html_content = urlopen(url).read().decode('utf8')

soup = BeautifulSoup(html_content,'html.parser')
datas=[]
dict_data= OrderedDict()

title = soup.find('table', id ='tblGridData')
list_td_title = title.tr.find_all('td')

for td in list_td_title:
    dict_data[td.string] = None
# print(dict_data)

table = soup.find('table', id = 'tableContent')
list_tr = table.find_all('tr',['r_item', 'r_item_a'])
for tr in list_tr:
    list_td_data = tr.find_all('td','b_r_c')
    i=0
    for key in dict_data:
        while i < len(list_td_data):
            dict_data[key] = list_td_data[i].string
            break
        i += 1
    print(dict_data)
    datas.append(dict_data)
pyexcel.save_as(records = datas, dest_file_name= 'VNM_test.xls')
