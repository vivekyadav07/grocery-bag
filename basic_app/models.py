from django.db import models
from django.urls import reverse
STAT=[('Bought','Bought'),('Not Available','Not Available'),('Pending','Pending')]
# Create your models here.
class Bag(models.Model):
    item_name=models.CharField(max_length=20)
    item_quantity=models.PositiveIntegerField()
    item_status=models.CharField(max_length=60,choices=STAT)
    purchase_date=models.DateTimeField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("list")

    def __str__(self):
        return self.item_name+" "+str(self.item_quantity)
