from django.urls import path

from user import views

urlpatterns = [
    path("register/",views.UserAPIView.as_view()),
    path("check_emp/",views.EmpView.as_view()),
    path("check_emp/<str:id>",views.EmpView.as_view())
]