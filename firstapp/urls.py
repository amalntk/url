from django.urls import path
from firstapp import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('reg',views.reg,name='register'),
    path('',views.welcome,name='welcome'),
    path('cipher.html',views.cipher,name='cipher'),
    path('welcome.html',views.logout,name='logout'),
    path('encrypt',views.encrypt,name='encrypt'),
    path('decrypt',views.decrypt,name='decrypt'),
    path('articles',views.articles,name='articles'),
    path('phising.html',views.phising,name='phising'),
    path('predict',views.predict,name='predict'),
    path('safe',views.safe,name='safe'),
    path('unsafe',views.unsafe,name='unsafe')




]
