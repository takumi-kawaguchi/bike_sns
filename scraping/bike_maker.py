import requests
import csv
import time
from bs4 import BeautifulSoup

engine_capacity_classes_table = {
    '50cc以下': 1,
    '51～125cc': 2,
    '126～250cc': 3,
    '251～400cc': 4,
    '401～750cc': 5,
    '751～1000cc': 6,
    '1001cc以上': 7,
    'その他': 8
}

start_time = time.perf_counter()

# HTML取得
url = 'https://www.goobike.com/motocle/bike'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'lxml')

# バイクメーカー取得
bike_makers = []
bikes = []
bike_id = 1
for bm_num in range(1, 3, 2):
    # メーカー名取得
    bm_resultset = soup.select(f'#main > div > h2:nth-child({bm_num}) > span')
    bike_maker_id = str(bm_num//2+1)
    bike_maker_name = bm_resultset[0].text
    bike_makers.append([bike_maker_id, bike_maker_name])
    print(f'バイクメーカー取得完了: {bike_maker_name}')

    # メーカー毎に排気量取得
    each_maker_capacity_classes = []
    each_maker_capacity_count = len(soup.select(f'#main > div > ul:nth-child({bm_num+1}) > li'))
    for c_num in range(1, each_maker_capacity_count+1):
        each_maker_capacity_classes.append(soup.select_one(f'#main > div > ul:nth-child({bm_num+1}) > li:nth-child({c_num}) > h2 > span').text)
    print(f'メーカー {bike_maker_name}: 排気量取得完了')

    # 排気量毎にバイク車種名取得
    for bc_num in range(0, each_maker_capacity_count):
        engine_capacity_classes_name = each_maker_capacity_classes[bc_num]
        engine_capacity_classes_id = engine_capacity_classes_table[each_maker_capacity_classes[bc_num]]
        bc_resultset = soup.select(f'#main > div > ul:nth-child({bm_num+1}) > li:nth-child({bc_num+1}) > h2 + ul > li')
        for bike_tag in bc_resultset:
            bikes.append([bike_id, bike_maker_id, engine_capacity_classes_id, bike_tag.text])
            bike_id += 1
        print(f'メーカー {bike_maker_name} 排気量 {engine_capacity_classes_name}: バイク車種取得完了')

    print(f'メーカー {bike_maker_name} 全排気量: バイク車種取得完了')

# メーカーマスターをCSVに書き出し
print('メーカーマスターCSV書き出し開始')
with open('bike_makers.csv', 'w', encoding='utf-8', newline='') as bmf:
    bmw = csv.writer(bmf)
    bmw.writerow(['id', 'name'])
    bmw.writerows(bike_makers)
print('メーカーマスターCSV書き出し完了')


# バイク車種名をCSVに書き出し
print('バイク車種マスターCSV書き出し開始')
with open('bikes.csv', 'w', encoding='utf-8', newline='') as bf:
    bfw = csv.writer(bf)
    bfw.writerow(['id', 'bike_maker_id', 'engine_capacity_class_id', 'name'])
    bfw.writerows(bikes)
print('バイク車種マスターCSV書き出し完了')

end_time = time.perf_counter()
print(f'処理時間: {end_time - start_time}')