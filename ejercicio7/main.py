
import functions, csv,lit
def main():
    print(lit.str2,lit.str3)
    option =  int(input(lit.str1))
    while option != 0 :
        match option:
            case 1: functions.read_file()
            case 2: functions.add_record()
        if option == 1:
            option = 0
        else:
            print(lit.str2, lit.str3)
            option = int(input(lit.str1))
if __name__ == "__main__":
    main()
