from django.db import models

class FireFighter(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    age = models.PositiveIntegerField()


class FireTruck(models.Model):
    side_number = models.CharField(max_length=15)
    model = models.CharField(max_length=50)
    prod_year=models.PositiveIntegerField()
    seats=models.PositiveIntegerField()

class Squad(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    truck = models.ForeignKey(FireTruck, on_delete=models.RESTRICT)

class FirefighterInSquad(models.Model):
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE)
    firefighter = models.ForeignKey(FireFighter, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    class Meta:
        unique_together = (('squad', 'firefighter'),)












































































































































