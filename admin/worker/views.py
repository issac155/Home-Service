from django.shortcuts import render,redirect
from.models import Worker,Customer
from django.contrib.auth.models import User,auth
from django.http.response import JsonResponse
from django.db.models.query_utils import Q
from django.http import JsonResponse
from .forms import LocationForm
from .models import Location,PinCode
from django.shortcuts import render, get_object_or_404
from datetime import datetime
#new
from django.contrib.auth.models import User
from .models import Profile
import random
from .helper import MessageHandler
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from django.shortcuts import render, redirect







def register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        pincode = request.POST.get('pincode')
        otp = request.POST.get('methodOtp')
        print(otp,"here you can check it")
        


        if not user_name or not phone_number:
            messages.error(request, "Please fill in all the required fields.")
            return redirect('register')

        if not phone_number.isdigit() or len(phone_number) != 10:
            messages.error(request, "Invalid mobile number.")
            return redirect('register')
        
        if not otp:
            messages.error(request, "Please select the OTP verification method.")
            return redirect('register')

        request.session['user_name'] = user_name
        request.session['phone_number'] = phone_number
        request.session['pincode'] = pincode
    

        otp = random.randint(1000, 9999)
        print(otp, "the generated otp")

        request.session['otp'] = otp

        if request.POST.get('methodOtp'):
         message_handler = MessageHandler(phone_number, otp)
         message_handler.send_otp_via_message()

        return redirect('otp')
       

    return render(request, 'register.html')


def otpVerify(request):
    if request.method == "POST":
        user_name = request.session.get('user_name')
        phone_number = request.session.get('phone_number')
        otp = request.session.get('otp')
        pincode = request.session.get('pincode')
        print(pincode,user_name,phone_number,otp)

        if not user_name or not phone_number or not otp:
            messages.error(request, "Session expired. Please try again.")
            return redirect('register')
        entered_otp = request.POST.get('otp')

        if entered_otp == str(otp):

            if User.objects.filter(username__iexact=user_name).exists():
                messages.error(request, "Username already exists.")
                return redirect('register')

            if Profile.objects.filter(phone_number=phone_number).exists():
                messages.error(request, "Mobile number already exists.")
                return redirect('register')
          
            User.objects.create(
                            username = user_name,
                            
            )
            user_instance = User.objects.get(username=user_name)
            Profile.objects.create(
                            user = user_instance,phone_number=phone_number,otp=otp,pincode=pincode
            )
            
            request.session.delete('user_name')
            request.session.delete('phone_number')
            request.session.delete('pincode')
            request.session.delete('otp')

            return redirect("index")

        else:
            messages.error(request, "Wrong OTP.")
            return redirect('otp')

    return render(request, "otp.html")

# #home page


def index(request):
  if request.user.is_authenticated:
    return render(request,'search.html') 
  else:
   return render(request,'login.html')

#login
def login(request):
    if request.method == "POST":
        mobile_number = request.POST['ph']
        if not mobile_number:
            messages.error(request, "Please enter a mobile number.")
            return redirect('login')

        if Profile.objects.filter(phone_number=mobile_number).exists():
            # User is registered, perform login action
            # Add your login logic here
            
            request.session['ph'] = mobile_number
            return render(request, 'search.html')
        else:
            # User is not registered, redirect to the registration page
            messages.error(request, "User not found.")
            return redirect('login')
    
    return render(request, 'login.html')
    


#search result
def result(request):
   query = request.GET.get('query')
   qu = request.GET.get('qu')
#    if not query:
#         m = "Enter the correct pincode"
#         return render(request,'search.html')
   results = Worker.objects.all()
   if query:
        results = results.filter(pin__icontains=query)
   if qu:
        results = results.filter(work__icontains=qu)
   context = {'results': results, 'query': query, 'qu': qu}
   if not results.exists():
        context['not_found'] = True
        mobile_number = request.session.get('ph')
        print(mobile_number)
   return render(request, 'result.html', context)
#logout
def logout_view(request):
  logout(request)
  request.session.delete('ph')
  messages.success(request, "You have been logged out.")
  return redirect('login')

# #call request
def request(request,result_id):
 result = get_object_or_404(Worker, id=result_id)
 h = result.mobile
 k = result.name
 l = result.work
 context= {'h': h,'k':k,'l':l}
 return render(request, 'request.html',context)


# #adding customer details

def cust(request):
    if request.method == 'POST':
        a = request.POST['name1']
        b = request.POST['name2']
        c = request.POST['ji']
        h = request.POST['hel']
        j = request.POST['ten']
        emai = request.POST.get('email')
        address_line_1 = request.POST.get('address1')
        address_line_2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal')
        o = datetime.now()
        done = Customer(
            name=a,
            mobile=b,
            work_name=c,
            work_no=h,
            work_wo=j,
            date=o,
            email=emai,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state=state,
            postal_code=postal_code,
            approved=False
        )
        done.save()

        # Get the mobile number from the session
        mobile_number = request.session.get('ph')

        # Get the user's profile based on the mobile number
        try:
            profile = Profile.objects.get(phone_number=mobile_number)
        except Profile.DoesNotExist:
            profile = None

        if profile:
            # Associate the customer with the profile
            profile.bookings.add(done)

        return redirect('had')

    return render(request, 'request.html')
#serach functionality
def search1(request):
  pin = request.GET.get('pin', '')
  work_options = Worker.objects.filter(pin=pin).values_list('work', flat=True).distinct()
  return JsonResponse({'work_options': list(work_options)})


def li(request):
   return render(request,'search.html')


def hai(request):
   return render(request,'register.html')

def approved_customers(request):
    mobile_number = request.session.get('ph')
    profile = Profile.objects.filter(phone_number=mobile_number).first()
    context = {}

    if profile:
        approved_customers = profile.bookings.filter(approved=True)
        if approved_customers.exists():
            context['approved_customers'] = approved_customers
        else:
            context['booking_found'] = True
            context['approved'] = False
    else:
        context['booking_found'] = False
    
    return render(request, 'cust.html', context)
