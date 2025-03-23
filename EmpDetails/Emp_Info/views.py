from django.shortcuts import render,redirect
from .models import EmpDetails

# Create your views here.
def home(request):
    context = {'emp_details': EmpDetails.objects.all()}
    return render(request, 'home.html',context)

def create_emp_details(request):
    mesg="NOT Saved"
    if request.method=="POST":
        emp_name_form=request.POST['Empname']
        emp_city_form = request.POST['Empcity']
        emp_company_form = request.POST['Empcompany']
        emp_desc_form = request.POST['desc']
        emp_image_form = request.POST['img']
        EmpDetails(emp_name=emp_name_form,
                    emp_city=emp_city_form,
                    emp_company=emp_company_form,
                    descriptions=emp_desc_form,
                    emp_photo=emp_image_form).save()
        mesg="Saved"
    context={'mesg':mesg}
    return render(request,"Emp_details_form.html",context)

def delete_emp_details(request,pk):
    try:
        data=EmpDetails.objects.get(id=pk)
        data.delete()
        details=EmpDetails.objects.all()
        context={'emp_details':details}
        return render(request,"home.html",context)
    except:
        return redirect('emp_details')
def update_emp_page(request,pk):
    pr=pk
    data = EmpDetails.objects.get(id=pk)
    context = {'emp_name': data.emp_name,
               'emp_city': data.emp_city,
               'emp_company': data.emp_company,
               'pr':data.id}
    return render(request,"update_emp.html",context)

def update_emp(request,pk):
    data=EmpDetails.objects.get(id=pk)
    context={'emp_name':data.emp_name,
             'emp_city':data.emp_city,
             'emp_company':data.emp_company,
             'pr': data.id,
             'msg':'UPDATED'}
    msg='not updated'
    if request.method=='POST':
        data.emp_name=request.POST['up_Empname']
        data.emp_city=request.POST['up_Empcity']
        data.emp_company=request.POST['up_Empcompany']
        data.save()

        msg="updated"
    return render(request,"update_emp.html",context)

def emp_card(request,pk):
    data=EmpDetails.objects.get(id=pk)
    context={'emp_name':data.emp_name,'emp_city':data.emp_city,'emp_company':data.emp_company,'descriptions':data.descriptions,'emp_photo':data.emp_photo}
    return render(request,"employe_card.html",context)