str ="insert a text:"
W = 'w'
A = 'a'
def write_file(fname):
    file = open(fname, W)
    text = input(str)
    file.write(text)
    file.close()
def add_text(fname):
    file = open(fname, A)
    text = input(str)
    file.write(text)
    file.close()