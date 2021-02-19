from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import newreq
from .models import proof
from django.core.mail import send_mail



from django.core.mail import EmailMultiAlternatives


from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def home(request):
    return render(request,"1_homepage.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('customer_signin_left.html')
        else:
            messages.info(request, 'passwords do not match')
            return redirect("register")
    else:
        return render(request,"customer_register_left.html")
def newrequest_sub(request):
    if request.method == 'POST':
        nickname = request.POST['username']
        location = request.POST['location']
        area = request.POST['area']
        aadhar = request.POST['aadhar']
        land_docs=request.POST['land_docs']
        a= newreq( nickname = nickname, location = location, area = area , aadhar = aadhar, land_docs = land_docs )
        a.save()
        c=(int(area)*100)
        print(c)
        subject = 'tst'
        message = f' Your request for {location} location has been accepted You are required to plant  {c} trees of  type  ashoka tree in east delhi location. You are also required to submit the proof of the same'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["kvgaming1501@gmail.com", ]
        send_mail(subject, message, email_from, recipient_list)


        return redirect("homepage_customer.html")
    else:
        return render(request, 'newrequest-customer.html')


def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['pass']
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            messages.info(request,'invalid credentials')
            return redirect("customer_signin_left.html")
        else:
            if x.is_staff is True:
               return redirect('homepage_admin.html')
            else:
                auth.login(request,x)
                return render(request,'homepage_customer.html')

    else:
        return render(request,"customer_signin_left.html")


def homepage_admin(request):
    return render(request,"homepage_admin.html")

def homepage_customer(request):
    return render(request,"homepage_customer.html")
def about(request):
    return render(request,"about.html")
def two_customer(request):
    return render(request,"2ndpage_customer.html")
def newrequest1(request):
    return render(request,'newrequest-customer.html')
def add_proof(request):
    if request.method == 'POST':
        urname = request.POST['username']
        image1 = request.POST['image1']
        image2 = request.POST['image2']
        image3 = request.POST['image3']
        image4 = request.POST['image4']
        b = proof(urname=urname,image1=image1,image2=image2,image3=image3,image4=image4)
        b.save()

        return redirect("homepage_customer.html")
    else:
        return render(request,"addproof-customer.html")
def check_request(request):
    return render(request,'checkrequest-admin.html')
def check_proof(request):
        return render(request,'checkproof_admin_left.html')
def checkrequest2(request):
    return render(request,'checkrequest2-admin.html')
def generate_page(request):
    return render(request,"home_a")

