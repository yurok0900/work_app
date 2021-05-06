from django.urls import path
from . import views

urlpatterns=[
    path('', views.list_view, name = "index"),
    path('create/', views.create_view, name = "create"),
    path('createtext/', views.create_text, name = "create_text"),
    path('<int:recv_id>/', views.template_detail_view, name = "detail_view"),
    path('update/<int:recv_id>/', views.update_view, name = "update_view"),
    path('updatetext/<int:recv_id>/', views.update_text_view, 
         name = "update_text"),
    path('delete/<int:recv_id>/', views.delete_view, name = "delete_view"),
    path('genermessage/', views.generate_message, name = "generate_message"),
        
]
