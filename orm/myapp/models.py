from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import UUIDField,TimeField, JSONField
#from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models

import uuid
# Create your models here.
class Customer(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=90)
    email=models.EmailField(unique=True,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=90,null=True)
    Price=models.FloatField()
    Digital=models.BooleanField()
    image=models.ImageField(default='')
    dep=models.CharField(max_length=90,null=True,blank=True)
    salary=models.FloatField(blank=True,default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    order_date=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=True)
    transaction=models.CharField(max_length=90,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class Order_Item(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

class Shipping_Address(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=90,null=True)
    state=models.CharField(max_length=90,null=True)
    city=models.CharField(max_length=90)
    zipcode=models.CharField(max_length=90)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=250)

class Author(models.Model):
   first_name = models.CharField(max_length=512)
   last_name = models.CharField(max_length=512)
   country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='authors', blank=True,null=True)
   
   
   def __str__(self):
        return self.first_name

class Book(models.Model):
    BOOK_STATUS = (
        ('PUBLISHED', 'Published'),
        ('ON_HOLD', 'On Hold'),
    )
    title = models.CharField(max_length=512)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,blank=True,null=True)
    author1 = models.ManyToManyField(Author, related_name='many')
    salary = models.FloatField(default=0)
    status = models.CharField(max_length=255, choices = BOOK_STATUS, default= '')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.BinaryField(models.CharField(max_length=255))
    add = JSONField(max_length=200, default=dict)





class Author1(models.Model):
   first_name = models.CharField(max_length=512)
   last_name = models.CharField(max_length=512)


class Book1(models.Model):
   title = models.CharField(max_length=512)
   authors = models.ManyToManyField(Author1)

   def __str__(self):
       return "%s (%s)" % (
           self.title,
           ", ".join(author.last_name for author in self.authors.all()),
       )

class MyClass(models.Model):
    my_integer = models.IntegerField()
    created_ts = models.DateTimeField(default=datetime.utcnow, editable=False)

    def __str__(self):
        return str(self.my_integer)




class AppCustomerTpRel(models.Model):
    id_rel = models.AutoField(primary_key=True)
    idcst_rel = models.ForeignKey('AppCustomerCst', models.DO_NOTHING, db_column='idcst_rel')
    idtrp_rel = models.ForeignKey('AppTradingPartnerTrp', models.DO_NOTHING, db_column='idtrp_rel')
    cust_vendor_rel = models.CharField(max_length=50, blank=True, null=True)
    sender_id_rel = models.CharField(max_length=50, blank=True, null=True)
    old_vendor_rel = models.CharField(max_length=50, blank=True, null=True)
    vendor_name_rel = models.CharField(max_length=50, blank=True, null=True)
    category_rel = models.CharField(max_length=50, blank=True, null=True)
    #id = models.BigAutoField(primary_key=True)
class AppTradingPartnerTrp(models.Model):
    id_trp = models.IntegerField(primary_key=True)
    tpid_trp = models.CharField(max_length=50, blank=True, null=True)
    name_trp = models.CharField(max_length=50)
    description_trp = models.CharField(max_length=100, blank=True, null=True)
   # idtrn_trp = models.ForeignKey('AppTransmissionTrn', models.DO_NOTHING, db_column='idtrn_trp', blank=True, null=True)
    #IP = models.IntegerField(max_length=250, primary_key=True)
class AppCustomerCst(models.Model):
    id_cst = models.AutoField(primary_key=True)
    is_active_cst = models.BooleanField()
    name_cst = models.CharField(max_length=50, blank=True, null=True)
    address_1_cst = models.CharField(max_length=50, blank=True, null=True)
    address_2_cst = models.CharField(max_length=50, blank=True, null=True)
    address_3_cst = models.CharField(max_length=50, blank=True, null=True)
    city_cst = models.CharField(max_length=50, blank=True, null=True)
    state_cst = models.CharField(max_length=50, blank=True, null=True)
    zip_cst = models.CharField(max_length=10, blank=True, null=True)
    country_cst = models.CharField(max_length=50, blank=True, null=True)
    salesrep_cst = models.CharField(max_length=50, blank=True, null=True)
    type_cst = models.CharField(max_length=10, blank=True, null=True)
    is_allowed_flat_cst = models.BooleanField()
    iddef_cst = models.IntegerField()
    date_created_cst = models.DateTimeField()
    date_suspended_cst = models.DateTimeField(blank=True, null=True)
    date_first_tran_cst = models.DateTimeField(blank=True, null=True)
    date_last_tran_cst = models.DateTimeField(blank=True, null=True)
    is_credit_hold_cst = models.BooleanField()
    old_balance_cst = models.DecimalField(max_digits=8, decimal_places=2)
    balance_notify_cst = models.DecimalField(max_digits=8, decimal_places=2)
    balance_statement_cst = models.DecimalField(max_digits=8, decimal_places=2)
    balance_conversion_cst = models.DecimalField(max_digits=8, decimal_places=2)
    balance_cst = models.DecimalField(max_digits=8, decimal_places=2)
    receive_emails_cst = models.BooleanField()
    contact_domain_cst = models.CharField(max_length=100, blank=True, null=True)
    #IP = models.CharField(max_length=250, primary_key=True)


'''

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=False,blank=False)
    total = models.FloatField(null=False,blank=False)

    @property
    def save_total(self):
        total = self.quantity * self.product.price
        self.total = total
        return total
'''


class Crawl(models.Model):
    name=models.CharField(max_length=100, default=True,null=True)

    def __str__(self):
        return self.name

        #country.author_set.all() not required for if applied related name
        #country.authors.all()

        #Author.objects.all()[0].country
        #Author.objects.select_related('country')[0].country
        #Author.objects.prefetch_related()[0].country

        #Country.objects.prefetch_related('authors') if no relation use pref_rel

class Plan(models.Model):

    """user plan subscriptions"""
    PACKAGE = (
        ("novice", "Novice"),
        ("elite", "Elite")  )# lowercase, check celery task
    package = models.CharField(verbose_name="plan", max_length=10, choices=PACKAGE,
                               default=None)  # Novice, Elite, Legendary
    level = models.PositiveIntegerField(default=1)
    link = models.URLField(verbose_name="link", unique=True, editable=False, null=True)
    commission = models.DecimalField(decimal_places=2, max_digits=10, editable=False, default=0.00)
    referals = models.ManyToManyField("Account", related_name="invites")
    is_paid = models.BooleanField(verbose_name="account validity", default=True, blank=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE, related_name='account')
    def __str__(self):
        return self.package

class Account(models.Model):

    """Registered user accounts"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    plan = models.ManyToManyField(Plan, related_name="subscription", blank=True)

    def __str__(self):
        return f"{self.user.username}'s account"

class Blog(models.Model):

    """Blog model"""

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class YoutubeVideo(models.Model):
    video = models.FileField(upload_to='youtube')

class BaseModel(models.Model):
    class Meta:
        abstract = True
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
class Colors(BaseModel):
    color_code = models.CharField(max_length=100)

class People(BaseModel):
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    Colors = models.ManyToManyField(Colors)

class PeopleAddress(BaseModel):
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name="people_address")
    address = models.TextField()