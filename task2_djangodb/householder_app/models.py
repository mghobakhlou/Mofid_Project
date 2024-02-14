from django.db import models

# Create your models here.

class Person99(models.Model):
    ID = models.IntegerField(primary_key=True)
    ParentID = models.IntegerField()  
    BirthDate = models.DateField()
    # GENDER_CHOICES = (
    #     (1, 'Male'),
    #     (2, 'Female'),
    # )
    # GenderId = models.IntegerField(choices=GENDER_CHOICES)
    GenderId = models.IntegerField()
    postalcode = models.CharField(max_length=7)
    Provincename = models.CharField(max_length=100)
    countyname = models.CharField(max_length=100)
    isurban = models.BooleanField()

    AmCrdtr_95 = models.BigIntegerField()
    Amdbtr_95 = models.BigIntegerField()
    frstPrd_95 = models.BigIntegerField()
    last_prd_95 = models.BigIntegerField()
    SmBnft_95 = models.BigIntegerField()

    AmCrdtr_96 = models.BigIntegerField()
    Amdbtr_96 = models.BigIntegerField()
    frstPrd_96 = models.BigIntegerField()
    lstPrd_96 = models.BigIntegerField()
    SmBnft_96 = models.BigIntegerField()

    AmCrdtr_97 = models.BigIntegerField()
    Amdbtr_97 = models.BigIntegerField()
    frstPrd_97 = models.BigIntegerField()
    lstPrd_97 = models.BigIntegerField()
    SmBnft_97 = models.BigIntegerField()

    AmCrdtr_98 = models.BigIntegerField()
    Amdbtr_98 = models.BigIntegerField()
    frstPrd_98 = models.BigIntegerField()
    lstPrd_98 = models.BigIntegerField()
    SmBnft_98 = models.BigIntegerField()

    Card98_Rials = models.BigIntegerField()
    Card98_PaymentCount = models.IntegerField()

    Card99_Rials = models.BigIntegerField()
    Card99PaymentCount = models.IntegerField()

    IsBiamrKhas = models.IntegerField()
    IsMalool = models.IntegerField()
    IsBimePardaz_Sandoghha = models.IntegerField()
    IsBazneshaste_Sandoghha = models.IntegerField()
    
    IsMaliati_Shaghel = models.IntegerField() # آیا فرد شاغل مشمول مالیات است؟
    daramad_Total_Rials = models.BigIntegerField()
    
    Cars_Count = models.IntegerField()
    CarsPrice_Sum = models.BigIntegerField()

    Trips_Count_AirNotPilgrimage = models.IntegerField()
    Trips_Count_NotAirNotPilgrimage = models.IntegerField()
    Trips_Count_AirPilgrimage = models.IntegerField()
    Trips_Count_NotAirPilgrimage = models.IntegerField()
    
    HasMojavezSenfi = models.IntegerField()
    Senf = models.CharField(max_length=200, null=True, blank=True)  # Assuming it can be null
    HasBimeSalamat = models.IntegerField()
    BimeSalmat_Type = models.CharField(max_length=100, null=True, blank=True)  # Assuming it can be null
