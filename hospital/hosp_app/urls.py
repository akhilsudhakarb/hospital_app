from django.urls import path

from hosp_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('appointment', views.make_appointment, name='make-appointment'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('get-doctor/<str:slug>', views.get_doc, name='get-doctor'),
    path('get-doctor/<int:id>/<str:slug>', views.doc_details, name='doctor'),
    path('ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'),
]