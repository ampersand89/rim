#!/usr/bin/env python
# 
#============================================================================#
# helpers.py, este archivo se utiliza para exportar funciones que recaban# 
# infomacion general de la maquina objetivo                                  #
# @HB.                                                                       #
#============================================================================#
import wmi


#========================================================#
#========================================================#
# Seccion Clase Win32_PWin32_CDROMDrive                  #
#========================================================#
#========================================================#

def cd(machine):
    cds = []
    for cd in machine.Win32_CDROMDrive():
        cds.append(cd.Caption)
        return cds
#========================================================#
#========================================================#
# Seccion Clase Win32_BIOS                               #
#========================================================#
#========================================================#

#Funcion Version de Bios
def BiosVersion(machine):
    BiosVersion = ""
    algo = ""
    for version in machine.Win32_BIOS():
        bv = version.BiosVersion
    for x in range(0, len(bv)):
        BiosVersion+=algo.join(bv[x])
    return str(BiosVersion)
    
def SerialNumber(machine):
    """ Obtener numero de serie """
    for Serial in machine.Win32_BIOS():
        Serie = Serial.serialnumber
        return Serie
    
def Bios(machine):
    dataBios = []
    for B in machine.Win32_BIOS():
        dataBios.append(B.Name)
        dataBios.append(B.BiosCharacteristics) #create dict
        dataBios.append(B.Manufacturer)
        return dataBios
        
        
        

#========================================================#
#========================================================#
# Seccion Clase Win32_Processor              #
#========================================================#
#========================================================#      
        
#Funcion Nombre de Procesador 
def Nom_proc(machine):
        dataProcessor = []
        for data in machine.Win32_Processor():
                dataProcessor.append(data.Name) # [0]                     
                dataProcessor.append(data.Status) # [1]
                dataProcessor.append(data.CurrentClockSpeed)  # [2] Actual velocidad del reloj
                dataProcessor.append(data.MaxClockSpeed)# [3] Maxima velocidad del reloj
                dataProcessor.append(data.Family) # [4]
                dataProcessor.append(data.L2CacheSize) # [5]
                dataProcessor.append(data.L3CacheSize) # [6]
                # Seleccion arquitectura [7]
                if data.Architecture == 0:
                        dataProcessor.append('x86')
                elif data.Architecture == 1:
                        dataProcessor.append('MIPS')
                elif data.Architecture == 2:
                        dataProcessor.append('Alpha')
                elif data.Architecture == 3:
                        dataProcessor.append('PowerPC')
                elif data.Architecture == 5:
                        dataProcessor.append('ARM')
                elif data.Architecture == 6:
                        dataProcessor.append('Itanium-based systems')
                elif data.Architecture == 9:
                        dataProcessor.append('x64')
                else:
                        dataProcessor.append('Unknown')

                dataProcessor.append(data.Manufacturer) # [8] Fabricante
                dataProcessor.append(data.NumberOfCores) # [9] Numero de Cores
                dataProcessor.append(data.NumberOfLogicalProcessors)#[10] Procesadores Logicos
                return dataProcessor # retorna una lista 
        
        
#========================================================#
#========================================================#
# Seccion Clase Win32_ComputerSystem()           #
#========================================================#
#========================================================#  

#Memoria Ram se transforma a formato MB para realizar   
def memoriaram(machine):
    for memory in machine.Win32_ComputerSystem():
        MemoriaRam = int(memory.TotalPhysicalMemory)/1048576.0
        return int(MemoriaRam) #FREE

# Definimos marca de la maquina


def marca(machine):
    for marca in machine.Win32_ComputerSystem():
        Marca = marca.Manufacturer
        return Marca

# Definimos modelo de la maquina
def modelo(machine):
    for modelo in machine.Win32_ComputerSystem():
        Model = modelo.Model
        return Model

# Nombre de maquina

def NameMachine(machine):
    for nombre in machine.Win32_ComputerSystem():
        NameMachine = nombre.Name
        return NameMachine
# usuario
def DomainAndUsername(machine):
    for u in machine.Win32_ComputerSystem():
        user = u.username
        return user

#========================================================#
#========================================================#
# Seccion Clase Win32_OperatingSystem()                  #
#========================================================#
#========================================================#

#Sistema Operativo
def so(machine):
    for version in machine.Win32_OperatingSystem():
        so = version.Caption
        OSA = version.OSArchitecture
        ver = version.Version
        SistemaOperativo = so + " " + OSA + " " + ver 
        return SistemaOperativo


#========================================================#
#========================================================#
# Seccion Clase Win32_DiskDrive()                        #
#========================================================#
#========================================================#


#Datos de Harddisk

def harddiskdata(machine):
        harddiskinfo = []
        for datos in machine.Win32_DiskDrive():
                harddiskinfo.append(datos.Name) #[0]
                harddiskinfo.append(datos.Model)#[1]
                harddiskinfo.append(float(datos.Size)/(10.0**9))#[2]
                harddiskinfo.append(datos.SerialNumber)#[3]
                harddiskinfo.append(datos.TotalCylinders)#[4]
                harddiskinfo.append(datos.TotalHeads)#[5]
                harddiskinfo.append(datos.TotalSectors)#[6]
                harddiskinfo.append(datos.TotalTracks)#[7]
                harddiskinfo.append(datos.TracksPerCylinder)#[8]
                harddiskinfo.append(datos.Status) #Status #[9]
                harddiskinfo.append(datos.Partitions)#Numero de particiones [10]
                return harddiskinfo
                

#========================================================#
#========================================================#
# Seccion Clase Win32_Baseboard()                        #
#========================================================#
#========================================================#
                
def baseboard(machine):
    baseboard = []
    for data in machine.Win32_Baseboard():
        baseboard.append(data.Product)
        baseboard.append(data.Manufacturer)
        baseboard.append(data.Name)
        baseboard.append(data.Model)
        baseboard.append(data.Status)
        return baseboard


#========================================================#
#========================================================#
# Seccion Clase Win32_PhysicalMemory()                   #
#========================================================#
#========================================================#

def MemoriaFisica(machine):
    mfisica = []
    for data in machine.Win32_PhysicalMemory():
        mfisica.append(data.Caption) # [0]
        mfisica.append(data.Capacity) # [1]
        mfisica.append(data.DataWidth)# [2]
        mfisica.append(data.DeviceLocator) #[3]
        mfisica.append(data.FormFactor) #[4] complementa con diccionario
        mfisica.append(data.InterleavePosition)#[5]
        mfisica.append(data.Manufacturer)#[6]
        mfisica.append(data.MemoryType) # [7] complementa con diccionario
        mfisica.append(data.PartNumber) # [8]
        mfisica.append(data.PositionInRow) # [9]
        mfisica.append(data.SerialNumber)  # [10] Numero de serie correspondiente al dispositivo de memoria en SMBIOS INFORMACION
        mfisica.append(data.Speed) # [11] Nanosegundos
        mfisica.append(data.Tag) #  [12] Tag de la memoria
        mfisica.append(data.TypeDetail) # [13] ver el tipo de memoria complementa con diccionario
        return mfisica

#========================================================#
#========================================================#
# Seccion Clase Win32_PhysicalMemoryArray                #
#========================================================#
#========================================================#

def MatrizMemoriaFisica(machine):
    mafisica = []
    for data in machine.Win32_PhysicalMemoryArray():
        mafisica.append(data.MemoryDevices)
        if data.Use == 0:
            mafisica.append('Reserved')
        elif data.Use == 1:
            mafisica.append('Other')
        elif data.Use == 2:
            mafisica.append('Unknown')
        elif data.Use == 3:
            mafisica.append('System Memory')
        elif data.Use == 4:
            mafisica.append('Video Memory')
        elif data.Use == 5:
            mafisica.append('Flash Memory')
        elif data.Use == 6:
            mafisica.append('Non-volatile RAM')
        elif data.Use == 7:
            mafisica.append('Cache Memory')
        else:
            mafisica.append('')
        return mafisica 
                
#========================================================#
#========================================================#
# Seccion Clase Win32_SoftwareFeature                 #
#========================================================#
#========================================================#

def  softwareInstalado(machine):
    listaSoftware = [] 
    for software in machine.Win32_Product():
        programa = []
        programa.append(software.Name)
        programa.append(software.Version)
        programa.append(software.InstallDate)
        listaSoftware.append(programa)	
    return listaSoftware	