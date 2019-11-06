from rest_framework import serializers, viewsets
from home.models import AllGames
from home.views import date_picker
from rest_framework.response import Response
from itertools import chain


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllGames
        fields = ('teams', 'start_time', 'pick',
                  'score', 'odds', 'won_or_lost', 'date')


class GamesViewSet(viewsets.ViewSet):
    def list(self, request):
        today_date = date_picker

        yesterday = AllGames.objects.filter(
            date=today_date(-1)).order_by('start_time', 'teams')
        today = AllGames.objects.filter(
            date=today_date(0)).order_by('start_time', 'teams')
        tomorrow = AllGames.objects.filter(
            date=today_date(1)).order_by('start_time', 'teams')

        queryset = [yesterday, today, tomorrow]
        games = []
        for day in queryset:
            serializer = GamesSerializer(day, many=True)
            games.append(serializer.data)
        return Response(games)



