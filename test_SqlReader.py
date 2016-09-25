import SqlReader
def main():
    reader=SqlReader.SqlReader("SELECT p.objid,p.ra,p.dec,p.r,s.z as redshift FROM galaxy as p join specobj as s on s.bestobjid=p.objid WHERE p.ra BETWEEN 194.138787 AND 195.548787 AND p.dec BETWEEN 27.259389 AND 28.709389")
    reader.dataCollect()

if __name__ =="__main__":
    main()