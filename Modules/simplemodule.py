# import a custom module here
import custommodule
import os
path = os.path.basename(__file__)

if __name__ == '__main__':
    print('This is the main module, and the module name is {0}'.format(path))
else:
    print('This is NOT the main module, and the module name is {0}'.format(path))

print(custommodule.add(1, 4))

