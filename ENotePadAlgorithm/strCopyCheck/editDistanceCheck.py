from ENotePadAlgorithm.strMetric.editDistance import *
import os


class EditDistanceCheck(object):
    def fileCheck(self, lFile, rFile):
        results = 0
        if os.path.exists(lFile) and os.path.exists(rFile):
            with open(lFile, 'r',encoding='utf-8') as lFin:
                with open(rFile, 'r',encoding='utf-8') as rFin:
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine and rLine:
                    results += getEditDistance(lLine, rLine)
                    lLine = lFin.readline()
                    rLine = rFin.readline()
                while lLine:
                    results += getEditDistance(lLine, '')
                    lLine = lFin.readline()
                while rLine:
                    results += getEditDistance('', rLine)
                    rLine = rFin.readline()
        else:
            print('%s or %s does not exited, please check whether the file path is correct' % lFile, rFile)
        return results
