import lit, csv


def imp_dict():
    book = dict()
    book['isbn'] = input(lit.str2)
    book['title'] = input(lit.str3)
    book['author'] = input(lit.str4)
    book['editorial'] = input(lit.str5)
    book['pub_date'] = input(lit.str6)
    return book

def check_file():
    try:
        f = open('files/books.csv', "r")
        return True
    except FileNotFoundError as e:
        return False
    else:
        f.close()


def open_file(book):
    ckf = check_file()
    try:
        with open('files/books.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = [lit.fl_nam]
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if ckf == False:
                writeCSV.writeheader()
            writeCSV.writerow(book)
    except:
        print(lit.str7)
    else:
        print(lit.str8)
