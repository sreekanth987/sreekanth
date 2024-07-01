from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import razorpay
from .models import *
from .forms import *


# Create your views here.

def index(re):
    return render(re,'index.html')

def about(re):
    return render(re,'about.html')

def contact(re):
    if re.method == 'POST':
        a = (re.POST['name'])
        b = (re.POST['email'])
        c = int(re.POST['phone'])
        d = (re.POST.get('message', ''))
        contact_1.objects.create(name=a, phone=c, email=b, message=d).save()
        messages.success(re, 'DATA SAVED')
    return render(re,'contact.html')

def portfolio(re):
    return render(re,'portfolio.html')

def service(re):
    return render(re,'service.html')

def photos(re):
    return render(re,'user/photos.html')

def videos(re):
    return render(re,'user/videos.html')



def Registration(re):
    if re.method=='POST':
        a = (re.POST['name'])
        b = (re.POST['email'])
        c = int(re.POST['phone'])
        d = (re.POST['username'])
        e = (re.POST['password'])
        f = (re.POST['confirm password'])
        if register.objects.filter(username=d).exists():
            messages.error(re,'username already exist')
        else :
            if e==f:
                register.objects.create(name=a,email=b,phone=c,username=d,password=e).save()
                return HttpResponse("<script>alert('registerd successfully')</script>")
    return render(re, 'registration.html')

def login(re):
    if re.method == "POST":
        d = re.POST['username']  # to get data
        e = re.POST['password']
        try:
            data = register.objects.get(username=d)  # to get the username
            print(data)
            if e == data.password:
                re.session['user'] = d
                # return HttpResponse("<script>alert('login successfully')</script>")
                return redirect(userhome)
            return HttpResponse("Password Incorrect")  # work as else
        except Exception:
            if d == 'admin' and e == '1234':
                re.session['admin'] = d
                return redirect(adminhome)
            else:
                return HttpResponse("invalid usrname and password for admin")
    else:
        return render(re, 'login.html')

def adminhome(re):
    if 'admin' in re.session:
        return render(re, 'admin/adminhome.html')
    return redirect(login)

def userhome(re):
    if 'user' in re.session:
        return render(re, 'user/userhome.html')
    return redirect(login)

def about_1(re):
    if 'user' in re.session:
        return render(re,'user/about_1.html')

def contactas_1(re):
    if 'user' in re.session:
        if re.method=='POST':
            a=(re.POST['name'])
            b=(re.POST['email'])
            c=int(re.POST['phone'])
            d=(re.POST.get('message', ''))
            contact_1.objects.create(name=a,phone=c,email=b,message=d).save()
            messages.success(re,'DATA SAVED')
        return render(re,'user/contactas_1.html')

def portfolio_1(re):
    if 'user' in re.session:
        return render(re,'user/portfolio_1.html')

def services_1(re):
    if 'user' in re.session:
        data =newevent.objects.all()
        print(data)
        return render(re,'user/services_1.html',{'data':data})
    return redirect(login)

def addevents(re):
    if 'admin' in re.session:
        if re.method=='POST':
            a=re.POST['eventname']
            c=re.POST['amount']
            e=re.POST['amount1']
            d=re.POST['discription']
            b=re.FILES['image']
            newevent.objects.create(eventname=a,image=b,advanceamount=c,discription=d,fullamount=e).save()
            messages.success(re,'DATA SAVED')
        return render(re,'admin/addevents.html')

def bookingdetails(re):
    if 'admin' in re.session:
        d = booked.objects.all()
        return render(re,'admin/bookingdetails.html',{'r': d})

def userdetails(re):
    if 'admin' in re.session:
        d = register.objects.all()
        return render(re, 'admin/userdetails.html', {'r': d})

def profile(re):
    if 'user' in re.session:
        d = register.objects.filter(username=re.session['user'])
        print(d)
        return render(re, 'user/profile.html', {'data': d})
    return redirect(login)


def updateprofile(re):
    if 'user' in re.session:
        data=register.objects.get(username=re.session['user'])
        print(data)
        n=new_form(instance=data)
        if re.method=='POST':
           n=new_form(re.POST,re.FILES,instance=data)
           if n.is_valid():
               n.save()
               return redirect(profile)
        return render(re,'user/update_profile.html',{'data':n})
    return redirect(login)


def delete_event(re,d):
    if 'user' in re.session:
        booked.objects.filter(pk=d).update(bookingstatus='cancelled')
        return redirect(booking1)


def contactdetails(re):
    if 'admin' in re.session:
        d = contact_1.objects.all()
        return render(re, 'admin/contactdetails.html', {'r': d})

def logout(re):
    if 'user' in re.session or 'admin' in re.session:
        re.session.flush()
        return redirect(login)

# from .forms import *

# def form(re):
#     n=nform()
#     if re.method=='POST':
#         n=nform(re.POST,re.FILES)
#         if n.is_valid():
#             a=n.cleaned_data['clintname']
#             b=n.cleaned_data['phone']
#             c=n.cleaned_data['email']
#             d=n.cleaned_data['eventname']
#             f=n.cleaned_data['date_from']
#             g=n.cleaned_data['date_to']
#             booked.objects.create(clintname=a,phone=b,email=c,eventname=d,date_from=f,date_to=g).save()
#         return redirect(payment)
#     return render(re,'user/forms.html',{'data':n})
l = []
def form(re,d,amt):
    if 'user' in re.session:
        d1 = newevent.objects.get(pk=d)
        if re.method=='POST':
            a = (re.POST['name'])
            b = int(re.POST['phone'])
            c = (re.POST['email'])
            d = (re.POST['event'])
            g = (re.POST['venue'])
            e = (re.POST['setTodaysDate'])
            f = (re.POST['setTodaysDate1'])
            cat=re.POST.getlist('n1')
            # print(cat)
            # for i in cat:
            #     print(i)
            #     re.session['cat']=i
            #     print(re.session['cat'])
            # print("New",re.session['cat'])
            l.append(a)
            l.append(b)
            l.append(c)
            l.append(d)
            l.append(e)
            l.append(f)
            l.append(cat)
            l.append(g)
            l.append(amt)
            print("hai",l)

            # booked.objects.create(clintname=a,phone=b,email=c,eventname=d,date_from=e,date_to=f,category=cat,venue=g,username=re.session['user'],amt=amt).save()
            return redirect(payment,amt)
        return render(re, 'user/forms.html',{'d1':d1})


def success_2(re):
#     username = re.session['user']

    # data = booked.objects.get(pk=username)
    booked(clintname=l[0], phone=l[1], email=l[2], eventname=l[3], date_from=l[4], date_to=l[5], category=l[6], venue=l[7],username=re.session['user'], amt=l[8]).save()

    return render(re, 'success.html')


def payment(request,amt):
    amount = amt*100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    # cursor = connection.cursor()
    # cursor.execute(
    #     "update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(
    #         id) + "' ")

    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    return render(request, "user/payment.html",{'amount':amount})

# def payment_callback(request):
#     payment = request.POST  # or however the payment gateway sends the response
#     if payment.get('status') == 'success':
#         user = request.session.get('user')
#         if user:
#             booked.objects.create(**user)
#             del request.session['user']  # Clear session
#             return render(request, 'success.html', {'message': 'Payment successful, booking confirmed!'})
#     return render(request, 'error.html', {'message': 'Payment failed or booking details not found'})



from django.utils.crypto import get_random_string
from django.core.mail import send_mail
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        try:
            user = register.objects.get(email=email)
            print(user)
        except:
            messages.info(request, "Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}',
                      'settings.EMAIL_HOST_USER', [email], fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request, "Network connection failed")
            return redirect(forgot_password)

    return render(request,'forgot.html')

def reset_password(request,token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset_password.html', {'token': token})

def updateevent(re,d):
    if 'admin' in re.session:
        data=newevent.objects.get(pk=d)
        n=model_form(instance=data)
        if re.method=='POST':
           n=model_form(re.POST,re.FILES,instance=data)
           if n.is_valid():
               n.save()
               return redirect(manageevent)
        return render(re,'admin/update_event.html',{'data':n})
    return redirect(login)

def delete_product(re,d):
    if 'admin' in re.session:
        data=newevent.objects.get(pk=d)
        data.delete()
        messages.success(re,'product deleted succesfully')
        return redirect(manageevent)
    return redirect(login)

def manageevent(re):
    if 'admin' in re.session:
        data =newevent.objects.all()
        print(data)
        return render(re,'admin/manageevent.html',{'data':data})
    return redirect(login)

def booking(re,d):
    if 'user' in re.session:
        u=register.objects.get(username=re.session['user'])
        p = booked.objects.get(pk=d)
        book_1.objects.create(user_1=u,booking_1=p).save()
    return redirect(booking)

def booking1(re):
    if 'user' in re.session:
        d=booked.objects.filter(username=re.session['user'])
        print(d)
        return render(re,'user/booking_details.html',{'m':d})
    return redirect(login)