import os
import json
import requests

from django.shortcuts import render

REST_API_KEY = "b99712a0fe7d08fc13dcc9613be9bb15"

APPKEY = "d1226d2eaf8146caf0e412f6158a8dbc"


with open('./WEapp/data/placename.json', 'r', encoding='UTF8') as f:
    category = json.load(f)
cat_food = list(category['foods'].keys())
cat_cafe = list(category['cafes'].keys())
cat_other = list(category['others'].keys())

# foods에 속한 데이터 수집
def data_food(cat):
    placesList = list()
    place_names = category["foods"][cat]
    for place_name in place_names:
        searching = place_name
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?category_group_code=FD6&y=37.5847000272458&x=126.997120875677&radius=900&query={}'.format(searching)
        headers = {
            "Authorization": "KakaoAK "+REST_API_KEY
        }
        places = requests.get(url, headers=headers).json()['documents']
        if places == []:
            pass
        else:
            places[0]['src'] = 'static/img/'+places[0]['id']+'.png'
            places[0]['src_map'] = 'map/static/img/'+places[0]['id']+'.png'
            placesList.append(places[0])
    return placesList
    

# cafes에 속한 데이터 수집
def data_cafe(cat):
    placesList = list()
    place_names = category["cafes"][cat]
    for place_name in place_names:
        searching = place_name
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?category_group_code=CE7&y=37.5847000272458&x=126.997120875677&radius=900&query={}'.format(searching)
        headers = {
            "Authorization": "KakaoAK "+REST_API_KEY
        }
        places = requests.get(url, headers=headers).json()['documents']
        if places == []:
            pass
        else:
            places[0]['src'] = 'static/img/'+places[0]['id']+'.png'
            places[0]['src_map'] = 'map/static/img/'+places[0]['id']+'.png'
            placesList.append(places[0])
    return placesList
    
# others에 속한 데이터 수집
def data_other(cat):
    placesList = list()
    place_names = category["others"][cat]
    for place_name in place_names:
        searching = place_name
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?category_group_code=FD6&y=37.5847000272458&x=126.997120875677&radius=900&query={}'.format(searching)
        headers = {
            "Authorization": "KakaoAK "+REST_API_KEY
        }
        places = requests.get(url, headers=headers).json()['documents']
        if places == []:
            pass
        else:
            places[0]['src'] = 'static/img/'+places[0]['id']+'.png'
            places[0]['src_map'] = 'map/static/img/'+places[0]['id']+'.png'
            placesList.append(places[0])
    return placesList

food1 = data_food(cat_food[0])
food2 = data_food(cat_food[1])
food3 = data_food(cat_food[2])
food4 = data_food(cat_food[3])
food5 = data_food(cat_food[4])
food6 = data_food(cat_food[5])
food7 = data_food(cat_food[6])
food8 = data_food(cat_food[7])
food9 = data_food(cat_food[8])
food10 = data_food(cat_food[9])
food11 = data_food(cat_food[10])
food12 = data_food(cat_food[11])
food13 = data_food(cat_food[12])
food14 = data_food(cat_food[13])
food15 = data_food(cat_food[14])

cafe1 = data_cafe(cat_cafe[0])
cafe2 = data_cafe(cat_cafe[1])
cafe3 = data_cafe(cat_cafe[2])

other1 = data_other(cat_other[0])


def main(request):

    result = {
        "data1" : food1,
        "data2" : food2,
        "data3" : cafe1,
        "data4" : food3,
        "data5" : food4,
        "data6" : food5,
        "data7" : food6,
        "data8" : food7,
        "data9" : food8,
        "data10" : food9,
        "data11" : cafe2,
        "data12" : cafe3,
        "data13" : other1,
        "data14" : food10,
        "data15" : food11,
        "data16" : food12,
        "data17" : food13,
        "data18" : food14,
        "data19" : food15
    }


    return render(request, 'WEapp/main.html', result)



def map(request):
    
    ID = request.GET.get('ID', int)
    
    # cafe
    if int(ID) in [3, 11, 12]:
        data_map = globals()['cafe{}'.format([3,11,12].index(int(ID))+1)]
        cat_map = cat_cafe[[3,11,12].index(int(ID))]
    
    # other
    elif int(ID) in [13]:
        data_map = globals()['other{}'.format([13].index(int(ID))+1)]
        cat_map = cat_other[[13].index(int(ID))]
        
    # food
    else:
        data_map = globals()['food{}'.format([1,2,4,5,6,7,8,9,10,14,15,16,17,18,19].index(int(ID))+1)]
        cat_map = cat_food[[1,2,4,5,6,7,8,9,10,14,15,16,17,18,19].index(int(ID))]
    
    data_map_json = json.dumps(data_map, ensure_ascii=False)
    
    result = {
        "appkey" : APPKEY,
        "datas"     : data_map,
        "datasJson" : data_map_json,
        "ID"        : ID,
        "catName"   : cat_map
    }
    
    
    return render(request, 'WEapp/map.html', result)


def listup(request):
    
    ID = request.GET.get('ID', int)
    
    # cafe
    if int(ID) in [3, 11, 12]:
        data_listup = globals()['cafe{}'.format([3,11,12].index(int(ID))+1)]
        cat_listup = cat_cafe[[3,11,12].index(int(ID))]
    
    # other
    elif int(ID) in [13]:
        data_listup = globals()['other{}'.format([13].index(int(ID))+1)]
        cat_listup = cat_other[[13].index(int(ID))]
        
    # food
    else:
        data_listup = globals()['food{}'.format([1,2,4,5,6,7,8,9,10,14,15,16,17,18,19].index(int(ID))+1)]
        cat_listup = cat_food[[1,2,4,5,6,7,8,9,10,14,15,16,17,18,19].index(int(ID))]
        
    result = {
        "datas"  : data_listup,
        "ID"     : ID,
        "catName": cat_listup
    }
    
    return render(request, 'WEapp/listup.html', result)