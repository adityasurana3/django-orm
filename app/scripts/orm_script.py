from django.contrib.auth.models import User
from app.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Upper, Length, Concat
from django.db.models import Value, CharField, Avg, Sum, Count
from posts.models import Student, Score, Subject
from faker import Faker
import random

faker = Faker()

def run():
    # Restaurant 1 [rating: 4.3]
    # concat = Concat('name', Value(' [rating: '), Avg('ratings__rating'), Value(']'), output_field=CharField())
    # rating = Restaurant.objects.annotate(rat=Count('ratings__rating'))
    # for r in rating:
    #     print(r.name, r.rat)
    # rating = Restaurant.objects.annotate(num_rating=Count('ratings'), avg_rating=Avg('ratings__rating'))
    
    
    pass
    