import sys
import time
import urllib2

def prnt(inp):
    inp=inp.lower()
    if inp[-3:] is not "fin":
        sys.exit("[8var] ERROR: Unexpected end of file.")
    if inp[0:2] is not "8v":
        sys.exit("[8var] ERROR: Unexpected beginning for file.")
    outLines=''
    version=''
    ucFloat=0
    ucode=""
    ucodeInt=0
    outLinesInt=0
    out=''
    delay=""
    intVar=""
    lastInt=0
    curInt=0
    newInt=0
    intFin=0
    checkInt=[False, False, False, False, False, False, False, False]
    varInt=[0, 0, 0, 0, 0, 0, 0, 0]
    lastBool=0
    curBool=0
    newBool=0
    boolFin=0
    checkBool=[False, False, False, False, False, False, False, False]
    varBool=[False, False, False, False, False, False, False, False]
    strVar=""
    lastStr=0
    curStr=0
    newStr=0
    checkStr=[False, False, False, False, False, False, False, False]
    varStr=["", "", "", "", "", "", "", ""]
    strFin=0
    quotes=""
    floatVar=""
    lastFloat=0
    curFloat=0
    newFloat=0
    checkFloat=[False, False, False, False, False, False, False, False]
    varFloat=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    floatFin=0
    add=0
    sub=0

    def uc(uc):
        uc=int(uc)
        while uc>255:
            uc=uc-255
            continue
        while uc<0:
            uc=uc+255
            continue
        if uc==0:
            return u'\u0000'
        if uc==1:
            return u'\u0001'
        if uc==2:
            return u'\u0002'
        if uc==3:
            return u'\u0003'
        if uc==4:
            return u'\u0004'
        if uc==5:
            return u'\u0005'
        if uc==6:
            return u'\u0006'
        if uc==7:
            return u'\u0007'
        if uc==8:
            return u'\u0008'
        if uc==9:
            return u'\u0009'
        if uc==10:
            return u'\u000A'
        if uc==11:
            return u'\u000B'
        if uc==12:
            return u'\u000C'
        if uc==13:
            return u'\u000D'
        if uc==14:
            return u'\u000E'
        if uc==15:
            return u'\u000F'
        if uc==16:
            return u'\u0010'
        if uc==17:
            return u'\u0011'
        if uc==18:
            return u'\u0012'
        if uc==19:
            return u'\u0013'
        if uc==20:
            return u'\u0014'
        if uc==21:
            return u'\u0015'
        if uc==22:
            return u'\u0016'
        if uc==23:
            return u'\u0017'
        if uc==24:
            return u'\u0018'
        if uc==25:
            return u'\u0019'
        if uc==26:
            return u'\u001A'
        if uc==27:
            return u'\u001B'
        if uc==28:
            return u'\u001C'
        if uc==29:
            return u'\u001D'
        if uc==30:
            return u'\u001E'
        if uc==31:
            return u'\u001F'
        if uc==32:
            return u'\u0020'
        if uc==33:
            return u'\u0021'
        if uc==34:
            return u'\u0022'
        if uc==35:
            return u'\u0023'
        if uc==36:
            return u'\u0024'
        if uc==37:
            return u'\u0025'
        if uc==38:
            return u'\u0026'
        if uc==39:
            return u'\u0027'
        if uc==40:
            return u'\u0028'
        if uc==41:
            return u'\u0029'
        if uc==42:
            return u'\u002A'
        if uc==43:
            return u'\u002B'
        if uc==44:
            return u'\u002C'
        if uc==45:
            return u'\u002D'
        if uc==46:
            return u'\u002E'
        if uc==47:
            return u'\u002F'
        if uc==48:
            return u'\u0030'
        if uc==49:
            return u'\u0031'
        if uc==50:
            return u'\u0032'
        if uc==51:
            return u'\u0033'
        if uc==52:
            return u'\u0034'
        if uc==53:
            return u'\u0035'
        if uc==54:
            return u'\u0036'
        if uc==55:
            return u'\u0037'
        if uc==56:
            return u'\u0038'
        if uc==57:
            return u'\u0039'
        if uc==58:
            return u'\u003A'
        if uc==59:
            return u'\u003B'
        if uc==60:
            return u'\u003C'
        if uc==61:
            return u'\u003D'
        if uc==62:
            return u'\u003E'
        if uc==63:
            return u'\u003F'
        if uc==64:
            return u'\u0040'
        if uc==65:
            return u'\u0041'
        if uc==66:
            return u'\u0042'
        if uc==67:
            return u'\u0043'
        if uc==68:
            return u'\u0044'
        if uc==69:
            return u'\u0045'
        if uc==70:
            return u'\u0046'
        if uc==71:
            return u'\u0047'
        if uc==72:
            return u'\u0048'
        if uc==73:
            return u'\u0049'
        if uc==74:
            return u'\u004A'
        if uc==75:
            return u'\u004B'
        if uc==76:
            return u'\u004C'
        if uc==77:
            return u'\u004D'
        if uc==78:
            return u'\u004E'
        if uc==79:
            return u'\u004F'
        if uc==80:
            return u'\u0050'
        if uc==81:
            return u'\u0051'
        if uc==82:
            return u'\u0052'
        if uc==83:
            return u'\u0053'
        if uc==84:
            return u'\u0054'
        if uc==85:
            return u'\u0055'
        if uc==86:
            return u'\u0056'
        if uc==87:
            return u'\u0057'
        if uc==88:
            return u'\u0058'
        if uc==89:
            return u'\u0059'
        if uc==90:
            return u'\u005A'
        if uc==91:
            return u'\u005B'
        if uc==92:
            return u'\u005C'
        if uc==93:
            return u'\u005D'
        if uc==94:
            return u'\u005E'
        if uc==95:
            return u'\u005F'
        if uc==96:
            return u'\u0060'
        if uc==97:
            return u'\u0061'
        if uc==98:
            return u'\u0062'
        if uc==99:
            return u'\u0063'
        if uc==100:
            return u'\u0064'
        if uc==101:
            return u'\u0065'
        if uc==102:
            return u'\u0066'
        if uc==103:
            return u'\u0067'
        if uc==104:
            return u'\u0068'
        if uc==105:
            return u'\u0069'
        if uc==106:
            return u'\u006A'
        if uc==107:
            return u'\u006B'
        if uc==108:
            return u'\u006C'
        if uc==109:
            return u'\u006D'
        if uc==110:
            return u'\u006E'
        if uc==111:
            return u'\u006F'
        if uc==112:
            return u'\u0070'
        if uc==113:
            return u'\u0071'
        if uc==114:
            return u'\u0072'
        if uc==115:
            return u'\u0073'
        if uc==116:
            return u'\u0074'
        if uc==117:
            return u'\u0075'
        if uc==118:
            return u'\u0076'
        if uc==119:
            return u'\u0077'
        if uc==120:
            return u'\u0078'
        if uc==121:
            return u'\u0079'
        if uc==122:
            return u'\u007A'
        if uc==123:
            return u'\u007B'
        if uc==124:
            return u'\u007C'
        if uc==125:
            return u'\u007D'
        if uc==126:
            return u'\u007E'
        if uc==127:
            return u'\u007F'
        if uc==128:
            return u'\u0080'
        if uc==129:
            return u'\u0081'
        if uc==130:
            return u'\u0082'
        if uc==131:
            return u'\u0083'
        if uc==132:
            return u'\u0084'
        if uc==133:
            return u'\u0085'
        if uc==134:
            return u'\u0086'
        if uc==135:
            return u'\u0087'
        if uc==136:
            return u'\u0088'
        if uc==137:
            return u'\u0089'
        if uc==138:
            return u'\u008A'
        if uc==139:
            return u'\u008B'
        if uc==140:
            return u'\u008C'
        if uc==141:
            return u'\u008D'
        if uc==142:
            return u'\u008E'
        if uc==143:
            return u'\u008F'
        if uc==144:
            return u'\u0090'
        if uc==145:
            return u'\u0091'
        if uc==146:
            return u'\u0092'
        if uc==147:
            return u'\u0093'
        if uc==148:
            return u'\u0094'
        if uc==149:
            return u'\u0095'
        if uc==150:
            return u'\u0096'
        if uc==151:
            return u'\u0097'
        if uc==152:
            return u'\u0098'
        if uc==153:
            return u'\u0099'
        if uc==154:
            return u'\u009A'
        if uc==155:
            return u'\u009B'
        if uc==156:
            return u'\u009C'
        if uc==157:
            return u'\u009D'
        if uc==158:
            return u'\u009E'
        if uc==159:
            return u'\u009F'
        if uc==160:
            return u'\u00A0'
        if uc==161:
            return u'\u00A1'
        if uc==162:
            return u'\u00A2'
        if uc==163:
            return u'\u00A3'
        if uc==164:
            return u'\u00A4'
        if uc==165:
            return u'\u00A5'
        if uc==166:
            return u'\u00A6'
        if uc==167:
            return u'\u00A7'
        if uc==168:
            return u'\u00A8'
        if uc==169:
            return u'\u00A9'
        if uc==170:
            return u'\u00AA'
        if uc==171:
            return u'\u00AB'
        if uc==172:
            return u'\u00AC'
        if uc==173:
            return u'\u00AD'
        if uc==174:
            return u'\u00AE'
        if uc==175:
            return u'\u00AF'
        if uc==176:
            return u'\u00B0'
        if uc==177:
            return u'\u00B1'
        if uc==178:
            return u'\u00B2'
        if uc==179:
            return u'\u00B3'
        if uc==180:
            return u'\u00B4'
        if uc==181:
            return u'\u00B5'
        if uc==182:
            return u'\u00B6'
        if uc==183:
            return u'\u00B7'
        if uc==184:
            return u'\u00B8'
        if uc==185:
            return u'\u00B9'
        if uc==186:
            return u'\u00BA'
        if uc==187:
            return u'\u00BB'
        if uc==188:
            return u'\u00BC'
        if uc==189:
            return u'\u00BD'
        if uc==190:
            return u'\u00BE'
        if uc==191:
            return u'\u00BF'
        if uc==192:
            return u'\u00C0'
        if uc==193:
            return u'\u00C1'
        if uc==194:
            return u'\u00C2'
        if uc==195:
            return u'\u00C3'
        if uc==196:
            return u'\u00C4'
        if uc==197:
            return u'\u00C5'
        if uc==198:
            return u'\u00C6'
        if uc==199:
            return u'\u00C7'
        if uc==200:
            return u'\u00C8'
        if uc==201:
            return u'\u00C9'
        if uc==202:
            return u'\u00CA'
        if uc==203:
            return u'\u00CB'
        if uc==204:
            return u'\u00CC'
        if uc==205:
            return u'\u00CD'
        if uc==206:
            return u'\u00CE'
        if uc==207:
            return u'\u00CF'
        if uc==208:
            return u'\u00D0'
        if uc==209:
            return u'\u00D1'
        if uc==210:
            return u'\u00D2'
        if uc==211:
            return u'\u00D3'
        if uc==212:
            return u'\u00D4'
        if uc==213:
            return u'\u00D5'
        if uc==214:
            return u'\u00D6'
        if uc==215:
            return u'\u00D7'
        if uc==216:
            return u'\u00D8'
        if uc==217:
            return u'\u00D9'
        if uc==218:
            return u'\u00DA'
        if uc==219:
            return u'\u00DB'
        if uc==220:
            return u'\u00DC'
        if uc==221:
            return u'\u00DD'
        if uc==222:
            return u'\u00DE'
        if uc==223:
            return u'\u00DF'
        if uc==224:
            return u'\u00E0'
        if uc==225:
            return u'\u00E1'
        if uc==226:
            return u'\u00E2'
        if uc==227:
            return u'\u00E3'
        if uc==228:
            return u'\u00E4'
        if uc==229:
            return u'\u00E5'
        if uc==230:
            return u'\u00E6'
        if uc==231:
            return u'\u00E7'
        if uc==232:
            return u'\u00E8'
        if uc==233:
            return u'\u00E9'
        if uc==234:
            return u'\u00EA'
        if uc==235:
            return u'\u00EB'
        if uc==236:
            return u'\u00EC'
        if uc==237:
            return u'\u00ED'
        if uc==238:
            return u'\u00EE'
        if uc==239:
            return u'\u00EF'
        if uc==240:
            return u'\u00F0'
        if uc==241:
            return u'\u00F1'
        if uc==242:
            return u'\u00F2'
        if uc==243:
            return u'\u00F3'
        if uc==244:
            return u'\u00F4'
        if uc==245:
            return u'\u00F5'
        if uc==246:
            return u'\u00F6'
        if uc==247:
            return u'\u00F7'
        if uc==248:
            return u'\u00F8'
        if uc==249:
            return u'\u00F9'
        if uc==250:
            return u'\u00FA'
        if uc==251:
            return u'\u00FB'
        if uc==252:
            return u'\u00FC'
        if uc==253:
            return u'\u00FD'
        if uc==254:
            return u'\u00FE'
        if uc==255:
            return u'\u00FF'

    while len(inp)>0:
        
        
        
        add=0
        sub=0
        ucFloat=0
        quotes=""
        intVar=""
        strVar=""
        floatVar=""
        delay=""
        
        
        
        if newStr is not 7:
            while checkStr[newStr] is not False and newStr is not 8:
                newStr=newStr+1
            if newStr==8:
                strFin=1
        else:
            if checkStr[newStr] is not False:
                strFin=1
        
        if newFloat is not 7:
            while checkFloat[newFloat] is not False and newFloat is not 8:
                newFloat=newFloat+1
            if newFloat==8:
                floatFin=1
        else:
            if checkStr[newStr] is not False:
                strFin=1
        
        if newBool is not 7:
            while checkBool[newBool] is not False and newBool is not 8:
                newBool=newBool+1
            if newBool==8:
                boolFin=1
        else:
            if checkBool[newBool] is not False:
                boolFin=1
        
        if newInt is not 7:
            while checkInt[newInt] is not False and newInt is not 8:
                newInt=newInt+1
            if newInt==8:
                intFin=1
        else:
            if checkInt[newInt] is not False:
                intFin=1
        
        
        
        if inp.startswith("int"):
            inp=inp[3:]
            if inp[0]=="n":
                lastInt=newInt
                if intFin==1:
                    sys.exit("\n[8var] ERROR: Out of empty variables of type int.")
                if newInt<=7:
                    inp=inp[1:]
                    intVar=""
                    if inp[0]=="-":
                        sub=1
                        inp=inp[1:]
                    elif inp[0]=="+":
                        inp=inp[1:]
                    while inp[0] in "0123456789":
                        intVar=intVar+inp[0]
                        inp=inp[1:]
                    if intVar is not '':
                        if sub==1:
                            intVar="-"+intVar
                            sub=0
                        varInt[newInt]=int(intVar)
                        checkInt[newInt]=True
                    intVar=""
                else:
                    sys.exit("\n[8var] ERROR: Out of empty variables of type int.")
            elif inp[0] in ("01234567l"):
                if inp[0]=="l":
                    curInt=lastInt
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
                    if intVar is not '':
                        if add==1:
                            varInt[curInt]=varInt[curInt]+int(intVar)
                            add=0
                        elif sub==1:
                            varInt[curInt]=varInt[curInt]-int(intVar)
                            sub=0
                        else:
                            varInt[curInt]=int(intVar)
                        checkInt[curInt]=True
                    intVar=""
                else:
                    sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            continue
            
            
            
        elif inp.startswith("bool"):
            inp=inp[4:]
            if inp[0]=="n":
                lastBool=newBool
                if boolFin==1:
                    sys.exit("\n[8var] ERROR: Out of empty variables of type bool.")
                if newBool<=7:
                    inp=inp[1:]
                    if inp[0] in "1t0f+-":
                        if inp[0] in "1t+":
                            varBool[newBool]=True
                        if inp[0] in "0f-":
                            varBool[newBool]=False
                        checkBool[newBool]=True
                        inp=inp[1:]
                else:
                    sys.exit("\n[8var] ERROR: Out of empty variables of type bool.")    
            elif inp[0] in "01234567l":
                if inp[0]=="l":
                    curBool=lastBool
                else:
                    curBool=int(inp[0])
                inp=inp[1:]
                if inp[0] in "1t0f+-":
                    if inp[0] in "1t+":
                        varBool[curBool]=True
                    if inp[0] in "0f-":
                        varBool[curBool]=False
                    checkBool[curBool]=True
                    inp=inp[1:]
            else:
                sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            continue
        
        
        
        elif inp.startswith("str"):
            inp=inp[3:]
            if inp[0]=="n":
                lastStr=newStr
                if strFin==1:
                    sys.exit("\n[8var] ERROR: Out of variables of type str.")
                if newStr<=7:
                    inp=inp[1:]
                    strVar=""
                    while inp[0] is not "'" and inp[0] is not '"':
                        inp=inp[1:]
                    if inp[0]=="'":
                        quotes="s"
                    if inp[0]=='"':
                        quotes="d"
                    inp=inp[1:]
                    if quotes=="s":
                        while inp[0] is not "'":
                            strVar=strVar+inp[0]
                            inp=inp[1:]
                    if quotes=="d":
                        while inp[0] is not '"':
                            strVar=strVar+inp[0]
                            inp=inp[1:]
                    inp=inp[1:]
                    quotes=""
                    varStr[newStr]=strVar
                    checkStr[newStr]=True
                    strVar=""    
                else:
                    sys.exit("\n[8var] ERROR: Out of variables of type str.")    
            if inp[0] in "01234567l":
                if inp[0]=="l":
                    curStr=lastStr
                else:
                    curStr=int(inp[0])
                inp=inp[1:]
                strVar=""
                if inp[0]=="+":
                    add=1
                    inp=inp[1:]    
                while inp[0] is not "'" and inp[0] is not '"':
                    inp=inp[1:]
                if inp[0]=="'":
                    quotes="s"
                if inp[0]=='"':
                    quotes="d"
                inp=inp[1:]
                while inp[0] is not "'" and inp[0] is not '"':
                    strVar=strVar+inp[0]
                    inp=inp[1:]
                inp=inp[1:]
                if add==1:
                    varStr[curStr]=varStr[curStr]+strVar
                    add=0
                else:
                    varStr[curStr]=strVar
                checkStr[curStr]=True
                strVar=""    
                continue    
                
                
                
        elif inp.startswith("float"):
            inp=inp[5:]
            if inp[0]=="n":
                lastFloat=newFloat
                if floatFin==1:
                    sys.exit("\n[8var] ERROR: Out of variables of type float.")
                if newFloat<=7:
                    inp=inp[1:]
                    floatVar=""
                    if inp[0]=="+":
                        inp=inp[1:]
                    if inp[0]=="-":
                        sub=1
                        inp=inp[1:]
                    while inp[0] in "0123456789.":
                        floatVar=floatVar+inp[0]
                        inp=inp[1:]
                    if floatVar is not '':
                        if sub==1:
                            floatVar="-"+floatVar
                            sub=0
                        varFloat[newFloat]=float(floatVar)
                        checkFloat[newFloat]=True
                    floatVar=""
            if inp[0] in "01234567l":
                if inp[0]=="l":
                    curFloat=lastFloat
                else:
                    curFloat=int(inp[0])
                inp=inp[1:]
                if inp[0]=="+":
                    add=1
                    inp=inp[1:]
                if inp[0]=="-":
                    sub=1
                    inp=inp[1:]
                while inp[0] in "0123456789.":
                    floatVar=floatVar+inp[0]
                    inp=inp[1:]
                if floatVar is not '':
                    if sub==1:
                        varFloat[curFloat]=varFloat[curFloat]-float(floatVar)
                        sub=0
                    elif add==1:
                        varFloat[curFloat]=varFloat[curFloat]+float(floatVar)
                        add=1
                    else:
                        varFloat[curFloat]=float(floatVar)
                    checkFloat[curFloat]=True
                    floatVar=""    
            continue
                
            
        
        elif inp.startswith("flt"):
            inp=inp[3:]
            inp="float"+inp
            continue
        
        
            
        elif inp.startswith("dly"):    
            inp=inp[3:]
            while inp[0] in "0123456789.":
                delay=delay+inp[0]
                inp=inp[1:]
            time.sleep(float(delay))
            sys.stdout.write("\n")
            delay=""
            continue
        
            
        

        
        
            
        elif inp.startswith("out"):
            inp=inp[3:]
            if inp[0]=="'":
                inp=inp[1:]
                while inp[0] is not "'":
                    sys.stdout.write(inp[0])
                    inp=inp[1:]
                inp=inp[1:]
            elif inp[0]=='"':
                inp=inp[1:]
                while inp[0] is not '"':
                    sys.stdout.write(inp[0])
                    inp=inp[1:]
                inp=inp[1:]
            elif inp.startswith("int"):
                inp=inp[3:]
                if inp[0] in "01234567l":
                    if inp[0]=="l":
                        sys.stdout.write(str(varInt[int(lastInt)]))
                    else:
                        sys.stdout.write(str(varInt[int(inp[0])]))
                    inp=inp[1:]
                else:
                    sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            elif inp.startswith("float"):
                inp=inp[5:]
                if inp[0] in "01234567l":
                    if inp[0]=="l":
                        sys.stdout.write(str(varFloat[int(lastFloat)]))
                    else:
                        sys.stdout.write(str(varFloat[int(inp[0])]))
                    inp=inp[1:]
                else:
                    sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            elif inp.startswith("flt"):
                inp=inp[3:]
                if inp[0] in "01234567l":
                    if inp[0]=="l":
                        sys.stdout.write(str(varFloat[int(lastFloat)]))
                    else:
                        sys.stdout.write(str(varFloat[int(inp[0])]))
                    inp=inp[1:]
                else:
                    sys.exit("\n: Variable doesn't exist.")
            elif inp.startswith("str"):
                inp=inp[3:]
                if inp[0] in "01234567l":
                    if inp[0]=="l":
                        sys.stdout.write(str(varStr[int(lastStr)]))
                    else:
                        sys.stdout.write(str(varStr[int(inp[0])]))
                    inp=inp[1:]
                else:
                    sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            elif inp.startswith("bool"):
                inp=inp[4:]
                if inp[0] in "01234567l":
                    if inp[0]=="l":
                        sys.stdout.write(str(varBool[int(lastBool)]))
                    else:
                        sys.stdout.write(str(varBool[int(inp[0])]))
                    inp=inp[1:]
                else:
                    sys.exit("\n[8var] ERROR: Variable doesn't exist.")
            elif inp[0] in "0123456789":
                while inp[0] in "0123456789.":
                    sys.stdout.write(inp[0])
                    inp=inp[1:]
            elif inp.startswith("ln"):
                inp=inp[2:]
                outLines=""
                if inp[0] in "0123456789":
                    while inp[0] in "0123456789":
                        outLines=outLines+inp[0]
                        inp=inp[1:]
                else:
                    outLines="1"  
                outLinesInt=int(outLines)
                outLines=""
                while outLinesInt>0:
                    sys.stdout.write("\n")
                    outLinesInt=outLinesInt-1
                outLinesInt=0    
            continue
            
        
        
        elif inp.startswith("uout"):
            inp=inp[4:]
            if inp[0] in "0123456789":
                while inp[0] in "0123456789":
                    ucode=ucode+inp[0]
                    inp=inp[1:]
            elif inp.startswith("int"):
                inp=inp[3:]
                if inp[0] in "01234567":
                    ucode=varInt[int(inp[0])]
                    inp=inp[1:]
                elif inp[0]=="l":
                    ucode=varInt[lastInt]
                    inp=inp[1:]
            elif inp.startswith("fl"):
                inp=inp[2:]
                if inp.startswith("oat"):
                    ucFloat=1
                    inp=inp[3:]
                elif inp[0]=="t":
                    ucFloat=1
                    inp=inp[1:]
                if ucFloat==1:
                    ucFloat=0
                    if inp[0] in "01234567":
                        ucode=varFloat[int(inp[0])]
                        inp=inp[1:]
                    elif inp[0]=="l":
                        ucode=varInt[lastInt]
                        inp=inp[1:]
            ucodeInt=int(ucode)
            ucode=""
            sys.stdout.write(uc(ucodeInt))
            ucodeInt=0
            continue
            
            
            
        # if inp.startswith("inp"):
        #     inp=inp[3:]
        #     if inp.startswith(""):
        
            
        
        elif inp.startswith("fin"):
            inp=inp[3:]
            sys.stdout.write("\n")                      
            # print varInt
            # print varBool
            # print varStr
            # print varFloat
            sys.stdout.flush()
            sys.exit(0)   
            continue 
            
            
            
        elif inp.startswith("8v"):
            inp=inp[3:]
            while inp[0:2] not "v.":
                version=version+inp[0]
                inp=inp[1:]
            inp=inp[2:]
            if version.lower() not in requests.get("")
            continue
            
            
        else:
            inp=inp[1:]
            continue
