# print a tree
from string import Template
from email.message import EmailMessage
import smtplib
import ssl
import glob
import os
import random
import re
import sys
from time import time
from pathlib import Path

import img2pdf
from PIL import Image, UnidentifiedImageError
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfMerger
import requests
import hashlib


def show_tree():
    tree = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]
    # 1 iterate over tree
    # if 0 -> print ''
    # if 1 -> print *
    fill = '*'
    empty = ' '
    new_line = ''
    for col in tree:
        for row in col:
            if row:
                print(fill, end='')
            else:
                print(empty, end='')
        print(new_line)

# Check for duplicates in list.


def check_duplicate_list():
    some_list = ['a', 'b', 'a', 'c', 'd', 'e', 'd',
                 'n', 'c', 's', 'g', 'c', 's', 'g', 'a']
    # some_list = ['a', 'b', 'a', 'c', 'a', 'a', 'c']
    # print items duplicated
    duplicated_list = []
    for item in some_list:
        if some_list.count(item) > 1:
            if item not in duplicated_list:
                duplicated_list.append(item)
    print(duplicated_list)

# Find highest even number


def highest_even(li):
    even_list = []
    for number in li:
        if number % 2 == 0:
            even_list.append(number)
    return max(even_list)


# print(highest_even([1, 19, 20, 2, 4, 8, 17, 24, 12, 56, 3, 45, 38, 69, 94]))


# class SuperList(list):
#     def __len__(self):
#         return super().__len__()


# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(3)
# print(super_list1)
# print(len(super_list1))

# # Order a list by the second item in a tuple of the list
# my_list = [(0, 2), (4, 3), (9, 9), (10, -1)]
# my_list.sort(key=lambda item: item[1])
# print(my_list)

# # create list, dict, set by comprehension.
# my_list = [num ** 2 for num in range(0, 10)]
# my_list2 = [num for num in my_list if num % 2 == 0]
# print(my_list)
# print(my_list2)

# my_set = {num for num in [1, 1, 2, 3, 4, 1, 2, 5, 4, 5, 2, 6, 3]}
# print(my_set)

# my_dict = {key: value ** 2 for key, value in enumerate(range(0, 10))}
# my_dict2 = {key: value for key,
#             value in my_dict.items() if value % 2 == 0}
# my_dict3 = {num: num*3 for num in range(0, 10)}
# print(my_dict)
# print(my_dict2)
# print(my_dict3)

# # Check for duplicates in list by comprehension
# test_list = ['a', 'b', 'a', 'c', 'd', 'e', 'd',
#              'n', 'c', 's', 'g', 'c', 's', 'g', 'a']
# duplicates = list(set([duplicate_item for duplicate_item in test_list if test_list.count(
#     duplicate_item) > 1]))
# print(duplicates)

# # Decorator pattern
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         func(*args, **kwargs)
#     return wrap_func


# @ my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)


# hello('hello', ':)')

# Create a function to check the run time of a function that other
def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}s to run function')
        return result
    return wrap_func


@performance
def long_time():
    for item in range(1000000):
        item * 2


# long_time()

# # Error handling
# while True:
#     try:
#         age = int(input("What is your age?"))
#         print(age)
#     except ValueError:
#         print("Please enter your age")
#     except ZeroDivisionError:
#         print("Please enter your age that bigger than 0")
#     else:
#         print("Thank you!")
#         break

def total(*args):
    try:
        total = 0
        for num in args:
            total += num
        return total
    except (TypeError, ValueError) as err:
        print(err)
    else:
        print("Thank you")
    finally:
        print("Finally, we done.")

    # end try
# print(total(1, 2, 3, 4, 5))


# # Generators
# def generator_func(num):
#     for item in range(num):
#         yield item


# def new_list(li):
#     new_list = []
#     for num in generator_func(li):
#         new_list.append(num)
#     return new_list


# new_list = new_list(100000)
# print(new_list)


# # Under the hood of Generators
# class Generator():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if Generator.current < self.last:
#             num = Generator.current
#             Generator.current += 1
#             return num
#         raise StopIteration


# ge = Generator(0, 1000000)
# my_list = []
# for item in ge:
#     my_list.append(item)
# print(my_list)

# # Fibonacci Numbers by using list
# def fib(number: int):
#     fib = []
#     for item in range(0, number + 1):
#         if item < 2:
#             fib.append(item)
#         else:
#             fib.append(fib[item - 1] + fib[item - 2])
#     return fib


# print(fib(30))

# #  Fibonacci Numbers by using Generator


# class Fibonacci_generator():
#     current = 0
#     previous = 0
#     pre_previous = 0

#     def __init__(self, first, last) -> None:
#         self.first = first
#         self.last = last
#         pass

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if Fibonacci_generator.current <= self.last:
#             if Fibonacci_generator.current < 2:
#                 num = Fibonacci_generator.current
#                 if num == 0:
#                     Fibonacci_generator.pre_previous = num
#                 elif num == 1:
#                     Fibonacci_generator.previous = num
#             else:
#                 num = Fibonacci_generator.pre_previous + Fibonacci_generator.previous
#                 Fibonacci_generator.pre_previous = Fibonacci_generator.previous
#                 Fibonacci_generator.previous = num
#             Fibonacci_generator.current += 1
#             return num
#         raise StopIteration


# fi = Fibonacci_generator(0, 30)
# li = []
# for item in fi:
#     li.append(item)

# print(li)


# # Create Fibonacci Numbers by using Generator with yield
# def fib_gen(number: int):
#     fib_number = 0
#     pre_num = 0
#     pre_pre_num = 0
#     for num in range(0, number + 1):
#         if num < 2:
#             fib_number = num
#             if num == 0:
#                 pre_pre_num = num
#             elif num == 1:
#                 pre_num = num
#         else:
#             fib_number = pre_pre_num + pre_num
#             pre_pre_num = pre_num
#             pre_num = fib_number
#         yield fib_number


# fib_nums = []
# for fib_num in fib_gen(30):
#     fib_nums.append(fib_num)
# print(fib_nums)
# first_arg = sys.argv[1]
# last_arg = sys.argv[2]
# ran_num = random.randint(first_arg, last_arg)
# print(first_arg, last_arg)
# input('What your answer?')
# print(f'random number {ran_num}')
# Game guess a number
def get_random_number(first: int, last: int):
    return random.randint(int(first), int(last))


def get_number_entered(first: int, last: int):
    return int(input(f'Please enter a number from {first} ~ {last}: '))


def check_guess(guess: int, answer: int, first: int, last: int):
    if int(guess) >= first and int(guess) <= last:
        if int(guess) == int(answer):
            return True
    return False


def GuessNumber(first: int, last: int):
    answer = get_random_number(first, last)
    print(answer)
    while True:
        try:
            guess = get_number_entered(first, last)
            if check_guess(guess, answer, first, last):
                return 'You are a genius'
                # break
                # else:
                #     continue
        except ValueError as err:
            print(f'Please enter a number')

        # end try
# if __name__ == '__main__':
#     print(GuessNumber(1, 10))


# Email, Password Validation


def user_validate(email: str, password: str):
    """User Validation

    Args:
        email (str): Email address of user
        password (str): Password of user

    Returns:
        'User Valid': Email and Password is valid
        'Password Invalid': Email is valid but Password is invalid
        'Email InValid': Password is valid but Email is invalid
        'User Invalid': Both Email and Password is invalid
    """
    email_pattern = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    password_pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()])[a-zA-Z\d!@#$%^&*()]{8,20}$')
    valid_email = re.fullmatch(email_pattern, email)
    valid_password = re.fullmatch(password_pattern, password)
    if valid_email != None and valid_password != None:
        return 'User Valid'
    elif valid_email != None and valid_password == None:
        return 'Password Invalid'
    elif valid_email == None and valid_password != None:
        return 'Email Invalid'
    else:
        return 'User Invalid'
    # return (valid_email, valid_password)


# print(user_validate('thi@thi.com.vn', '1234asdJASsda@!#2'))

# Image handling with Pillow Library
def isDirExist(name_dir: str):
    """Check directory is exist

    Args:
        name_dir (str): Name directory checked
    Outputs:
        True: Directory is exist
        False: Directory is not exist
    """
    return os.path.exists(name_dir)


def createFolder(path_folder: str):
    """Create a folder

    Args:
        path_folder (str): Path of folder created
    """
    if isDirExist(path_folder) == False:
        os.makedirs(path_folder)
        print(f'Finish creating folder: {path_folder}.')
    else:
        print(f'Folder {path_folder} is exist.')


def convert_to_png(image_folder: str, output_folder: str):
    """Convert all image to png format and save all converted images into new folder

    Args:
        image_folder (str: path): Folder save original images
        output_folder (str: path): New folder save converted images
    """
    createFolder(output_folder)
    file_list = os.listdir(image_folder)
    count = 0
    for image in file_list:
        try:
            count += 1
            path_image = f'{image_folder}{image}'
            change_png = image.split('.jpg')[0]
            output_image = f'{output_folder}{change_png}.png'
            with Image.open(path_image) as im:
                im.thumbnail((400, 400))
                im.save(output_image, 'png')
                print(f'save png image {count} done')
        except UnidentifiedImageError:
            print(UnidentifiedImageError)
    count = 0


# convert_to_png(sys.argv[1], sys.argv[2])
# convert_to_png('.\images\\', '.\images_png\\')

# Handling pdf files
def convert_img2pdf(img_folder: str, pdf_folder: str):
    """Convert images to pdf files

    Args:
        img_folder (str: path): Path image folder
        pdf_folder (str: path): Path pdf folder
    """
    createFolder(pdf_folder)
    img_list = os.listdir(img_folder)
    count = 0
    err_count = 0
    err_imgs = []
    for img in img_list:
        count += 1
        pdf_name_file = img.split('.png')[0]+'.pdf'
        # print(pdf_name_file)
        try:
            with open(os.path.join(pdf_folder, pdf_name_file), 'wb') as pdf_file:
                pdf_file.write(img2pdf.convert(os.path.join(
                    img_folder, img), rotation=img2pdf.Rotation.ifvalid))
                print(
                    f'Finish converting image {img} to pdf. Done {count} file.')
                pdf_file.close()
        except img2pdf.ExifOrientationError as err:
            err_count += 1
            err_imgs.append(img)
            print(f'Image {img} is errored: {err}. Converting is canceled.')
            pass
        # print(img)
        pass
    if err_count > 0:
        print(
            f'Have {err_count} image is errored. Images: {err_imgs} have been yet converted to pdf file')
    else:
        print('All image have been converted to pdf file.')
        pass
    err_count = 0
    count = 0
    pass


# convert_img2pdf('.\images_png\\', '.\handling_PDF_file\seperate_pdfs\\')


def combine_pdfs(merge_pdf_folder: str, seperate_pdf_folder: str):
    """Combine multiple pdf files into one pdf file

    Args:
        merge_pdf_folder (str: path): Path folder save pdf file is combined
        seperate_pdf_folder (str: path): Path folder contain pdf files need to be combined
    """
    createFolder(merge_pdf_folder)
    merge_pdfs = PdfMerger()
    pdf_list = os.listdir(seperate_pdf_folder)
    for pdf in pdf_list:
        merge_pdfs.append(os.path.join(seperate_pdf_folder, pdf))
    merge_pdfs.write(os.path.join(merge_pdf_folder, 'pokemon_family.pdf'))
    print(
        f'Complete combining {len(pdf_list)} pdf file into one pdf file unique.')


# combine_pdfs('.\handling_PDF_file\combine_pdf\\',
#              '.\handling_PDF_file\seperate_pdfs\\')


def insert_watermark_pdf(pdf_file: str, watermark_file: str, output_file: str):
    """Insert a watermark into all pages of pdf file

    Args:
        pdf_file (str: path): Path of pdf file need to be insert a watermark
        watermark_file (str): Path of watermark file
        output_file (str): Path of output file was inserted a watermark
    """
    reader = PdfFileReader(pdf_file)
    writer = PdfFileWriter()
    for page_num in list(range(0, reader.numPages)):
        get_content = reader.pages[page_num]
        content_box = get_content.mediaBox

        watermark_reader = PdfFileReader(watermark_file)
        get_watermark = watermark_reader.pages[0]

        # get_content.merge_page(get_watermark)
        # get_content.mediaBox = content_box
        get_watermark.merge_page(get_content)
        get_watermark.mediaBox = content_box
        writer.add_page(get_watermark)
    with open(output_file, 'wb') as f:
        writer.write(f)
    pass


# insert_watermark_pdf(
#     'pdf_example.pdf', '.\handling_PDF_file\combine_pdf\pokemon_family.pdf', 'pdf_example_waternark.pdf')

def insert_stamp_pdf(pdf_file: str, stamp_file: str, output_file: str):
    """Insert a stamp into all pages of pdf file

    Args:
        pdf_file (str: path): Path of file need to be inserted a stamp
        stamp_file (str: path): Path of file stamp
        output_file (str: path): Path of out file was inserted a stamp
    """
    reader = PdfFileReader(pdf_file)
    writer = PdfFileWriter()
    for page_num in list(range(0, reader.numPages)):
        get_content = reader.pages[page_num]
        content_box = get_content.mediaBox

        watermark_reader = PdfFileReader(stamp_file)
        get_watermark = watermark_reader.pages[0]

        get_content.merge_page(get_watermark)
        get_content.mediaBox = content_box
        writer.add_page(get_content)
    with open(output_file, 'wb') as f:
        writer.write(f)
    pass


# Check security of password
def generator_hash_password(password: str):
    hashed_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_chars_5, tail = hashed_pass[:5], hashed_pass[5:]
    return first_chars_5, tail


def get_hash_data(first5hashchar: str):
    """Get hash data of passwords have first five hash characters

    Args:
        first5hashchar (str): First five hash characters of password need to be check security

    Returns:
        res: A list password hashes that gotten from website: https://api.pwnedpasswords.com/range/
    """
    url = 'https://api.pwnedpasswords.com/range/' + first5hashchar
    res = requests.get(url).text.splitlines()
    return res


def get_password_leaks_count(hashes: str, hash_to_check: str):
    """Get password leaks count

    Args:
        hashes (str): A list password hashes that goten from webshite: https://api.pwnedpasswords.com/range/
        hash_to_check (str): Password hash of password need to be checked security

    Returns:
        count: A count of how many times password appears in the data breaches
    """
    hashes = (line.split(':') for line in hashes)
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def check_security_password(password: str):
    """Check security of password

    Args:
        password (str): Password need to be checked security
    """
    first5, tail = generator_hash_password(password)
    response = get_hash_data(first5)
    count = get_password_leaks_count(response, tail)
    if count:
        print(
            f'Password: {password} had been found {count} times. You should change to another password.')
    else:
        print(f'Password: {password} NOT found. Carry on!')


# check_security_password('AiYeuToiKhong1234')


# Send email
def send_email():
    html = Path('index.html').read_text(encoding=None, errors=None)
    html_template = Template(html)
    smtp_server = 'smtp.gmail.com'
    port = '587'
    msg = EmailMessage()
    sender_email = 'nnthibk1234@gmail.com'
    password = 'aygkzrvjssphtluc'
    context = ssl.create_default_context()
    msg['Subject'] = 'Hello, my name is Thi'
    msg['from'] = 'nnthibk1234@gmail.com'
    msg['to'] = 'onhanam1234@gmail.com'
    msg.set_content(html_template.substitute({'name': 'your bastard'}), 'html')
    try:
        with smtplib.SMTP(smtp_server, port) as server_email:
            server_email.ehlo()
            server_email.starttls(context=context)
            server_email.ehlo()
            server_email.login(sender_email, password)
            server_email.send_message(msg)
    except Exception as err:
        print(err)
    finally:
        server_email.close()
