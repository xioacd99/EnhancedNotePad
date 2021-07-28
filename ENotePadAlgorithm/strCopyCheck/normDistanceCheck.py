from ENotePadAlgorithm.strMetric.normDistance import *
import os


class NormDistanceCheck(object):
    def __init__(self):
        pass

    def fileCheck(self, lFile, rFile):
        results = 0
        if os.path.exists(lFile) and os.path.exists(rFile):
            with open(lFile, 'r') as lFin:
                with open(rFile, 'r') as rFin:
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine and rLine:
                    results += getL2NormDistance(lLine, rLine)
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine:
                    results += getL2NormDistance(lLine, '')
                    lLine = lFin.readline()
                while rLine:
                    results += getL2NormDistance('', rLine)
                    rLine = rFin.readline()
        else:
            print('%s or %s does not exited, please check whether the file path is correct' % lFile, rFile)
        return results
