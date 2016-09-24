import sqlcl

class SqlReader(object):
    """Using this class to generate a Sqlreader, search and collect the date from SDSS server,
    and also generate a file named "data_as_requested.[frm]"
    """
    formats = ['csv', 'xml', 'html']

    astro_url = 'http://skyserver.sdss3.org/public/en/tools/search/x_sql.aspx'
    public_url = 'http://skyserver.sdss3.org/public/en/tools/search/x_sql.aspx'

    default_url = public_url
    default_fmt = 'csv'
    def __init__(self,url=default_url,sql="",fmt=default_fmt):
        self.url=url;
        self.sql=sql;
        self.fmt=fmt;
    def fileWriter(self):
        pass

    def dataCollector(self):
        import os, getopt, string

        queries = []
        url = os.getenv("SQLCLURL", SqlReader.default_url)
        fmt = SqlReader.default_fmt
        writefirst = 1
        verbose = 0

        # Parse command line
        try:
            optlist, args = getopt.getopt(argv[1:], 's:f:q:vlh?')
        except getopt.error, e:
            usage(1, e)

        for o, a in optlist:
            if o == '-s':
                url = a
            elif o == '-f':
                fmt = a
            elif o == '-q':
                queries.append(a)
            elif o == '-l':
                writefirst = 0
            elif o == '-v':
                verbose += 1
            else:
                usage(0)

        if fmt not in formats:
            usage(1, 'Wrong format!')

        # Enqueue queries in files
        for fname in args:
            try:
                queries.append(open(fname).read())
            except IOError, e:
                usage(1, e)

        # Run all queries sequentially
        for qry in queries:
            ofp = sys.stdout
            if verbose:
                write_header(ofp, '#', url, qry)
            file = query(qry, url, fmt)
            # Output line by line (in case it's big)
            line = file.readline()
            if line.startswith("ERROR"):  # SQL Statement Error -> stderr
                ofp = sys.stderr
            if writefirst:
                ofp.write(string.rstrip(line) + os.linesep)
            line = file.readline()
            while line:
                ofp.write(string.rstrip(line) + os.linesep)
                line = file.readline()



