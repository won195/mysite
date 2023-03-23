# django.apps 모듈에서 AppConfig 클래스 import
from django.apps import AppConfig


# AppConfig를 상속하는 클래스 BbsnoteConfig를 정의
class BbsnoteConfig(AppConfig):
    # default_auto_field 속성의 기본값을 'django.db.models.BigAutoField'로 설정 
    # 새로운 모델을 생성할 때 사용할 기본 키 필드의 유형을 지정
    default_auto_field = 'django.db.models.BigAutoField'
    # name 속성의 값을 'bbsnote'로 설정
    name = 'bbsnote'