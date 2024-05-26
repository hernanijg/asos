from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# User Config
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.username
    
# Product
class Product(models.Model):
    name = models.CharField(max_length=300)
    image_url = models.ImageField()

    creator = models.ManyToManyField(User, related_name='creators')
    comment = models.ManyToManyField(User, through='Comment', related_name='commented_products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Details
    product_detail = models.TextField()
    brand = models.TextField()
    size = models.TextField()
    about = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
# Connected database
class Comment(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.product}"
    
# See and Like (DeepLearnig)
class ProductSee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.product}"
    
class ProductLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.product}"
    
# Products orders
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    user = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name