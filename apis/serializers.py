from rest_framework import serializers

# ClimateChangeInfo Class to create the object of UKMetWeather response
class ClimateChangeInfo(object):
    def __init__(self, year, jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, win, spr, sum, aut, ann):
        self.year = year
        self.jan = jan
        self.feb = feb
        self.mar = mar
        self.apr = apr
        self.may = may
        self.jun = jun
        self.jul = jul
        self.aug = aug
        self.sep = sep
        self.oct = oct
        self.nov = nov
        self.dec = dec
        self.win = win
        self.spr = spr
        self.sum = sum
        self.aut = aut
        self.ann = ann

# ClimateChangeInfoSerializer class to serialize the object of ClimateChangeInfo class
class ClimateChangeInfoSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    jan = serializers.FloatField()
    feb = serializers.FloatField()
    mar = serializers.FloatField()
    apr = serializers.FloatField()
    may = serializers.FloatField()
    jun = serializers.FloatField()
    jul = serializers.FloatField()
    aug = serializers.FloatField()
    sep = serializers.FloatField()
    oct = serializers.FloatField()
    nov = serializers.FloatField()
    dec = serializers.FloatField()
    win = serializers.FloatField()
    spr = serializers.FloatField()
    sum = serializers.FloatField()
    aut = serializers.FloatField()
    ann = serializers.FloatField()