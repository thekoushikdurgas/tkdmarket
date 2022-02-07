from django.test import TestCase
import python_minifier
import json
from django.http import HttpResponse, JsonResponse
from .models import Category1,Category2,Customeraddtocart,Product,customerdeatail,customeraddresses,countrylist,continentlist,customerpayment,Customeraddtoorder,productstatusmodel,Customeraddtowishlist,Producttogether
import decimal
from random import randint
import uuid   
from django.core.files import File 
import urllib
import os

def insertdata(request):
        ko1=list(Product.objects.filter(id=59).values())[0]['product_gender']
        ko2=list(Product.objects.filter().order_by('-id').values())[0]['productid']
        with open('localserver/abc.json') as f:
            data = json.load(f)
        a=len(data)
        print(a)
        for i in range(a):
            # print(len(erorlist1))
            # if (len(list(Product.objects.filter(name=data[i]['name']).values())) == 0):
                # if(data[i]['descriptions']):
                    # description = data[i]['descriptions'].split('":"')[-1][:-3]
                    # for j in b:
                    #     if(j['name'] in data[i]['categories']):
                    #         lp=j['id']
                    # if(data[i]['imageURLs']):
                        # try:  
                            # image_url = data[i]['imageURLs'].split(',')[0]
                            # userid = randint(0, 5)
                            print('<---'+str(i))
                            print(data[i]['id'])
                            ko2=nextid(ko2)
                            result = urllib.request.urlretrieve(data[i]['imageURLs'])            
                            cl = Product(userid=data[i]['userid'],catagory_id=data[i]['catagory_id'],product_gender=ko1,brand=data[i]['brand'],name=data[i]['name'],description=data[i]['descriptions'],price=data[i]['price'],productid=ko2)
                            cl.image.save(os.path.basename(str(uuid.uuid4())+".jpg"),File(open(result[0], 'rb')))
                            cl.save()
                        # except:
                            # pass
        # i=1
        # a = koushikcard
        # l = len(a)
        # for i in range(len(a)):
        #     icon = customerpayment(userid =1 ,userpaymentno = i+1,userpaymentprimary = False ,usercardtype = a[i]['type'],usercardnumber = a[i]['usercardnumber'],usercardname = "Koushik Chandra Saha",usercardcvc = a[i]['usercardcvc'],usercardmonth = a[i]['usercardmonth'],usercardyear = a[i]['usercardyear'])
        #     icon.save()
        return HttpResponse('hello world')
def deletetable(request):
    for i in range(5358,6635):
        # if(str(i) != "NAN"):
            print(i)
            cl =Product.objects.filter(id=i)
            cl.delete()
    return HttpResponse('hello world')
    
def updatetable(request):
    for i in list(Category.objects.all().values()):
        # if(str(i) != "NAN"):
            ko=i['catagory_name'].split(' > ')
            print(ko[0]+" > "+ko[-1])
            Category.objects.filter(catagory_id = i['catagory_id']).update(catagory_name=(ko[0]+" > "+ko[-1]))
            # cl =Category.objects.filter(name=i)
            # cl.delete()
    return HttpResponse('hello world')
def nextid(a):
    b=list(a)
    for j in range(len(b)-1,-1,-1):
            if(j%2==0):
                teampnext = ord(b[j])
                if(b[j].isupper()):
                    temptop = 90
                else:
                    temptop = 122
                if(teampnext<temptop):
                    b[j]=chr(teampnext+1)
                    break
                else:
                    b[j]=chr(temptop-25)
            else:
                if(int(b[j])<9):
                    b[j]=str(int(b[j])+1)
                    break
                else:
                    b[j]="0"
    return "".join(b)

def showtable(request):
    ko='hey sir'
    # catagoryid=list(Product.objects.filter(id=2).values().all())[0]['catagory_id']
    # tempintlist = list(Category2.objects.filter(catagory_id=catagoryid).values().all())[0]
    # catagoryname= tempintlist['catagory_name']
    # catagoryname2= tempintlist['catagory_name2']
    # Product.objects.filter(id=2).update(productcatagory=catagoryname,productcatagory2=catagoryname2)
    # a="A0a0A0a0A0a0A0a0A0a0"
    for i in list(Product.objects.all().values()):
        catagoryid=list(Product.objects.filter(id=i['id']).values().all())[0]['catagory_id']
        tempintlist = list(Category2.objects.filter(catagory_id=catagoryid).values().all())[0]
        catagoryname= tempintlist['catagory_name']
        catagoryname2= tempintlist['catagory_name2']
        Product.objects.filter(id=i['id']).update(productcatagory=catagoryname,productcatagory2=catagoryname2)
        print(i['id'])
    # ko = list(Product.objects.filter().order_by('-id').values())[0]['productid']
    return HttpResponse(ko)
# with open('admin.py') as f:
#     print(python_minifier.minify(f.read()))