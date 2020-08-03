from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice

# views의 function이 하는 일은 request를 받아서
# 결과 template html을 이용해서 결과 파일을 만들어 내는 일
def index(request):
    # 데이터베이스에서 질문의 목록을 가져옴
    # 원래는 문자열로 표현돼야 하는데 ORM을 사용하다 보니,
    # 각 record가 Question class의 객체로 표현
    my_list = Question.objects.all().order_by('-pub_date')
    context = {'question_list': my_list}
    return render(request, 'index.html', context)


def detail(request, page_num1):
    tmp = get_object_or_404(Question, pk=page_num1)
    context = {'question': tmp}
    return render(request, 'detail.html', context)

def vote(request, page_num2):
    # URL로 넘어온 데이터(page_num2)는 Question 객체의 id
    question = get_object_or_404(Question, pk=page_num2)
    # request header 안에 form에서 선택한 데이터가 포함되서 전달되고
    # 이것을 추출하기 위해서 request.POST('choice')를 사용
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    choice = get_object_or_404(Question, pk=page_num2)
    context = {'votes_result': choice}
    #result.html에서 현재 투표 항목에 대한 각 항목들의 투표현황을 출력
    return render(request, 'result.html', context)