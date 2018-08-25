from django.db import models


class Owner(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    position = models.CharField(verbose_name="Position", max_length=5)
    team = models.CharField(verbose_name="Team", max_length=20)
    bye = models.IntegerField(verbose_name="Bye")
    rank = models.IntegerField(verbose_name="Rank")
    year = models.CharField(verbose_name="Year", max_length=20,
                            null=True, default=None, blank=True)

    def __str__(self):
        return self.name


class DraftOrder(models.Model):
    order = models.IntegerField(verbose_name="Draft Order")
    owner = models.ForeignKey(Owner, verbose_name="Owner", null=True,
                              default=None, blank=True)
    player = models.ForeignKey(Player, verbose_name="Player", null=True,
                               default=None, blank=True)

    def __str__(self):
        name = str(self.order) + ": " + str(self.owner)
        return name
