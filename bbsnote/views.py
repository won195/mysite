# django.shortcuts 모듈에서 render, redirect 함수를 가져옴
from django.shortcuts import render, redirect
# django.http 모듈에서 HttpResponse 클래스를 가져옴 HTTP 응답
from django.http import HttpResponse
# django.utils 모듈에서 timezone 모듈을 가져옴
from django.utils import timezone
# 현재 디렉토리의 models 모듈에서 Board, Comment 클래스를 가져옴 데이터베이스 테이블
from .models import Board, Comment
from .forms import BoardForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

# 첫 번째 뷰 함수 index를 정의, HTTP 요청 객체인 request를 인자로 받음
def index(request):
    # 입력인자
    page = request.GET.get('page', 1)
    
    # 조회
    # 데이터베이스에서 Board 객체 목록을 가져옴 이 목록은 생성 날짜의 역순으로 정렬
    board_list = Board.objects.order_by('-create_date')
    # board_list는 페이지로 나눌 데이터 목록이고 3는 한 페이지에 표시할 항목 수
    paginator = Paginator(board_list, 3)
    # get_page 메소드는 페이지 번호를 받아 해당 페이지를 리턴
    page_obj = paginator.get_page(page)
    
    # 컨텍스트 변수, 템플릿에 전달되어 렌더링에 사용
    context = {'board_list': page_obj}
    ##return HttpResponse("bbsnote에 오신 것을 환영합니다")
    # 템플릿 파일 'bbsnote/board_list.html'을 렌더링하여 HTTP 응답 객체를 반환 
    return render(request, 'bbsnote/board_list.html', context)

# HTTP 요청 객체인 request와 정수형 변수인 board_id를 인자로 받음
def detail(request, board_id):
    # 데이터베이스에서 id가 board_id인 Board 객체를 가져옴
    board = Board.objects.get(id=board_id)
    # 컨텍스트 변수, 이 변수는 템플릿에 전달되어 렌더링에 사용
    context = {'board': board}
    # 템플릿 파일 'bbsnote/board_detail.html'을 렌더링하여 HTTP 응답 객체를 반환
    return render(request, 'bbsnote/board_detail.html', context)

# 사용자가 로그인하지 않은 상태에서 이 뷰 함수에 접근하려고 할 때 common:login으로 지정된 URL로 리다이렉트 
@login_required(login_url='common:login')
# request와 board_id라는 두 개의 인자를 받음
def comment_create(request, board_id):
    # POST인 경우에만 다음 코드를 실행
    if request.method == 'POST':
        # Board 모델에서 id가 board_id와 일치하는 객체를 가져와서 board 변수에 저장
        board = Board.objects.get(id=board_id)
        ## comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
        ## comment.save()
        # # content=request.POST.get('content') : content 필드를 요청의 POST 데이터에서 'content' 키의 값을 가져와서 설정
        
        # create_date=timezone.now() : create_date 필드를 현재 시간으로 설정
        # author=request.user : 현재 로그인한 사용자의 인스턴스를 가져와서 author 필드에 설정
        board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    # 'bbsnote:detail'으로 지정된 URL로 리다이렉트, 인자로 board_id가 전달
    return redirect('bbsnote:detail', board_id=board_id)

# 이 데코레이터는 사용자가 로그인하지 않은 상태에서 해당 뷰 함수나 메소드에 접근하려고 할 때, 지정된 로그인 URL로 리다이렉트
@login_required(login_url='common:login')
# board_create라는 이름의 뷰 함수 정의 request 객체를 인자로 받음
def board_create(request):
    # 요청의 HTTP 메소드가 'POST’인지 확인
    if request.method == 'POST':
        # ‘POST’ 요청의 데이터를 사용하여 BoardForm 객체 생성
        form = BoardForm(request.POST)
        # valid 로 True, False폼이 유효한지 검사
        if form.is_valid():
            # 폼 데이터를 사용하여 board 객체를 생성하고 데이터베이스에 저장하지 않함
            board = form.save(commit=False)
            # board 객체의 creat_date 속성을 현재 시간으로 설정
            # board.creat_date = timezone.now()
            board.author=request.user
            # board 객체를 데이터베이스에 저장
            board.save()
            # 'bbsnote:index’라는 이름의 URL로 리다이렉트
            return redirect('index')
    # HTTP 메소드가 'POST’가 아닌 경우 실행
    else:
        # 빈 BoardForm 객체를 생성
        form = BoardForm()
    # ‘bbsnote/board_form.html’ 템플릿을 사용하여 응답을 생성하고, 템플릿 컨텍스트에 ‘form’ 변수로 폼 객체를 전달
    return render(request, 'bbsnote/board_form.html', {'form':form})