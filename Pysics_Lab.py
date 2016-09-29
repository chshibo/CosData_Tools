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

    MeanVelocity=mathCalculator.Meancalculate(galaxies,'velocity')
    RMSDispersion=mathCalculator.rootMeanSquareV(galaxies,'velocity')
    Distance=MeanVelocity/HUBBLE_CONSTANT
    Radius=Distance*(0.75/180)*math.pi
    MasstoSun=2*RMSDispersion*RMSDispersion*Radius*232*1e6
    LumitoSun=0.0

    for object in galaxies:
        Mr = object.__getattribute__('r')-5*math.log10(object.__getattribute__('distance')*1e6/10)
        LumitoSun+=math.pow(10,(-0.4)*(Mr-4.68))

    print 'total galaxies data used: ',len(galaxies)
    print 'redshift: ',Redshift
    print 'meanVelocity',MeanVelocity
    print 'RMSDispersion: ',RMSDispersion
    print 'Distance: ',Distance
    print 'Radius: ',Radius
    print 'MasstoSun: ',MasstoSun
    print 'LumitoSun: ',LumitoSun
    print 'MasstoLumino: ',MasstoSun/LumitoSun