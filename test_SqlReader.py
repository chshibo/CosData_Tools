import SqlReader
def main():
    reader=SqlReader("select top 2 ra, dec from galaxy");
    reader.dataCollect();

if __name__ =="__main__":
    main()