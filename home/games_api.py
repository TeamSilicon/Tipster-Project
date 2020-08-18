from rest_framework import serializers, viewsets
from home.models import Match
from home.views import date_picker
from rest_framework.response import Response
from itertools import chain


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ('homeTeam', 'awayTeam', 'startTime', 'pick',
                  'result', 'odds', 'status', 'date')


class GamesViewSet(viewsets.ViewSet):
    def list(self, request):
        today_date = date_picker

        yesterday = Match.objects.filter(
            date=today_date(-1)).order_by('startTime')
        today = Match.objects.filter(
            date=today_date(0)).order_by('startTime')
        tomorrow = Match.objects.filter(
            date=today_date(1)).order_by('startTime')

        queryset = [yesterday, today, tomorrow]
        games = []
        for day in queryset:
            serializer = GamesSerializer(day, many=True)
            games.append(serializer.data)
        return Response(games)
