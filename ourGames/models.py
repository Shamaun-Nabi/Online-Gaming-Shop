from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def category():
        return Category.objects.all()
        

class Game(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description=models.TextField(default="Write description..")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    year = models.IntegerField()
    publisher = models.CharField(max_length=30)
    platform = models.CharField(max_length=10)
    image=models.ImageField(upload_to='Product_img/images',default="default.png")
    # categories = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL)
    @staticmethod
    def getAllProducts():
        return Game.objects.all()
    
    # @staticmethod
    # def get_products_by_id(ids):
    #     # ids=int(ids)
    #     return Game.objects.filter(id__in =ids)
    
    @staticmethod
    def get_products_by_id(ids):
        print(ids)
        return Game.objects.filter(id__in=ids)

    
    @staticmethod
    def get_product_by_id(category_id):
        if category_id:
            return Game.objects.filter(category=category_id)
        else:
            Game.getAllProducts()
    
    
    def __str__(self):
        return self.name