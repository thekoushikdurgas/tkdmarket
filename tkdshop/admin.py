from django.contrib import admin
from .models import Category1,Category2,Customeraddtocart,Product,customerdeatail,customeraddresses,countrylist,continentlist,customerpayment,Customeraddtoorder,productstatusmodel,Customeraddtowishlist,Producttogether
from django.utils.html import format_html

class customerdeatailAdmin(admin.ModelAdmin):
    list_display = ['useremail','userpic','username', 'userdob',  'usergender','userphone','userrewardpoints', 'created_at', 'updated_at']
    list_filter = ['usergender','userrewardpoints', 'created_at', 'updated_at']
    list_editable = ['username','userdob', 'usergender','userphone','userrewardpoints']
    search_fields = ['username','useremail','userphone']
admin.site.register(customerdeatail,customerdeatailAdmin)

class customeraddressesAdmin(admin.ModelAdmin):
    list_display = ['useraddressno','useraddress','username', 'usercity', 'userstate', 'usercountry','useraddressprimary', 'created_at', 'updated_at']
    list_filter = ['useraddressprimary', 'created_at', 'updated_at']
    list_editable = ['useraddress','username', 'usercity', 'userstate', 'usercountry']
    search_fields = ['useraddress','username', 'usercity', 'userstate', 'usercountry']
admin.site.register(customeraddresses,customeraddressesAdmin)

class customerpaymentAdmin(admin.ModelAdmin):
    list_display = ['userpaymentno','usercardnumber','usercardtype','usercardname','usercardcvc','usercardmonth','usercardyear','userpaymentprimary', 'created_at', 'updated_at']
    list_filter = ['userpaymentprimary', 'created_at', 'updated_at']
    list_editable = ['usercardnumber','usercardtype','usercardname','usercardcvc','usercardmonth','usercardyear']
    search_fields = ['usercardnumber','usercardtype','usercardname','usercardcvc','usercardmonth','usercardyear']
admin.site.register(customerpayment,customerpaymentAdmin)

class countrylistAdmin(admin.ModelAdmin):
    list_display = ['countryvalue','countryname', 'countryccode', 'countrymcode']
    list_editable = ['countryname', 'countryccode', 'countrymcode']
    search_fields = ['countryname','countryvalue', 'countryccode', 'countrymcode']
admin.site.register(countrylist,countrylistAdmin)

class continentlistAdmin(admin.ModelAdmin):
    list_display = ['countryname','continentname']
    list_editable = ['continentname']
    search_fields = ['continentname','countryname']
admin.site.register(continentlist,continentlistAdmin)

class productstatusmodelAdmin(admin.ModelAdmin):
    list_display = ['trackingid','orderdesc','productstatustype', 'created_at', 'updated_at']
    list_filter = ['productstatustype', 'created_at', 'updated_at']
    list_editable = ['orderdesc','productstatustype']
    search_fields = ['trackingid','orderdesc','productstatustype',]
admin.site.register(productstatusmodel,productstatusmodelAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productid','name','catagory_id', 'productcatagory','productcatagory2', 'price', 'stock', 'available','created_at', 'updated_at']
    list_filter = ['available','productcatagory', 'created_at', 'updated_at']
    list_editable = ['price','catagory_id', 'stock', 'available']
    search_fields = ['name','image']
admin.site.register(Product, ProductAdmin)

class Category2Admin(admin.ModelAdmin):
    list_display = ['catagory_name', 'catagory_id','catagory_name2']
    # list_editable = ['catagory_name','catagory_name2']
    search_fields = ['catagory_name','catagory_name2']
admin.site.register(Category2, Category2Admin)

class Category1Admin(admin.ModelAdmin):
    list_display = ['catagory_id','catagory_name']
    list_editable = ['catagory_name']
    search_fields = ['catagory_name']
admin.site.register(Category1, Category1Admin)

class ProducttogetherAdmin(admin.ModelAdmin):
    list_display = ['userid','Producttogetherid','productid','productid1','discount', 'created_at', 'updated_at']
    list_editable = ['productid','productid1','discount']
    search_fields = ['productid','productid1','discount']
admin.site.register(Producttogether, ProducttogetherAdmin)

class CustomeraddtocartAdmin(admin.ModelAdmin):
    list_display = ['userid','productid','Productquantity','one_price','total_price', 'created_at', 'updated_at']
    list_filter = ['Productquantity','created_at', 'updated_at']
    list_editable = ['Productquantity']
admin.site.register(Customeraddtocart, CustomeraddtocartAdmin)

class CustomeraddtowishlistAdmin(admin.ModelAdmin):
    list_display = ['userid','productid','Productquantity','one_price','total_price', 'created_at', 'updated_at']
    list_filter = ['Productquantity','created_at', 'updated_at']
    list_editable = ['Productquantity']
admin.site.register(Customeraddtowishlist, CustomeraddtowishlistAdmin)

class CustomeraddtoorderAdmin(admin.ModelAdmin):
    list_display = ['trackingid','orderid','Productquantity','one_price','total_price','productstatus','paid', 'created_at', 'updated_at']
    list_filter = ['productstatus','paid', 'created_at', 'updated_at']
    list_editable = ['Productquantity','paid','productstatus']
    search_fields = ['trackingid','orderid']
admin.site.register(Customeraddtoorder, CustomeraddtoorderAdmin)