# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Customer
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
class customerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['usn','cName','address','city','ckName']

class customerBase(ModelForm):
    class Meta:
        model = Customer
        fields=['cName','ckName','address','city','usn','kcity']

def importFromXLS():
    import xlrd
    customList=xlrd.open_workbook("list.xls")
    worksheet=customList.sheet_by_name("Sheet1")

    for i in range(9,3582):
        if worksheet.cell(i,9).value!="":
            city=worksheet.cell(i,9).value
        if worksheet.cell(i,7).value!="":
            uniqueCode=worksheet.cell(i,3).value
            customer = worksheet.cell(i,7).value
            address= worksheet.cell(i,14).value
            customerObject = Customer()
            customerObject.cName = customer
            customerObject.address = address
            customerObject.city = city
            customerObject.usn = uniqueCode
            customerObject.save()
def customerView(request,template_name='index.html'):
    customers=Customer.objects.all()
    return render(request,template_name,{'customers':customers})


def customerDetail(request,pk,template_name="detail.html"):
    customer = get_object_or_404(Customer,pk=pk)
    return render(request,template_name,{"customer":customer})

def printPage(request,template_name="print.html"):
    pk=request.POST.get('pk')
    ckName=request.POST.get('ckName')
    kcity=request.POST.get('kcity')
    numberofbox=request.POST.get('numberofbox')
    customer=Customer()
    customer = Customer.objects.get(pk=pk)
    customer.ckName=ckName
    customer.kcity=kcity
    customer.numberofbox=numberofbox
    customer.save()
    return render(request,template_name,{"customer":customer})
def new(request,template_name="new.html"):
    if request.method == 'POST':
        form=customerBase(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = customerBase()
  
    return render(request,template_name,{'form':form})
def deleteCustomer(request,template_name="delete.html"):
    customers=Customer.objects.all()

    return render(request,template_name,{'customers':customers})
def delete(request,pk,template_name="delete.html"):
    customer=get_object_or_404(Customer,pk=pk)
    if request.method == 'GET':
        customer.delete()
        return redirect('deleteCustomer')
    return render(request,template_name,context=None)