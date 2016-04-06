import eightvar
inp=raw_input("Drag and drop a file or enter /path/to/input.8v here: ")
if inp!='':
    if inp[-1]==' ' and inp[-2]!="\\":
        inp=inp[:-1]
    print("\n")
    eightvar.prnt(open(inp, "r").read())
