from django.shortcuts import render, HttpResponse
from .models import *
from .tasks import add 
from .serializers import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
#result = add.delay(2, 3) 

import io
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.parsers import JSONParser

# @method_decorator()
class StudentApi1(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        pythondata = JSONParser().parse(stream)
        print(pythondata)
        id = pythondata.get('id', None)
        print(id)
        if id is not None:
            stu = Customer.objects.get(id=id)
            serializer = EmployeeSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Customer.objects.all()
        ser = EmployeeSerializers(stu, many =True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json')


# Create your views here.

def home(request):
    user = People.objects.all()
    print(dir(user))
    print(user.values())
    print(user.query)
    print(user.count())
    fil = People.objects.filter(email__icontains='77').only('age').values()
    print('========',fil)
    fil = People.objects.filter(email__icontains='@')[0].age
    print('========',fil)

    fil = People.objects.filter(email__startswith='r')[0].email
    print('========',fil)

    fil = People.objects.filter(age__gt=26).only('age').values()
    print('========',fil)
    fil = PeopleAddress.objects.filter(people__email__icontains='@').count()
    print('======forei==',fil)
    fil = PeopleAddress.objects.first()
    print('======forei==',fil.people.age)
    obj = People.objects.first() # reverse relationship
    print(obj.people_address.all()[0].address)
    print(obj.people_address.first().address)

    obj =People.objects.get(email__icontains = 'r') # throws error if not matched record is there or multiple record for single query
    #obj =People.objects.get(email__icontains = '2')
    print('-obj',obj)
    obj, status =People.objects.get_or_create(email__icontains = '.net') # if present matched record , then no new record create and st=False else create new and return True 
    print(obj, status)
    user1 = People.objects.get(age = 26)
    print(user1.Colors)
    #print(user1.count())
    result = add.delay(2, 3) 
    print('====',result)
    return HttpResponse(user)

# #ModelVieSet api class base
# class StudentDetails(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = EmployeeSerializers
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#ViewSet api views class based
class StudentViewset(viewsets.ViewSet):
    def list(self,request):

        queryset = Customer.objects.all()
        serializer_data = EmployeeSerializers(queryset, many=True)
        return Response(serializer_data.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        print(id)
        if id is not None:
            st = Customer.objects.get(id=id)
            serializer_data = EmployeeSerializers(st)
            return Response(serializer_data.data)
    
    def create(self, request):
        serial_Data = EmployeeSerializers(data=request.data)
        if serial_Data.is_valid():
            serial_Data.save()
            return Response({'msg':'Data_created'},status=status.HTTP_201_CREATED)
        return Response(serial_Data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request,pk):
        print(pk)
        id = pk
        stu = Customer.objects.get(id=id)
        ser = EmployeeSerializers(stu, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Updated'})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        stu = Customer.objects.get(pk=pk)
        ser = EmployeeSerializers(stu, data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Partially Updated'})
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,pk,request):
        id = pk
        stu = Customer.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Deleted'})

#functioned base api
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def student_api(request, id=None):
    print('id',id)
    if request.method == 'GET':
        print(request.body)
        print(request.data)
        
        # id = request.data.get('id') use this if we use myapp.py/requests module else get id as param from ui
        #id = pk
        print('dd',id)
        if id is not None:
            cus = Customer.objects.get(id=id)
            print(cus)
            ser = EmployeeSerializers(cus)
            return Response(ser.data)
        stu = Customer.objects.all()
        ser = EmployeeSerializers(stu, many = True)
        return Response(ser.data)
    
    if request.method == 'POST':
        ser = EmployeeSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Data Created'})
        return Response(ser.errors)
    
    if request.method == 'PATCH':
        print(request.body)
        print(request.data)
        
        print('pp',id)
        #id = request.data.get('id')
        st = Customer.objects.get(id=id)
        ser = EmployeeSerializers(st, data=request.data, partial =True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':' partially updated'})
        return Response(ser.errors)
    
    if request.method == 'PUT':
        #id = pk 
        id = request.data.get('id')
        st = Customer.objects.get(id=id)
        ser = EmployeeSerializers(st, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'updated'})
        return Response(ser.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        obj = Customer.objects.get(pk=id)
        if obj:
            obj.delete()
            return Response({'msg': 'Deleted'})
        else:
            return Response({'msg': 'None'})



#class based views

from rest_framework.views import APIView

class StudentApi(APIView):
    def get(self,request,pk=None):

        #id = request.data.get('id')
        id = pk
        if id is not None:
            print('pp')
            cus = Customer.objects.get(id=pk)
            ser = EmployeeSerializers(cus)
            return Response(ser.data)
        stu = Customer.objects.all()
        ser = EmployeeSerializers(stu, many = True)
        return Response(ser.data)
    
    def post(self,request):
        ser = EmployeeSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'Data Created'})
        return Response(ser.errors)
    
    def patch(self,request,pk):
        #id = request.data.get('id')
        id = pk
        st = Customer.objects.get(id=id)
        ser = EmployeeSerializers(st, data=request.data, partial =True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':' partially updated'})
        return Response(ser.errors)
    
    def put(self,request,pk=None):
        id = pk 
        #id = request.data.get('id')
        st = Customer.objects.get(id=id)
        ser = EmployeeSerializers(st, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'updated'})
        return Response(ser.errors)
    
    def delete(self,request,pk=None):
        id = request.data.get('id')
        id = pk
        obj = Customer.objects.get(pk=id)
        if obj:
            obj.delete()
            return Response({'msg': 'Deleted'})
        else:
            return Response({'msg': 'None'})

def select_re(request):
    # example 1
    d = Blog.objects.all()
    p = Plan.objects.all()
    for ref in p:
        for referal in ref.referals.all():
            print(referal, 'ref')
    print(d)
    for i in d:
        print(i.account, 'p')
    blogs = Blog.objects.select_related("account")
    print(blogs)
    for blog in blogs:
        print(blog,'l')
        print(blog.account)

    # example 2
    blog = Blog.objects.select_related("account__user").get(id=1)
    print(blog.account)
    # print(blog.user)

    # example 3
    # account = Account.objects.select_related("user").get(id=1)
    # print(account.user) # no database hit

    # example 1 
    accounts = Account.objects.prefetch_related("plan")
    for account in accounts:
        print(account.user)
        for plan in account.plan.all():
            print(plan.package)

    # example 2
    accounts = Account.objects.prefetch_related("blog_set")
    for account in accounts:
        print(account.user)
        for blog in account.blog_set.all():
            print(blog.title)
    return render(request, 'home.html', {'queryset':d})

from django.shortcuts import get_object_or_404

class PlanView(APIView):
    def get(self, request, pk = None):
        if pk is not None:
            data = Plan.objects.get(pk = pk)
            print(data)
            plan_ser = PlanSerializer(data, many=False)
            return Response({'data':plan_ser.data})
        else:
            data = Plan.objects.all()
            p = data
            # r = Plan.objects.all().order_by('-id')[0]#.values()#values_list('package','level','link')
            # r = dict(Plan.objects.only(['id','link']).get())
            r = Plan.objects.only('id','link')
            values = r.values('id', 'link')
            for value in values:
                print(value, 'ppp')
            print(r, 'r')
            r2 = Plan.objects.filter(id=1).only('id','link')#.get()
            print(r2, 'r2')
            r3 = Plan.objects.filter(link=None).only('id','link').filter()
            print(r3, 'r3')
            r4 = Plan.objects.filter(link=None).only('id','link').values('id', 'link')
            print(r4, 'r4')
            r1 = Plan.objects.defer('id')#.values()
            print(r1)
            # l = Plan.objects.all().values_list('id', flat=True)
            # print('l',l)
            # for i in r:
            #     print(i.level)
            # print(dir(request) )
            for i in r1:
                print(i.account)
                print(i.referals.all())#.values_list(flat=True))
                    # print(j)
            ser_data = PlanSerializer(data, many = True)
            return Response({'data':ser_data.data})
        

    def post(self,request):
            ser = PlanSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({'msg':'Data Created'})
            return Response(ser.errors)

import json
class UpdatePlan(APIView):
    def get_object(self, pk):
        return get_object_or_404(Plan, id=pk)
    def put(self, request, pk):
        plan_obj = self.get_object(pk = pk)
        print(plan_obj)
        data = request.data
        print(data.get('account'))
        print(data.get('referals'))
        ref =data.get('referals')
        print(ref)
        plan_serializer = PlanSerializer(plan_obj, data = data)
        if plan_serializer.is_valid():
            p = plan_serializer.save( )
            # p.account.clear()
            acc = Account.objects.get(id= pk)
            p.account = acc 
            a = [1]
            ref = Account.objects.filter(id__in=a)
            print(ref, 'ref')
            p.referals.add(*ref)
            p.save()
            
            return Response({'data':'updated'})
            # account_object = plan_serializer.save()
            # account_object.referals.add(*ref)
        else:
            return Response({'errors':plan_serializer.errors})
