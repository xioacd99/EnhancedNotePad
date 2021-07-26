from ENotePadAlgorithm.strFind.SBOM import *

if __name__ == '__main__':
    start(['announce'], ['announce', 'announ', 'announce123', '123announce', 'announceannounce',
                         'announce123announc456nnounce789announce123announce'])
    start(['ab', 'bab', 'bca', 'caa'], ['abccab'])
    start(['aa'], ['aaaaaaaaa'])