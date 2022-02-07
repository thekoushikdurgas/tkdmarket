from django.shortcuts import render, redirect
from .models import Category1,Category2,Customeraddtocart,Product,customerdeatail,customeraddresses,countrylist,continentlist,customerpayment,Customeraddtoorder,productstatusmodel,Customeraddtowishlist,Producttogether
from django.http import HttpResponse, JsonResponse
# from studentmanagmentsoftware.forms import Adminmodelform
import datetime
import random
import decimal
def floatconvert(x):
    return decimal.Decimal("%.2f" % x)

def generaterandomstring(n):
    chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join((random.choice(chars)) for x in range(n))

def navbarclear(a,b):
    if b==1:
        for i,j in a.items():
            for k in j:
                k['active'] = ''
    else:
        for i in a:
            i['active'] = ''

def clearactive(b,a):
    navbarclear(userdeatails['navlink'],1)
    navbarclear(userdeatails['2ndnavlink'],0)
    userdeatails['navlink'][b][a]['active'] = 'active'
    userdeatails['usertitle'] = b
    if b=='Dashboard':
        userdeatails['usertitleicon'] = "fa-light fa-gauge fa-fw"
    elif b=='Payment settings':
        userdeatails['usertitleicon'] = "fa-regular fa-money-check-dollar-pen fa-fw"
    userdeatails['usertitle1'] = userdeatails['navlink'][b][a]['name']
    userdeatails['usertitleicon1'] = userdeatails['navlink'][b][a]['icon']
    userdeatails['currentsite'] = userdeatails['navlink'][b][a]['link']

def updateprofile(a,b):        
    tempobjectA = list(customerdeatail.objects.filter(id=a).values())[0]
    userdeatails['id'] = a
    userdeatails['username'] = tempobjectA['username']
    userdeatails['userpic'] = tempobjectA['userpic']
    userdeatails['userdob'] = '-'.join(tempobjectA['userdob'].split('/')[::-1])
    userdeatails['useremail'] = tempobjectA['useremail']
    userdeatails['userpassword'] = tempobjectA['userpassword']
    userdeatails['usergender'] = tempobjectA['usergender']
    userdeatails['userphone'] = tempobjectA['userphone']
    userdeatails['userrewardpoints'] = tempobjectA['userrewardpoints']
    userdeatails['usertype'] = b
    userdeatails['navlink'] = customernavbar
    userdeatails['Requirements']['usershopcart']=list(Customeraddtocart.objects.filter(userid=tempobjectA['id']).values())
    c=floatconvert(0)
    c1=floatconvert(0)
    for i in range(len(userdeatails['Requirements']['usershopcart'])):
        userdeatails['Requirements']['usershopcart'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['usershopcart'][i]['productid']).values())[0]
        userdeatails['Requirements']['usershopcart'][i]['productnos'] = i
        c+=floatconvert(userdeatails['Requirements']['usershopcart'][i]['total_price'])
    c=floatconvert(c)
    addresslists= list(customeraddresses.objects.filter(userid=a).values())
    paymentlists= list(customerpayment.objects.filter(userid=a).values())
    for i in range(len(paymentlists)):
        customerpayment.objects.filter(id = paymentlists[i]["id"]).update(userpaymentno = i+1)
    for i in range(len(addresslists)):
        customeraddresses.objects.filter(id = addresslists[i]["id"]).update(useraddressno = i+1)
    userdeatails['Requirements']['usertotalprice']=c
    userdeatails['Requirements']['usertotalpricegst']=floatconvert((c*userdeatails['gstrate'])/floatconvert(100))
    userdeatails['Requirements']['useralltotalprice']=floatconvert(userdeatails['Requirements']['usertotalpricegst']+userdeatails['Requirements']['usertotalprice'])
    userdeatails['Requirements']['usershopcartno']=len(userdeatails['Requirements']['usershopcart'])
    userdeatails['Requirements']['addresslists'] = list(customeraddresses.objects.filter(userid=a).values())
    userdeatails['Requirements']['paymentlist'] = list(customerpayment.objects.filter(userid=a).values())

def errorpage(request):
    i=random.randint(1,8)
    userdeatails['usertype'] = "Error | 404 | "+str(i)
    return render(request, 'error/404-'+str(i)+'.html', {'userdeatails': userdeatails})

def helptopics(request):
    userdeatails['currentsite'] = "/help_topics"
    userdeatails['usertype'] = "Help topics"
    return render(request, 'main/helptopics.html', {'userdeatails': userdeatails})

def contacts(request):
    userdeatails['currentsite'] = "/contacts"
    userdeatails['usertype'] = "Contacts"
    return render(request, 'main/contacts.html', {'userdeatails': userdeatails})

def tkdlogin(request):
    if request.method == 'POST':
        rollno = request.POST['username']
        password = request.POST['password']
        tempobjectA = list(customerdeatail.objects.filter(username=rollno).values())
        if (len(tempobjectA) > 0):
            tempobjectA = tempobjectA[0]
            if (tempobjectA['userpassword'] == password):
                response = JsonResponse(userdeatails['currentsite'], safe = False) 
                updateprofile(tempobjectA['id'],"Customer")
                response.set_cookie(userdeatails['idrandam'],tempobjectA['id'])
            else:
                response = JsonResponse("password wrong", safe = False) 
        else:
            response = JsonResponse("No Username", safe = False) 
        return response 
    return render(request, 'login/signin.html')

def customerregistration(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['userphone']
        tempobjectA = list(customerdeatail.objects.filter(useremail=email).values())
        tempobjectB = list(customerdeatail.objects.filter(userphone=phone).values())
        if (len(tempobjectA) == 0 and len(tempobjectB) == 0):
            cl = customerdeatail(username=request.POST['fullname'], userpic=request.FILES['profileavatar'], userdob=request.POST['dateofbirth'], useremail=email, usergender=request.POST['gender'], userpassword=request.POST['password'], userphone=phone)
            cl.save()
            tempalert = "Success"
        elif(len(tempobjectB) == 0):
            tempalert = "Telephone is already registered"
        else:
            tempalert = "Email is already registered"
        return JsonResponse(tempalert, safe = False)
    return render(request, 'login/signup.html')

def customerforgotusername(request):
    return render(request, 'login/forgot.html')

def customerforgotpassword(request):
    return render(request, 'login/forgot.html')

def restartprofile():
    userdeatails['id'] = 0
    userdeatails['username'] = ""
    userdeatails['userpic'] = ""
    userdeatails['userdob'] = ""
    userdeatails['usergender'] = ""
    userdeatails['userphone'] = ""
    userdeatails['useremail'] = ""
    userdeatails['userpassword'] = ""
    userdeatails['userpassword'] = ""
    # userdeatails['usertype'] = "Home"
    userdeatails['usertitle'] = ""
    userdeatails['usertitleicon'] = ""
    userdeatails['usertitle1'] = ""
    userdeatails['usertitleicon1'] = ""
    userdeatails['navlink'] = {}
    userdeatails['product'] = {}
    userdeatails['2ndnavlinkactive'] = {}
    userdeatails['Copyright'] = Copyright
    # userdeatails['currentsite'] = '/'
    userdeatails['2ndnavlink'] = []
    userdeatails['gstrate'] =floatconvert(2.5)

def userlogout(request):
    restartprofile()
    response = redirect('home')
    response.delete_cookie(userdeatails['idrandam'])
    return response

def home(request):
    userdeatails['currentsite'] = "/"
    userdeatails['usertype'] = "Home"
    all = list(Product.objects.all().values())
    userdeatails['Requirements']['womenitems']=[x for x in all if 'female' in list(x['product_gender'])]
    userdeatails['Requirements']['menitems']=[x for x in all if 'male' in list(x['product_gender'])]
    userdeatails['Requirements']['kidsitems']=[x for x in all if 'kid' in list(x['product_gender'])]
    if(request.COOKIES.get(userdeatails['idrandam'])):
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        response = render(request, 'main/main.html', {'userdeatails': userdeatails})
    else:
        restartprofile()
        response = render(request, 'main/main.html', {'userdeatails': userdeatails})
        response.delete_cookie(userdeatails['idrandam'])
    return response
    
def search(request,id,id1,id2,id3):
    userdeatails['currentsite'] = "/"
    userdeatails['usertype'] = userdeatails['productlist'][id]
    userdeatails['Requirements']['row']= id
    userdeatails['Requirements']['row1']= id1
    userdeatails['Requirements']['row2']= id2
    userdeatails['Requirements']['row3']= id3
    userdeatails['Requirements']['searchlink'] = userdeatails['currentsite'] = '/search/'+id+'/'+str(id1)+'/'+str(id3)+'/'+id2
    # /search/row/row1/row3/row2
    # /search/all/1/0/sss
    # /search/animals_&_pet_supplies/1/0/all
    # print(productdict[userdeatails['Requirements']['row']])
    if(userdeatails['Requirements']['row'] == "all"):
        if(userdeatails['Requirements']['row2'] == "all"):
            userdeatails['Requirements']['searchproductlist'] = list(Product.objects.all().values())
        else:
            userdeatails['Requirements']['searchproductlist'] = list(Product.objects.filter(name__contains=userdeatails['Requirements']['row2']).values())
    else:
        if(userdeatails['Requirements']['row2'] == "all"):
            userdeatails['Requirements']['searchproductlist'] = list(Product.objects.filter(productcatagory=productdict[userdeatails['Requirements']['row']]).values())
            # print(userdeatails['Requirements']['searchproductlist'])
        else:
            userdeatails['Requirements']['searchproductlist'] = list(Product.objects.filter(productcatagory=productdict[userdeatails['Requirements']['row']],name__contains=userdeatails['Requirements']['row2']).values())
    userdeatails['Requirements']['searchproductlistno'] = len(userdeatails['Requirements']['searchproductlist'])
    userdeatails['Requirements']['searchproductlistpre'] = (id1-1)*10
    userdeatails['Requirements']['searchproductlistnex'] = id1*10
    if(userdeatails['Requirements']['searchproductlistpre'] > 0):
        userdeatails['Requirements']['searchproductlistpreno'] = id1-1
    else:
        userdeatails['Requirements']['searchproductlistpreno'] = 0
    if(userdeatails['Requirements']['searchproductlistnex'] < userdeatails['Requirements']['searchproductlistno']):
        userdeatails['Requirements']['searchproductlistnexno'] = id1+1
    else:
        userdeatails['Requirements']['searchproductlistnexno'] = 0
    userdeatails['Requirements']['searchproductlistpageno'] = int(userdeatails['Requirements']['searchproductlistno']/10)+1
    userdeatails['Requirements']['searchproductlistpagenolist'] = [x for x in range(1,userdeatails['Requirements']['searchproductlistpageno']+1)]
    userdeatails['Requirements']['searchproductlistpagenolistno'] = len(userdeatails['Requirements']['searchproductlistpagenolist'])
    userdeatails['Requirements']['searchproductlist'] = userdeatails['Requirements']['searchproductlist'][userdeatails['Requirements']['searchproductlistpre']:userdeatails['Requirements']['searchproductlistnex']]
    userdeatails['Requirements']['searchproductlistpre'] += 1
    userdeatails['Requirements']['searchproductlistnex'] += 1
    return render(request, 'main/search.html', {'userdeatails': userdeatails})

def profile(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        clearactive('Account settings',0)
        userdeatails['currentsite'] = "/profile/"+str(id)
        userdeatails['2ndnavlinkactive']={"profile{0}".format(id):'show active'}
        return render(request, 'main/accountprofile.html', {'userdeatails': userdeatails})

def profileavaterchange(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        tempobjectA = list(customerdeatail.objects.filter(id=id).values())[0]
        cl = customerdeatail(id=id,username=tempobjectA["username"], userpic=request.FILES['profileavatar'], userdob=tempobjectA["userdob"], useremail=tempobjectA["useremail"], usergender=tempobjectA["usergender"], userpassword=tempobjectA["userpassword"], userphone=tempobjectA["userphone"])
        cl.save()
        updateprofile(id,"Customer")
        return JsonResponse("profile/1", safe = False)

def profiledeatailschange(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        customerdeatail.objects.filter(id = id).update(username=request.POST['fullname'], userdob=request.POST['userdob'], usergender=request.POST['gender'], userphone=request.POST['userphone'])
        updateprofile(id,"Customer")
        return redirect('/profile/1')

def profilepasswordchange(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(userdeatails['userpassword'] == request.POST['oldpassword']):
            customerdeatail.objects.filter(id = id).update(userpassword=request.POST['newpassword'])
            updateprofile(id,"Customer")
            tempalert = 0
        else:
            tempalert = 1
        return JsonResponse(tempalert, safe = False)

def addresslist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        clearactive('Account settings',1)
        userdeatails['currentsite'] = "/addresslist/"+str(id)
        userdeatails['2ndnavlinkactive']={"addresslist{0}".format(id):'show active'}
        userdeatails['Requirements']['countrylist'] = list(countrylist.objects.all().values())
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return render(request, 'main/accountprofile.html', {'userdeatails': userdeatails})

def addaddresslist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        useraddressno = list(customeraddresses.objects.filter(userid=id).values())
        completed = request.POST.get('address-primary')
        completed = True if completed else False
        if completed :
            customeraddresses.objects.filter(userid = id).update(useraddressprimary = False)
        cl = customeraddresses(username=request.POST['address-fn'], userid=id, useraddressno=len(useraddressno)+1, useraddressprimary=completed, useraddress=request.POST['address-line'],usercity=request.POST['address-city'], usercountry=request.POST['address-country'], userstate=request.POST['address-state'], userzipcode=request.POST['address-zip'])
        cl.save()
        tempalert = 1
        return JsonResponse(tempalert, safe = False)
        return redirect('/addresslist/1')

def editaddresslist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if request.method == 'POST':
            completed = request.POST.get('address-primary')
            completed = True if completed else False
            if completed :
                customeraddresses.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam']))).update(useraddressprimary = False)
            else :
                useraddressprimaryno = list(customeraddresses.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam'])),useraddressprimary = True).values())[0]['id']
                if(useraddressprimaryno == id):
                    customeraddresses.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam'])),useraddressno = 1).update(useraddressprimary = True)
            customeraddresses.objects.filter(id = id).update(username=request.POST['address-fn'], useraddressprimary=completed, useraddress=request.POST['address-line'],usercity=request.POST['address-city'], usercountry=request.POST['address-country'], userstate=request.POST['address-state'], userzipcode=request.POST['address-zip'])
            return redirect('./../addresslist/1')
        clearactive('Account settings',1)
        tempcountry = list(customeraddresses.objects.filter(id=id).values())[0]['usercountry']
        userdeatails['Requirements']['countrylist'] = list(countrylist.objects.all().values())
        userdeatails['Requirements']['continentlist'] = list(continentlist.objects.filter(countryname=tempcountry).values())
        userdeatails['Requirements']['addresslists'] = customeraddresses.objects.filter(id=id).values()
        return render(request, 'main/accountaddressedit.html', {'userdeatails': userdeatails})

def adduseraddressprimary(request,id,id1,id2):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if id1 == 1:
            customeraddresses.objects.filter(userid = id).update(useraddressprimary = False)
            customeraddresses.objects.filter(id = id2).update(useraddressprimary = True)
        elif id1 == 2:
            tempobjectA = list(customeraddresses.objects.filter(id=id2).values())[0]
            if(tempobjectA['useraddressprimary']):
                if(tempobjectA['useraddressno'] == "1"):
                    customerpayment.objects.filter(userid = id,useraddressno = 2).update(userpaymentprimary = True)
                else:
                    customerpayment.objects.filter(userid = id,useraddressno = 1).update(userpaymentprimary = True)
            cl = customeraddresses.objects.get(id=id2)
            cl.delete()
        return redirect(userdeatails['currentsite'])

def statelistshow(request):
    if request.method == "POST":
        countryname = request.POST['countryname']
        statelists = continentlist.objects.filter(countryname = countryname)
        return JsonResponse(list(statelists.values('id', 'countryname', 'continentname')), safe = False) 

def paymentlist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        clearactive('Account settings',2)
        userdeatails['currentsite'] = "/paymentlist/"+str(id)
        userdeatails['2ndnavlinkactive']={"paymentlist{0}".format(id):'show active'}
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        # print(userdeatails['Requirements']['paymentlist'])
        return render(request, 'main/accountprofile.html', {'userdeatails': userdeatails})

def addpaymentlist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        cardnolist = list(customerpayment.objects.filter(usercardnumber=request.POST['cardnumber']).values())
        if(len(cardnolist)==0):
            tempalert = 0
            userpaymentno = list(customerpayment.objects.filter(userid=id).values())
            completed = request.POST.get('paymentprimary')
            completed = True if completed else False
            if completed :
                customerpayment.objects.filter(userid = id).update(userpaymentprimary = False)
            cl = customerpayment(userid =id ,userpaymentno = len(userpaymentno)+1,userpaymentprimary = completed ,usercardtype = request.POST['paycardtype'],usercardnumber = request.POST['cardnumber'],usercardname = request.POST['cardname'],usercardcvc = request.POST['cardcvc'],usercardmonth = request.POST['cardexpirymonth'],usercardyear = request.POST['cardexpiryyear'])
            cl.save()
        else:
            tempalert = 1
        return JsonResponse(tempalert, safe = False)

def adduserpaymentprimary(request,id,id1,id2):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if id1 == 1:
            customerpayment.objects.filter(userid = id).update(userpaymentprimary = False)
            customerpayment.objects.filter(id = id2).update(userpaymentprimary = True)
        elif id1 == 2:
            tempobjectA = list(customerpayment.objects.filter(id=id2).values())[0]
            if(tempobjectA['userpaymentprimary']):
                if(tempobjectA['userpaymentno'] == "1"):
                    customerpayment.objects.filter(userid = id,userpaymentno = 2).update(userpaymentprimary = True)
                else:
                    customerpayment.objects.filter(userid = id,userpaymentno = 1).update(userpaymentprimary = True)
            cl = customerpayment.objects.get(id=id2)
            cl.delete()
        return redirect('/paymentlist/1')

def editpaymentlist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if request.method == 'POST':
            completed = request.POST.get('paymentprimary')
            completed = True if completed else False
            if completed :
                customerpayment.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam']))).update(userpaymentprimary = False)
            else :
                useraddressprimaryno = list(customerpayment.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam'])),userpaymentprimary = True).values())[0]['id']
                if(useraddressprimaryno == id):
                    customerpayment.objects.filter(userid = int(request.COOKIES.get(userdeatails['idrandam'])),userpaymentno = 1).update(userpaymentprimary = True)
            customerpayment.objects.filter(id = id).update(userpaymentprimary = completed ,usercardtype = request.POST['paycardtype'],usercardnumber = request.POST['cardnumber'],usercardname = request.POST['cardname'],usercardcvc = request.POST['cardcvc'],usercardmonth = request.POST['cardexpirymonth'],usercardyear = request.POST['cardexpiryyear'])
            return redirect('/paymentlist/1')
        clearactive('Account settings',2)
        userdeatails['Requirements']['paymentlists'] = customerpayment.objects.filter(id=id).values()
        return render(request, 'main/accountpaymentedit.html', {'userdeatails': userdeatails})

def payoutslist(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/payoutslist"
        return render(request, 'main/dashboard-payouts.html', {'userdeatails': userdeatails})

def orderlist(request,id,id1,id2):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        clearactive('Payment settings',1)
        if(id1 == 1):
            userdeatails['Requirements']['orderby1'] = "selected"
            userdeatails['Requirements']['orderby2'] = ""
            temporderby=''
        else:
            userdeatails['Requirements']['orderby1'] = ""
            userdeatails['Requirements']['orderby2'] = "selected"
            temporderby='-'
        userdeatails['currentsite'] = "/orderlist/"+id+"/"+str(id1)+"/"+str(id2)
        userdeatails['2ndnavlinkactive']={'orderlist':'show active'}
        if id == "all":
            userdeatails['Requirements']['orderlist'] = list(Customeraddtoorder.objects.filter(userid=int(request.COOKIES.get(userdeatails['idrandam']))).values().order_by(temporderby+'created_at'))
        else:
            userdeatails['Requirements']['orderlist'] = list(Customeraddtoorder.objects.filter(userid=int(request.COOKIES.get(userdeatails['idrandam'])),productstatus=productstatuslist[id]).values().order_by(temporderby+'created_at'))
        templen = len(userdeatails['Requirements']['orderlist'])
        userdeatails['Requirements']['orderlist'] = userdeatails['Requirements']['orderlist'][:(id2*5)]
        userdeatails['Requirements']['orderlisttype'] = id
        if(id2*5 < templen):
            userdeatails['Requirements']['orderlistnext'] = id2+1
            userdeatails['Requirements']['orderlistnexttype'] = str(id1)
            userdeatails['Requirements']['totalorderlistno'] = templen
            userdeatails['Requirements']['orderlistno'] = id2*5
            userdeatails['Requirements']['orderlistprogressno'] = (id2*5*100)/templen
        else:
            userdeatails['Requirements']['orderlistnext'] = 0
        for i in range(len(userdeatails['Requirements']['orderlist'])):
            userdeatails['Requirements']['orderlist'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['orderlist'][i]['productid']).values())[0]
            userdeatails['Requirements']['orderlist'][i]['addressdetails'] = list(customeraddresses.objects.filter(id=userdeatails['Requirements']['orderlist'][i]['addressid']).values())[0]
            userdeatails['Requirements']['orderlist'][i]['productstatuscolor'] = userdeatails['Requirements']['orderlist'][i]['productstatus'].replace(' ','-').lower()
        userdeatails['Requirements']['productstatuslist'] = productstatuslist
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return render(request, 'main/accountprofile.html', {'userdeatails': userdeatails})
        
def order(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/order/"+id
        userdeatails['Requirements']['orderdeatailsno'] = id
        userdeatails['Requirements']['orderdeatails'] = list(Customeraddtoorder.objects.filter(orderid=id).values().order_by('-created_at'))
        a=floatconvert(0)
        for i in range(len(userdeatails['Requirements']['orderdeatails'])):
            userdeatails['Requirements']['orderdeatails'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['orderdeatails'][i]['productid']).values())[0]
            tempaddress = list(customeraddresses.objects.filter(id=userdeatails['Requirements']['orderdeatails'][i]['addressid']).values())
            temppayment = list(customerpayment.objects.filter(id=userdeatails['Requirements']['orderdeatails'][i]['paymentid']).values())
            a+=floatconvert(userdeatails['Requirements']['orderdeatails'][i]['total_price'])
            userdeatails['Requirements']['orderdeatails'][i]['productstatuscolor'] = userdeatails['Requirements']['orderdeatails'][i]['productstatus'].replace(' ','-').lower()
        userdeatails['Requirements']['orderdeatailsaddressdetails'] = tempaddress
        userdeatails['Requirements']['orderdeatailspaymentdetails'] = temppayment
        userdeatails['Requirements']['productstatuslist'] = productstatuslist
        a=floatconvert(a)
        userdeatails['Requirements']['orderdeatailstotalprice']=a
        userdeatails['Requirements']['orderdeatailstotalpricegst']=floatconvert((a*userdeatails['gstrate'])/floatconvert(100))
        userdeatails['Requirements']['orderdeatailsalltotalprice']=floatconvert(floatconvert(userdeatails['Requirements']['orderdeatailstotalpricegst'])+floatconvert(userdeatails['Requirements']['orderdeatailstotalprice'])+floatconvert(100))
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return render(request, 'main/orderdetails.html', {'userdeatails': userdeatails})
        
def ordercancel(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        Customeraddtoorder.objects.filter(id=id).update(productstatus='Cancel')
        return redirect(userdeatails['currentsite'])

def ordertracker(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/order/"+id
        userdeatails['Requirements']['orderdeatailsno'] = id
        userdeatails['Requirements']['orderdeatails'] = list(Customeraddtoorder.objects.filter(trackingid=id).exclude(productstatus="Pending").values())
        if(len(userdeatails['Requirements']['orderdeatails'])==0 or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=="Cancel" or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=="Pending"):
            return redirect('errorpage')
        elif(userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Accepted' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Packed' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Shipped' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='On The Way' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Delivered'):
            userdeatails['Requirements']['trackingstatuslist'] = trackingstatuslist1
        elif(userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Returned Request' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Returned' or userdeatails['Requirements']['orderdeatails'][0]['productstatus']=='Refunded'):
            userdeatails['Requirements']['trackingstatuslist'] = trackingstatuslist2
        for i in range(len(userdeatails['Requirements']['orderdeatails'])):
            tempaddress = list(customeraddresses.objects.filter(id=userdeatails['Requirements']['orderdeatails'][i]['addressid']).values())
            userdeatails['Requirements']['orderdeatails'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['orderdeatails'][i]['productid']).values())[0]
            userdeatails['Requirements']['orderdeatails'][i]['productstatuscolor'] = userdeatails['Requirements']['orderdeatails'][i]['productstatus'].replace(' ','-').lower()
            for j in range(len(userdeatails['Requirements']['trackingstatuslist'])):
                temptracker=list(productstatusmodel.objects.filter(trackingid=id,productstatustype=userdeatails['Requirements']['trackingstatuslist'][j]['status']).values())
                if(len(temptracker)):
                    userdeatails['Requirements']['trackingstatuslist'][j]['description']=temptracker[0]['orderdesc']
                    userdeatails['Requirements']['trackingstatuslist'][j]['date']=str(temptracker[0]['created_at'].strftime("%d/%m/%Y %H:%M:%S"))
        userdeatails['Requirements']['orderdeatailsaddressdetails'] = tempaddress
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return render(request, 'main/ordertracker.html', {'userdeatails': userdeatails})

def returnitems(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        Customeraddtoorder.objects.filter(trackingid=id).update(productstatus='Returned Request',productstatusdate='')
        return redirect('/ordertracker/'+id)

def wishlistlist(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        clearactive('Payment settings',2)
        userdeatails['currentsite'] = "/wishlistlist/"+str(id)
        userdeatails['2ndnavlinkactive']={'wishlistlist':'show active'}
        userdeatails['Requirements']['usershopwishlist']=list(Customeraddtowishlist.objects.filter(userid=request.COOKIES.get(userdeatails['idrandam'])).values())
        templen = len(userdeatails['Requirements']['usershopwishlist'])
        userdeatails['Requirements']['usershopwishlist'] = userdeatails['Requirements']['usershopwishlist'][:(id*5)]
        if(id*5 < templen):
            userdeatails['Requirements']['shopwishlistnext'] = id+1
            userdeatails['Requirements']['totalwishlistno'] = templen
            userdeatails['Requirements']['wishlistno'] = id*5
            userdeatails['Requirements']['wishlistprogressno'] = (id*5*100)/templen
        else:
            userdeatails['Requirements']['shopwishlistnext'] = 0
        for i in range(len(userdeatails['Requirements']['usershopwishlist'])):
            userdeatails['Requirements']['usershopwishlist'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['usershopwishlist'][i]['productid']).values())[0]
            userdeatails['Requirements']['usershopwishlist'][i]['productnos'] = i
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return render(request, 'main/accountprofile.html', {'userdeatails': userdeatails})

def addwishlist(request,id,id1):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(id1==1):
            productdetails = list(Customeraddtowishlist.objects.filter(id = id).values())
            tempk = int(request.POST['quantity'+str(id)])*productdetails[0]['one_price']
            Customeraddtowishlist.objects.filter(id = id).update(Productquantity = int(request.POST['quantity'+str(id)]),total_price = tempk)
            return JsonResponse(tempk, safe = False)
        elif(id1==2):
            productdetails = list(Customeraddtowishlist.objects.filter(id = id).values())
            productdetails1 = list(Customeraddtocart.objects.filter(productid = productdetails[0]['productid']).values())
            if(len(productdetails1)):
                Customeraddtocart.objects.filter(id = productdetails1[0]['id']).update(Productquantity = productdetails[0]['Productquantity']+productdetails1[0]['Productquantity'],total_price = productdetails[0]['total_price']+productdetails1[0]['total_price'])
            else:
                cl =Customeraddtocart(userid = productdetails[0]['userid'],productid = productdetails[0]['productid'],Productquantity = productdetails[0]['Productquantity'])
                cl.save()
            cl = Customeraddtowishlist.objects.get(id=id)
            cl.delete()
        else:
            cl = Customeraddtowishlist.objects.get(id=id)
            cl.delete()
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return redirect(userdeatails['currentsite'])
            
def ticketslist(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/orderlist"
        return render(request, 'main/account-tickets.html', {'userdeatails': userdeatails})

def purchaseslist(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/orderlist"
        return render(request, 'main/dashboard-purchases.html', {'userdeatails': userdeatails})

def productdetails(request,id):
    userdeatails['currentsite'] = "/productdetails/"+str(id)
    productdetails = list(Product.objects.filter(id=id).values())
    if(len(productdetails)):
        productdetails = productdetails[0]
    else:
        return redirect('errorpage')
    userdeatails['usertype'] = productdetails['name']
    userdeatails['Requirements']['productdetaillist']=list(Product.objects.filter(productcatagory2=productdetails['productcatagory2']).exclude(id=id).values())
    if(len(userdeatails['Requirements']['productdetaillist']) > 15):
        userdeatails['Requirements']['productdetaillist'] = random.choices(userdeatails['Requirements']['productdetaillist'], k=10)
    userdeatails['Requirements']['productdetaillistno']=len(userdeatails['Requirements']['productdetaillist'])
    templist1 = list(Producttogether.objects.filter(productid=productdetails['id']).values())
    templist2 = list(Producttogether.objects.filter(productid1=productdetails['id']).values())
    userdeatails['Requirements']['productdetailtogetherlist']=[{} for i in range(len(templist1)+len(templist2))]
    if(len(templist1)+len(templist2)):
        for i in range(len(templist1)):
            userdeatails['Requirements']['productdetailtogetherlist'][i]['productid'] = templist1[i]['productid1']
            userdeatails['Requirements']['productdetailtogetherlist'][i]['discout'] = templist1[i]['discount']
            userdeatails['Requirements']['productdetailtogetherlist'][i]['productdetails1'] = productdetails
            userdeatails['Requirements']['productdetailtogetherlist'][i]['productdetails2'] = list(Product.objects.filter(id=templist1[i]['productid1']).values())[0]
            userdeatails['Requirements']['productdetailtogetherlist'][i]['total_price'] = floatconvert(list(Product.objects.filter(id=productdetails['id']).values())[0]['price_save'] + list(Product.objects.filter(id=templist1[i]['productid1']).values())[0]['price_save'])
            userdeatails['Requirements']['productdetailtogetherlist'][i]['discout_price'] = floatconvert(userdeatails['Requirements']['productdetailtogetherlist'][i]['total_price'] - floatconvert(userdeatails['Requirements']['productdetailtogetherlist'][i]['total_price'] * floatconvert(templist1[i]['discount']) / floatconvert(100)))
        for i in range(len(templist2)):
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['productid'] = templist2[i]['productid']
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['discout'] = templist2[i]['discount']
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['productdetails1'] = productdetails
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['productdetails2'] = list(Product.objects.filter(id=templist2[i]['productid']).values())[0]
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['total_price'] = floatconvert(list(Product.objects.filter(id=productdetails['id']).values())[0]['price_save'] + list(Product.objects.filter(id=templist2[i]['productid']).values())[0]['price_save'])
            userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['discout_price'] = floatconvert(userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['total_price'] - floatconvert(userdeatails['Requirements']['productdetailtogetherlist'][len(templist1)+i]['total_price'] * floatconvert(templist2[i]['discount']) / floatconvert(100)))
    userdeatails['Requirements']['productdetailtogetherlistno']=len(userdeatails['Requirements']['productdetailtogetherlist'])
    # print(productdetails)
    if(request.COOKIES.get(userdeatails['idrandam'])):
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
    return render(request, 'main/productdetails.html', {'userdeatails': userdeatails,'productdetails': productdetails})
    
def useraddtocart(request,id,id1):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        productdetails = list(Customeraddtocart.objects.filter(userid = id1,productid = id).values())
        if(len(productdetails)==0):
            cl =Customeraddtocart(userid = id1,productid = id,Productquantity = 1)
            cl.save()
        else:
            Customeraddtocart.objects.filter(userid = id1,productid = id).update(Productquantity = productdetails[0]['Productquantity']+1,total_price = productdetails[0]['total_price']+productdetails[0]['one_price'])
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return redirect("/productdetails/"+str(id))

# def shopcsprfunction(a,n):
#     userdeatails['Requirements']['shopcspr'] = shopcspr
#     for i in range(0,n+1):
#         userdeatails['Requirements']['shopcspr'][i]['class'] = "active"
#     for i in range(0,n):
#         userdeatails['Requirements']['shopcspr'][i]['icon'] = "fa-regular fa-badge-check fa-fw"
#     userdeatails['Requirements']['shopcspr'][n]['class'] += " current"
#     userdeatails['currentsite'] = "/"+userdeatails['Requirements']['shopcspr'][n]['link']
#     userdeatails['usertype'] = shopcspr[n]['title']
#     updateprofile(a,"Customer")

# shopcspr = [
#     {'class':'','title':'Cart','icon':"ci-cart",'link':"usershopcart"},
#     {'class':'','title':'Shipping','icon':"ci-package",'link':"usercheckoutshipping"},
#     {'class':'','title':'Payment','icon':"ci-card",'link':"usercheckoutpayment"},
#     {'class':'','title':'Review','icon':"ci-check-circle",'link':"usercheckoutreview"},
# ]

def usershopcart(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/usershopcart"
        userdeatails['usertype'] = 'Cart'
        userdeatails['Requirements']['usershopwishlist']=list(Customeraddtowishlist.objects.filter(userid=request.COOKIES.get(userdeatails['idrandam'])).values())
        for i in range(len(userdeatails['Requirements']['usershopwishlist'])):
            userdeatails['Requirements']['usershopwishlist'][i]['productdetails'] = list(Product.objects.filter(id=userdeatails['Requirements']['usershopwishlist'][i]['productid']).values())[0]
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
        return render(request, 'main/shopcart.html', {'userdeatails': userdeatails})

def usershopcartsettings(request,id,id1):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(id1==1):
            productdetails = list(Customeraddtocart.objects.filter(id = id).values())
            tempk = int(request.POST['quantity'+str(id)])*productdetails[0]['one_price']
            Customeraddtocart.objects.filter(id = id).update(Productquantity = int(request.POST['quantity'+str(id)]),total_price = tempk)
            tempk1=list(Customeraddtocart.objects.filter(userid=int(request.COOKIES.get(userdeatails['idrandam']))).values())
            a=0
            for i in tempk1:
                a+=i['total_price']
            return JsonResponse([tempk,a], safe = False)
        elif(id1==2):
            productdetails = list(Customeraddtocart.objects.filter(id = id).values())
            productdetails1 = list(Customeraddtowishlist.objects.filter(productid = productdetails[0]['productid']).values())
            if(len(productdetails1)):
                Customeraddtowishlist.objects.filter(id = productdetails1[0]['id']).update(Productquantity = productdetails[0]['Productquantity']+productdetails1[0]['Productquantity'],total_price = productdetails[0]['total_price']+productdetails1[0]['total_price'])
            else:
                cl =Customeraddtowishlist(userid = productdetails[0]['userid'],productid = productdetails[0]['productid'],Productquantity = productdetails[0]['Productquantity'])
                cl.save()
            cl = Customeraddtocart.objects.get(id=id)
            cl.delete()
        else:
            cl = Customeraddtocart.objects.get(id=id)
            cl.delete()
        updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
        return redirect(userdeatails['currentsite'])

def userbuyproduct(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/userbuyproduct/"+str(id)
        userdeatails['usertype'] = 'Shipping'
        userdeatails['Requirements']['userbuyproductdeatailsid']=id
        userdeatails['Requirements']['userbuyproductdeatails']=list(Product.objects.filter(id=id).values())
        userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'] = 1*userdeatails['Requirements']['userbuyproductdeatails'][0]['price_save']
        userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalpricegst'] = floatconvert((floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['price_save'])*userdeatails['gstrate'])/floatconvert(100))
        userdeatails['Requirements']['userbuyproductdeatails'][0]['Productquantity'] = 1
        userdeatails['Requirements']['userbuyproductdeatails'][0]['useralltotalprice'] = floatconvert(floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalpricegst'])+floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'])+floatconvert(100))
        updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
        return render(request, 'main/checkoutshippingonce.html', {'userdeatails': userdeatails})

def usercheckoutshipping(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/usercheckoutshipping"
        userdeatails['usertype'] = 'Shipping'
        updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
        return render(request, 'main/checkoutshipping.html', {'userdeatails': userdeatails})

def usertkdaddressoption(request,id,id1):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['Requirements']['addressoptionid'] = id
        if(id1):
            return redirect('usercheckoutpayment')
        else:
            return redirect('usercheckoutpaymentonce')

def usercheckoutpaymentonce(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(userdeatails['Requirements']['userbuyproductdeatailsid']==0):
            return redirect(userdeatails['currentsite'])
        userdeatails['currentsite'] = "/usercheckoutpaymentonce"
        userdeatails['usertype'] = 'Payment'
        updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
        return render(request, 'main/checkoutpaymentonce.html', {'userdeatails': userdeatails})

def usercheckoutpayment(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['currentsite'] = "/usercheckoutpayment"
        userdeatails['usertype'] = 'Payment'
        updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
        return render(request, 'main/checkoutpayment.html', {'userdeatails': userdeatails})

def usertkdpaymentoption(request,id,id1):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['Requirements']['paymentoptionid'] = id
        if id1:return redirect('usercheckoutreview')
        else:return redirect('usercheckoutreviewonce')

def usercheckoutreviewonce(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(userdeatails['Requirements']['addressoptionid']):
            if(userdeatails['Requirements']['paymentoptionid']):
                userdeatails['currentsite'] = "/usercheckoutreviewonce"
                userdeatails['usertype'] = 'Review'
                updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
                userdeatails['Requirements']['addressoptionlist'] = customeraddresses.objects.filter(id=userdeatails['Requirements']['addressoptionid']).values()
                userdeatails['Requirements']['paymentoptionlist'] = customerpayment.objects.filter(id=userdeatails['Requirements']['paymentoptionid']).values()
                return render(request, 'main/checkoutreviewonce.html', {'userdeatails': userdeatails})
            else:
                return redirect('usercheckoutpaymentonce')
        else:
            return redirect('home')

def usercheckoutreviewoncesettings(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'] = int(request.POST['quantity'+str(id)])*userdeatails['Requirements']['userbuyproductdeatails'][0]['price_save']
        userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalpricegst'] = floatconvert((floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'])*userdeatails['gstrate'])/floatconvert(100))
        userdeatails['Requirements']['userbuyproductdeatails'][0]['Productquantity'] = int(request.POST['quantity'+str(id)])
        userdeatails['Requirements']['userbuyproductdeatails'][0]['useralltotalprice'] = floatconvert(floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalpricegst'])+floatconvert(userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'])+floatconvert(100))
        tempk1=[userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalprice'],userdeatails['Requirements']['userbuyproductdeatails'][0]['useralltotalprice'],userdeatails['Requirements']['userbuyproductdeatails'][0]['usertotalpricegst']]
        return JsonResponse(tempk1, safe = False)

def usercheckoutreview(request):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(userdeatails['Requirements']['addressoptionid']):
            if(userdeatails['Requirements']['paymentoptionid']):
                userdeatails['currentsite'] = "/usercheckoutreview"
                userdeatails['usertype'] = 'Review'
                updateprofile(request.COOKIES.get(userdeatails['idrandam']),"Customer")
                userdeatails['Requirements']['addressoptionlist'] = customeraddresses.objects.filter(id=userdeatails['Requirements']['addressoptionid']).values()
                userdeatails['Requirements']['paymentoptionlist'] = customerpayment.objects.filter(id=userdeatails['Requirements']['paymentoptionid']).values()
                return render(request, 'main/checkoutreview.html', {'userdeatails': userdeatails})
            else:
                return redirect('usercheckoutpayment')
        else:
            return redirect('usercheckoutshipping')

def usercheckoutcomplete(request,id):
    if(request.COOKIES.get(userdeatails['idrandam'])==None):
        return redirect('tkdlogin')
    else:
        if(userdeatails['Requirements']['addressoptionid']):
            if(userdeatails['Requirements']['paymentoptionid']):
                orderidgen=generaterandomstring(11)
                if id:
                    tempcom = userdeatails['Requirements']['usershopcart']
                else:
                    tempcom = userdeatails['Requirements']['userbuyproductdeatails']
                for i in tempcom:
                    trackingidgen=generaterandomstring(15)
                    if id:
                        userid1=i['userid']
                        productid=i['productid']
                    else:
                        userid1=request.COOKIES.get(userdeatails['idrandam'])
                        productid=i['id']
                    cl = Customeraddtoorder(productid=productid,Productquantity=i['Productquantity'],userid=userid1,addressid=userdeatails['Requirements']['addressoptionid'],paymentid=userdeatails['Requirements']['paymentoptionid'],paid=True,orderid=orderidgen,trackingid=trackingidgen)
                    cl.save()
                    if id:
                        cl1 = Customeraddtocart.objects.get(id=i['id'])
                        cl1.delete()
                userdeatails['Requirements']['orderidgen']=orderidgen
                updateprofile(int(request.COOKIES.get(userdeatails['idrandam'])),"Customer")
                return render(request, 'main/checkoutcomplete.html', {'userdeatails': userdeatails})
            else:
                return redirect('usercheckoutpayment')
        else:
            if id:return redirect('usercheckoutshipping')
            else:return redirect('home')

sociallink = [
    {'title': "logo",'title1': "the koushik durgas",'icon': "tkd-title2",'link': "http://thekoushikdurgas.in/"},
    {'title': "telegram",'title1': "telegram",'icon': "socicon-telegram",'link': "https://t.me/The_Koushik_Durgas"},
    {'title': "facebook",'title1': "facebook",'icon': "fab fa-facebook",'link': "https://facebook.com"},
    {'title': "twitter",'title1': "twitter",'icon': "tkd11-twitter",'link': "https://twitter.com"},
    {'title': "google",'title1': "google",'icon': "fi fi-google",'link': "https://google.com"},
    {'title': "linkedin",'title1': "linkedin",'icon': "tkd9-linkedin-round",'link': "https://linkedin.com"},
    {'title': "youtube",'title1': "youtube",'icon': "fab fa-youtube",'link': "https://youtube.com"},
    {'title': "instagram",'title1': "instagram",'icon': "fab fa-instagram",'link': "https://instagram.com"},
    {'title': "stackoverflow",'title1': "stack overflow",'icon': "tkd4-iconmonstr-stackoverflow-4",'link': "https://stackoverflow.com"},
    {'title': "skype",'title1': "skype",'icon': "icon3-skype",'link': "https://skype.com"},
    {'title': "android",'title1': "android",'icon': "icon2-android",'link': "https://android.com"},
    {'title': "github",'title1': "github",'icon': "fab fa-github",'link': "https://github.com"},
    {'title': "whatsapp",'title1': "whatsapp",'icon': "tkd4-iconmonstr-whatsapp-1",'link': "https://web.whatsapp.com"},
    {'title': "discord",'title1': "discord",'icon': "socicon-discord",'link': "https://discord.com/"},
]
    
customernavbar={
    "Payment settings":[
        {'class':"border-bottom mb-0",'link':'/payoutslist','name':'Payouts','icon':'ci-currency-exchange','active':""},
        {'class':"border-bottom mb-0",'link':'/orderlist/all/1/1','name':'Orders','icon':'ci-bag','active':""},
        {'class':"border-bottom mb-0",'link':'/wishlistlist/1','name':'Wishlist','icon':'ci-heart','active':""},
        {'class':"border-bottom mb-0",'link':'/ticketslist','name':'Support tickets','icon':'ci-help','active':""},
        {'class':"mb-0",'link':'/purchaseslist','name':'Purchases','icon':'ci-basket','active':""},
    ],
    "Account settings":[
        {'class':"border-bottom mb-0",'link':'/profile/1','name':'Profile','icon':'ci-user','active':""},
        {'class':"border-bottom mb-0",'link':'/addresslist/1','name':'Addresses','icon':'ci-location','active':""},
        {'class':"border-bottom mb-0",'link':'/paymentlist/1','name':'Payment methods','icon':'ci-card','active':""},
        {'class':"mb-0",'link':'/userlogout','name':'Sign out','icon':'ci-sign-out','active':""},
    ]
}
productstatuslist={
'all':"All",
"pending":"Pending",
"accepted":"Accepted",
"packed":"Packed",
"shipped":"Shipped",
"on-the-way":"On The Way",
"delivered":"Delivered",
"cancel":"Cancel",
"returned-request":"Returned Request",
"returned":"Returned",
"refunded":"Refunded",
}
trackingstatuslist1=[
    {'status':"Accepted",'icon':"fa-solid fa-clipboard-check fa-fw",'date':"",'description':""},
    {'status':"Packed",'icon':"fa-duotone fa-box-check fa-fw",'date':"",'description':""},
    {'status':"Shipped",'icon':"fa-light fa-clipboard-list-check fa-fw",'date':"",'description':""},
    {'status':"On The Way",'icon':"ci-delivery",'date':"",'description':""},
    {'status':"Delivered",'icon':"fa-solid fa-location-check fa-fw",'date':"",'description':""},
]
trackingstatuslist2=[
    {'status':"Returned Request",'icon':"fa-light fa-rotate-left fa-fw",'date':"",'description':""},
    {'status':"Returned",'icon':"fa-solid fa-house-person-return fa-fw",'date':"",'description':""},
    {'status':"Refunded",'icon':"fa-solid fa-hands-holding-dollar fa-fw",'date':"",'description':""},
]
productlist=list(Category1.objects.filter().values('catagory_name').all())
productdict={'all':"All"}
for i in range(len(productlist)):
    productdict[productlist[i]['catagory_name'].replace(' ','_').lower()]=productlist[i]['catagory_name']
Copyright = {'name':'TheKoushikDurgas' , 'link':'http://thekoushikdurgas.in/' , 'year':"(2020-"+datetime.datetime.now().strftime("%Y")+")"}
userdeatails = {'id': 0,'idrandam': generaterandomstring(10),'username': "",'userpic': "",'userdob': "",'usergender': "",'userphone': "",'useremail': "",'userpassword': "",'usertype': "",'usertitle': "",'usertitleicon': "",'usertitle1': "",'usertitleicon1': "","navlink":{},'Copyright': Copyright,"currentsite": "../../../",'product':{},'2ndnavlink':[],'2ndnavlinkactive':{},'Requirements':{'paymentoptionid':0,'addressoptionid':0,'userbuyproductdeatailsid':0,'searchlink':'/search/all/1/all'},'gstrate':floatconvert(2.5),'productlist':productdict}