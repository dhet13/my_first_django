from django.http import HttpResponse
from .models import Memo

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