from django.contrib import admin
from .models import Tournament, User, Deck


class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'address', 'date')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'cpf', 'address', 'tel')


class DeckAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'desc')
# Register your models here.


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(User, UsersAdmin)
admin.site.register(Deck, DeckAdmin)
