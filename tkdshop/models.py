from django.db import models
from multiselectfield import MultiSelectField
import os
import random
from django.contrib.auth.models import User
import computed_property
from django.utils.html import mark_safe
from django.core.files import File
import urllib
GENDER_CHOICES = [
    ['all', 'All'],
    ['male', 'Male'],
    ['female', 'Female'],
    ['kid', 'Kids'],
    ['others', 'Others'],
]
STATUS_CHOICES = [
    ['Pending', 'Pending'],
    ['Accepted', 'Accepted'],
    ['Packed', 'Packed'],
    ['Shipped', 'Shipped'],
    ['On The Way', 'On The Way'],
    ['Delivered', 'Delivered'],
    ['Returned Request', 'Returned Request'],
    ['Returned', 'Returned'],
    ['Refunded', 'Refunded'],
    ['Cancel', 'Cancel'],
]
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'


def photo_path(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'customer/pic/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)


def productpath(instance, filename):
    basename, file_extension = os.path.splitext(filename)
    return 'products/pic/{randomstring}{ext}'.format(randomstring=''.join((random.choice(chars)) for x in range(11)), ext=file_extension)


def generaterandomstring(n):
    return ''.join((random.choice(chars)) for x in range(n))

class customerdeatail(models.Model):
    username = models.CharField(max_length=30)
    userpic = models.ImageField(upload_to=photo_path, blank=True, null=True, default='customer/pic/default.jpg')
    userdob = models.CharField(max_length=30)
    useremail = models.EmailField()
    userpassword = models.CharField(max_length=30)
    usergender = models.CharField(choices=GENDER_CHOICES, default="male", max_length=150)
    userphone = models.CharField(max_length=30)
    userrewardpoints = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.useremail

    class Meta:
        db_table = "customerdeataillist"


class customeraddresses(models.Model):
    username = models.CharField(max_length=30)
    userid = models.CharField(max_length=30)
    useraddressno = models.CharField(max_length=3000)
    useraddressprimary = models.BooleanField(default=False, blank=True)
    useraddress = models.CharField(max_length=3000)
    usercountry = models.CharField(max_length=3000)
    userstate = models.CharField(max_length=3000)
    usercity = models.CharField(max_length=3000)
    userzipcode = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userid + " " + self.useraddressno

    class Meta:
        db_table = "customeraddresseslist"


class customerpayment(models.Model):
    userid = models.CharField(max_length=30)
    userpaymentno = models.CharField(max_length=3000)
    userpaymentprimary = models.BooleanField(default=False, blank=True)
    usercardtype = models.CharField(max_length=3000)
    usercardnumber = models.CharField(max_length=3000)
    usercardname = models.CharField(max_length=3000)
    usercardcvc = models.CharField(max_length=3000)
    usercardmonth = models.CharField(max_length=3000)
    usercardyear = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def usercardnumberformat(self):
        templist = list(self.usercardnumber)
        return '**** **** **** ' + ''.join(templist[-4:])

    def usercardcvcformat(self):
        return '*' * len(self.usercardcvc)

    usercardnumber_format = computed_property.ComputedCharField(max_length=150, compute_from='usercardnumberformat')
    usercardcvc_format = computed_property.ComputedCharField(max_length=150, compute_from='usercardcvcformat')

    def __str__(self):
        return self.userid + " " + self.userpaymentno

    class Meta:
        db_table = "customerpaymentlist"


class countrylist(models.Model):
    countryccode = models.CharField(max_length=30)
    countryvalue = models.CharField(max_length=30)
    countryname = models.CharField(max_length=30)
    countrymcode = models.CharField(max_length=30)

    def __str__(self):
        return self.countryname

    class Meta:
        db_table = "countrylist"


class continentlist(models.Model):
    countryname = models.CharField(max_length=30)
    continentname = models.CharField(max_length=30)

    def __str__(self):
        return self.continentname

    class Meta:
        db_table = "continentlist"


class Category1(models.Model):
    catagory_id = models.AutoField(primary_key=True)
    catagory_name = models.CharField(max_length=150)

    class Meta:
        db_table = "Category1list"

    def __str__(self):
        return self.catagory_name


class Category2(models.Model):
    catagory_id = models.AutoField(primary_key=True)
    catagory_name = models.CharField(max_length=150)
    catagory_name2 = models.CharField(max_length=150, default="")

    class Meta:
        db_table = "Category2list"

    def __str__(self):
        return self.catagory_name + " > " + self.catagory_name2


class Product(models.Model):
    userid = models.CharField(max_length=150)
    catagory_id = models.CharField(max_length=150,default="3")
    product_gender = MultiSelectField(choices=GENDER_CHOICES)
    brand = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=5)
    available = models.BooleanField(default=True)
    payondelivery = models.BooleanField(default=True)
    replacement = models.BooleanField(default=True)
    delivered = models.BooleanField(default=True)
    sale = models.BooleanField(default=True)
    warranty = models.PositiveIntegerField(default=2)
    stock = models.PositiveIntegerField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=productpath, blank=True, null=True, default='customer/pic/default.jpg')
    @property
    def pricesave(self):
        return self.price - (self.price * self.discount / 100)

    @property
    def yourprice(self):
        return self.price * self.discount / 100

    @property
    def product_catagory(self):
        tempintlist = list(Category2.objects.filter(catagory_id=self.catagory_id).values().all())[0]
        return tempintlist['catagory_name']

    @property
    def product_catagory2(self):
        tempintlist = list(Category2.objects.filter(catagory_id=self.catagory_id).values().all())[0]
        return tempintlist['catagory_name2']

    def image_tag(self):
        return mark_safe('<img src="/tkdproduct/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    productid = models.CharField(max_length=150,default="VTtT1tdymGUomg12nbZ1")
    productcatagory =  models.CharField(max_length=150)
    productcatagory2 =  models.CharField(max_length=150)
    price_save = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='pricesave')
    your_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='yourprice')

    class Meta:
        db_table = "Productlist"

    def __str__(self):
        return str(self.name)


class Customeraddtocart(models.Model):
    productid = models.CharField(max_length=150)
    userid = models.CharField(max_length=150)
    Productquantity = models.PositiveIntegerField(default=1000)

    @property
    def cart_id(self):
        return str(self.id)

    @property
    def totalprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save'] * self.Productquantity

    @property
    def oneprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save']

    cartid = computed_property.ComputedCharField(max_length=150, compute_from='cart_id')
    total_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='totalprice',
                                                         default="0")
    one_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='oneprice',
                                                       default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Customeraddtocartlist"

    def __str__(self):
        return self.cartid + " -- " + self.productid + " -- " + str(self.total_price)


class productstatusmodel(models.Model):
    trackingid = models.CharField(max_length=150)
    orderdesc = models.CharField(max_length=150)
    productstatustype = models.CharField(choices=STATUS_CHOICES, default="Pending", max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "productstatuslist"

    def __str__(self):
        return self.trackingid


class Customeraddtoorder(models.Model):
    productid = models.CharField(max_length=150)
    Productquantity = models.PositiveIntegerField(default=1000)
    userid = models.CharField(max_length=150)
    addressid = models.CharField(max_length=150)
    paymentid = models.CharField(max_length=150)
    paid = models.BooleanField(default=False)
    productstatus = models.CharField(choices=STATUS_CHOICES, default="Pending", max_length=150)
    orderid = models.CharField(max_length=150, default="")
    trackingid = models.CharField(max_length=150, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def totalprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save'] * self.Productquantity

    @property
    def oneprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save']

    @property
    def product_status_date(self):
        if self.productstatus == 'Cancel':
            if (len(list(productstatusmodel.objects.filter(trackingid=self.trackingid,
                                                           productstatustype='Cancel').values())) == 0):
                cl = productstatusmodel(trackingid=self.trackingid, orderdesc="Order is Cancel",
                                        productstatustype='Cancel')
                cl.save()
            else:
                productstatusmodel.objects.filter(trackingid=self.trackingid, productstatustype='Cancel').update(
                    orderdesc="Order is Cancel")
        else:
            for i in range(len(STATUS_CHOICES)):
                if (len(list(productstatusmodel.objects.filter(trackingid=self.trackingid, productstatustype=STATUS_CHOICES[i][0]).values())) == 0):
                    cl = productstatusmodel(trackingid=self.trackingid, orderdesc="Order is " + STATUS_CHOICES[i][0],
                                            productstatustype=STATUS_CHOICES[i][0])
                    cl.save()
                else:
                    productstatusmodel.objects.filter(trackingid=self.trackingid,
                                                      productstatustype=STATUS_CHOICES[i][0]).update(
                        orderdesc="Order is " + STATUS_CHOICES[i][0])
                if STATUS_CHOICES[i][0] == self.productstatus:
                    break
            for j in range(i + 1, len(STATUS_CHOICES)):
                cl = productstatusmodel.objects.filter(trackingid=self.trackingid,
                                                       productstatustype=STATUS_CHOICES[j][0])
                cl.delete()
        return ""

    productstatusdate = computed_property.ComputedCharField(max_length=150, compute_from='product_status_date',
                                                            default="")
    total_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='totalprice',
                                                         default="0")
    one_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='oneprice',
                                                       default="0")

    class Meta:
        db_table = "Customeraddtoorderlist"

    def __str__(self):
        return self.orderid + " -- " + self.productid + " -- " + str(self.total_price)

class Customeraddtowishlist(models.Model):
    productid = models.CharField(max_length=150)
    userid = models.CharField(max_length=150)
    Productquantity = models.PositiveIntegerField(default=1000)

    @property
    def wishlist_id(self):
        return str(self.id)

    @property
    def totalprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save'] * self.Productquantity

    @property
    def oneprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save']

    wishlistid = computed_property.ComputedCharField(max_length=150, compute_from='wishlist_id')
    total_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='totalprice',
                                                         default="0")
    one_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='oneprice',
                                                       default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wishlistlist"

    def __str__(self):
        return self.wishlistid + " -- " + self.productid + " -- " + str(self.total_price)
        
class Producttogether(models.Model):
    userid = models.CharField(max_length=150)
    productid = models.CharField(max_length=150)
    productid1 = models.CharField(max_length=150)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=5)

    @property
    def Producttogether_id(self):
        return str(self.id)

    # @property
    # def totalprice(self):
    #     return list(Product.objects.filter(id=self.productid).values())[0]['price_save'] * list(Product.objects.filter(id=self.productid1).values())[0]['price_save']

    @property
    def productprice(self):
        return list(Product.objects.filter(id=self.productid).values())[0]['price_save']
    @property
    def product1price(self):
        return list(Product.objects.filter(id=self.productid1).values())[0]['price_save']

    product_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='productprice', default="0")
    product1_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='product1price', default="0")
    Producttogetherid = computed_property.ComputedCharField(max_length=150, compute_from='Producttogether_id')
    # total_price = computed_property.ComputedDecimalField(max_digits=10, decimal_places=2, compute_from='totalprice', default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Producttogetherlist"

    def __str__(self):
        return self.productid1 + " -- " + self.productid + " -- " + str(self.discount)
