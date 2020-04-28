from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    dry = models.TextField(blank=True, null=True)
    sensitive = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    oily = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingredient'


class ItemIngredient(models.Model):
    id = models.AutoField(primary_key=True)
    dry = models.TextField()
    sensitive = models.TextField()
    name = models.TextField()
    oily = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_ingredient'


class ItemProduct(models.Model):
    imageid = models.CharField(db_column='imageId', max_length=50)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    gender = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    ingredient = models.CharField(max_length=50)
    monthlysales = models.IntegerField(db_column='monthlySales')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_product'


class Product(models.Model):
    id = models.IntegerField(primary_key=True,blank=True, null=False)
    imageid = models.CharField(db_column='imageId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    ingredients = models.CharField(max_length=50, blank=True, null=True)
    monthlysales = models.IntegerField(db_column='monthlySales', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'

class SkinType(models.Model):
    choices = {
        (1,('매우적다')),
        (2,('적다')),
        (3,('보통이다')),
        (4,('많다')),
        (5,('매우 많다'))
    }
    dry = models.IntegerField(choices=choices)
    sensitive = models.IntegerField(choices=choices)
    oily = models.IntegerField(choices=choices)
