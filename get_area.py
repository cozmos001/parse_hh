import requests  # Для запросов по API
import json  # Для обработки полученных результатов

# Функция получения зон поиска
def getAreas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    areas = []
    for k in jsObj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name'],
                                  k['areas'][i]['areas'][j]['parent_id']])
            else:  # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name'],
                              k['areas'][i]['parent_id']])
    return areas


# areas = getAreas()
# for i in areas:
#     if '1679' in i:
#         print(i)
