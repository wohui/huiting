from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
# Create your views here.

def home(request):
    return render(request,'tiny/index.html')

def index(request):
    return render(request,'tiny/index.html')

#
def getSongs(request):
    '''
    api_host； url= "https://api.imjad.cn/cloudmusic/"
    查询：params；{'search_type': '1','s':'冰雨'}
    根据id查询歌词：{'id': '34532800','type':'lyric'}
    '''
    url= "https://api.imjad.cn/cloudmusic/"
    payload = {'type': 'search','search_type':'10','s':'薛之谦'}
    res = requests.get(url,params=payload)
    print(res.url)
    print(res.json())
    print(res.text)
    return HttpResponse("songs")
#歌手列表
def singer_list(request):

    return render(request,'tiny/singer_list.html')

def singer_info(request,singer_id):

    return render(request, 'tiny/singer_info.html')

#歌手详细列表
def get_singer_data(request):
    '''
    根据歌手id查询歌手信息
    '''
    singer_id = request.GET.get('id')
    url = "https://api.imjad.cn/cloudmusic/"
    payload = {'type': 'artist', 'id': singer_id}
    res = requests.get(url, params=payload)
    # 转换成json
    res_json = res.json()

    singer_data = {}
    singer_data['id'] = singer_id
    singer_data['name'] = res_json['artist']['name']
    singer_data['img'] = res_json['artist']['img1v1Url']
    singer_data['musicSize'] = res_json['artist']['musicSize']
    singer_data['albumSize'] = res_json['artist']['albumSize']
    singer_data['mvSize'] = res_json['artist']['mvSize']
    response_data = {"data": singer_data}
    return JsonResponse(response_data)

def get_singer_list(request):
    url = "https://api.imjad.cn/cloudmusic/"
    payload = {'type': 'search', 'search_type': '100', 's': '古风','limit':10}
    res = requests.get(url, params=payload)
    # 转换成json
    res_json = res.json()
    # 每条返回的数据组合到list
    singer_list = []
    for i in range(0, 10):
        singer_dict = {}
        singer_id = res_json['result']['artists'][i]['id']
        singer_name = res_json['result']['artists'][i]['name']
        singer_img = res_json['result']['artists'][i]['img1v1Url']
        singer_dict['singer_id'] = singer_id
        singer_dict['singer_name'] = singer_name
        singer_dict['singer_img'] = singer_img
        singer_list.append(singer_dict)
    # 最终返回的json
    response_data = {"result": singer_list}
    return JsonResponse(response_data)