from django.shortcuts import render
import xmltodict, requests
from hospitalAPI import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def chosen(request):
    map_api_key = settings.GOOGLE_MAPS_API_KEY

    region = str(request.GET.get('region'))
    zipCode = str(request.GET.get('zipCode'))

    API_SERVICE_KEY = settings.HOSPITAL_API_KEY
    raw_data = f'http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?pageNo=1&sidoCd=110000&numOfRows=1000&sgguCd={region}&zipCd={zipCode}&ServiceKey={API_SERVICE_KEY}'

    data = requests.get(raw_data).content
    xmlObject = xmltodict.parse(data)
    api_data = xmlObject['response']['body']['items']['item']

    infos = []
    for i in api_data:
        infos.append({
            'name':i['yadmNm'],
            'x':round(float(i['XPos']), 3),
            'y':round(float(i['YPos']), 3),
            'telno':i['telno']
        })

    x1 = 127.086
    y1 = 37.584
    return render(request, 'chosen.html', {'infos':infos,'map_api_key':map_api_key, 'x1':x1, 'y1':y1})
