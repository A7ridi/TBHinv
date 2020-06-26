from django.db import models
from datetime import datetime, date

class Item_choices(models.Model):
    item_choices = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.item_choices

class Storage(models.Model):
    item = models.CharField(max_length=200)
    amount = models.IntegerField()
    expected_need_in = models.IntegerField()
    choices_field = models.ForeignKey(Item_choices, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=200)
    issue_date = models.DateField('Purchase date(dd/mm/yy)', auto_now_add=False, auto_now=False)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)
    # export_to_CSV = models.BooleanField(default=False)

def __str__(self):
    return self.item

class StorageHistory(models.Model):
     item = models.CharField(max_length=30, blank=True, null=True)
     amount = models.IntegerField()
     expected_need_in = models.IntegerField()
     choices_field = models.ForeignKey(Item_choices, on_delete=models.DO_NOTHING, blank=True, null=True)
     location = models.CharField(max_length=30, blank=True, null=True)
     issue_date = models.DateField('Purchase date(mm/dd/yy)', auto_now_add=False, auto_now=False, blank=True, null=True)
     timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)

# Username/Mysql User/Postgres user server putty - InventoryTbh
# Password/Putty pass/Postgres pass server putty/Ddjangoadmin pass - TBHInventory@2018
# Email    - thebiryanihotspot@gmail.com
# DO Pass  - WnN!H6LgWCCg5D
# MySQL Pass - WnN!H6LgWCCg5D
# MySQL db - Inventorydb
# User Putty/DO - djangoadmin
# Postgres DBname - inv_prod
# ssh key/putty - ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA5mRDssdyOQQ+af3SNxw1kVdH5iOopsveuSMo3vdbg6qVCxjFkJItdzuUsPl3Jy5ngGyEbluFhsOmyE+aPrmd9U2lFI+F1VHCczPi+tkM7McKK9GVPn0eM8AE6tXvID+eVvMc5++3Ar8IkV4Dp2+FOYgSkQGkePgzQ5V/a6NA7NngxhPUX/zRRzaz/lquh71Ho6G3K/MNKREcgaRuOnQ9a3eVp0Qn1KRO0VREVwiWgsctFLF9LP6fITapw2vvPj1wppVuwbu+JISYH+k5tynI6DC1ea9g6/njMKnWWFt0MA+bj2hV+Un/E0IPk1Wvoj6qzbnJFAhe4/BsOAWy1ZGcgw== rsa-key-20200626
