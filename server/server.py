# -*- coding: utf-8 -*-
import socket
import os, os.path
import struct

MAX_ARRAY_SIZE = 100000
responseCounter = 0

def startSocket():
    if os.path.exists( "/tmp/sockets" ):
        os.remove( "/tmp/sockets" )
    if os.path.exists( "/tmp/socketc" ):
        os.remove( "/tmp/socketc" )
    server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
    server.bind("/tmp/sockets")
    return server

def buildResponse(code, length, buff):    
    if code == 0:
        response = struct.pack('QQ', 0, 1)
        return response
    if code == 1:
        response = struct.pack('QQ', 1, length)
        response += bytearray(length)
        return response
        

if __name__ == '__main__':
    
    receivedOffs = []
    
    server = startSocket()
    print("Listening...")
    
    while True:
        
        (data, addr) = server.recvfrom(MAX_ARRAY_SIZE)

        off = int
        length = int
        buff = ""

        if len(data) >= 8:
            off = int.from_bytes(data[:8], byteorder='little')
        if len(data) >=12:
            length = int.from_bytes(data[8:12], byteorder='little')
        if len(data) >12:
            buff = data[12:]

        print("offset:", off)
        #print("buff:", "".join("%02x" % b for b in buff)) #prints in hexadecimal
        print("paramlen:", length)
        #print("bufflen:", len(buff))
        
        response = buildResponse(0, length, buff)
        
        server.sendto(response, addr)
        responseCounter += 1
        print("Response sent. Total responses: ", responseCounter, "\n")
        
        if not off in receivedOffs:
            receivedOffs.append(off)
        
    server.close()
