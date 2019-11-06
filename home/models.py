from django.db import models
from django.utils import timezone


class AllGames(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)


class TipGG(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip_gg = models.CharField(max_length=10)
    tip_gg_odds= models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)


class Over15(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip_ov = models.CharField(max_length=10)
    tip_ov_odds= models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)


class Over25(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip_ov = models.CharField(max_length=10)
    tip_ov_odds= models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)


class Over35(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip_ov = models.CharField(max_length=10)
    tip_ov_odds= models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)


class Featured(models.Model):
    date = models.CharField(max_length=40)
    start_time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    score = models.CharField(max_length=40)
    won_or_lost = models.CharField(max_length=40)
