from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('good/', views.good),
    path('debug/', views.debug_request),
    path('memo/', views.memo_list, name='memo_list'),
    path('memo/stats/', views.memo_stats, name='memo_stats'),
    path("", views.index, name='index'),
    path('demo/', views.demo_index, name='demo_index')
]