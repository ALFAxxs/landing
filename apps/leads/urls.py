# apps/leads/urls.py

from django.urls import path
from apps.leads import views

urlpatterns = [
    path('',                           views.index,              name='index'),
    path('admin-panel/login/',         views.admin_login,        name='admin_login'),
    path('admin-panel/logout/',        views.admin_logout,       name='admin_logout'),
    path('admin-panel/',               views.admin_leads,        name='admin_leads'),
    path('admin-panel/<int:pk>/',      views.admin_lead_detail,  name='admin_lead_detail'),
    path('admin-panel/<int:pk>/status/', views.admin_lead_status, name='admin_lead_status'),
    path('admin-panel/export/csv/',    views.admin_export_csv,   name='admin_export_csv'),
]
