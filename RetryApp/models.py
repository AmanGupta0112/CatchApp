from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    email = models.EmailField()
    query = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'Contact_Info'

class FeedBackModel(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField(blank=False)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'Feedback'

class NewApplicationModel(models.Model):
    title = models.CharField(max_length=255)
    icon_img = models.CharField(max_length=255)
    detail = models.TextField()
    rating = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    downloads= models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'New_App_Data'


class NewWebSiteModel(models.Model):
    title = models.CharField(max_length=255)
    icon_img = models.CharField(max_length=255)
    detail = models.TextField()
    rank_c = models.CharField(max_length=80)
    rank_g = models.CharField(max_length=80)
    rating= models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'New_Web_Data'

class NewSoftwareModel(models.Model):
    title = models.CharField(max_length=255)
    icon_img = models.CharField(max_length=255)
    detail = models.TextField()
    rating = models.CharField(max_length=80)
    price = models.CharField(max_length=80)
    size= models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta():
        db_table = 'New_Soft_Data'

class SearchModel(models.Model):
    option = models.CharField(max_length=255)
    search_item = models.CharField(max_length=255)

    def __str__(self):
        return self.option

    class Meta():
        db_table = 'Search_Item'
