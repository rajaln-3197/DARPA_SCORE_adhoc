
from flask import Flask
import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
# from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from io import StringIO
# import PyPDF2
# from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from io import StringIO
# import PyPDF2

app = Flask(__name__)

@app.route('/grobid_titles', methods = ['GET', 'POST'])



def grobid_titles():

    GROBID_HOST = 'http://localhost:8070'
    method = 'processHeaderDocument'
    url = '{0}/api/{1}'.format(GROBID_HOST, method)
    
    path = '/data/szl577/score/Updated_Downloads/Academy_of_Management_Journal/20788785.pdf'
    files = {'input': (path, open(path, 'rb')),}
    # return "hello"

    try:
        resp = requests.post(url, files=files)
    except requests.exceptions.RequestException as ex:
        return ""
        
    if resp.status_code != 200:
        # raise RunnableError('Grobid returned status {0} instead of 200\nPossible Error:\n{1}'.format(resp.status_code, resp.text))
        return ""

    soup = BeautifulSoup(resp.content, "html.parser")
    # print(soup)
    b = soup.find('title', attrs = {'level': "a", 'type' : "main"})
    if b.text:
        return b.text
    else:
        return ""


if __name__ == '__main__':
    app.run(debug=True, threaded=True)




    
 

         



