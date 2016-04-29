#!/usr/bin/env python

import eightvar
import sys
import os

def prompt(inp):
    if not inp.startswith('8v'):
        inp = '8v1.0v.' + inp + 'fin'
    retval = eightvar.prnt(inp)
    if retval:
        return retval

if len(sys.argv) == 1:
    prm = ''
    inp = ''
    print '8var 1.0 (v1.0 April 29, 2016 07:15:29 UTC)'
    print '8var interpreter from https://www.github.com/neelusb/8var'
    print ''
    while not prm[-4:] == 'exit':
        prm = raw_input('>>> ')
        if prm.startswith('in') and prm[2] != 't':
            prmx = raw_input('')
            if prm.startswith('instr'):
                prm = prm[2:] + "'" + prmx + "'"
            else:
                prm = prm[2:] + prmx
        if prm.startswith('int') or prm.startswith('flt') or prm.startswith('float') or prm.startswith('str') or prm.startswith('bool') or prm.startswith('out') or prm.startswith('uout') or prm.startswith('in') or prm.startswith('dly'):
            if not prm.startswith('out'):
                inp = inp + prm
                retval = prompt(inp)
                if retval:
                    print retval
                    inp = inp[-1 * len(prm)]
            else:
                retval = prompt(inp + prm)
                if retval:
                    print retval
        else:
            sys.stdout.write("\n")
elif len(sys.argv) > 3:
    sys.exit('Too many arguments and/or invalid arguments received.')

elif len(sys.argv) == 3:
    script, flag, toeightvar = sys.argv
    if flag != '-c':
        sys.exit('Too many arguments and/or invalid arguments received.')
    else:
        eightvar.prnt(toeightvar)    
        
else:
    script, fname = sys.argv
    if not os.path.isfile(fname):
        sys.exit('File ' + fname + ' not found. Please check the path and try again.')
    else:
        
        eightvar.prnt(open(fname, "r").read())
