from django.contrib import admin
from django.urls import path, re_path
from wallettrust import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/wallets/<str:WALLET_UUID>/operation', views.info),      http://localhost:8000/wallet/12/?operationType=dep&amount=100
    path('wallet/<str:WALLET_UUID>/', views.info)

]
