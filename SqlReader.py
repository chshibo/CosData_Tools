import sqlcl
import sys

class SqlReader(object):
    """Using this class to generate a Sqlreader, search and collect the date from SDSS server,
    and also generate a file named "data_as_requested.[frm]"
    """

    astro_url = 'http://skyserver.sdss3.org/public/en/tools/search/x_sql.aspx'
    public_url = 'http://skyserver.sdss3.org/public/en/tools/search/x_sql.aspx'

    default_url = public_url
    default_fmt = 'xml'
    doc_default_name="data_requested"

    def __init__(self,sql=""):
        self.sql=sql;

    def fileWrite(self,file):
        import os, string
        with open(SqlReader.doc_default_name + "." + SqlReader.default_fmt, "w+") as f:
            # Output line by line (in case it's big)
            line = file.readline()
            if line.startswith("ERROR"):  # SQL Statement Error -> stderr
                f.write(sys.stderr)
            while line:
                f.write(string.rstrip(line) + os.linesep)
                line = file.readline()

    def dataCollect(self):
        import os

        queries = [self.sql]
        url = os.getenv("SQLCLURL", SqlReader.default_url)
        fmt = SqlReader.default_fmt


        # Run all queries sequentially
        for qry in queries:
            file = sqlcl.query(qry, url, fmt)
            self.fileWrite(file)


