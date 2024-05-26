from django.contrib import admin
from .models import User, Order, Car, Product, Comment, ProductSee, ProductLike

admin.site.register(User)
admin.site.register(Order)
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(ProductSee)
admin.site.register(ProductLike)
