from django.conf.urls import url
from basic_app import views
from django.urls import path

app_name = 'basic_app' #For template tagging in relative_urls_template.html, the name assigned here gets used.

urlpatterns= [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative')
]
