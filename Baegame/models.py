from django.db import models

# Create your models here.

class Test(models.Model):
    ans01 = models.CharField(max_length=50, blank=True,null=True, default='')
    ans02 = models.CharField(max_length=50, blank=True,null=True, default='')
    ans03 = models.CharField(max_length=50, blank=True,null=True, default='')


    def __str__(self):
     return '%s %s ' % (self.ans01, self.ans02)


    class Meta:
        db_table = "BAE TEST"
        verbose_name = 'Test'