from django.urls import path

from . import views

urlpatterns = [
    path('microtask/', views.microtask, name='microtask'),
    path('MALrequirements/',views.handleSubmit, name='MALrequirements'),
    path('home/',views.index, name='home'),
    path('posting/<pk>',views.posting_page,name ='Posting_Page'),
]