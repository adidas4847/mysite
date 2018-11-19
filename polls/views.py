from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question

def save(request, question_id):
    q = request.POST['q']
    question = Question.objects.get(id = question_id)
    question.question_text =q
    question.save()

    return HttpResponse('수정완료')


def edit(request, question_id):
    q =Question.objects.get(id=question_id)

    return render(
        request, 'polls/edit.html',{'q':q}
    )

def vote(request, question_id):
    q=Question.objects.get(id=question_id)

    try:
        select = request.POST['select']


        c=q.choice_set.get(id=select)

        c.votes +=1
        c.save()

        print(select)
    except:
        pass
    return render(
        request,
        'polls/result.html',
        {'q':q}
    )

def index(request):

    # 1번 create를 이용하여 데이터 입력
    # Question.objects.create()

    # 2번 save를 이용하여 데이터 입력
    # Question(question_text='aaaa', pub_date=timezone.now()).save()

    questions=Question.objects.all()

    return render(request,'polls/index.html',{'question' : questions})


def detail(request, question_id): # 질문 상세 페이지
    q = Question.objects.get(id=question_id) #조건에 맞는 데이터 1개 조회
    c = q.choice_set.all()
    choice =''
    for a in c:
        choice+=a.choice_text
# 랜더 사용법 =    request,템플릿,컨테스트(데이터)
    return render(
        request,
        'polls/detail.html',
        {
            'question' : q.question_text,
            'num':q.id,
            'choice' : c
        }
    )
#    return HttpResponse(q.question_text+'<br>'+ choice) #문자연 + 리스트x

def detail2(request, num1, num2): # 질문 상세 페이지
    return HttpResponse(num1+num2)