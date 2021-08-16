import os
def EditResults(f):
    print "  Edit Results List Of IP ............. \n"
    for x in open(f):
        if ":" in x and "COMMAND" not in x:
            I=open('FinalOpenIP.txt','a')
            I.write(x.split(':')[0]+'\n')
    print "All Operations Done ;) \n "

List=raw_input('Enter your RangeList File Path : ')
RangeList=open(List)
Tport=raw_input('Number Of Port : ')
t=raw_input('Theread : ')
for line in RangeList:
    line=line.strip()
    print "vnc.exe -i %s -p %s -cT -T %s"%(line,Tport,t)
    os.system("vnc.exe -i %s -p %s -cT -T %s"%(line,Tport,t))
    print "-"*75
EditResults("VNC_bypauth.txt")
os.remove("VNC_bypauth.txt")
