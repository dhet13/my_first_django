<<<<<<< HEAD
# polls/views.py에 간단한 뷰 작성
from django.contrib.auth.forms import User
from django.http import HttpResponse

# 장고 페이지 구성의 핵심
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article, Memo

# index에서 context 만들어서 보내기기
def index(request):
    return render(request=request,template_name="polls/index.html")
    
# def blog_list(request):
#     return render(request,"not_good.html")

def lion(request,name):
    return HttpResponse(f"""{name}가 장고를 배웁니다!!""")

# 내가 request라는 객체가 생소한데, 안에 어떤 내용들이 있는지 확인해 보고 싶어
# 이거를 하나의 뷰로 만들어서 웹에 표시해 볼까?
# 디버그 하는 역할 이네 -> dubug_request로 이름짓자
def dubug_request(request):
    # request 의 메서드와
    # request 의 path
    # request 의 META.REMOTE_ADDR를 화면에 표시하자!!
    content = f"""이것이 request가 가지고 있는 정보의 예시입니다.<br>
    request.path = {request.path}    <br>
    request.method = {request.method}    <br>
    request.META.REMOTE_ADDR = {request.META.get('REMOTE_ADDR', 'Unknown')}    <br>
    """
    return HttpResponse(content)

# 디버그 버튼누르시고, launch.json파일 만들기 선택(우리가 디버그 설정을 직접 관리하는 방법)
# 엉뚱한 디버그들 선택해 보기(실수를 해도 스트레스 받지 않기?!)
# 생성된 launch.json을 삭제하고 다시 장고 디버그 설정으로 수정하기
# 디버그 가동(F5 또는 디버그 버튼 클릭)
# 디버그 뷰에서 브레이크 포인트 잡기(코드 왼쪽 숫자의 왼쪽을 클릭, 또는 f9)
# 해당 포인트에 멈추게 해보기!!(서버를 가동하고 해당 뷰가 호출되도록 브라우저에서 주소 입력)
# 디버그 콘솔에서 이것저것 해보기기
# 9시 50분까지 하겠습니다!!!




# 여러개 여러분 마음대로 만들어 보세요!

# view 만들기
# polls에 urls.py 작성
# path("경로",뷰함수)

# config urls.py
# path("아무거나경로", inclued(polls.urls))

# 브라우저에서 확인


# 3시 20분까지
# 각 url로 접근하여 페이지가 나오도록 해보겠습니다.
# 1. /polls/hello/ -> "안녕하세요" 라고 페이지에 표시하기
# 2. /polls/good/ -> AI를 통해 작성된 다양한 페이지 표시하기

# 2시 40분까지 ORM 체험해 보겠습니다~!

# 메모리스트를 보여주는 뷰를 만들어 보겠습니다.
def memo_list(request):
    # 메모 전체 가져오기
    memos=Memo.objects.all()
    # # content 구성하기
    # content=""
    # for memo in all_memo:
    #     content += "제목 : "+memo.title+"<br>"
    #     content += "내용 : "+memo.content+"<br>"
    #     content += "----"*10
    #     content += "<br>"
    context = {
        "memos":memos
    }
    return render(request, 'polls/memo_list.html', context)

def test1(request):
    return render(request, 'polls/index.html')

def test2(request):
    return render(request,'polls/test2.html')

from .forms import MemoModelForm
from django.contrib.auth.decorators import login_required

# update와 delete 기능을 개발해 보겠습니다!!
# 그냥 개발 시작해 보시고
# 막히는 부분 있으면 교안 또는 직원 참고해서 완성해 보겠습니다!
# 10:50 까지 하겠습니다!


@login_required
def memo_create(request):
    if request.method=="POST":
        # title = request.POST.get['title']
        # form??
        # return ??
        form = MemoModelForm(request.POST)
        if form.is_valid():
            # 직접 입력되지 않는 정보(ex- user)를 추가 입력할때는 form.save(commit=False)를 사용한다!
            user= User.objects.get(pk=request.POST['author'])
            memo=form.save(commit=False)            
            memo.author=user
            memo.save()
            # 
            #-------------------------------------------------
            # 1. 메모리스트? list
            # return redirect('polls:memo_list')
            # 2. 지금 작성한 메모를 보여주기? detail
            #-------------------------------------------------
            return redirect('polls:memo_detail',pk=memo.id)
        # 1.form을 이용해서 저장하는 프로세스 체크
        # 2.페이지 요청할때, 인자를 담아서 보내기
        # 3. 과제 -> memo detail 페이지 기존에 하드코딩된 형태에서 template이용한 내용으로 변경하기기
        # 9시 50분까지 진행해 보겠습니다!

    else:
        form = MemoModelForm()
        return render(request, 'polls/memo_create.html', context={'form':form})
    # # step 1
    # # 고객이 입력할 수 있는 화면 보여주기
    # if request.method=='GET':
    #     return render(request,'polls/memo_create.html')
    # # step 2
    # # 고객이 입력한 정보를 확인 -> 고객이 입력한 정보 어디있나?
    # # title, content
    # # Memo에 입력
    # # 다음 페이지로 보내기
    # else:
    #     title = request.POST.get('title','no_title') # request.POST['title']
    #     content = request.POST.get('content','no content')
    #     Memo.objects.create(title=title, content=content)
    #     return redirect('polls:memo_list')       

# content = "제목 : 타이틀
# 내용 : 콘텐트
# 제목 : 타이틀
# 내용 : 콘텐트
# 제목 : 타이틀
# 내용 : 콘텐트
# " 줄바꿈 -> <br>
@login_required
def my_memo_list(request):

    # memos=Memo.objects.filter(author=request.user)
    memos = request.user.memos.all()

    context = {
        "memos":memos
    }
    return render(request, 'polls/my_memo_list.html', context)


def memo_detail(request, pk):
    # memo = Memo.objects.get(id=pk)
    memo = get_object_or_404(Memo, pk=pk)
    return render(request,'polls/memo_detail.html', {"memo":memo})
    # content = f"""<h1>제목 : {memo.title}</h1> <br><br> 
    # 내용 : {memo.content}<br>
    # {memo.is_important}<br>
    # {memo.created_at}
    # """
    # return HttpResponse(content)
from django.contrib import messages
@login_required
def memo_update(request, pk):
    """메모 수정 - 작성자만 가능"""
    memo = get_object_or_404(Memo, pk=pk)

    # 작성자 확인
    if memo.author != request.user:
        messages.error(request, '자신의 메모만 수정할 수 있습니다.')
        return redirect('polls:memo_detail', pk=pk)

    if request.method == 'POST':
        form = MemoModelForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            messages.success(request, '메모가 수정되었습니다.')
            return redirect('polls:memo_detail', pk=pk)
    else:
        form = MemoModelForm(instance=memo)

    return render(request, 'polls/memo_form.html', {
        'form': form,
        'is_update': True
    })

from django.core.exceptions import PermissionDenied
@login_required
def memo_delete(request, pk):
    """메모 삭제 - 작성자만 가능"""
    memo = get_object_or_404(Memo, pk=pk)

    # 작성자 확인
    if memo.author != request.user:
        raise PermissionDenied('삭제 권한이 없습니다.')

    if request.method == 'POST':
        memo.delete()
        messages.success(request, '메모가 삭제되었습니다.')
        return redirect('polls:memo_list')

    return render(request, 'polls/memo_confirm_delete.html', {'memo': memo})
# 1. CRUD
# 2. Update Delete에 해당하는 뷰, 템플릿 구성
# 3. 각 템플릿에 base.html 적용

from django.db.models import Q
def memo_search(request):
    # base.url의 검색 영역을 form으로 감싸기
    # polls urls.py에 검색 url 추가
    # views에 memo_search 작성 준비
    query = request.GET.get('q',"")
    memos = Memo.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    context = {
        "memos":memos
    }
    return render(request, 'polls/my_memo_list.html', context)
=======
from django.http import HttpResponse
from django.shortcuts import render
from .models import Memo

def index(request):
    memos = Memo.objects.all()
    context = {
        'name': '홍길동',
        'context': '장고 템플릿 연습',
        'memos': memos
    }
    return render(request, 'polls/index.html', context)


def hello(request):
    return HttpResponse ("안녕하세요")

def good(request):
    return HttpResponse ("""
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>화려한 웹페이지</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(135deg, #667eea, #764ba2);
      color: #fff;
      text-align: center;
      animation: fadeIn 2s ease-in;
    }

    header {
      padding: 50px 0;
      background-color: rgba(0, 0, 0, 0.2);
      font-size: 2.5em;
      font-weight: bold;
    }

    .container {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      padding: 30px;
    }

    .card {
      background: white;
      color: #333;
      border-radius: 15px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.3);
      margin: 20px;
      padding: 30px;
      width: 300px;
      transition: transform 0.3s, box-shadow 0.3s;
    }

    .card:hover {
      transform: translateY(-10px);
      box-shadow: 0 15px 30px rgba(0,0,0,0.4);
    }

    footer {
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.1);
      font-size: 0.9em;
    }

    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  </style>
</head>
<body>

  <header>
    🌟 화려한 나의 첫 웹페이지 🌟
  </header>

  <div class="container">
    <div class="card">
      <h3>깔끔한 카드 디자인</h3>
      <p>이 카드는 CSS로 스타일링되어 있으며, 마우스를 올리면 애니메이션 효과가 적용됩니다.</p>
    </div>
    <div class="card">
      <h3>반응형 디자인</h3>
      <p>화면 크기에 따라 자동으로 배치가 조정됩니다.</p>
    </div>
    <div class="card">
      <h3>그라디언트 배경</h3>
      <p>배경은 그라디언트로 구성되어 있어 화려한 느낌을 줍니다.</p>
    </div>
  </div>

  <footer>
    ⓒ 2025 나의 멋진 웹페이지 – [GPT Online](https://gptonline.ai/ko/)
  </footer>

</body>
</html>
""")

def debug_request(request):
    return HttpResponse("디버그 확인")

def memo_list(request):
    #중요한 메모와 일반 메모 구분분
    important_memos = Memo.objects.filter(is_important=True)
    normal_memos = Memo.objects.filter(is_important=False)

    html = ""
    html += "<html><body>"
    html += "<h1> 나의 메모 </h1>"

    #중요 메모
    html += "<h2> 중요한 메모 </h2>"
    if important_memos:
        html += "<ul>"
        for memo in important_memos:
            html += f"<li><strong>{memo.title}</strong> - {memo.content[:50]}...</li>"
        html += "</ul>"
    else:
        html += "<p> 중요한 메모가 없습니다. </p>"

    #일반 메모
    html += "<h2> 일반 메모 </h2>"
    if normal_memos:
        html += "<ul>"
        for memo in normal_memos:
            html += f"<li><strong>{memo.title}</strong> - {memo.content[:50]}...</li>"
        html += "</ul>"
    else:
        html += "<p> 일반 메모가 없습니다. </p>"

    html += f"<hr><p> 전체 메모: {Memo.objects.count()}개 </p>"
    html += "<a href='/admin/polls/memo/add/'> 새 메모 추가 (Admin) </a>"
    html += "</body></html>"

    return HttpResponse(html)

def memo_stats(request):
    """메모 통계 페이지"""
    total = Memo.objects.count()
    important = Memo.objects.filter(is_important=True).count()
    # normal = Memo.objects.filter(is_important=False).count()

    html = f"""
  <html>
  <body>
    <h1> 메모 통계 </h1>
    <p> 전체 메모 개수: {total}개 </p>
    <p> 중요 메모 개수: {important}개</p>
    <p> 일반 메모 개수: {total -important}개</p>
    <p> 중요 메모 비율: {important / total * 100:.1f}% </p>
    <hr>
    <a href="/memo/"> 메모 목록으로 </a>
  </body>
  </html>
  """
    return HttpResponse(html)
>>>>>>> d08acb3d802c4d43e517fb5a0c8d9db6c115538e
