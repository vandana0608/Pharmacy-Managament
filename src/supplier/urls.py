from django.urls import path

from . import views

urlpatterns = [
    path('', views.SupplierList.as_view(), name='supplier_list'),
    path('view/<pk>', views.SupplierView.as_view(), name='supplier_view'),
    path('new', views.SupplierCreate.as_view(), name='supplier_new'),
    path('view/<pk>', views.SupplierView.as_view(), name='supplier_view'),
    path('edit/<pk>', views.SupplierUpdate.as_view(), name='supplier_edit'),
    path('delete/<pk>', views.SupplierDelete.as_view(), name='supplier_delete'),
]