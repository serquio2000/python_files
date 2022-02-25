import functions
#FL_DR='files/fitxer2.txt'
op = 'select option:'
str1,str2,str3,str4 = "create file (1)","\nshow file (2)", "\nmodify file(3)","\n leave(4)"
def main():
    print(str1,str2,str3,str4)
    option = int(input(op))
    match option:
        case 1:
            file = functions.create_file()
        case 2:
            file = functions.create_file()
            functions.read_file(file)
        case 3:
            file = functions.create_file()
            functions.write_file(file)
        case 4:
            functions.leave()
if __name__ == "__main__":
    main()
