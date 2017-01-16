print "while loop "

i = 1
total_numbers = 0

while i <= 10:
    print 'loop at %d : %d + %d' %(i,total_numbers,i)
    total_numbers = total_numbers + i
    i+=1

print "total numbert that we have calculated is", total_numbers