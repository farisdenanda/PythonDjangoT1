from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View 
from django.http import HttpResponse

class AnggotaView(View):
    def get(self, request):
        template = 'anggota/index.html'
        data = {
            'nama' :'Faris Denanda Aditya Firdaus',
            'umur' : 21,
            'Status' : 'Mahasiswa',
            'ar' : [1,2,3,4],
            'logika' : True
        }
        return render(request, template, data)

