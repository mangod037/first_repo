from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    textList = text.split()
    textcount = len(textList)

    textSetList = list(set(textList))
    textDic = {}
    for i in textSetList:
        textDic[i] = 0
    for i in textList:
        textDic[i] += 1
 
    return render(request, 'result.html', {
    'text':text,
    'textcount':textcount,
    'textDic':textDic,
})