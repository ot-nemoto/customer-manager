from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    short_name = models.CharField(max_length=255,null=True)
    index_name = models.CharField(max_length=255,null=True)
    zip_code = models.CharField(max_length=255,null=True)
    address_1 = models.CharField(max_length=255,null=True)
    address_2 = models.CharField(max_length=255,null=True)
    address_3 = models.CharField(max_length=255,null=True)
    telephone_number_1 = models.CharField(max_length=255,null=True)
    telephone_number_2 = models.CharField(max_length=255,null=True)
    fax_number = models.CharField(max_length=255,null=True)
    mail_address = models.CharField(max_length=255,null=True)
    note = models.CharField(max_length=255,null=True)
    sort_number = models.CharField(max_length=255,null=True)
    delete_flg = models.CharField(max_length=255,null=True)
    create_user = models.CharField(max_length=255,null=True)
    create_date = models.CharField(max_length=255,null=True)
    update_user = models.CharField(max_length=255,null=True)
    update_date = models.CharField(max_length=255,null=True)
    version = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name
