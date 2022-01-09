# ページにアクセスがあった時の動作を規定するファイル
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'CalcPlus'
    }
    return render(request, 'calcplus/index.html', params)