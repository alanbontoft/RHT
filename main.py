#!/usr/bin/env python
"""
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

"""
# --------------------------------------------------------------------------- #
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from os import system, name

SLAVE = 247

def clearScreen():
    
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    

def run_sync_client():

    clearScreen()

    print ("Enter 1 to take reading, 0 to quit")

    running = True

    while running == True:
        client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=1, baudrate=9600)
        client.connect()
        hr = client.read_holding_registers(7,3, unit=SLAVE)

        value = input(":")

        if value == 0:
           running = False
        else:
            temperature = hr.registers[0] / 10.0
            humidity = hr.registers[1] / 10.0
            dewpoint = hr.registers[2] / 10.0
            print("Temperature : " + str(temperature))
            print("Humidity : " + str(humidity))
            print("Dew Point : " + str(dewpoint))


    # ----------------------------------------------------------------------- #
    # close the client
    # ----------------------------------------------------------------------- #
    client.close()


if __name__ == "__main__":
    run_sync_client() 