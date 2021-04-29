from pdf2image import convert_from_path
pdf_file = "Label_08889880002145.pdf"
pages = convert_from_path(pdf_file)
for page in pages:
    page.save('out.jpg', 'JPEG')