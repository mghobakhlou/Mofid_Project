from django.db import models

# Create your models here.

class Person99(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()  
    birth_date = models.DateField()
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender_id = models.IntegerField(choices=GENDER_CHOICES)
    postal_code = models.CharField(max_length=7)
    province_name = models.CharField(max_length=100)
    county_name = models.CharField(max_length=100)
    is_urban = models.BooleanField()

    am_creditor_95 = models.BigIntegerField()
    am_debtor_95 = models.BigIntegerField()
    first_prd_95 = models.BigIntegerField()
    last_prd_95 = models.BigIntegerField()
    sm_benefit_95 = models.BigIntegerField()

    am_creditor_96 = models.BigIntegerField()
    am_debtor_96 = models.BigIntegerField()
    first_prd_96 = models.BigIntegerField()
    last_prd_96 = models.BigIntegerField()
    sm_benefit_96 = models.BigIntegerField()

    am_creditor_97 = models.BigIntegerField()
    am_debtor_97 = models.BigIntegerField()
    first_prd_97 = models.BigIntegerField()
    last_prd_97 = models.BigIntegerField()
    sm_benefit_97 = models.BigIntegerField()

    am_creditor_98 = models.BigIntegerField()
    am_debtor_98 = models.BigIntegerField()
    first_prd_98 = models.BigIntegerField()
    last_prd_98 = models.BigIntegerField()
    sm_benefit_98 = models.BigIntegerField()

    card98_rials = models.BigIntegerField()
    card98_paymentcount = models.IntegerField()

    card99_rials = models.BigIntegerField()
    card99_paymentcount = models.IntegerField()

    is_bimar_khas = models.BooleanField()
    is_malool = models.BooleanField()
    is_bime_pardaz_sandoghha = models.BooleanField()
    is_bazneshaste_sandoghha = models.BooleanField()
    
    is_maliati_shaghel = models.BooleanField() # آیا فرد شاغل مشمول مالیات است؟
    daramad_total_rials = models.BigIntegerField()
    
    cars_count = models.IntegerField()
    cars_price_sum = models.BigIntegerField()

    trips_count_air_not_pilgrimage = models.IntegerField()
    trips_count_not_air_not_pilgrimage = models.IntegerField()
    trips_count_air_pilgrimage = models.IntegerField()
    trips_count_not_air_pilgrimage = models.IntegerField()
    
    has_mojavez_senfi = models.BooleanField()
    senf = models.CharField(max_length=200, null=True, blank=True)  # Assuming it can be null
    has_bime_salamat = models.BooleanField()
    bime_salamat_type = models.CharField(max_length=100, null=True, blank=True)  # Assuming it can be null
