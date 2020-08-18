from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Match(models.Model):
    homeTeam = models.CharField(_("Home Team"), max_length=100)
    awayTeam = models.CharField(_("Away Team"), max_length=100)
    date = models.DateField(_("Date"))
    startTime = models.TimeField(_("Start Time"))
    slug = models.SlugField(_("Slug"), unique=True, max_length=100)
    pick = models.CharField(_("Pick"), max_length=100)
    odds = models.FloatField(_("Odds"))
    result = models.CharField(_("Result"), max_length=10)
    isLive = models.BooleanField(_("isLive"), default=False)

    MATCH_STATUS = (
        ('won', 'Won'),
        ('lost', 'Lost'),
        ('postponed', 'Postponed'),
        ('waiting', 'Waiting'),
    )
    status = models.CharField(_("Status"),
                              choices=MATCH_STATUS, max_length=10)

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")

    def __str__(self):
        return f'{self.homeTeam} - {self.awayTeam}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.date}-{self.homeTeam}-{self.awayTeam}')
        super(Match, self).save(*args, **kwargs)


class TipGG(models.Model):
    date = models.CharField(max_length=40)
    startTime = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    tip_gg = models.CharField(max_length=10)
    tip_gg_odds = models.CharField(max_length=10, default="0.00")
    result = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class Over15(models.Model):
    date = models.CharField(max_length=40)
    startTime = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    result = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class Over25(models.Model):
    date = models.CharField(max_length=40)
    startTime = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    result = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class Over35(models.Model):
    date = models.CharField(max_length=40)
    startTime = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    result = models.CharField(max_length=40)
    status = models.CharField(max_length=40)


class Featured(models.Model):
    date = models.CharField(max_length=40)
    startTime = models.CharField(max_length=40)
    teams = models.CharField(max_length=400, primary_key=True)
    pick = models.CharField(max_length=10)
    odds = models.CharField(max_length=10, default="0.00")
    result = models.CharField(max_length=40)
    status = models.CharField(max_length=40)
