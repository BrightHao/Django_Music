from django.shortcuts import render
# from demo.models import Singers


def singer_index(request):
    return render(request, 'singerlist_index.html')


# 查询数据库内容展示在网页上
# def singer(request, id, initial):
#     ids = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003]  # id的值
#     initials = [1, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 0]
#     global index
#     Id = 0
#     Num = 0
#     index = 0
#     for i in range(12):
#         if int(id) == ids[i]:
#             index = i * 28
#             print(index)
#             Id = i
#             break
#     for i in range(28):
#         if int(initial) == initials[i]:
#             index += i
#             print(index)
#             Num = i
#             break
#     ClassList = ["华语男歌手", "华语女歌手", "华语组合/乐队", "欧美男歌手", "欧美女歌手", "欧美组合/乐队",
#                  "日本男歌手", "日本女歌手", "日本组合/乐队", "韩国男歌手", "韩国女歌手", "韩国组合/乐队"]
#     singerclass = ClassList[Id]
#     singers = Singers.objects.all()[index*100:(index+1)*100]
#     kwgs = {
#         'singers': singers,
#         'singerclass': singerclass,
#         'charnum': Num,
#     }
#     return render(request, 'tests/Singerslist.html', kwgs)


# 爬取网页内容展示
def singer_spider(request, id, initial):
    import requests
    from bs4 import BeautifulSoup

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                            " Chrome/67.0.3396.99 Safari/537.36"}
    from lxml import etree

    ids = {'1001': "华语男歌手", '1002': "华语女歌手", '1003': "华语组合/乐队",
           '2001': "欧美男歌手", '2002': "欧美女歌手", '2003': "欧美组合/乐队",
           '6001': "日本男歌手", '6002': "日本女歌手", '6003': "日本组合/乐队",
           '7001': "韩国男歌手", '7002': "韩国女歌手", '7003': "韩国组合/乐队"}  # id对应的类名称
    singer_list = list()
    index = 0
    if initial == '1':
        initial = '-1'
    elif initial == '0':
        index = 27
    else:
        index = int(initial) - 64
    url = 'http://music.163.com/discover/artist/cat?id=' + id + '&initial=' + initial
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
            singer_list.append([singer_name, singer_id])
    kwgs = {
        'singers': singer_list,
        'singerclass': ids[id],
        'charnum': index,
        'classnum': id,
    }
    return render(request, 'singerlist_detail.html', kwgs)


def singer_detail(request, id, name):
    # 1.从本地数据库查询歌手的歌曲信息
    # try:
    #     from demo.models import Singers, Songs
    #     SingerId = Singers.objects.filter(name=name)[0].id
    #     sinegrs = Songs.objects.filter(singer_id=SingerId)
    #     songs_list = []
    #     for singer in sinegrs:
    #         songs_list.append([singer.singer_id, singer.name, 'sad', '06:66'])
    #     kwgs = {
    #         "songslist": songs_list,
    #         "singer": name,
    #     }
    #     return render(request, "SingerDetail.html", kwgs)

    # 2.直接从网易云上爬取资源
    # except:
    import requests
    from bs4 import BeautifulSoup as bs
    import random
    url = "https://music.163.com/artist?id=" + id
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99"
                      " Safari/537.36"}
    html = requests.get(url=url, headers=headers).text
    singer_list = list()
    soup = bs(html, 'lxml')
    find_list = soup.find('textarea', id="song-list-pre-data").text
    null = "null"
    false = "false"
    true = "true"
    find_list = eval(find_list)
    for list_info in find_list:
        singer_id = list_info["privilege"]["id"]
        singer_name = list_info["name"]
        abulm_name = list_info["album"]["name"]
        duration = list_info["duration"]
        sec = duration / 1000
        m, s = divmod(sec, 60)
        duration = ("%02d：%02d" % (m, s))
        singer_list.append([singer_id, singer_name, abulm_name, duration])
    pic_num = random.randrange(0, len(singer_list))
    image = find_list[pic_num]["album"]['picUrl']

    kwgs = {
        "songslist": singer_list,
        "singer": name,
        "coverimage": image,
        "songs_num": len(singer_list),
    }
    return render(request, "SingerDetail.html", kwgs)
