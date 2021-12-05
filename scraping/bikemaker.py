from typing import Text
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.goobike.com/motocle/bike'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
print('----- HTML取得完了 -----')

# バイクメーカー取得
print('----- バイクメーカー取得開始 -----')
bike_makers = []
for bm_num in range(1, 391, 2):
    bm_resultset = soup.select(f'#main > div > h2:nth-child({bm_num}) > span')
    bike_maker_name = bm_resultset[0].text
    bike_makers.append([str(bm_num//2+1), bike_maker_name])
    print('取得完了: ', bike_maker_name)
print('----- バイクメーカー取得完了 -----')

print('----- バイクメーカー書込開始 -----')
with open('bike_makers.csv', 'w', encoding='utf-8', newline='') as bmf:
    bmw = csv.writer(bmf)
    bmw.writerows(bike_makers)
print('----- バイクメーカー書込完了 -----')





# # bikes = soup.select('h2.maker_name + ul > li > ul.clearfix.bike_list > li > a')
# bikes = soup.select('#main > div > ul:nth-child(2) > li:nth-child(1) > ul > li > a')
# output = []
# num = 0
# for b in bikes:
#     output.append([str(num), b.text])
#     num += 1

# with open('bikes.csv', 'w', encoding='utf-8', newline='') as f:
#     w = csv.writer(f)
#     w.writerows(output)



# with open('bikes.csv', 'w', encoding='utf-8') as f:
#     w = csv.writer(f)

# ary = []
# for i in bikes:
#     ary.append(i.text)
    # test = type(i.text)
    # w.writerow(i.text)
# print(ary)