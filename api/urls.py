from django.urls import path

from api import views

urlpatterns=[ 
    path("",views.prodListAPIView.as_view(),name="todo_list"),
    path("ta/",views.tamilresults.as_view(),name="suma"),
    path("getdata/",views.getdata.as_view(),name="getdata"),
    path("create/", views.prodcreateAPIView.as_view(),name="todo_create"),
    path("get/<int:pk>/",views.getAPIVIEW.as_view(),name="get"),
    #path("update/<int:pk>/",views.empupdateAPIView.as_view(),name="update_todo"),
    #path("delete/<int:pk>/",views.empdeleteAPIView.as_view(),name="delete_todo"),
    #path("get/<str:emp_type>/",views.test,name="test")

]