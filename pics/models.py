from django.db import models

# Create your models here.
class Location(models.Model):

    '''
    locations model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
       return self.location
       
    def save_locations(self):
        self.save()

    # def delete_locations(self):
    #     self.delete()

class Category(models.Model):

    '''
    Pics category model
    '''
    
    name = models.CharField(max_length=120)

    def __str__(self):
       return self.name
    
    def save_category(self):
        self.save()

    # def delete_category(self):
    #     self.delete()

class Image(models.Model):

    '''
    Images model
    '''
    
    image = models.ImageField(upload_to='mediia/')
    
    image_name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)
    category = models.ManyToManyField(Category)
    pub_date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)

    def __str__(self):
       return self.image_name
    # ordering data everytime we query the database might be very tedoius. It thus makes available a Meta subclass in any models to specify model-specific options.
    # I used the - minus sign before the order by parameter. This returns the objects in reverse order.
    class Meta:
        ordering = ['-pub_date_posted']

    # def save_image(self):
    #     self.save()

    # def delete_image(self):
    #     self.delete()
    
    # @classmethod
    # def get_all(cls):
    #     images = cls.objects.all()
    #     return images

    # @classmethod
    # def filter_category(cls,query):
    #     images = cls.objects.filter(category__name=query)
    #     return images

    # @classmethod
    # def search_by_category(cls, search_term):
    #     images = cls.objects.filter(category__name__icontains = search_term).order_by('-pub_date_posted')
    #     return images