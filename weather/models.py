from django.db import models

# Create your models here.
class Weather:
    id: int
    city: str
    weather: str
    temp : str
    preci : str
    hum : str
    wind : str
    temp2 : str
    img_svg : str