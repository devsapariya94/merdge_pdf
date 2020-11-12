
from tkinter import filedialog
from tkinter import *
from PyPDF2 import *
filename=[]
total=int(input('enter:  '))
root = Tk()
for i in range (0,total):
          root.filename =  filedialog.askopenfilename(initialdir = "C:\\Users\\Admin\\Desktop",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
          a=root.filename
          filename.append(a)


root.destroy()


mergedObject = PdfFileMerger(strict=False)

for i in filename:
    mergedObject.append(str(i), bookmark=None, pages=None, import_bookmarks=True)

outputname=input('enter name of output file')
outputname=outputname+'.pdf'
output="C:\\Users\\Admin\\Desktop\\.py file\\pdf to text\\output here\\"+outputname
mergedObject.write(output)
print("done!!... check output folder")
