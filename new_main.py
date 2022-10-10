

from occupationcoder.coder import SOCCoder
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
myCoder = SOCCoder()
CLEANR = re.compile('<.*?>')


def clean_html(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


def clean_text(text):
    text = re.sub('[^0-9a-zA-Z]+', ' ', text)
    text = re.sub(
        '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});', ' ', text)
    text = re.sub('<.*?>', ' ', text)
    return text


def clean_data(file_path: str):
    # Import Rozee Data in Stata
    df = pd.read_stata(
        file_path,
        convert_dates=True,
        convert_categoricals=True,
        index_col=None,
        convert_missing=False,
        preserve_dtypes=True,
        columns=None,
        order_categoricals=True,
        chunksize=None,
        iterator=False,
        storage_options=None
    )
    # print(df)

    # Random Sample
    #df = df.sample(frac = 0.001)
    #df.head()
    #index = df.index
    #obs=len(index)
    #print(obs)

    #df = df.replace(np.nan, '', regex=True)

    # Cleaning all Texts
    df['job_title'] = df['job_title'].apply(clean_html)
    df['job_title'] = df['job_title'].apply(clean_text)
    df['job_sector'] = df['job_sector'].apply(clean_html)
    df['job_sector'] = df['job_sector'].apply(clean_text)
    df['job_description'] = df['job_description'].apply(clean_html)
    df['job_description'] = df['job_description'].apply(clean_text)
    # df.head()
    # print(df['job_description'].value_counts())
    return df


def get_code_df(df, title_column, sector_column, description_column):
    return myCoder.code_data_frame(
        df,
        title_column=title_column,
        sector_column=sector_column,
        description_column=description_column
    )
    # print(df)

    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    # print(df)

    # df.head()


if __name__ == "__main__":
    # Input file path, must be a dta
    input_file_path = sys.argv[1]  # <input_file_path>

    # Output file path with extension
    output_file_path = sys.argv[2]  # <output_file_path>

    # Default values in case the user does not provide them
    title_column = 'job_title'
    sector_column = 'job_sector'
    description_column = 'job_description'

    # If the user choose to override the values
    if len(sys.argv) > 3:
        title_column = sys.argv[3]
        sector_column = sys.argv[4]
        description_column = sys.argv[5]

    # Clean data
    df = clean_data(input_file_path)
    df = get_code_df(df, title_column, sector_column, description_column)
    df.to_csv(output_file_path, index=False)

    print(f'File Saved in {output_file_path}')
