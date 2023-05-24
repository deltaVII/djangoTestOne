from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    companyName = models.CharField('Имя компании', max_length=50)
    companyNumber = models.IntegerField('Номер компании', unique=True)
    companyPost = models.TextField('Описание компании')

    def __str__(self):
        back=[]
        return str(self.companyName)

       
