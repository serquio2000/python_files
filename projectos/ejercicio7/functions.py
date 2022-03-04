import csv,lit
def read_file():
    file = open('files/bio.csv', 'r')
    print(file.read())
    file.close()
def add_record():
    bio = dict()
    bio['date'] = input(lit.str4)
    bio['name'] = input(lit.str5)
    bio['location'] = input(lit.str6)
    bio['breed'] = input(lit.str7)
    bio['measure'] = input(lit.str8)
    bio['features'] = input(lit.str9)
    ckf = check_file()
    try:
        with open('files/bio.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = [lit.fl_nam1, lit.fl_nam2, lit.fl_nam3, lit.fl_nam4, lit.fl_nam5, lit.fl_nam6]
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if ckf == False:
                writeCSV.writeheader()
            writeCSV.writerow(bio)
    except:
        print(lit.str10)
    else:
        print(lit.str11)


def check_file():
    def check_file():
        try:
            f = open('files/bio.csv', "r")
            return True
        except FileNotFoundError as e:
            return False
        else:
            f.close()



