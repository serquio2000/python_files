import lit,csv,functions

def main():
    records = int(input(lit.str1))
    for i in range(records):
        file = functions.imp_dict()
        functions.open_file(file)

if __name__ == '__main__':
    main()
