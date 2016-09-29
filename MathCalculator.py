import math

class MathCalculator(object):
    def __init__(self):
        pass;
  #this method calculate the RMS based on set
    def Meancalculate(self,set):
        num=20
        total = 0.0
        while(num>=0):
            count=len(set)
            for object in set:
                total+=object
            mean=total/count
            for object in set:
                differenceRate=math.fabs(object-mean)/mean
                if differenceRate>1:
                    set.remove(object)
            num-=1
            total = 0.0
        for object in set:
            total+=object
        count=len(set)
        mean=total/count

        return mean

    def MeanRedshift(self,set):
        num = 20
        total = 0.0
        while (num >= 0):
            count = len(set)
            for object in set:
                total += object.__getattribute__('redshift')
            mean = total / count
            for object in set:
                differenceRate = math.fabs(object.__getattribute__('redshift') - mean) / mean
                if differenceRate > 2:
                    set.remove(object)
            total = 0.0
            num -= 1
        num=20
        while (num >= 0):
            count = len(set)
            for object in set:
                total += object.__getattribute__('redshift')
            mean = total / count
            for object in set:
                differenceRate = math.fabs(object.__getattribute__('redshift') - mean) / mean
                if differenceRate > 0.5:
                    set.remove(object)
            total = 0.0
            num -= 1
        for object in set:
            total+=object.__getattribute__('redshift')
        count=len(set)
        mean=total/count


        return mean


    def rootMeanSquareV(self, set):
        sumForCalculateRms = 0.0
        num = 20
        total = 0.0
        while (num >= 0):
            count = len(set)
            for object in set:
                total += object
            mean = total / count
            for object in set:
                differenceRate = math.fabs(object - mean) / mean
                if differenceRate > 1:
                    set.remove(object)
            total = 0.0
            num -= 1
        for object in set:
            total += object
        count=len(set)
        mean = total / count
        for object in set:
            sumForCalculateRms += math.pow((object- mean), 2)

        RMS = math.sqrt(sumForCalculateRms / (count - 1))

        return RMS