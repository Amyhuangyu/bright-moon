# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:44:24 2019

@author: DELL
"""

import jieba
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
import re
import collections
import matplotlib.pyplot as plt
data=open(r'C:\Users\DELL\Desktop\2019上python\银河.txt','r',errors='ignore').read()
pattern=re.compile('\t|\n|\.|-|:|;|\)|\(|\?|"|的|不|，|曾|一|成为|你|也|大家|大人|最后|了|将|“|')
data=re.sub(pattern, '',data)
cut=jieba.lcut(data)
words_count=collections.Counter(cut)
path='爱心.jpg'
img=imread(path)
wd=WordCloud(background_color='white',font_path=r'C:\Windows\Fonts\FZSTK.TTF',
             mask=img).generate_from_frequencies(words_count)
image_colors = ImageColorGenerator(img)
plt.imshow(wd)
plt.axis('off')
plt.show()

