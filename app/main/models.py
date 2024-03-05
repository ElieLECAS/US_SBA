from django.db import models

# Create your models here.
class PredictApi(models.Model):
    State = models.CharField(max_length=2, null=False, blank=False)
    Zip = models.IntegerField()
    BankState = models.CharField(max_length=2, null=False, blank=False)
    ApprovalFY = models.IntegerField()
    Term = models.IntegerField()
    GrAppv = models.IntegerField()
    SBA_Appv = models.IntegerField()


