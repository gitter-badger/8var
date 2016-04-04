import sys

inp=sys.stdin.read()
out=''
intVar=""
curInt=0
newInt=0
varInt=[0, 0, 0, 0, 0, 0, 0, 0]
boolVar=""
curBool=0
newBool=0
varBool=[False, False, False, False, False, False, False, False]
strVar=""
curStr=0
newStr=0
varStr=["", "", "", "", "", "", "", ""]
add=0
sub=0

while len(inp)>0:
    if inp.startswith("int"):
        inp=inp[3:]
        if inp[0]=="n":
            if newInt<=7:
                inp=inp[1:]
                intVar=""
                if inp[0]=="-":
                    intVar="-"
                    inp=inp[1:]
                elif inp[0]=="+":
                    inp=inp[1:]
                while inp[0] in "0123456789":
                    intVar=intVar+inp[0]
                    inp=inp[1:]
                varInt[newInt]=int(intVar)
                intVar=""
            else:
                sys.exit("ERROR: Too many variables of type int used.")
        else:
            curInt=int(inp[0])
            if 0<=curInt<=8:
                inp=inp[1:]
                intVar=""
                if inp[0]=="+":
                    inp=inp[1:]
                    add=1
                elif inp[0]=="-":
                    inp=inp[1:]
                    sub=1
                while inp[0] in "0123456789":
                    intVar=intVar+inp[0]
                    inp=inp[1:]
                if add==1:
                    varInt[curInt]=varInt[curInt]+int(intVar)
                    add=0
                elif sub==1:
                    varInt[curInt]=varInt[curInt]-int(intVar)
                    sub=0
                else:
                    varInt[curInt]=int(intVar)
                intVar=""
            else:
                sys.exit("ERROR: Variable doesn't exist.")
        continue
    elif inp.startswith("bool"):
    else:
        inp=inp[1:]
                        
print varInt
print varBool
print varStr
sys.stdout.flush()
