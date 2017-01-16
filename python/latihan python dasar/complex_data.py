#list, tuple and dictionary

print "List definition namelist=[]"
os_list = ['Zorin OS','Ubuntu', 'FreeBSD', 'NetBSD','OpenBSD', 'Backtrack','Fedora','Slackware']

print "Tuple definition nameTuple=()"
number_tuple = (0,1,2,3,4,5,6,7,8,9)

print "Dictionary definition nameDictionary={key:value}"
identity_dictionary = {'name':'masMAY', 'prodi':'Teknik Informatika', 'email':'masMAY24@gmail.com',
                       'website':'on initial process'}

#How to access element name[] --> for all type complex data
print "Access an element"
print "-----------------------------"
print os_list[3]
print number_tuple[4]
print identity_dictionary['website']

print '\n\n'

#Access some element in list and tuple
print "Access some elements : "
print "-----------------------------"
print os_list[2:4]
print number_tuple[2:4]

#Access element with loop for --> for xxx(sebuah) in (tuple,list,dicionary)
print "Access all elements with loop for"
print "-----------------------------"

for a in os_list:
    print a
print '\n'

for b in number_tuple:
    print b
print '\n'

for c in identity_dictionary:
    print c, ':', identity_dictionary[c]


#how to change the value of complex data --> name[]="new value" **tuple is doesnt work for this function
print "Update an element"

print 'update list'
print os_list
os_list[2] = 'masMAY OS'
print os_list

print 'update dictionary'
print identity_dictionary
identity_dictionary['website'] = 'www.MM.com'
print identity_dictionary

#How to insert new data in complex data --> + new data, nameDictionary.update(newDictionary)

print 'insert new data for complex data'

print 'insert new data'
new_os_list = os_list + ['PC Linux OS', 'Blankon', 'IGOS', 'OpenSUSE']
print new_os_list

new_number_tuple = number_tuple + (100,1000,10000)
print new_number_tuple

new_identity_dictionary = {'telp': '0213456784', 'alamat':'Griya Indah Serpong'}
identity_dictionary.update(new_identity_dictionary)
print identity_dictionary

#Built in function of List, Tuple and Dictionary

#how to compare complex data --> cmp()
print "if the resulst is -1 it means data1<data2, else if the result is 0 it means data1==data2, else the result is +1 it " \
      "it means data1>data2"
print "Comparing the old data with new data complex"
print "os_list compare new_os_list", cmp(os_list, new_os_list)
print "number_tuple compare new_number_tuple", cmp(number_tuple, new_number_tuple)
print "identity_dictionary compare new_identity_dictionary", cmp(identity_dictionary, new_identity_dictionary)

#how to determine length of the tuple, list or dictionary --> len(dataname)
print "Determine length of list, tuple and dictionary"
print "number_tuple length", len(number_tuple)
print "os_list length", len(os_list)
print "identity_dictionary length", len(identity_dictionary)

#How to convert list, tuple, dictionary to be string -->str()
print "Convert list, tuple and dictionary to be string"
print str(os_list), 'charachter length is', len(str(os_list))
print str(number_tuple), 'charachter length is', len(str(number_tuple))
print str(identity_dictionary), 'character length is', len(str(identity_dictionary))

#How to determine min and max value of list, tuple and dictionary-->max/min(dataname)
print 'Determine min and max complex data'
print 'min os_list :', min(os_list)
print 'max os_list :',max(os_list)
print 'min number_tuple :', min(number_tuple)
print 'max number_tuple :',max(number_tuple)
print 'min identity_dictionary :', min(identity_dictionary)
print 'max identity_dictionary :',max(identity_dictionary)


#convert list to tuple or on the reverse
print 'Convert list to tuple'
print 'intial list', os_list
print 'convert result', tuple(os_list)

print 'Convert tuple to list'
print 'initial tuple', number_tuple
print 'convert result', list(number_tuple)


#how to delete an element in list and dictionary -->del namelist[number], del nameDictionary['key'] tuple doesnt support this function
print "Delete an elment in list"
print os_list
del os_list[2]
print os_list

print "Delete an element in Dictionary"
print identity_dictionary
del identity_dictionary['website']
print identity_dictionary

#How to delete list, tuple and dictionary --> del name
#note : if you call the list, tuple, dictionary are deleted it will show error
print "Delete tuple, list and Dictionary"
print number_tuple
del number_tuple
#print number_tuple
print os_list
del os_list
#print os_list
print identity_dictionary
del identity_dictionary
#print identity_dictionary




