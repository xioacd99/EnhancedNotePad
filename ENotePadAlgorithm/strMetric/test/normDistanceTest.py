from ENotePadAlgorithm.strMetric.normDistance import *

if __name__ == '__main__':
    a = 'hello, world'
    b = 'HELLO, WORLD'
    print(getL0NormDistance(a, b))
    print(getL1NormDistance(a, b))
    print(getL2NormDistance(a, b))
    print(getMinNormDistance(a, b))
    print(getMaxNormDistance(a, b))
