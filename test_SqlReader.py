import SqlReader
def main():
    reader=SqlReader.SqlReader("SELECT objid,ra,dec,r,z FROM galaxy WHERE ra BETWEEN 194.138787 AND 195.548787 AND dec BETWEEN 27.259389 AND 28.709389");
    reader.dataCollect();

if __name__ =="__main__":
    main()