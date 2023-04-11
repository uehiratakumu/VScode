import glob
from PyPDF2 import PdfFileMerger

pdf_file_merger = PdfFileMerger()

for file_name in glob.glob('*.pdf'):

	pdf_file_merger.append(file_name)

pdf_file_merger.write('merge.pdf')

pdf_file_merger.close()