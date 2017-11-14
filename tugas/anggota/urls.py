from django.conf.urls import url
from anggota import views

urlpatterns = [
    url(r'^lihat$',views.AnggotaView.as_view(), name='view'),

]