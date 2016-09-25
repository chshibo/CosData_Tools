import Galaxy
import MathCalculator
import SqlReader
import XMLDomReader

if __name__ == '__main__':
    #update information and write to the file
    sqlReader=SqlReader.SqlReader("SELECT p.objid,p.ra,p.dec,p.r,s.z as redshift FROM galaxy as p join specobj as s on s.bestobjid=p.objid WHERE p.ra BETWEEN 194.138787 AND 195.548787 AND p.dec BETWEEN 27.259389 AND 28.709389")
    sqlReader.dataCollect()

    #parse and get data
    xmlReader=XMLDomReader.XmlDomReader('data_requested.xml')
    galaxies=xmlReader.getClusterofGalaxies()

    mathCalculator=MathCalculator.MathCalculator()

    RMSVelocity=mathCalculator.rootMeanSquareV(galaxies)
    print 'total galaxies data collected: ',len(galaxies)
    print RMSVelocity
