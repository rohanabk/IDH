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
    importFromXLS1()
    importFromXLS4()
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
def importFromXLS1():
    import xlrd
    customList=xlrd.open_workbook("VVM STOCKIEST LIST.XLS")
    worksheet=customList.sheet_by_name("Sheet1")


    for i in range(5,707,6):
        code=worksheet.cell(i,1).value
        customer=worksheet.cell(i,3).value
        
        address1=worksheet.cell(i+1,3).value
        address2=worksheet.cell(i+2,3).value
        address3=worksheet.cell(i+3,3).value
        city=worksheet.cell(i+4,3).value
        customerObject = Customer()
        customerObject.cName = customer
        customerObject.address = address1+" "+address2+" "+address3
        customerObject.city = city
        customerObject.usn = code
        customerObject.save()
def importFromXLS4():
    import xlrd
    customList=xlrd.open_workbook("ALL PARTY DETAILS.xlsx")
    worksheet=customList.sheet_by_name("Sheet1")

    for i in range(2,50):
        customer=worksheet.cell(i,0).value
        city=worksheet.cell(i,3).value
        address=worksheet.cell(i,10).value
        customerObject = Customer()
        customerObject.cName = customer
        customerObject.address = address
        customerObject.city = city
        customerObject.save()
def importFromXLS6():
    import xlrd
    customList=xlrd.open_workbook("ALL STOCKIEST.xlsx")
    worksheet=customList.sheet_by_name("MARG ERP 9+ Excel Report")

    for i in range(5,58):
        customer=worksheet.cell(i,1).value
        city=worksheet.cell(i,2).value
        customerObject = Customer()
        customerObject.cName = customer
        customerObject.city = city
        customerObject.save()