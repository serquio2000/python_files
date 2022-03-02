import csv,lit


def imp_rec():
    user = list()
    name = input(lit.str1)
    surname =input(lit.str2)
    age = int(input(lit.str3))
    user.append(name)
    user.append(surname)
    user.append(age)
    user.append(choose_les())
    user.append(imp_code(name,surname,age))
    return user

def imp_code(name,surname,age):
    cod = str(name[:2]) +"-"+ str(surname[-2:]) +"-" +str(age)
    return cod

def choose_les():
    print(lit.str4)
    option = int(input(lit.str5))
    while option != 0:
        match option :
            case 1:
                print(lit.str6)
                lesson = "SMIX"
                return lesson
            case 2:
                print(lit.str7)
                lesson = "ASIX"
                return lesson
            case 3:
                print(lit.str8)
                lesson = "DAW"
                return lesson
            case _:
                choose_les()

def imp_csv(records):
    with open ('files/grades.csv','a') as csvfile:
        writeCSV = csv.writer(csvfile,delimiter="|", quotechar='"', quoting= csv.QUOTE_MINIMAL)
        writeCSV.writerow([lit.header])
        writeCSV.writerow(records)
