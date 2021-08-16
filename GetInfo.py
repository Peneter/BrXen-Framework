import cymruwhois
from cymruwhois import Client

def GetInfo(IP,N):
    try:
        c=Client()
        r=c.lookup(IP)
        print IP+"\t"+r.cc+"\t"+r.owner
        I=open('Info_%s.txt'%N,"a")
        I.write(IP+"\t"+r.cc+"\t"+r.owner+'\n')
    except:
        print IP+"\tUnknown\tUnknown"

IpList=raw_input("Enter IP List Path : ")
n=IpList.split('.')[0]
print "IP Address\tCountry\t\t\tOwner"
print "--------------\t-------\t-------------------------------------"
for line in open(IpList):
    line=line.strip()
    GetInfo(line,n)
