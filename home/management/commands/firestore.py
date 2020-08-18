import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings
from home.models import Match
from datetime import date
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Updates games in firestore db"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        cred = credentials.Certificate(settings.SERVICE_ACCOUNT_JSON_FILE)
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        self.databaseRefence = db.collection('football')

    def handle(self, *args, **options):
        matches = Match.objects.filter(date__gte=date.today())
        for match in matches:
            matchDate = match.date.strftime('%Y-%m-%d')
            data = self.databaseRefence.document(
                matchDate).collection(matchDate).document(match.slug)
            data.set({
                'homeTeam': match.homeTeam,
                'awayTeam': match.awayTeam,
                'date': matchDate,
                'startTime': match.startTime.strftime('%H:%M'),
                'pick': match.pick,
                'odds': match.odds,
                'result': match.result,
                'status': match.status,
                'isLive': match.isLive,
            })
