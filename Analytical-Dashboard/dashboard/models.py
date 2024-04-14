""" 
Definition of models.
"""
from operator import truediv
from tkinter import CASCADE
from typing_extensions import Self
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.
class AdminUser(models.Model):
    admin_id = models.BigAutoField(primary_key = True)
    admin_firstname = models.CharField(max_length=200)
    admin_lastname = models.CharField(max_length=200)
    admin_email = models.CharField(max_length=200)
    admin_pass = models.CharField(max_length=20)
    admin_accountNum = models.IntegerField()
    admin_LastAccess_DT = models.DateTimeField()
    def __str__(self):
        return self.adminFirstName

class User(models.Model):
    user_id = models.BigAutoField(primary_key = True)
    user_firstName = models.CharField(max_length=200)
    user_lastName = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_pass = models.CharField(max_length=20)
    user_accountNum = models.IntegerField()    
    registration_DT = models.DateTimeField()
    user_LastAccess_DT = models.DateTimeField()
    def __str__(self):
        return self.userFirstName
    @property
    def get_user_value(self):
        return '{}{}{}{}'.format(self.user_firstName, self.user_lastName, self.user_email, self.registration_DT)

class UserGroup(models.Model):
    user_group_id = models.BigAutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group_Name = models.CharField(max_length=200)
    user_group_Creation_DT = models.DateTimeField()
    def __str__(self):
        return self.user_group_Name
    @property
    def get_reports_value(self):
        return '{}{}'.format(self.user_group_Name, self.user_group_Creation_DT)

    
class Reports(models.Model):
    report_id = models.BigAutoField(primary_key = True)
    admin_id = models.ForeignKey(AdminUser, on_delete=models.CASCADE) #foreign key relationship for an admin user running a report for the user group -> (HR)
    user_group_id = models.ForeignKey(UserGroup, on_delete=models.CASCADE) #foreign key relationship for a userGroup receiving a report from the admin -> (UserGroup)
    inventory_item = models.CharField(max_length=300)    
    inventory_item_qty = models.IntegerField() #quantity of the item in stock
    isAvailable = models.BooleanField(default=True) #Whether the report is available to display to the employees()
    report_DT = models.DateTimeField()
    def __str__(self):
        return self.inventory_item
    @property
    def get_reports_value(self):
        return '{}{}{}{}'.format(self.inventory_item, self.inventory_item_qty, self.isAvailable, self.report_DT)

class Products(models.Model):
    product_id = models.BigAutoField(primary_key = True)
    product_name = models.CharField(max_length=200)
    produced_by = models.CharField(max_length=200)
    product_qty = models.IntegerField()    
    isAvailable = models.BooleanField(default=True) 
    isRefundable = models.BooleanField(default=False)
    warranty_exp_DT = models.DateTimeField()
    row_insert_DT = models.DateTimeField()
    def __str__(self):
        return self.product_name 
    @property
    def get_products_value(self):
        return '{}{}{}{}{}{}'.format(self.product_name, self.produced_by, self.product_qty, self.isAvailable, self.isRefundable, self.warranty_exp_DT)


class Audit(models.Model):
    audit_id = models.BigAutoField(primary_key = True)
    admin_id = models.ForeignKey(AdminUser, on_delete=models.CASCADE) #foreign key relationship for an admin user running a report for the employees -> (UserGroup)
    user_id = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    tbl_name = models.CharField(max_length=300)  # name of the model that performed the action in our (e.g UserGroup)
    tbl_col = models.CharField(max_length=300) # name of the model's column that the action was performed on (e.g PassWord change would show UserGroup -> userPass)
    tbl_row = models.IntegerField() #indicatr of the model's row that the action was performed on (e.g PassWord change would show UserGroup -> userPass-> row == 6)
    isAdmin = models.BooleanField(default=True) #Determines whether the action was performed by an administrator(true) or an employee(false)
    def __str__(self):
        return self.tbl_name
    @property
    def get_audit_value(self):
        return '{}{}{}{}'.format(self.tbl_name, self.tbl_col, self.tbl_row, self.isAdmin)

#As user requirements increase, we can always make adjustments to our models to add new features. 