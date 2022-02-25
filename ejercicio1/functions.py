str ="insert a text:"
W = 'w'
def write_file(fname):
    file = open(fname, W)
    text = input(str)
    file.write(text)
    file.close()
