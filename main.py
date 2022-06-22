#Command-line parsing module
#import argparse
#pip install PDF to resolve the issue
#import PDF file reader from pyPDF module
from PyPDF4 import PdfFileReader
#create a function to get the metadata
file_location=input("Provide the file location ")
#open and read the file - call the PDF file as file 
with open(file_location,'rb') as file:
  #Perform all the operations related to reading a file and call the variable as pfd_file 
    pdf_file=PdfFileReader(file)
  #print the exact location of the file as a string 
    print(f'[+] PDF MetaData for:{str(file_location)}')
  #get the document information and call it fileinfo 
    fileinfo=pdf_file.getDocumentInfo()
    #print(fileinfo)
    for data in fileinfo:
        print(f'[+] {data}:{fileinfo[data]}')