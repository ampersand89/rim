#!/usr/bin/env python
# -*- coding: cp1252 -*-
import wmi
from recursos import helpers
import os

class Machine(object):
    def conexion(self):
        self.ip=raw_input("IP: ")
        # Se realiza la excepcion en caso de no haber conexion
        try:
            self.machine = wmi.WMI(self.ip)
        except:
            print "No fue posible realizar la conexión... \nVerifique si el host tiene conexión o si las credenciales tienen permisos para conectar"

# en cada metodo se debe utilizar self.machine para las clases wmi, que muestra una conexion establecida
    def Hardware(self):
        '''Se utiliza para recolectar datos de Hardware de la maquina'''
        self.marca = helpers.marca(self.machine) # pasamos self.machine a los helpers para generar consulta
        self.modelo = helpers.modelo(self.machine)
        self.serie = helpers.SerialNumber(self.machine)
        self.memoria_ram = helpers.memoriaram(self.machine)
        self.harddiskdata= helpers.harddiskdata(self.machine)

    def data_hardware(self):
        print self.marca
        print self.modelo
        print self.serie
        print self.memoria_ram
        print self.harddiskdata[0]

    def software(self):
        '''se utiliza para recolectar datos de Software de la maquina'''
        self.so = helpers.so(self.machine)
        self.namemachine=helpers.NameMachine(self.machine)
           
  
    def __init__(self):
        self.conexion()
        self.Hardware()
        self.data_hardware()
        


# instanciar clase
machine = Machine()





