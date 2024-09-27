from django.urls import path
from .views import RandomPrediction, RandomNumber, RandomNumberRange, RandomNumberSet, RandomPoem, RandomPoemByAuthor
from .views import AllAuthors, AllThemes, AllPoemsByAuthor, AllPoemsByTheme, RandomPoemByTheme, index, random_authors

urlpatterns = [
    path('', index, name='index'),
    path('random/', random_authors, name='random_authors'),
    path('api/prediction/', RandomPrediction.as_view()),

]

urlpatterns += [
    path('api/random-number/', RandomNumber.as_view(), name='random-number'),
    path('api/random-number/<int:min_num>/<int:max_num>/', RandomNumberRange.as_view(), name='random_number_range'),
    path('api/random-numbers/<int:count>/', RandomNumberSet.as_view()),
    path('api/random-poem/', RandomPoem.as_view(), name='random-poem'),
    path('api/random-author/', RandomPoemByAuthor.as_view(), name='random-author'),
    path('api/random-theme/', RandomPoemByTheme.as_view(), name='random-theme'),
    # path('api/random-poem/<str:author>/', RandomPoemByAuthor.as_view(), name='random_author'),
    # path('api/random-poem/theme/<str:theme>/', RandomPoemByTheme.as_view()),
    path('api/authors/', AllAuthors.as_view(), name='authors'),
    path('api/themes/', AllThemes.as_view(), name='themes'),
    path('api/poems/author/<str:author>/', AllPoemsByAuthor.as_view(), name='poem_author'),
    path('api/poems/theme/<str:theme>/', AllPoemsByTheme.as_view()),
]

