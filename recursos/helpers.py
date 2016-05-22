# -*- coding: cp1252 -*-
# Coding para windows cp1252
#============================================================================#
# helpers.py, este archivo se utiliza para exportar funciones que recaban# 
# infomacion general de la maquina objetivo                                  #
# @HB.                                                                       #
#============================================================================#
import wmi

#Funcion Version de Bios
def BiosVersion(machine):
	for version in machine.Win32_BIOS():
		BiosVersion = version.BiosVersion
		return BiosVersion
	
def SerialNumber(machine):
        """ Obtener número de serie """
        for Serial in machine.Win32_BIOS():
                Serie = Serial.serialnumber
                return Serie

#========================================================#
#========================================================#
# Seccion Clase Win32_Processor				 #
#========================================================#
#========================================================#		
		
#Funcion Nombre de Procesador 
def Nom_proc(machine):
        dataProcessor = []
	for data in machine.Win32_Processor():
		dataProcessor.append(data.Name)
		dataProcessor.append(data.Status)
		dataProcessor.append(data.CurrentClockSpeed) #Actual velocidad del reloj
		dataProcessor.append(data.MaxClockSpeed)# Maxima velocidad del reloj
		dataProcessor.append(data.Family)
		dataProcessor.append(data.L2CacheSize)
		dataProcessor.append(data.L3CacheSize)
		return dataProcessor
		
		
#========================================================#
#========================================================#
# Seccion Clase Win32_ComputerSystem()			 #
#========================================================#
#========================================================#	

#Memoria Ram se transforma a formato MB para realizar 	
def memoriaram(machine):
	for memory in machine.Win32_ComputerSystem():
		MemoriaRam = int(memory.TotalPhysicalMemory)/1048576.0
		return int(MemoriaRam)

# Definimos marca de la maquina

def marca(machine):
	for marca in machine.Win32_ComputerSystem():
		Marca = marca.Manufacturer
		return str(Marca)

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
                
                
