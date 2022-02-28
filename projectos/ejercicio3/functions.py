str ="insert a text:"
W = 'w'
R = 'r'
A = 'a'
BYE = "bye bye!"
def select_name():
    fname = input("insert a name of file:")
    val = fname[-4:]
    while val != ".txt":
        fname = input("insert a name of file:")
    fname = 'files/' + fname
    return fname

def read_file(fname):
    file = open(fname, R)
    print(file.read())
    file.close()
def write_file(fname):
    file = open(fname, W)
    text = input(str)
    file.write(text)
    file.close()
def append_file(fname):
    file = open(fname, A)
    text = input(str)
    file.write(text)
    file.close()
def leave():
    print(BYE)

