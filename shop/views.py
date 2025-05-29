
from django.shortcuts import render
from .models import Product
from django.db import connection

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})
def repair_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM repairrequest")
        columns = [col[0] for col in cursor.description]
        repairs = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, "shop/repair_list.html", {"repairs": repairs})

def schedule_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM schedule")
        columns = [col[0] for col in cursor.description]
        schedules = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return render(request, "shop/schedule_list.html", {"schedules": schedules})