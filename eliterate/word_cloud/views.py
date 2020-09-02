from django.shortcuts import render
from word_cloud.wordcld import create_word_cloud, text  #importing from wordcld file
# Create your views here.
    

dataset = text


def wordcloudview(request):
    
    wordcloud = create_word_cloud(dataset)
    return render(request, 'base.html')

    