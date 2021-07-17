from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Bùi văn Mạnh"
    myasset = {"Điện thoại", "Máy tính", "Xe máy", "Balo", "Tri thức", "Người yêu", "Giày"}
    context = {
        "name": name,
        "asset": myasset
    }
    return render(request, "app_all_res/index.html", context)