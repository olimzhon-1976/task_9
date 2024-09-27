from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prediction, Poem
from django.shortcuts import render
import random


def index(request):
    return render(request, 'predictions/index.html')


def random_authors(request):
    return render(request, 'predictions/random_author.html')


class RandomPrediction(APIView):
    def get(self, request):
        predictions = Prediction.objects.all()
        prediction = random.choice(predictions)
        return Response({'prediction': prediction.text})


class RandomNumber(APIView):
   def get(self, request):
       num = random.randint(1, 100)
       return Response({'random_number': num})


class RandomNumberRange(APIView):
   def get(self, request, min_num, max_num):
       num = random.randint(min_num, max_num)
       return Response({'random_number': num})


class RandomNumberSet(APIView):
   def get(self, request, count):
       numbers = random.sample(range(1, 101), count)
       return Response({'random_numbers': numbers})


class RandomPoem(APIView):
   def get(self, request):
       poems = Poem.objects.all()
       poem = random.choice(poems)
       return Response({'poem': {'title': poem.title, 'text': poem.text}})


class RandomPoemByAuthor(APIView):
   def get(self, request):
       poems = Poem.objects.all()
       poem = random.choice(poems)
       return Response({'Author': {'Name': poem.author, 'Book': poem.title}})


class RandomPoemByTheme(APIView):
   def get(self, request):
       poems = Poem.objects.all()
       poem = random.choice(poems)
       return Response({'Поэмы': {'Жанр': poem.theme, 'Книга': poem.title}})


# class RandomPoemByAuthor(APIView):
#    def get(self, request, author):
#        poems = Poem.objects.filter(author=author)
#        poem = random.choice(poems)
#        return Response({'poem': {'title': poem.title, 'text': poem.text}})


# class RandomPoemByTheme(APIView):
#    def get(self, request, theme):
#        poems = Poem.objects.filter(theme=theme)
#        poem = random.choice(poems)
#        return Response({'poem': {'title': poem.title, 'text': poem.text}})


class AllAuthors(APIView):
   def get(self, request):
       authors = Poem.objects.values_list('author').distinct()
       return Response({'authors': list(authors)})


class AllThemes(APIView):
   def get(self, request):
       themes = Poem.objects.values_list('theme').distinct()
       return Response({'themes': list(themes)})


class AllPoemsByAuthor(APIView):
   def get(self, request, author):
       poems = Poem.objects.filter(author=author).values('title')
       return Response({'poems': list(poems)})


class AllPoemsByTheme(APIView):
   def get(self, request, theme):
       poems = Poem.objects.filter(theme=theme).values('title')
       return Response({'poems': list(poems)})