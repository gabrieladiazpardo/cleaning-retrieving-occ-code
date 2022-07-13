import pandas as pd
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import warnings 
import string
import unidecode
import re
import unicodedata
import emoji
from bs4 import BeautifulSoup
import nltk
import pickle
import re
import json
import sys
import warnings 
warnings.filterwarnings('ignore')


from occupationcoder.coder import SOCCoder
myCoder = SOCCoder()

#Import Rozee Data in Stata
df = pd.read_stata('./jobs_py.dta', convert_dates=True, convert_categoricals=True, index_col=None, convert_missing=False, preserve_dtypes=True, columns=None, order_categoricals=True, chunksize=None, iterator=False, storage_options=None)
#print(df)  

#Random Sample
#df = df.sample(frac = 0.00001)
#df.head()
#index = df.index
#obs=len(index)
#print(obs)

df = df.replace(np.nan, '', regex=True)

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
     cleantext = re.sub(CLEANR, '', raw_html)
     return cleantext
  

def clean_text(text):
     text = re.sub('[^0-9a-zA-Z]+', ' ', text)
     text = re.sub('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', ' ', text)
     text = re.sub('<.*?>', ' ', text)
     return text
    
# Cleaning all Texts
df['job_title'] = df['job_title'].apply(cleanhtml)
df['job_title'] = df['job_title'].apply(clean_text)
df['job_sector'] = df['job_sector'].apply(cleanhtml)
df['job_sector'] = df['job_sector'].apply(clean_text)
df['job_description'] = df['job_description'].apply(cleanhtml)
df['job_description'] = df['job_description'].apply(clean_text)

#df.head()

#print(df['job_description'].value_counts())
    
  
#if __name__ == '__main__':
df = myCoder.code_data_frame(df, title_column='job_title', sector_column='job_sector',description_column='job_description')
#print('aca esta')
#print(df)

#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#print(df)
    
df.to_csv('jobcodesfff.csv', index=False)

#df.head()
