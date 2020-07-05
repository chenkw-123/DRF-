from django.db import models

# Create your models here.

class User(models.Model):

    gender_choice = (
        ("0","male"),
        ("1","female")
    )

    username = models.CharField(max_length=20)
    real_name = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices=gender_choice,default=0)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"
        verbose_name="用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Emp(models.Model):

    emp_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic",default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    age = models.IntegerField()

    @property
    def check_age(self):
        if self.age>30:
            return "中年"
        else :
            return "少年"

    class Meta:
        db_table = "EMP"
        verbose_name = "员工表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name