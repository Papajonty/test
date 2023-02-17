import wikipedia
import numpy as np
import sys
from wordcloud import wordcloud as wd,STOPWORDS
from PIL import Image

title = str(input('Enter the title : '))
keyword = wikipedia.search(title)
page=wikipedia.page(keyword)
content =page.content

stopwords = set(STOPWORDS)
word_cloud = wd(background_color='white', max_words=300,stopwords= stopwords)
wd.generate(content)
wd.to_file('output.jpg')