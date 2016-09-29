import Galaxy
import MathCalculator
import SqlReader
import XMLDomReader
import math
VEGA_LUMINOSITY=74.4731973982
NGC_4874_RA=194.898787
NGC_4874_DEC=27.959389
HUBBLE_CONSTANT=67.6

if __name__ == '__main__':
    #update information and write to the file
    sqlReader=SqlReader.SqlReader("SELECT p.objid,p.ra,p.dec,p.r,s.z as redshift FROM galaxy as p join specobj as s on s.bestobjid=p.objid WHERE p.ra BETWEEN 194.148787 AND 195.648787 AND p.dec BETWEEN 27.209389 AND 28.709389")
    sqlReader.dataCollect()

    #parse and get data
    xmlReader=XMLDomReader.XmlDomReader('data_requested.xml')
    galaxies=xmlReader.getClusterofGalaxies()
    print "galaxies collected: ",len(galaxies)

    mathCalculator=MathCalculator.MathCalculator()
    Redshift=mathCalculator.MeanRedshift(galaxies)
    angles=[0]
    angles.pop(0)
    rband=[0]
    rband.pop(0)
    velocity=[0]
    velocity.pop(0)
    for galaxy in galaxies:
        theta=math.sqrt(math.pow(galaxy.__getattribute__('ra')-NGC_4874_RA,2)+math.pow(galaxy.__getattribute__('dec')-NGC_4874_DEC,2))
        angles.append(theta)
        rband.append(galaxy.__getattribute__('r'))
        velocity.append(galaxy.velocityOfObject())
    Meantheta=mathCalculator.Meancalculate(angles)
    MeanVelocity=mathCalculator.Meancalculate(velocity)
    RMSDispersion=mathCalculator.rootMeanSquareV(velocity)
    Distance=MeanVelocity/HUBBLE_CONSTANT
    Radius=Distance*0.75/180*math.pi  #TODO
    MasstoSun=2*RMSDispersion*RMSDispersion*Radius*232*1e6
    LumitoSun=0.0

    for object in rband:
        Mr = object-5*math.log10(Distance*1e6/10)
        LumitoSun+=math.pow(10,(-0.4)*(Mr-4.68))
    for object in galaxies:
        print 'redshift ',object.__getattribute__('redshift'),'  r: ',object.__getattribute__('r')

    print 'total galaxies data used: ',len(galaxies)
    print 'redshift: ',Redshift
    print 'meanVelocity',MeanVelocity
    print 'RMSDispersion: ',RMSDispersion
    print 'Meantheta: ',Meantheta
    print 'Distance: ',Distance
    print 'Radius: ',Radius
    print 'MasstoSun: ',MasstoSun
    print 'LumitoSun: ',LumitoSun
    print 'MasstoLumino: ',MasstoSun/LumitoSun