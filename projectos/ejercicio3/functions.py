str ="insert a text:"
W = 'w'
A = 'a'
R = 'r'
def create_file():
    fname = input("insert a name of file:")
    val = fname[-4:]
    while val != ".txt":
        fname = input("insert a name of file:")
    fname = 'files/' + fname
def read_file(fname):
    file = open(fname, R)
    print(file.read())
    file.close()
def write_file(fname):
    file = open(fname, W)
    text = input(str)
    file.write(text)
    file.close()
    read_file(fname)
def leave():
    print("bye bye")

