# django.shortcuts 모듈에서 render 함수를 가져옴
# 템플릿 파일을 렌더링하고 HTTP 응답 객체를 반환
from django.shortcuts import render
# django.http 모듈에서 HttpResponse 클래스를 가져오고 HTTP 응답
from django.http import HttpResponse

# Create your views here.

# 첫 번째 뷰 함수 index를 정의 HTTP 요청 객체인 request를 인자로 받음
def index(request):
    # 문자열 "bbsnote에 오신 것을 환영합니다"를 포함하는 HTTP 응답 객체를 반환합니다.
    return HttpResponse("bbsnote에 오신 것을 환영합니다")

# 두 번째 뷰 함수 index를 정의
# 이 함수는 첫 번째 뷰 함수와 이름이 같으므로 첫 번째 뷰 함수를 덮어쓰게 됩니다.
def index(request):
    # 문자열 "Hello, world."를 포함하는 HTTP 응답 객체를 반환합니다.
    return HttpResponse("Hello, world.")