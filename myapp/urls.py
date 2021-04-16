from django.urls import path
from myapp import views
app_name="myapp"#name of the urlspace
#name of the url space is not mandatory
#if it is not given navigation jinja tag will be {% url 'mappingname' %}
urlpatterns = [
    path('sample2/<data>',views.sample2,name="sample2"),
    path('sample3/',views.sample3,name="sample3")
    
]