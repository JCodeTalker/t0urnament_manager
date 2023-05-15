from django.db import models

# Create your models here.

# missing id's...


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField("date it happens")

    def __str__(self):
        return self.name


class Tournament_players(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(
        User, on_delete=models.CASCADE)  # many to one, etc?

    def __str__(self) -> str:
        return super().__str__()


class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    desc = models.CharField(max_length=200)

    def __str__(self) -> str:
        return super().__str__()


class Cards(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    name = models.CharField(max_length=65)
    desc = models.CharField(max_length=200)
    api_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()
