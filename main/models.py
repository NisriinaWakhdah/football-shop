import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    # membuat tipe-tipe kategori dari barang-barang yang dijual
    category_choices = [('perlengkapanUtama', 'Perlengkapan Utama'),
                        ('bolanAksesrori', 'Bola dan Aksesoris'),
                        ('peralatanLatihan', 'Peralatan Latihan'),
                        ('perlatanWasit', 'Peralatan Wasit'),
                        ('sportCare', 'Sport Care'),
                        ('update', 'Update'),
                        ('exclusive', 'Exclusive'),
                        ('hotDeals', 'Hot Deals')]
    
    # Atribut-atribut pada model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices= category_choices, default='update')
    is_featured = models.BooleanField(default=False)
    launch_at = models.DateTimeField(default=timezone.now)
    stock = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    brand = models.CharField()
    product_viewer = models.PositiveIntegerField(default=0)
    size = models.CharField()

    # method untuk mengembalikan nama produk yang dijual
    def __str__(self):
        return self.name
    
    @property
    # method untuk menunjukkan apakah barang yang dijual recommended
    def is_recommended (self):
        return self.rating >= 3.5
    
    @property
    # method untuk mengecek apakah barangnya tersedia
    def is_availaible(self):
        return self.stock > 0
    
    @property
    # method untuk barang yang memiliki stock terbatas
    def is_limited (self):
        return 0 < self.stock <= 10
       
    
    # method untuk menaikkan jumlah viewer
    def increment_views(self):
        self.product_viewer += 1
        self.save()
    

 


