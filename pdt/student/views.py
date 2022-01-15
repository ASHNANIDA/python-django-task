from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from django.contrib.auth import logout

# Create your views here.
def fnhome(req):
    return render(req,'home.html')
def fnabout(req):
    return render(req,'about.html')
def fnlogin(req):
    if req.method =='POST':
        username = req.POST['username'] 
        password= req.POST['password']
        try:   
            obj1=User.object.create(username=username)
            obj1.set_password(password)
            obj1.save()
            obj2=authenticate(username=username,password=password)
            return render(req,'login.html')
        except Exception as e:
            print(e)
            return render(req,'login.html') 
    
    return render(req,'login.html')
def fnfeed(req):
    if req.method =='POST':
        name = req.POST['name'] 
        print(name)
        email= req.POST['email']
        text= req.POST['text']
        obj1=feedback(name=name,email=email,text=text)
        obj1.save()
        return render(req,'feedback.html')
    return render(req,'feedback.html')
    
def profile(req):

    obj1=student.objects.all()
    print(obj1)
    return render(req,'pro.html',{
        'message':obj1
    })
    
def logout(req):
    try :
        logout(req)
    except:
        return redirect(req,'home.html')
def fnnotif(req):
    return render(req,'notification.html')
def fnregister(req):
    try: 
        phoneno=req.POST['phoneno']
        obj2= student.objects.filter(phoneno=phoneno).exists()
        if obj2== False:
            name = req.POST['name']
            print(name)
            email = req.POST['email']
            password = req.POST['password']
            rollno= req.POST['rollno']
            college = req.POST['college']
            obj1=student(name=name,email=email,password=password,rollno=rollno,college=college,phoneno=phoneno)
            obj1.save()
            return render(req,'register.html',{'message':'user registered'})
        else:
            return render(req,'register.html',{'message':'user already  registered'})

    except Exception as e:
        print(e)
    return render(req,'register.html') 