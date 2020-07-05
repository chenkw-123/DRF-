from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView

from untls.response import APIResponse
from user.models import User, Emp
from user.serializers import UserSerializers,EmpSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.generics import GenericAPIView

class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        request_data = request.data
        serializer = UserSerializers(data=request_data)
        print(serializer)
        password = request_data.get("password")
        re_password = request_data.get("re_password")
        # print(password,re_password)
        if password == re_password:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            # print(user)
            return APIResponse(200, True, results=UserSerializers(user).data)



    def get(self,request,*args,**kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        print(username,password)
        user = User.objects.filter(username=username,password=password).first()
        if user:
            user_data = UserSerializers(user).data
            return APIResponse(200,True,results=user_data)





class EmpView(GenericAPIView,ListModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin):

    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    lookup_field = "id"

    def get(self,request,*args,**kwargs):
        emp_id = kwargs.get("id")
        print(emp_id)
        users = self.list(request,*args,**kwargs)
        return APIResponse(200,True,results=users.data)

    def post(self,request,*args,**kwargs):
        # data = request.data
        # print(data)
        user = self.create(request,*args,**kwargs)
        return APIResponse(200,True,results=user.data)
    #
    # def put(self,request,*args,**kwargs):
    #     print('1111')
    #     return APIResponse("ok")

    def delete(self,request,*args,**kwargs):
        emp_id = kwargs.get("id")
        print(emp_id)

        self.destroy(request,*args,**kwargs)

        return APIResponse(http_status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        print(1111)
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)