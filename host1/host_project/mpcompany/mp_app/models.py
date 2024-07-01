from django.db import models

# Create your models here.
class register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username

class booked(models.Model):
    username = models.CharField(max_length=20)
    clintname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    eventname = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date_from=models.DateField(default='2024-01-01')
    date_to=models.DateField(default='2024-01-01')
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='paid')
    bookingstatus = models.CharField(max_length=100, default='booked')
    amt = models.IntegerField()



class book_1(models.Model):
    username = models.CharField(max_length=20)
    clintname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    eventname = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date_from = models.DateField(default='2024-01-01')
    date_to = models.DateField(default='2024-01-01')
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='paid')
    bookingstatus = models.CharField(max_length=100, default='booked')
    amt = models.IntegerField()

class newevent(models.Model):
    # CATEGORY_CHOICES = [
    #     ('photography', 'photography'),
    #     ('videography', 'videography'),
    #     ('decoration', 'decoration'),
    #     ('transport', 'transport'),
    #     ('food', 'food'),
    # ]
    eventname=models.CharField(max_length=100)
    advanceamount=models.IntegerField()
    fullamount=models.IntegerField()
    discription=models.CharField(max_length=500)
    image=models.FileField()



class contact_1(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=500)


class PasswordReset(models.Model):
    user=models.ForeignKey(register,on_delete=models.CASCADE)
    token=models.CharField(max_length=10)


class payment_1(models.Model):
    book_1=models.ForeignKey(booked,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=100,default='paid')

