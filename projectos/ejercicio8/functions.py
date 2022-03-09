import csv,lit

def read_file():
    with open('files/projects_board.csv','r') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            print(f'\t codi_proj:{row[0]},\tnom_proj:{row[1]},\tcodi_client:{row[2]},\tcodi_resp:{row[3]},\tpreu:{row[4]},\tdata_inici:{row[5]},\tdata_fi:{row[6]}')
def count_proj():
    count = 0
    with open('files/projects_board.csv','r') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            count += 1
        print(count)
def total_price():
    with open('files/projects_board.csv') as csvfile:
        readCSV = csv.DictReader(csvfile)  # si lempleas el metodo DicReader...

        for row in readCSV:
            print(row['preu'])  # reconoce el diccionario y puede acceder con la clave preu
            val = val + int(row['preu'])
        print(val)


