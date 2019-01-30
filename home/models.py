from django.db import models
from django.utils import timezone


class ZuluBet(models.Model):
    match_date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip = models.CharField(max_length=40)
    tip_odd = models.CharField(max_length=20)
    ft_results = models.CharField(max_length=40)

    def __str__(self):
        return [
            self.match_date, self.time, self.teams, self.tip, self.tip_odd,
            self.ft_results]


class Progress(models.Model):
    from_date = models.DateTimeField(
        default=timezone.now)
    upto_date = models.DateTimeField(
        blank=True, null=True)
    counter_lost_odd = models.CharField(max_length=20)
    counter_won_odd = models.CharField(max_length=20)
    counter_lose = models.CharField(max_length=20)
    counter_win = models.CharField(max_length=20)

    def __str__(self):
        return self.from_date

    def __str__(self):
        return self.upto_date

    def __str__(self):
        return self.counter_lost_odd

    def __str__(self):
        return self.counter_win

    def __str__(self):
        return self.counter_lose

    def __str__(self):
        return self.counter_won_odd
