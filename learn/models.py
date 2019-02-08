from django.db import models


# Create your models here.

def default_path(instance,filename):
    field=instance.field
    type=instance.type
    title=instance.title
    return '%s/%s/%s/%s' % (type, field, title, filename)

class Worker(models.Model):
    userNo=models.IntegerField()
    pwd=models.CharField(max_length=16)
    userName=models.CharField(max_length=30)
    userEmail=models.EmailField()
    userAge=models.IntegerField()
    userBirthday=models.DateField()
    userProfession=models.TextField()

    def __str__(self):
        return self.userName


class Manager(models.Model):
    userNo=models.IntegerField()
    pwd=models.CharField(max_length=16)
    userName=models.CharField(max_length=30)
    userEmail=models.EmailField()
    userAge=models.IntegerField()
    userBirthday=models.DateField()
    userTitle=models.TextField()

    def __str__(self):
        return self.userName


class KnowledgeManager(models.Model):
    userNo = models.IntegerField()
    pwd = models.CharField(max_length=16)
    userName = models.CharField(max_length=30)
    userEmail = models.EmailField()
    userAge = models.IntegerField()
    userBirthday = models.DateField()
    userTitle = models.TextField()

    def __str__(self):
        return self.userName


class File(models.Model):
    title=models.CharField(max_length=30)
    type=models.CharField(max_length=10)
    field=models.CharField(max_length=10)
    fileNo=models.CharField(max_length=20,default=00)
    devotionTime=models.DateField()
    devoter=models.CharField(max_length=20)
    remarks=models.TextField()
    link=models.FileField(upload_to=default_path)

    def __str__(self):
        return self.title


class Data(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    field = models.CharField(max_length=10)
    dataNo = models.CharField(max_length=20, default=00)
    devotionTime = models.DateField()
    devoter = models.CharField(max_length=20)
    remarks = models.TextField()
    link = models.FileField(upload_to=default_path)

    def __str__(self):
        return self.title


class Chart(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    field = models.CharField(max_length=10)
    chartNo = models.CharField(max_length=20, default=00)
    devotionTime = models.DateField()
    devoter = models.CharField(max_length=20)
    remarks = models.TextField()
    link = models.ImageField(upload_to=default_path)

    def __str__(self):
        return self.title



