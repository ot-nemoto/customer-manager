from django.db import models

class Company(models.Model):
    INDEX_NAME_CHOICES = (
        ( 0, 'その他'),
        ( 1, 'あ行'),
        ( 2, 'か行'),
        ( 3, 'さ行'),
        ( 4, 'た行'),
        ( 5, 'な行'),
        ( 6, 'は行'),
        ( 7, 'ま行'),
        ( 8, 'や行'),
        ( 9, 'ら行'),
        (10, 'わ行'),
    )
    name = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    short_name = models.CharField(max_length=255,null=True)
    index_name = models.SmallIntegerField(choices=INDEX_NAME_CHOICES)
    zip_code = models.CharField(max_length=255,null=True)
    address_1 = models.CharField(max_length=255,null=True)
    address_2 = models.CharField(max_length=255,null=True)
    address_3 = models.TextField()
    telephone_number_1 = models.CharField(max_length=255,null=True)
    telephone_number_2 = models.CharField(max_length=255,null=True)
    fax_number = models.CharField(max_length=255,null=True)
    mail_address = models.CharField(max_length=255,null=True)
    note = models.TextField()
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name

class Section(models.Model):
    company = models.ForeignKey(Company,on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    zip_code = models.CharField(max_length=255,null=True)
    address_1 = models.CharField(max_length=255,null=True)
    address_2 = models.CharField(max_length=255,null=True)
    address_3 = models.TextField()
    telephone_number_1 = models.CharField(max_length=255,null=True)
    telephone_number_2 = models.CharField(max_length=255,null=True)
    fax_number = models.CharField(max_length=255,null=True)
    mail_address = models.CharField(max_length=255,null=True)
    note = models.TextField()
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.name

class Person(models.Model):
    company = models.ForeignKey(Company,on_delete=models.PROTECT)
    section = models.ForeignKey(Section,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    zip_code = models.CharField(max_length=255,null=True)
    address_1 = models.CharField(max_length=255,null=True)
    address_2 = models.CharField(max_length=255,null=True)
    address_3 = models.TextField()
    telephone_number_1 = models.CharField(max_length=255,null=True)
    telephone_number_2 = models.CharField(max_length=255,null=True)
    fax_number = models.CharField(max_length=255,null=True)
    mail_address = models.CharField(max_length=255,null=True)
    person_role_name = models.CharField(max_length=255,null=True)
    retier_flg = models.BooleanField(default=False)
    retier_date = models.DateField(null=True)
    note = models.TextField()
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name
