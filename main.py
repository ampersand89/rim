#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wmi
from recursos import helpers
import os
import sys
import getpass
import getopt 
import socket

def usage():
        print "Usage: rim <ip> <Arguments> <Output Arguments> \n" \
        "\n" \
        "Arguments: \n \n" \
        "-h   --help \t \t - Show this help\n" \
        "-u <username> \t - Specifies optional user name for login to remote computer.\n" \
        "-p <password> \t\t - Specifies optional password for user name. \n\n" \
        "-m <namemachine> \t - Specifies the hostname Windows\n" \
        "-i <ip address> \t - Specifies the IP Address\n" \
        "Output Arguments: \n\n" \
        "-a --all \t\t - Show all Machine Information\n" \
        "-j --hardware  \t\t - Show Hardware Information\n" \
        "-s --software  \t\t - Show Software Information\n\n" \
        "Examples:\n" \
        "rim 192.168.0.10 --all\n" \
        "rim 192.168.0.11 --hardware --software \n" \
        "rim 192.168.0.20 \n" \

def errorEnMismaMaquina():
    print '''Error: You Must Specify ip or Hostname!
RIM can be executed locally with the default credentials
Try to execute RIM without arguments
RIM has stopped!!!'''
    sys.exit(2)

def hardwareInformation(connect):
    print '''
Hardware Information Machine: %s\n
Processor:\n

Processor model\t\t= \t%s
Status\t\t\t= \t%s
Current Clock Speed\t= \t%s Mhz
Max Clock Speed\t\t= \t%s Mhz
Processor Family\t= \t%s 
Level 2 Cache Size\t= \t%s KB
Level 3 Cache Size\t= \t%s KB
Architecture\t\t= \t%s
Manufacturer\t\t= \t%s
Number Of Cores\t\t= \t%s
Logical Processor\t= \t%s

HardDisk:\n

HDD Name\t\t= \t%s
HDD Model\t\t= \t%s
HDD Size\t\t= \t%s GB
HDD Serial Number\t= \t%s
HDD Cylinders\t\t= \t%s
HDD Heads\t\t= \t%s
HDD Sectors\t\t= \t%s
HDD Tracks\t\t= \t%s
Tracks Per Cylinder\t= \t%s
HDD Partition Numbers\t= \t%s

Bios:\n

Model\t\t\t= \t%s
Version\t\t\t= \t%s
Serial Number\t\t= \t%s
Manufaturer\t\t= \t%s
Characteristics\t\t= \t%s

RAM: \n  

Capacity RAM\t\t= \t%s MB
Form Factor\t\t= \t%s
Manufacturer\t\t= \t%s
Memory Type\t\t= \t%s
Part Number\t\t= \t%s
Serial Number\t\t= \t%s
Speed\t\t\t= \t%s Nanoseconds
Tag\t\t\t= \t%s
Type Detail\t\t= \t%s
Slots\t\t\t= \t%s
Memory Use\t\t= \t%s
''' % (
        helpers.NameMachine(connect),
        helpers.Nom_proc(connect)[0],
        helpers.Nom_proc(connect)[1],
        helpers.Nom_proc(connect)[2],
        helpers.Nom_proc(connect)[3],
        helpers.Nom_proc(connect)[4],
        helpers.Nom_proc(connect)[5],
        helpers.Nom_proc(connect)[6],
        helpers.Nom_proc(connect)[7],
        helpers.Nom_proc(connect)[8],
        helpers.Nom_proc(connect)[9],
        helpers.Nom_proc(connect)[10],
        helpers.harddiskdata(connect)[0],
        helpers.harddiskdata(connect)[1],
        int(helpers.harddiskdata(connect)[2]), #Aprox
        helpers.harddiskdata(connect)[3],
        helpers.harddiskdata(connect)[4],
        helpers.harddiskdata(connect)[5],
        helpers.harddiskdata(connect)[6],
        helpers.harddiskdata(connect)[7],
        helpers.harddiskdata(connect)[8],
        helpers.harddiskdata(connect)[10],
        helpers.Bios(connect)[0],
        helpers.BiosVersion(connect),
        helpers.SerialNumber(connect),
        helpers.Bios(connect)[2],
        helpers.Bios(connect)[1],
        float(helpers.MemoriaFisica(connect)[1])/(1024*1024),
        helpers.MemoriaFisica(connect)[4],
        helpers.MemoriaFisica(connect)[6],
        helpers.MemoriaFisica(connect)[7],
        helpers.MemoriaFisica(connect)[8],
        helpers.MemoriaFisica(connect)[10],
        helpers.MemoriaFisica(connect)[11],
        helpers.MemoriaFisica(connect)[12],
        helpers.MemoriaFisica(connect)[13],
        helpers.MatrizMemoriaFisica(connect)[0],
        helpers.MatrizMemoriaFisica(connect)[1],
        
        
        )

def softwareInformation(connect):
    print "software information"
    pass

def defaultInformation(connect):
    print '''
General Information:\n
\nLogistics:\n
Machine Name\t= \t%s
Ip Address\t= \t%s
Machine Brand\t= \t%s
Machine Model\t= \t%s
Serial Number\t= \t%s
\nSummary:\n
Operating System= \t%s 
CPU\t\t= \t%s 
RAM \t\t= \t%s MB
Motherboard\t= \t%s
HardDrives \t= \t%s
Optical Drives\t= \t%s
''' % (
        helpers.NameMachine(connect), 
        resolveByHostname(helpers.NameMachine(connect)), 
        helpers.marca(connect), 
        helpers.modelo(connect), 
        helpers.SerialNumber(connect), 
        helpers.so(connect), 
        helpers.Nom_proc(connect)[0], 
        str(helpers.memoriaram(connect)), 
        helpers.baseboard(connect)[1] + " " + helpers.baseboard(connect)[0], 
        helpers.harddiskdata(connect)[1], 
        helpers.cd(connect)[0] 
        )
    sys.exit()

def allInformation(connect):
    print "mucha informacion"
    pass

def conexion(*args):

    if (len(args) == 0):
        try:
            machine = wmi.WMI()
            print "\n[*] Connected successfully..."
            print "[*] Search Information..."
            return machine
        except:
            print "[-] RIM isn't connected... \n" \
            "[!] Verify if the host is up or if credentials are valid!"
            sys.exit(2)
    else:
        try:
            machine = wmi.WMI(computer=args[0], user=args[1], password=args[2])
            print "\n[*] Connected successfully..."
            print "[*] Search Information..."
            return machine
        except:
            print "[-] RIM isn't connected... \n" \
            "[!] Verify if the host is up or if credentials are valid!"
            sys.exit(2)
            
def resolveByHostname(maquina):
    try:
        ip = socket.gethostbyname(maquina)
        return ip
    except socket.error:
        print "[-] Error: Invalid Hostname"
        sys.exit(2)
        
        
def resolveByIpAddress(ip):
    try:
        maquina = socket.gethostbyaddr(ip)[0]
        return maquina 
    except socket.error:
        print "[-] Error: Ip Address Not response to query"
        sys.exit(2)


def main():
    try:
        opts, args = getopt.getopt(
                                    sys.argv[1:], 
                                    "hajsi:u:m:p:", 
                                    [
                                        "help", 
                                        "all", 
                                        "hardware",
                                        "software",
                                        "ip=", 
                                        "user=",
                                        "machine=",
                                        "password=" ]
                                        )
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)

    if not opts:
        print ("\n[!] No Option selected...\n[+] Executing RIM in the Same Machine...")
        connect = conexion()
        defaultInformation(connect)
    

    ip = None
    user = None
    maquina = None
    password = None
    todo = False
    hw = False
    sw = False
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-m", "--machine"):
            maquina = arg
            if maquina.lower() == socket.gethostname().lower():
                print "The Hostname is the same than this Machine"
                errorEnMismaMaquina()
            else:
                pass
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-a", "--all"):
            todo = True
        elif opt in ("-j", "--hardware"):
            hw = True
        elif opt in ("-s", "--software"):
            sw = True
        else:
            assert False, "Error"
            sys.exit(2)
    
    if not ip and not maquina:
        if not user and not password:
            pass
    else:
        if not ip:
            ip = resolveByHostname(maquina)
        if not maquina:
            maquina = resolveByIpAddress(ip)
        if not user:
            user = helpers.DomainAndUsername(wmi.WMI())
            password = getpass.getpass("Enter Password for %s : " % str(user))
        if not password:
            password = getpass.getpass("Enter Password for %s : " % str(user))
        
    connect = conexion(maquina, user, password)
    if hw == True or sw == True:
        if todo == True:
                print "The option -a or --all can be executed without other output arguments"
                sys.exit(2)
        if hw == True:
                print "[*] Collecting Hardware Information..."   
                hardwareInformation(connect)
        if sw == True:
                print "[*] Collecting Software Information..."
                softwareInformation(connect)
    else:
        if todo == True:
                print "[*] Collecting Complete Information..."
                allInformation(connect)
        else:
                print "[*] Collecting General Information..."
                defaultInformation(connect)
        
        

if __name__ == "__main__":
    main()
