from django.urls import path
from reports.views import (
    report_list,
    report_detail,
    report_create,
    report_update,
    report_delete,
)

urlpatterns = [
    path('', report_list, name='report_list'),
    path('report/<int:pk>/', report_detail, name='report_detail'),
    path('report/create/', report_create, name='report_create'),
    path('report/<int:pk>/update/', report_update, name='report_update'),
    path('report/<int:pk>/delete/', report_delete, name='report_delete'),
]
