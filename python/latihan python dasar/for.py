#content of looping for it shoulb be use (',') to show the result without new line or reverse
print "For Loop use in tuple or list it still running well"

print "for loop from tuple :[1,2,3,4,5]"
for i in [1,2,3,4,5]:
	print "Loop at ", i

print "for loop from list :['a','b','c','d','e']"
for i in ('a','b','c','d','e'):
	print "Loop at ", i

print "for loop from list :'abcde'"
for i in "abcde":
	print i,
print "it will be abcde"



print "for loop from list :'a" \
	  "b" \
	  "c" \
	  "d" \
	  "e'"
for i in "abcde":
	print i
print "it will be \na\n" \
	  "b\n" \
	  "c\n" \
	  "d\n" \
	  "e"