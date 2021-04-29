import os
from pdf import main as pdf_reader

root_dir = r'C:\Users\HuyNV27\Desktop\python\Label_08889880002145.pdf'
filenames = [x for x in os.listdir(root_dir) if x.endswith('.pdf')]
for filename in filenames:
    pdf_path = os.path.join(root_dir, filename)
    pdf_reader(pdf_path)


