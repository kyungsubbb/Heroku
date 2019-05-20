from django.shortcuts import render

# Create your views here.
def wordhome(request) :
    return render(request,'wordhome.html')

def worddetail(request) :
    return render(request,'worddetail.html')

def wordresult(request) :
    
    text = request.GET['fulltext']                       # 전체 텍스트 받아오기
    word = text.split()                                  # 총 단어 수 개수 받아오기
    word_dic ={}

    for wds in word :                                    # wds는 키값이 된다.
        if wds in word_dic:
            word_dic[wds] += 1
        else :
            word_dic[wds] = 1
    return render(request, 'wordresult.html', {'full' : text, 'total' : len(word), 'dictionary' : word_dic.items()}) #full이라는 key값을 text라는 value값으로...

