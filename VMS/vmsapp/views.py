from django.shortcuts import render, redirect
from .models import Register_user

#home page or dashboard
def index(request):
    return render(request, 'index.html')

# Accept user data from form and save to databse
def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        cname = request.POST['cname']
        purpose = request.POST['purpose']
        ptm = request.POST['ptm']
        profile = request.FILES['profile']
        signature = request.FILES['signature']
        
        user = Register_user(fname = fname, lname = lname, email = email, phone = phone, cname = cname, purpose = purpose, ptm = ptm, profile = profile, signature = signature)
        user.save()
        return redirect('show')
    else:
        return render(request, 'register.html')

# show method to fetch data from database
def show(request):
    records = Register_user.objects.all().order_by('-id')
    return render(request, 'show.html', {'records':records })
