import PyPDF2

pdFiles= ["1.pdf", "2.pdf", "sample.pdf"]

merger = PyPDF2.PdfMerger()
for filename in pdFiles:
        pdFiles = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdFiles)
        merger.append(pdfReader)

pdFiles.close()
merger.write('merged.pdf')       