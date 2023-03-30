# django.db 모듈에서 models를 가져옴
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

#models.Model을 상속하는 새로운 클래스 Board를 정의 데이터베이스 테이블을 나타냄
class Board(models.Model):
    # Board 클래스의 속성으로 문자열 필드 subject를 정의 최대 길이 200자인 필드
    subject = models.CharField(max_length=200)
    # Board 클래스의 속성으로 텍스트 필드 content를 정의
    content = models.TextField()
    # ForeignKey로 User 모델과 연결하고  on_delete=models.CASCADE는 User 객체가 삭제될 때 이 객체도 함께 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Board 클래스의 속성으로 날짜/시간 필드 create_date를 정의 
    # 객체가 처음 생성될 때 자동으로 현재 날짜/시간으로 설정
    create_date = models.DateTimeField(auto_now_add=True)
    # Board 클래스의 속성으로 날짜/시간 필드인 update_date를 정의 
    # 객체가 저장될 때마다 자동으로 현재 날짜/시간으로 갱신
    update_date = models.DateTimeField(auto_now=True)

    # 객체가 문자열로 표현될 때 호출 예를 들어, 객체를 출력할 때
    def __str__(self):
        # [id] subject 형식의 문자열을 반환
        # 여기서 id와 subject는 각각 객체의 id와 subject 속성값
        return f'[{self.id}] {self.subject}'

# models.Model을 상속하는 새로운 클래스인 Comment를 정의 이 클래스는 데이터베이스 테이블
class Comment(models.Model):
    # 외래키 필드인 Board를 정의 이 필드는 Board 모델과 관계있음
    # on_delete 옵션은 Board 객체가 삭제될 때 관련된 Comment 객체도 함께 삭제되도록 지정
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # Comment 클래스의 속성으로 텍스트 필드 content를 정의
    content = models.TextField()
    
    # ForeignKey로 User 모델과 연결하고  on_delete=models.CASCADE는 User 객체가 삭제될 때 이 객체도 함께 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # like = models.IntegerField(blank=True, default=0)

    # 객체가 처음 생성될 때 자동으로 현재 날짜/시간으로 설정
    create_date = models.DateTimeField(auto_now_add=True)
    # 객체가 저장될 때마다 자동으로 현재 날짜/시간으로 갱신
    update_date = models.DateTimeField(auto_now=True)
