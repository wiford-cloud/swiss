from http import client
from django.conf import UserSettingsHolder
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from swiss_global_deliveries.users.forms import User


class Shipment(TimeStampedModel):
    class ShippingClass(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        BUSINESS = "business", "Business"
        ECONOMY = "economy", "Economy"

    country = models.CharField("Country", max_length=255)
    shipping_method = models.CharField("Shipping Method", max_length=255)
    location = models.CharField("Location", max_length=255)
    shipping_class = models.CharField(
        "Shipping Class",
        max_length=20,
        choices=ShippingClass.choices,
        default=ShippingClass.UNSPECIFIED,
    )
    refs = models.CharField("Refs", max_length=255)
    weights = models.CharField("Weights", max_length=255)
    total_weight = models.CharField("Total Weight", max_length=255)
    balance = models.CharField("Balance", max_length=255)
    payment = models.CharField("Payment", max_length=255)

    # sender details
    sender_name = models.CharField("Sender Name", max_length=255)
    sender_address = models.TextField("Sender Address", blank=False)
    sender_mobile = models.CharField("Sender Mobile", max_length=20)
    sender_email = models.CharField("Sender Email", max_length=255)
    sender_notes = models.TextField("Sender Notes", blank=True)

    # receiver details
    reciever_name = models.CharField("Receiver Name", max_length=255)
    reciever_address = models.TextField("Receiver Address", blank=False)
    reciever_mobile = models.CharField("Receiver Mobile", max_length=20)
    reciever_email = models.CharField("Receiver Email", max_length=255)
    reciever_notes = models.TextField("Receiver Notes", blank=True)
    # parcels



# clients table 
class Client(models.Model):
    id = primary_key = True
    Name_of_item = models.CharField(max_length=100)
    Supplier = models.CharField(max_length=100)
    Description_notes = models.TextField(max_length=50)
    Expected_Date_Delivery = models.DateField()
    Status = models.CharField(max_length=100)

    class Meta():
        ordering = ("Name_of_item", "Supplier", "Description_notes", "Expected_Date_Delivery","Status")


    def _str_(self):
        return f"{self.Name_of_item},{self.Supplier},{self.Description_notes},{self.Expected_Date_Delivery},{self.Status}"


    def get_absolute_url(self):
        return reverse('pages/home', kwargs={'pk': self.pk})
