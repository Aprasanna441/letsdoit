from django.urls import path
from listt import views

urlpatterns = [
    path('', views.welcome,name='welcome'),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("changestatus/<int:id>",views.changestatus,name="changestatus"),
    path("deletetask/<int:id>",views.deletetask,name="deletetask"),
    path('signout',views.signout,name='signout'),
    path('addtodo',views.addtodo,name='addtodo')


]