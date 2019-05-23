from django.test import TestCase
import xmltodict, requests
import os, sys
from django.shortcuts import render

# Create your tests here.
sys.path.append(os.path.abspath("/hospitalAPI/config"))
# API_SERVICE_KEY = os.environ.get('SERVICE_KEY')
API_SERVICE_KEY = f'HIPqS2%2BvxCTE%2FqhEWGTGogUVa7QqA0HDnLToATbxzmOWU6%2F9ZD1ABF4ex%2FUEEHLr188T7I%2BpeEdBKe27i7dynA%3D%3D'

raw_data = f'http://apis.data.go.kr/B551182/hospInfoService/getHospBasisList?pageNo=1&sidoCd=110000&numOfRows=1000&sgguCd=110019&ServiceKey={API_SERVICE_KEY}'
data = requests.get(raw_data).content

xmlObject = xmltodict.parse(data)

a = xmlObject['response']['body']['items']['item']
infos = []
if 'emdongNm' in a:
    for i in a:
        infos.append({
            'name':i['yadmNm'],
            'x':i['XPos'],
            'y':i['YPos'],
            'dong':i['emdongNm']
        })
else:
    for i in a:
        infos.append({
            'name':i['yadmNm'],
            'x':i['XPos'],
            'y':i['YPos'],
            'dong':None
        })
print(infos['dong'])