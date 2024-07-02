from django.shortcuts import render
from django.http import HttpResponse
from myApp.forms import FeedBackForm

# def view1(request):
#     s="welocme to python web development"
#     return HttpResponse(s)

# def view2(request):
#     n1=int(input("enter frist name"))
#     n2=int(input("enter second name"))
#     n3=n1+n2
#     return HttpResponse(str(n3))

def feedbackView(request):
    f=FeedBackForm()
    if request.method=="POST":
        f=FeedBackForm(request.POST)
        if f.is_valid():
            name=f.cleaned_date['name']
            rollno=f.cleaned_data['rollno']
            email=f.cleaned_data['email']
            feedback=f.cleaned_data['feedback']
            d={'name':name,'rollno':rollno,'email':email,'feedback':feedback}
            return render(request,'myapp/output.html',d)
    d={'form':f}
    return render(request,'myapp/feedback.html',d)
