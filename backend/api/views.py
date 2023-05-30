from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TournamentSerializer, CardsSerializer, TourPlayersSerializer, DeckSerializer, UserSerializer
from .models import Tournament, Cards, Deck, Tournament_players
# from .models import Tournament, User, Cards, Deck, Tournament_players
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.


class TournamentView(viewsets.ModelViewSet):
    serializer_class = TournamentSerializer
    queryset = Tournament.objects.all()


class CardsView(viewsets.ModelViewSet):
    serializer_class = CardsSerializer
    queryset = Cards.objects.all()


class UserView(viewsets.ModelViewSet):
    pass
    # user = User.objects.create_user()
    # serializer_class = UserSerializer
    # queryset = User.objects.all()



class DeckView(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class TourPlayerView(viewsets.ModelViewSet):
    serializer_class = TourPlayersSerializer
    queryset = Tournament_players.objects.all()

def create_user_view(request):
    print('create_user_view')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Optionally, you can perform additional actions here, such as logging in the user
            
            return redirect('home')  # Replace 'home' with the name of your desired redirect URL

    else:
        return HttpResponse("where is the light?")
        # pass 
        # form = CreateUserForm()s
        # return "Get used?"

    # return render(request, 'create_user.html', {'form': form})
