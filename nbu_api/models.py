from django.db import models


class Currency(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=3, unique=True)
    cb_price = models.FloatField()
    nba_buy_price = models.FloatField(blank=True, null=True)
    nba_cell_price = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title