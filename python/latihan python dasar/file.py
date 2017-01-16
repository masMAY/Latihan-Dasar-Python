#file operation

try:
    example_file = open("test.txt",'w')

    print "File Name :", example_file.name
    print "File Mode :", example_file.mode
    print "Has it closed?", example_file.closed

    example_file.close()
    print "Has it closed?", example_file.closed
except IOError, e:
    print "Failed process because of :", e


#writing content file
try:
    example_file = open("test.txt",'w')

    print "File Name :", example_file.name
    print "File Mode :", example_file.mode
    print "Has it closed?", example_file.closed

    example_file.write("1. Muhamad Arief Yulianto,Teknik Informatika, Unpam\n")
    example_file.write("2. masMAY,Teknik Informatika, UI\n")
    example_file.write("3. masMAY24,Teknik Informatika, OHIO\n  ")
    example_file.close()
    print "Has it closed?", example_file.closed
except IOError, e:
    print "Failed process because of :", e

#Read content file
try:
    example_file = open("test.txt",'r')

    print "File Name :", example_file.name
    print "File Mode :", example_file.mode
    print "Has it closed?", example_file.closed

    print "File content :\n",example_file.read()
    print "Pointer position :", example_file.tell()

    example_file.close()
    print "Has it closed?", example_file.closed
except IOError, e:
    print "Failed process because of :", e

#Read content file per line
try:
    example_file = open("test.txt",'r')

    print "File Name :", example_file.name
    print "File Mode :", example_file.mode
    print "Has it closed?", example_file.closed

    print "File content :\n"

    for line in example_file:
        print line

    print "Pointer position :", example_file.tell()

    example_file.close()
    print "Has it closed?", example_file.closed
except IOError, e:
    print "Failed process because of :", e

#Setting pointer position file --> seek(+/-,0/1/2)
#note : + = determine distance to right side or reverse --> reading file per charachter
#note : 0 = pointer will be in the beginning file, 1 : in the current position pointer, 2: pointer will be in the end file
try:
    example_file = open("test.txt",'r')

    print "File Name :", example_file.name
    print "File Mode :", example_file.mode
    print "Has it closed?", example_file.closed

    print "File content :\n"

    for line in example_file:
        print line

    print "Pointer position :", example_file.tell()
    print "Pointer back to the begining position",example_file.seek(-100,1)

    print "File content :\n"

    for line in example_file:
        print line

    print "Pointer position :", example_file.tell()

    example_file.close()
    print "Has it closed?", example_file.closed
except IOError, e:
    print "Failed process because of :", e


#Changing File Name --> should be import module os --> this modul can hanndle (rename,move,delete file)
import os

try:
    os.rename('test.txt','ujicoba.txt')
    print "File name has been changed"
except (IOError,OSError),e:
    print "Error Operation because of", e

#delete file
try:
    os.remove('ujicoba.txt')
    print "File has been deleted"
except(IOError,OSError),e:
    print "Error Operation because of", e


