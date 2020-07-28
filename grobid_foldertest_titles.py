import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from io import StringIO
import pandas as pd
import PyPDF2
from sympy import *
import re
import scipy
from scipy.stats import chi2
from scipy import stats
import numpy as np



#********************************************FOLDER PASSING AND GETTING PATHS OF ALL PDFS*************************************************

path1 = '/home/szl577/score_test/sample_for_grobid_test/' #folder to work on the pdfs
f1 = [os.path.join(r,file) for r,d,f in os.walk(path1) for file in f]
pdf_paths = list(filter(lambda f: f.endswith(('.pdf','.PDF')), f1))

# ********************************************************GROBID weaving ********************************************************************
#which url to request for GROBID
GROBID_HOST = 'http://localhost:8070'
method = 'processHeaderDocument'
url = '{0}/api/{1}'.format(GROBID_HOST, method)


#***********************************************************************************TEST GROBID TITLES CODE ***********************************
def grobid_titles(i):
    path = i
    files = {'input': (path, open(path, 'rb')),}
    print(files)
    try:
        resp = requests.post(url, files=files)
    except requests.exceptions.RequestException as ex:
        return ""   
    if resp.status_code != 200:
        # raise RunnableError('Grobid returned status {0} instead of 200\nPossible Error:\n{1}'.format(resp.status_code, resp.text))
        return ""
    soup = BeautifulSoup(resp.content, "html.parser")
    b = soup.find('title', attrs = {'level': "a", 'type' : "main"})
    if b.text:
        return b.text
    else:
        return ""

f1_title = []
for i in pdf_paths:
    title = grobid_titles(i)
    #remove punctuations, spaces, and uppercase
    # aa = ''.join(e for e in title if e.isalnum())
    # aaa = aa.lower()
    f1_title.append(title)

print(f1_title)



#**********************************************************TEST CODE ENDS*************************************************************
