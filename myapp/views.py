import time

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from progressbar import progressbar

from myapp.forms import userform, skillform
from myapp.models import userdetails, academicdetails, skill, exp, project, cert


def index(request):
    return render(request,'index.html')
# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         print(username)
#         password = request.POST.get('password')
#         print(password)
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('index')
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect('login')
#     return render(request,'login.html')
def logout(request):
    return redirect('login')

def userdetaillist(request,user_id):
    detail = userdetails.objects.get(user_id=user_id)
    mail = User.objects.get(id=user_id)
    edu=academicdetails.objects.filter(user_id=user_id)
    sk = skill.objects.filter(user_id=user_id)
    ex=exp.objects.filter(user_id=user_id)
    proj=project.objects.filter(user_id=user_id)
    cer=cert.objects.filter(user_id=user_id)

    return render(request,'index.html',{'detail':detail,'mail':mail,'edu':edu ,'sk':sk,'ex':ex,'proj':proj,'cer':cer })
def projectdetails(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            name=request.POST.get('pname')
            desc=request.POST.get('pdesc')
            image=request.FILES.get('pimage')

            lang=request.POST.get('plang')
            # desc=request.POST.get('description')
            username=request.POST.get('username')
            user_id = User.objects.get(username=username).id
            # print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=project(user_id=user_id,projectname=name,projectdescription=desc,projectimage=image,language=lang)
            acd.save()

            return redirect('login')
    return render(request,'project.html')
def certification(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            name=request.POST.get('cert')
            # desc=request.POST.get('pdesc')
            # image=request.POST.get('pimage')
            # lang=request.POST.get('planguage')
            # desc=request.POST.get('description')
            username=request.POST.get('username')
            user_id = User.objects.get(username=username).id
            # print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=cert(user_id=user_id,certifications=name)
            acd.save()

            return redirect('exp')
    return render(request,'certification.html')
# def profile(request,id):
#     detail = userdetails.objects.get(user_id=id)
#     mail = User.objects.get(id=id)
#     sk = skill.objects.filter(user_id=id)
#     return render(request, 'profile.html', {'detail': detail,'mail':mail,'sk':sk})
def user(request):
    if request.method=='POST':
        # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
        name=request.POST.get('name')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        phno=request.POST.get('phno')
        adrs=request.POST.get('address')
        hgt=request.POST.get('height')
        wt=request.POST.get('weight')
        image = request.FILES.get('image')
        username=request.POST.get('username')
        user_id = User.objects.get(username=username).id


        # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
        acd=userdetails(user_id=user_id,name=name,age=age,dob=dob,phonenumber=phno,address=adrs,height=hgt,weight=wt,image=image)
        acd.save()

        return redirect('Academicdetails')


    return render(request, 'userdetails.html')
    # details=userdetails.objects.all()
    #
    # if request.method=='POST':
    #     form=userform(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('Academicdetails')
    # else:
    #     form=userform()
    # return render(request,'userdetails.html',{'form':form,'details':details})

def userregisteration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        confirm_password = request.POST.get('confirmpassword')
        print(confirm_password)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email already exists')
                return redirect('registeration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name, first_name=first_name)
                user.save()
                return redirect('user')  # Corrected URL
        else:
            messages.info(request, 'Password mismatch')
            return redirect('registeration')
    return render(request, 'registeration.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user=auth.authenticate(username=username,password=password)
        print('user',user)
        if user is not None:
            auth.login(request,user)
            try:
                # user_id = User.objects.get(username=username).id
                user_id = user.id
                # return redirect(f'userdetaillist?uid={user_id}')
                return HttpResponseRedirect(f'/userdetaillist/{user_id}')
                # return redirect('userdetaillist/uid=user_id')
            except User.DoesNotExist:
                messages.info(request, 'User not found')
                return redirect('login')
            # id = userdetails.objects.only('id').get(name='username').id
            # # success_url = '/my-success-url/{pk}/'
            # return redirect(f'userdetaillist?uid={id}')
            # # return redirect('userdetaillist')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def Academicdetails(request):

    # details=academicdetails.objects.all()

    # if request.method=='POST':
    #     form=academicform(request.POST)
    #     if form.is_valid():
    #             form.save()
    # else:
    #     form=academicform()
    # return render(request,'academicdetails.html',{'form':form,'details':details})
#     # details=userdetails.objects.all()
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            yoj=request.POST.get('yoj')
            yop=request.POST.get('yop')
            qualification=request.POST.get('qualification')
            university=request.POST.get('university')
            institution = request.POST.get('institution')
            marks=request.POST.get('marks')
            desc=request.POST.get('description')

            username=request.POST.get('username')
            user_id = User.objects.get(username=username).id
            print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=academicdetails(user_id=user_id,yoj=yoj,yop=yop,qualification=qualification,university=university,institution=institution,mark=marks,desc=desc)
            acd.save()

            return redirect('skills')
    return render(request,'academicdetails.html')
def createedu(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            yoj=request.POST.get('yoj')
            yop=request.POST.get('yop')
            qualification=request.POST.get('qualification')
            university=request.POST.get('university')
            institution=request.POST.get('institution')
            marks=request.POST.get('mark')
            desc=request.POST.get('description')
            firstname=request.POST.get('first_name')
            user_id = request.user.id
            print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=academicdetails(user_id=user_id,yoj=yoj,yop=yop,qualification=qualification,mark=marks,university=university,institution=institution,desc=desc)
            acd.save()

            return HttpResponseRedirect(f'/userdetaillist/{user_id}')
    return render(request,'crud/crudedu.html')
def detailedu(request):
    # detedu = academicdetails.objects.fetch(user_id=user_id)

    cart1= academicdetails.objects.filter(user_id=request.user.id)
    # cart_items = cart1

    return render(request, 'crud/detedu.html', {'cart1': cart1})
def updateeducationaldetails(request,eid):
    det = academicdetails.objects.filter(user_id=request.user.id,id=eid)
    if request.method=='POST':
        yoj=request.POST.get('yoj')
        yop=request.POST.get('yoj')
        qualification = request.POST.get('qualification')
        institution=request.POST.get('institution')
        university=request.POST.get('institution')

        mark = request.POST.get('marks')
        desc = request.POST.get('description')



        det.mark=mark

        det.desc=desc
        for obj in det:
            obj.yoj = yoj
            obj.yop = yop
            obj.qualification = qualification
            obj.university = university
            obj.institution = institution

            obj.save()

        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request, 'crud/updateedu.html', {'det':det})

def deleteedu(request,eid):
    remove = academicdetails.objects.get(user_id=request.user.id,id=eid)
    if request.method=='POST':
        remove.delete()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')

    return render(request,'crud/deleteedu.html',{'remove':remove})

#

def createcert(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            ce=request.POST.get('cert')
            print(request.POST)
            # firstname=request.POST.get('first_name')
            # user_id = User.objects.get(first_name=firstname).id
            user_id=request.user.id
            print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=cert(user_id=user_id,certifications=ce)
            acd.save()

            return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request,'crud/crudcert.html')
def detailcert(request):
    # detedu = academicdetails.objects.fetch(user_id=user_id)

    cart1= cert.objects.filter(user_id=request.user.id)
    # cart_items = cart1

    return render(request, 'crud/detcert.html', {'cart1': cart1})
def updatecert(request,eid):
    det = cert.objects.filter(user_id=request.user.id,id=eid)
    if request.method=='POST':
        cer=request.POST.get('cer')
        for obj in det:

            obj.certifications=cer


            obj.save()
            return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request, 'crud/updatecert.html', {'det':det})

def deletecert(request,eid):
    remove = cert.objects.get(user_id=request.user.id,id=eid)
    if request.method=='POST':
        remove.delete()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')

    return render(request,'crud/deletecert.html',{'remove':remove})


def skills(request):
    # details=skill.objects.all()

    if request.method=='POST':
        if request.user.is_authenticated:
            print(request.user)
            if request.method == 'POST':
                # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
                skill1 = request.POST.get('skill1')
                skill2 = request.POST.get('skill2')
                skill3 = request.POST.get('skill3')
                # marks = request.POST.get('marks')
                # desc = request.POST.get('description')
                username = request.POST.get('username')
                user_id = User.objects.get(username=username).id
                print(request.user)
                # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
                acd = skill(user_id=user_id, skill1=skill1, skill2=skill2, skill3=skill3)
                acd.save()
                return redirect('certification')
    #     form=skillform(request.POST)
    #     firstname = request.POST.get('first_name')
    #     user_id = User.objects.get(first_name=firstname).id
    #     if form.is_valid():
    #         acd = skill(user_id=user_id)
    #         form.save()
    #
    #         acd.save()
    # else:
    #     form=skillform()

    return render(request,'skill.html')
def experience(request):


    if request.method == 'POST':
        # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
        year= request.POST.get('year')
        job = request.POST.get('job')
        comp = request.POST.get('company')
        state = request.POST.get('state')
        country = request.POST.get('country')
        username = request.POST.get('username')
        user_id = User.objects.get(username=username).id
        print(request.user)
        # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
        acd = exp(user_id=user_id, year=year, company=comp, job=job,state=state,country=country)
        acd.save()
        return redirect('projectdetails')
    return render(request,'exp.html')
def createskill(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method=='POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            skill1 = request.POST.get('skill1')
            skill2 = request.POST.get('skill2')
            skill3 = request.POST.get('skill3')

            # firstname=request.POST.get('first_name')
            # user_id = User.objects.get(first_name=firstname).id
            user_id=request.user.id

            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd=skill(user_id=user_id,skill1=skill1,skill2=skill2,skill3=skill3)
            acd.save()

            return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request,'crud/crudskill.html')
def detailskill(request):
    # detedu = academicdetails.objects.fetch(user_id=user_id)

    cart1= skill.objects.filter(user_id=request.user.id)
    # cart_items = cart1

    return render(request, 'crud/detskill.html', {'cart1': cart1})
def updateskill(request,eid):
    det = skill.objects.filter(user_id=request.user.id,id=eid)
    if request.method=='POST':
        skill1=request.POST.get('skill1')
        skill2 = request.POST.get('skill2')
        skill3 = request.POST.get('skill3')

        for obj in det:

            obj.skill1=skill1
            obj.skill2=skill2
            obj.skill3=skill3

            obj.save()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request, 'crud/updateskill.html', {'det':det})

def deleteskill(request,eid):
    remove = skill.objects.get(user_id=request.user.id,id=eid)
    if request.method=='POST':
        remove.delete()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')

    return render(request,'crud/deleteskill.html',{'remove':remove})

def createexp(request):
    if request.user.is_authenticated:
        print(request.user)
        if request.method == 'POST':
            # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
            year = request.POST.get('year')
            job = request.POST.get('job')
            comp = request.POST.get('company')
            state = request.POST.get('state')
            country=request.POST.get('country')
            user_id = request.user.id
            print(request.user)
            # user_cart= academicdetails.objects.get_or_create(user=request.user,yoj=yoj,yop=yop,qualification=qualification,mark=marks,desc=desc)
            acd = exp(user_id=user_id, year=year, company=comp, job=job, state=state, country=country)
            acd.save()
            return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request,'crud/crudexp.html')
def detailexp(request):
    # detedu = academicdetails.objects.fetch(user_id=user_id)

    cart1= exp.objects.filter(user_id=request.user.id)
    # cart_items = cart1

    return render(request, 'crud/detexp.html', {'cart1': cart1})
def updateexp(request,eid):
    det = exp.objects.filter(user_id=request.user.id,id=eid)
    if request.method=='POST':
        job=request.POST.get('job')
        year = request.POST.get('year')
        company = request.POST.get('company')
        state = request.POST.get('state')
        country = request.POST.get('country')
        for obj in det:

            obj.job=job
            obj.year=year
            obj.company=company
            obj.state=state
            obj.country=country

            obj.save()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')
    return render(request, 'crud/updateexp.html', {'det':det})
def deleteexp(request,eid):
    remove = exp.objects.get(user_id=request.user.id,id=eid)
    if request.method=='POST':
        remove.delete()
        return HttpResponseRedirect(f'/userdetaillist/{request.user.id}')

    return render(request,'crud/deleteexp.html',{'remove':remove})