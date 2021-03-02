from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.http import JsonResponse,HttpResponse
from django.core import serializers

def home(request):
    form = StudentForm()
    students = Student.objects.all().order_by("-id")
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize("json",[instance,])
            return JsonResponse({"instance":ser_instance},status=200)
    context={"form":form,"students":students}
    return render(request, 'core/home.html',context)

def delete_one(request,pk):
    list = Student.objects.get(id=pk)
    list.delete()
    return redirect('/')

