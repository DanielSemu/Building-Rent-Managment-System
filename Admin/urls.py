from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('Adminhome/',views.Adminhome,name="Adminhome"),
    path("addblock/", views.Add_Block, name="addblock"),
    path("addroom/", views.Add_Room, name="addroom"),
    path("addrole/", views.Add_Role, name="addrole"),
    path("addblocklocation/", views.Add_Block_Location, name="addblocklocation"),
    path("viewblock/", views.view_block, name="viewblock"),
    path("viewroom/<int:pk>", views.view_room, name="viewroom"),
    path("editblock/<int:pk>", views.edit_block, name="editblock"),
    path("editroom/<int:pk>", views.edit_room, name="editroom"),
    path("deleteroom/<int:pk>", views.delete_room, name="deleteroom"),
    path("delete_block/<int:pk>", views.delete_block, name="delete_block"),
    path("registerUser", views.registerUser, name="registerUser"),
    path("viewuser",views.view_user, name='viewuser'),
    path("edit_user/<int:pk>",views.edit_user, name="edit_user"),
    path("room_status",views.roomstatus,name='room_status'),
    path("logout/", views.logout_View, name="logout"),
]