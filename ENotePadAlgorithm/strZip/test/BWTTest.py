from ENotePadAlgorithm.strZip.BWT import *

if __name__ == '__main__':
    bwt = BWT(input('Enter sequence: '))
    print('Burrows-Wheeler Transform: ' + str(bwt))

    inverse = inverse_BWT(bwt)
    print('Inverse Burrows-Wheeler Transform: ' + str(inverse))