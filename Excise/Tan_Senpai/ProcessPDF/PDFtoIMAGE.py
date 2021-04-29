from pdf2image import convert_from_path
import os

def main(roots_file):
    file_names = [x for x in os.listdir(roots_file) if x.endswith('.pdf')]
    # print(file_names)
    for file_name in file_names:
        ten = os.path.splitext(file_name)[0]
        folder_path = os.path.join(roots_file, ten)
        os.makedirs(folder_path, exist_ok=True)
        pdf_path = os.path.join(roots_file, file_name)
        extract(pdf_path, ten, folder_path)


def extract(pdf_path, ten, folder_path):
    images = convert_from_path(pdf_path)
    for i in range(1, len(images)):
        save_image = os.path.join(folder_path, ten + '_' + str(i).zfill(3) + '.jpg')
        images[i].save(save_image, 'JPEG')
        break


if __name__ == '__main__':
    roots_file = r'C:\Users\HuyNV27\Desktop\python\task-tan\TEST_0415'
    main(roots_file)