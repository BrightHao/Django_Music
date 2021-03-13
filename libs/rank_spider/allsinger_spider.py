# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "music.settings")
# django.setup()
#
# from demo.models import Singers

import requests
from bs4 import BeautifulSoup
from lxml import etree

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                        " Chrome/67.0.3396.99 Safari/537.36"}


ls1 = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003]  # id的值
ls2 = [-1, 0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]  # initial的值
for i in ls1:
    for j in ls2:
        singer_list = list()
        url = 'http://music.163.com/discover/artist/cat?id=' + str(i) + '&initial=' + str(j)
        html = requests.get(url=url, headers=header).text
        soup = BeautifulSoup(html, 'lxml')
        detail = soup.find('ul', id='m-artist-box')
        singers_info = detail.find_all('a')
        for singer_info in singers_info:
            if singer_info.text:
                singer_name = singer_info.text
                singer_info = etree.HTML(str(singer_info))
                singer_id = singer_info.xpath('//@href')[0]
                if singer_id[0] == ' ':
                    singer_id = singer_id[12:]
                else:
                    singer_id = singer_id[11:]
                print(singer_name, singer_id)
                # singer_list.append(Singers(name=singer_name, singerid=singer_id))
        # Singers.objects.bulk_create(singer_list)


