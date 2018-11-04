from django.urls import path
from .views import *
app_name='blog'

urlpatterns=[
    #뷰클래스를 url등록할때 , 뷰 클래스명.as_view()로 등록해야함
    path('',Index.as_view(),name='index'),
    path('<int:pk>/',Detail.as_view(), name='detail'),
    path('postR/', PostRegiste.as_view(), name='postR')
    ]