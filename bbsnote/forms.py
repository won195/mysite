# 장고의 forms 모듈을 가져옴
from django import forms
# bbsnote 앱의 models 모듈에서 Board 모델을 가져옴
from bbsnote.models import Board

# BoardForm이라는 모델 폼을 정의 forms.ModelForm을 상속
class BoardForm(forms.ModelForm):
    # 내부 클래스인 Meta 클래스를 정의 모델 폼의 옵션 지정
    class Meta:
        # model 속성으로 Board 모델을 지정 BoardForm은 Board 모델과 연결
        model = Board
        # fields 속성으로 ['subject', 'content']를 지정합니다. 
        # 이렇게 하면 BoardForm에서 subject와 content 필드만 사용하여 데이터를 생성하거나 수정할 수 있습니다.
        fields = ['subject','content']
        # widgets = {
        #     'subject' : forms.TextInput(attrs={'class':'form=control'}),
        #     'content' : forms.Textarea(attrs={'class':'form-control','rows':10}),
        # }
        # labels = {
        #     'subject' : '제목',
        #     'content' : '내용',
        # }