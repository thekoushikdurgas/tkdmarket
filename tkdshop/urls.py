from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import tests

admin.site.site_header = "TKD Market Admin"
admin.site.site_title = "TKD Market"
admin.site.index_title = "Welcome to TKD Market"
urlpatterns = [
    path('', views.home, name="home"),
    # path('insertdata', tests.insertdata, name="insertdata"),
    # path('showtable', tests.showtable, name="showtable"),
    # path('deletetable', tests.deletetable, name="deletetable"),
    path('404', views.errorpage, name="errorpage"),
    path('search/<id>/<int:id1>/<int:id3>/<id2>', views.search, name="search"),
    path('help_topics', views.helptopics, name="helptopics"),
    path('contacts', views.contacts, name="contacts"),
    path('tkdlogin', views.tkdlogin, name="tkdlogin"),
    path('userlogout', views.userlogout, name="userlogout"),
    path('customerregistration', views.customerregistration, name="customerregistration"),
    path('customerforgotusername', views.customerforgotusername, name="customerforgotusername"),
    path('customerforgotpassword', views.customerforgotpassword, name="customerforgotpassword"),
    path('profile/<int:id>', views.profile, name="profile"),
    path('profileavaterchange/<int:id>', views.profileavaterchange, name="profileavaterchange"),
    path('profiledeatailschange/<int:id>', views.profiledeatailschange, name="profiledeatailschange"),
    path('profilepasswordchange/<int:id>', views.profilepasswordchange, name="profilepasswordchange"),
    path('addresslist/<int:id>', views.addresslist, name="addresslist"),
    path('addaddresslist/<int:id>', views.addaddresslist, name="addaddresslist"),
    path('editaddresslist/<int:id>', views.editaddresslist, name="editaddresslist"),
    path('adduseraddressprimary/<int:id>/<int:id1>/<int:id2>', views.adduseraddressprimary, name="adduseraddressprimary"),
    path('statelistshow', views.statelistshow, name="statelistshow"),
    path('paymentlist/<int:id>', views.paymentlist, name="paymentlist"),
    path('addpaymentlist/<int:id>', views.addpaymentlist, name="addpaymentlist"),
    path('editpaymentlist/<int:id>', views.editpaymentlist, name="editpaymentlist"),
    path('adduserpaymentprimary/<int:id>/<int:id1>/<int:id2>', views.adduserpaymentprimary, name="adduserpaymentprimary"),
    path('orderlist/<id>/<int:id1>/<int:id2>', views.orderlist, name="orderlist"),
    path('order/<id>', views.order, name="order"),
    path('ordertracker/<id>', views.ordertracker, name="ordertracker"),
    path('ordercancel/<int:id>', views.ordercancel, name="ordercancel"),
    path('returnitems/<id>', views.returnitems, name="returnitems"),
    path('wishlistlist/<int:id>', views.wishlistlist, name="wishlistlist"),
    path('addwishlist/<int:id>/<int:id1>', views.addwishlist, name="addwishlist"),
    path('payoutslist', views.payoutslist, name="payoutslist"),
    path('ticketslist', views.ticketslist, name="ticketslist"),
    path('purchaseslist', views.purchaseslist, name="purchaseslist"),
    path('usershopcart', views.usershopcart, name="usershopcart"),
    path('productdetails/<int:id>', views.productdetails, name="productdetails"),
    path('useraddtocart/<int:id>/<int:id1>', views.useraddtocart, name="useraddtocart"),
    path('usershopcartsettings/<int:id>/<int:id1>', views.usershopcartsettings, name="usershopcartsettings"),
    path('userbuyproduct/<int:id>', views.userbuyproduct, name="userbuyproduct"),
    path('usercheckoutshipping', views.usercheckoutshipping, name="usercheckoutshipping"),
    path('usertkdaddressoption/<int:id>/<int:id1>', views.usertkdaddressoption, name="usertkdaddressoption"),
    path('usercheckoutpayment', views.usercheckoutpayment, name="usercheckoutpayment"),
    path('usercheckoutpaymentonce', views.usercheckoutpaymentonce, name="usercheckoutpaymentonce"),
    path('usertkdpaymentoption/<int:id>/<int:id1>', views.usertkdpaymentoption, name="usertkdpaymentoption"),
    path('usercheckoutreview', views.usercheckoutreview, name="usercheckoutreview"),
    path('usercheckoutreviewonce', views.usercheckoutreviewonce, name="usercheckoutreviewonce"),
    path('usercheckoutreviewoncesettings/<int:id>', views.usercheckoutreviewoncesettings, name="usercheckoutreviewoncesettings"),
    path('usercheckoutcomplete/<int:id>', views.usercheckoutcomplete, name="usercheckoutcomplete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)