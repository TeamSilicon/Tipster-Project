from django.db import models
from django.utils import timezone


class AllGames(models.Model):
    match_date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip = models.CharField(max_length=40)
    tip_odd = models.CharField(max_length=5, default="0.00")
    tipGG = models.BooleanField(default=False)
    tipGG_odd = models.CharField(max_length=5, default="0.00")
    tipOv = models.CharField(max_length=5, default="2.5")
    tipOV_odd = models.CharField(max_length=5, default="0.00")
    ft_results = models.CharField(max_length=40)
    outcome_text = models.CharField(max_length=40)

# class Progress(models.Model):
#     from_date = models.DateTimeField(
#         default=timezone.now)
#     upto_date = models.DateTimeField(
#         blank=True, null=True)
#     counter_lost_odd = models.CharField(max_length=20)
#     counter_won_odd = models.CharField(max_length=20)
#     counter_lose = models.CharField(max_length=20)
#     counter_win = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.from_date
#
#     def __str__(self):
#         return self.upto_date
#
#     def __str__(self):
#         return self.counter_lost_odd
#
#     def __str__(self):
#         return self.counter_win
#
#     def __str__(self):
#         return self.counter_lose
#
#     def __str__(self):
#         return self.counter_won_odd
