from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator #importing functions from wordcloud
import matplotlib.pyplot as plt #to display our wordcloud
from PIL import Image #to load our image
import numpy as np #to get the color of our image
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))

#path to read image
image_path = os.path.join(my_path, "../static/cloud.png")

#path to save image
image_save_path = os.path.join(my_path, "../static/saved image/")

#path to read file
text_file_path = os.path.join(my_path, "../sample.txt")

#text Content-related
text = open(text_file_path, 'r').read()
stopwords = set(STOPWORDS)

def create_word_cloud(string):

    #using maskarray we are opening the image from image path
    maskArray = np.array(Image.open(image_path))
    #assigning cloud to wordcloud func
    cloud = WordCloud(background_color = "white", mask = maskArray, stopwords = set(STOPWORDS))

    cloud.generate(string)
    cloud.to_file(image_save_path+"wordCloud.png")




# create_word_cloud(dataset)