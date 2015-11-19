# serialize and de-serialize. We call this behavior pickle and de-pickle.
import pickle

# Serialized object into memory
aList = ['hello', 'this', 'is', 'python', 'code']
serializedList = pickle.dumps(aList)
print('Serialized object: '.format(serializedList))

deserializedList = pickle.loads(serializedList)
print('Deserialized object: %s', deserializedList)


# Serialized object into file
bList = ['believe', 'in', 'yourself', 'never', 'give', 'up']
filea = open('object.tmp', 'wb')
pickle.dump(bList, filea)
filea.close()

# Derialized object from file
fileb = open('object.tmp', 'rb')
cList = pickle.load(fileb)
print('De-serialized from file: {0}'.format(cList))


