from django.db.migrations import serializer
from rest_framework import exceptions, serializers

from rest_framework.serializers import ModelSerializer


from user.models import User, Emp


class UserSerializers(ModelSerializer):
    class Meta:

        model = User

        fields = ("username","real_name","password","gender",)

        extra_kwargs = {
            "username":{
                "required":True,
                "min_length" : 2,
                "error_messages":{
                    "required":"用户名不能为空",
                    "min_length":"用户名过短，请输入三位以上!"
                }
            },
        }
        re_password = serializers.CharField()

#钩子函数，判断用户名是否重复
    def validate(self, attrs):
        username = attrs.get("username")
        # print(username)
        user = User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError("用户名已存在！")
        return attrs


class EmpSerializer(ModelSerializer):
    class Meta:
        model = Emp

        # fields = "__all__"
        fields = ("id","emp_name","salary","img","age","check_age")

        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名不能为空",
                    "min_length": "用户名过短，请输入三位以上!"
                }
            }
        }