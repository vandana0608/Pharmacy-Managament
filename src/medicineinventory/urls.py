# from django.contrib import admin
# from django.conf.urls import url
# from .views import (medicineinventory_update_quantity_view)

# urlpatterns = [
#      url(r'^(?P<id>\d+)/edit/$', medicineinventory_update_quantity_view, name='edit'),
#      ]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.MedicineinventoryList.as_view(), name='medicineinventory_list'),
    path('view/<pk>', views.MedicineinventoryView.as_view(), name='medicineinventory_view'),
    path('new', views.MedicineinventoryCreate.as_view(), name='medicineinventory_new'),
    path('view/<pk>', views.MedicineinventoryView.as_view(), name='medicineinventory_view'),
    path('edit/<pk>', views.MedicineinventoryUpdate.as_view(), name='medicineinventory_edit'),
    path('delete/<pk>', views.MedicineinventoryDelete.as_view(), name='medicineinventory_delete'),
]
