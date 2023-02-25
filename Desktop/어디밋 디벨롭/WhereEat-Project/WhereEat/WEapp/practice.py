import requests
import json

REST_API_KEY = "b99712a0fe7d08fc13dcc9613be9bb15"


with open('WhereEat\WEapp\data\placename.json', 'r', encoding='UTF8') as f:
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
            placesList.append(places[0])
    return placesList
    

# # cafes에 속한 데이터 수집
# def data_cafe(cat):
#     placesList = list()
#     # place_names = category["cafes"][cat]
#     place_names = ["할리스", "스타벅스" , "프롬하츠", "킹스커피", "그림의 맛", "오가다"]
#     for place_name in place_names:
#         searching = place_name
#         # category_group_code=CE7&
#         url = 'https://dapi.kakao.com/v2/local/search/keyword.json?y=37.5847000272458&x=126.997120875677&radius=900&query={}'.format(searching)
#         headers = {
#             "Authorization": "KakaoAK "+REST_API_KEY
#         }
#         places = requests.get(url, headers=headers).json()['documents']
#         if places == []:
#             pass
#         else:
#             placesList.append(places)
#     return placesList
    
# # others에 속한 데이터 수집
# def data_other(cat):
#     placesList = list()
#     place_names = category["others"][cat]
#     for place_name in place_names:
#         searching = place_name
#         url = 'https://dapi.kakao.com/v2/local/search/keyword.json?category_group_code=FD6&y=37.5847000272458&x=126.997120875677&radius=900&query={}'.format(searching)
#         headers = {
#             "Authorization": "KakaoAK "+REST_API_KEY
#         }
#         places = requests.get(url, headers=headers).json()['documents']
#         if places == []:
#             pass
#         else:
#             placesList.append(places)
#     return placesList

food1 = data_food(cat_food[0])

# print(food1)
result = {}
    
for i in range(len(food1)):
    result[i] = food1[i]

print(result[0]['place_name'])