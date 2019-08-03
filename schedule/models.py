from django.contrib.postgres.fields import JSONField
from django.db import models
import datetime

def current_date():
    return datetime.date.today()

def get_default_json():
    return {
        'slot': '',
        'name': '',
        'modality': '', # No Contact, Phone, Email, Both
        'phone': '',
        'email': '',
        'status': '', # Unsent, Sent, Accepted, Declined
    }


# Create your models here.
class Schedule(models.Model):
    date    = models.DateField(primary_key=True, blank=False, verbose_name='Date', default=current_date)

    slot_1  = JSONField(default=get_default_json, verbose_name='Slot 1')
    slot_2  = JSONField(default=get_default_json, verbose_name='Slot 2')
    slot_3  = JSONField(default=get_default_json, verbose_name='Slot 3')
    slot_4  = JSONField(default=get_default_json, verbose_name='Slot 4')
    slot_5  = JSONField(default=get_default_json, verbose_name='Slot 5')
    slot_6  = JSONField(default=get_default_json, verbose_name='Slot 6')
    slot_7  = JSONField(default=get_default_json, verbose_name='Slot 7')
    slot_8  = JSONField(default=get_default_json, verbose_name='Slot 8')
    slot_9  = JSONField(default=get_default_json, verbose_name='Slot 9')
    slot_10 = JSONField(default=get_default_json, verbose_name='Slot 10')
    slot_11 = JSONField(default=get_default_json, verbose_name='Slot 11')
    slot_12 = JSONField(default=get_default_json, verbose_name='Slot 12')
    slot_13 = JSONField(default=get_default_json, verbose_name='Slot 13')
    slot_14 = JSONField(default=get_default_json, verbose_name='Slot 14')
    slot_15 = JSONField(default=get_default_json, verbose_name='Slot 15')
    slot_16 = JSONField(default=get_default_json, verbose_name='Slot 16')
    slot_17 = JSONField(default=get_default_json, verbose_name='Slot 17')
    slot_18 = JSONField(default=get_default_json, verbose_name='Slot 18')
    slot_19 = JSONField(default=get_default_json, verbose_name='Slot 19')
    slot_20 = JSONField(default=get_default_json, verbose_name='Slot 20')
    slot_21 = JSONField(default=get_default_json, verbose_name='Slot 21')
    slot_22 = JSONField(default=get_default_json, verbose_name='Slot 22')
    slot_23 = JSONField(default=get_default_json, verbose_name='Slot 23')
    slot_24 = JSONField(default=get_default_json, verbose_name='Slot 24')
    slot_25 = JSONField(default=get_default_json, verbose_name='Slot 25')
    slot_26 = JSONField(default=get_default_json, verbose_name='Slot 26')
    slot_27 = JSONField(default=get_default_json, verbose_name='Slot 27')
    slot_28 = JSONField(default=get_default_json, verbose_name='Slot 28')
    slot_29 = JSONField(default=get_default_json, verbose_name='Slot 29')
    slot_30 = JSONField(default=get_default_json, verbose_name='Slot 30')
    slot_31 = JSONField(default=get_default_json, verbose_name='Slot 31')
    slot_32 = JSONField(default=get_default_json, verbose_name='Slot 32')
    slot_33 = JSONField(default=get_default_json, verbose_name='Slot 33')
    slot_34 = JSONField(default=get_default_json, verbose_name='Slot 34')
    slot_35 = JSONField(default=get_default_json, verbose_name='Slot 35')
    slot_36 = JSONField(default=get_default_json, verbose_name='Slot 36')
    slot_37 = JSONField(default=get_default_json, verbose_name='Slot 37')
    slot_38 = JSONField(default=get_default_json, verbose_name='Slot 38')
    slot_39 = JSONField(default=get_default_json, verbose_name='Slot 39')
    slot_40 = JSONField(default=get_default_json, verbose_name='Slot 40')
    slot_41 = JSONField(default=get_default_json, verbose_name='Slot 41')
    slot_42 = JSONField(default=get_default_json, verbose_name='Slot 42')
    slot_43 = JSONField(default=get_default_json, verbose_name='Slot 43')
    slot_44 = JSONField(default=get_default_json, verbose_name='Slot 44')
    slot_45 = JSONField(default=get_default_json, verbose_name='Slot 45')
    slot_46 = JSONField(default=get_default_json, verbose_name='Slot 46')
    slot_47 = JSONField(default=get_default_json, verbose_name='Slot 47')
    slot_48 = JSONField(default=get_default_json, verbose_name='Slot 48')
