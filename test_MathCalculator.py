from MathCalculator import MathCalculator

def main():
    cal=MathCalculator();
    dic1={'num':1}
    dic2={'num':2}
    dic3={'num':3}
    tup=(dic1,dic2,dic3)
    print cal.rootMeanSquarecalculate('num',tup)

if __name__=='__main__':
    main()