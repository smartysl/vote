from django.urls import path
from . import views
urlpatterns=[
    path('<int:question_id>/',views.detail,name="detail"),
    path('<int:question_id>/result/',views.result,name="result"),
    path('<int:question_id>/vote/',views.vote,name="vote"),
    path('',views.index,name="index"),
    path('regist/',views.register,name="regist"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout")
]