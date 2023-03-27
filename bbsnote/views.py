# django.shortcuts 모듈에서 render, get_object_or_404, redirect 함수를 가져옴
from django.shortcuts import render, get_object_or_404, redirect
# django.http 모듈에서 HttpResponse 클래스를 가져옴 HTTP 응답
from django.http import HttpResponse
# django.utils 모듈에서 timezone 모듈을 가져옴
from django.utils import timezone
# 현재 디렉토리의 models 모듈에서 Board, Comment 클래스를 가져옴 데이터베이스 테이블
from .models import Board, Comment
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.

# 첫 번째 뷰 함수 index를 정의, HTTP 요청 객체인 request를 인자로 받음
def index(request):
    # 입력인자
    page = request.GET.get('page', 1)
    
    # 조회
    # 데이터베이스에서 Board 객체 목록을 가져옴 이 목록은 생성 날짜의 역순으로 정렬
    board_list = Board.objects.order_by('-create_date')
    # board_list는 페이지로 나눌 데이터 목록이고 5는 한 페이지에 표시할 항목 수
    paginator = Paginator(board_list, 5)
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

# 뷰 함수인 comment_create를 정의
# HTTP 요청 객체인 request와 정수형 변수인 board_id를 인자로 받음
def comment_create(request, board_id):
    # 데이터베이스에서 id가 board_id인 Board 객체를 가져옴
    board = Board.objects.get(id=board_id)
    # 이 객체의 속성값은 인자로 전달된 값으로 설정 
    # 여기서 content 속성값은 POST 데이터 중 content 키의 값으로 설정
    comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # Comment 객체를 데이터베이스에 저장
    comment.save()
    # bbsnote:detail이라는 URL 패턴으로 리디렉션하고 board_id라는 인자로 board.id 값을 전달
    # 사용자가 특정 게시판의 세부 정보 페이지로 이동
    return redirect('bbsnote:detail', board_id = board.id)

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
            board.creat_date = timezone.now()
            # board 객체를 데이터베이스에 저장
            board.save()
            # 'bbsnote:index’라는 이름의 URL로 리다이렉트
            return redirect('bbsnote:index')
    # HTTP 메소드가 'POST’가 아닌 경우 실행
    else:
        # 빈 BoardForm 객체를 생성
        form = BoardForm()
    # ‘bbsnote/board_form.html’ 템플릿을 사용하여 응답을 생성하고, 템플릿 컨텍스트에 ‘form’ 변수로 폼 객체를 전달
    return render(request, 'bbsnote/board_form.html', {'form': form})