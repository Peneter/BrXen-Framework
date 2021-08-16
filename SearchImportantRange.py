from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import netaddr
import time
import os
def unique(t):
    print "\n  Removing duplicated lines ........ \n"
    prev = None
    for line in sorted(open(t)):
        line = line.strip()
        if prev is not None and not line.startswith(prev):
            I=open("CIDR_Of_%s.txt"%q,"a")
            I.write(prev+'\n')
        prev = line
    if prev is not None:
        I=open("CIDR_Of_%s.txt"%q,"a")
        I.write(prev+'\n')
        
def ConToNetRange(tt):
    print "\n  Converting CIDR To NetRange ........ \n"
    for line in open(tt):
        ip=netaddr.IPNetwork(line)
        I=open("Range_Of_%s.txt"%q,"a")
        I.write('%s-%s'%(ip.network,ip.broadcast)+'\n')
def GetRange(flag):
    print "\n  Geting Range ........ \n"
    i=0
    time.sleep(5)
    for x in driver.find_elements_by_tag_name("a"):
        i=i+1
        li=x.get_attribute('href')
        if i > 20:
            try:
                if ":" not in (x.get_attribute('href').split('/net/')[1]):
                    I=open("Range_%s.txt"%q,"a")
                    I.write(x.get_attribute('href').split('/net/')[1]+'\n')
            except:
                if flag==0 and 'A' in li:
                    I=open("ASN_%s.txt"%q,"a")
                    I.write(x.get_attribute('href')+'\n')
                    I.close()
    
q=raw_input("Please Enter your KeyWord : ")
driver = webdriver.Firefox()
driver.get("http://bgp.he.net")
elem = driver.find_element_by_name("search[search]")
elem.send_keys(q + Keys.RETURN)
GetRange(0)
if os.path.isfile("ASN_%s.txt"%q):
    asl = sum(1 for line in open("ASN_%s.txt"%q))
    print "  Calculating ASN [%d]........ \n"%asl
    time.sleep(1)
    ASlist=open("ASN_%s.txt"%q,"r")
    s=0
    for br in ASlist:
        s=s+1
        print " ---------- %d --------- "%s
        driver.get(br+"#_prefixes")
        GetRange(1)
    ASlist.close()
    os.remove("ASN_%s.txt"%q)
if os.path.isfile("Range_%s.txt"%q):
    unique("Range_%s.txt"%q)
    ConToNetRange("CIDR_Of_%s.txt"%q)
    os.remove("Range_%s.txt"%q)
    os.remove("CIDR_Of_%s.txt"%q)
    nl = sum(1 for line in open("Range_Of_%s.txt"%q))
    print "#  Get %d Net Range For %s \n "%(nl,q)
else:
    print "#  Not Found Any Range ... ;( "
driver.close()
