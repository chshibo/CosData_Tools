import math

class MathCalculator(object):
    def __init__(self):
        pass;
  #this method calculate the RMS based on set
    def rootMeanSquarecalculate(self,datatype,set):
        mean=0.0
        total=0.0
        count=len(set)
        sumForCalculateRms = 0.0
        RMS=0.0

        for object in set:
            total+=object.__getattribute__(datatype)
        mean=total/count
        for object in set:
            sumForCalculateRms+=math.pow((object.__getattribute__(datatype)-mean),2)

        RMS=math.sqrt(sumForCalculateRms/(count-1))

        return RMS

