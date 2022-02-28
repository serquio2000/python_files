import files_functions.ejercicio3.functions
import functions
#FL_DR='files/fitxer2.txt'
op = 'select option:'
str1,str2,str3,str4 = "create file (1)","\nshow file (2)", "\nmodify file(3)","\n leave(4)"
def main():
    print(str1,str2,str3,str4)
    option = int(input(op))
    match option:
        case 1:
            fname = functions.select_name()
            functions.append_file(fname)
        case 2:
            fname = functions.select_name()
            functions.read_file(fname)
        case 3:
            fname = functions.select_name()
            functions.write_file(fname)
            functions.read_file(fname)
        case 4:
            functions.leave()
if __name__ == "__main__":
    main()
