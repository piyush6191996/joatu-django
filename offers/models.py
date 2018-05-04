from django.db import models
from profiles.models import Profile, ProfileHub
from hubs.models import Hub, HubGeolocation


class Offer(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    number = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=200, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=50, blank=False)
    seller=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_offers')
    is_CAPS = models.BooleanField(default=True)
    is_BARTER = models.BooleanField(default=True)
    is_GIVE = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price_CAPS = models.PositiveIntegerField(null=True, blank=True)
    price_barter = models.CharField(max_length = 200, null=True, blank=True)


class OfferHub(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE, null= True, related_name='offers')
    distance_km = models.DecimalField(max_digits=10, decimal_places=3, blank=False, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


