import pdfbox
p = pdfbox.PDFBox()

#iterating paths of pdfs in  folder
path1 = '/home/szl577/score_test/sample_for_grobid_test/'
files = [os.path.join(r,file) for r,d,f in os.walk(path1) for file in f]
pdf_paths = list(filter(lambda f: f.endswith(('.pdf','.PDF')), files))

#where i is the path of the pdfs
for i in pdf_paths:
  p.extract_text(i) #gives the .txt file in the same path along with .pdf with same file name