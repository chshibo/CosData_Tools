from xml.dom.minidom import parse
import xml.dom.minidom
import Galaxy
class XmlDomReader(object):

    def __init__(self,filename):
        self.filename=filename

    def getDomTree(self):
        return xml.dom.minidom.parse(self.filename)

    def getClusterofGalaxies(self):

        tableWanted=None
        tables=self.getDomTree().getElementsByTagName('Table')

        for table in tables:
            if(table.hasAttribute('name')):
                if(table.getAttribute('name')=="Table1"):
                    tableWanted=table
                    break
                else:
                    pass
            else:
                pass

        galaxies=tableWanted.getElementsByTagName('Row')
        cluster=[Galaxy.Galaxy(0,0,0,0,0)]
        count=0
        hasGalaxy=False;
        for galaxy in galaxies:
            hasGalaxy=True
            items=galaxy.getElementsByTagName('Item')
            objid=''
            ra=0.0
            dec=0.0
            r=0.0
            redshift=0.0
            for item in items:
                if item.getAttribute('name')=='objid':
                    objid=item.childNodes[0].data
                elif item.getAttribute('name')=='ra':
                    ra=float(item.childNodes[0].data)
                elif item.getAttribute('name')=='dec':
                    dec=float(item.childNodes[0].data)
                elif item.getAttribute('name')=='r':
                    r=float(item.childNodes[0].data)
                elif item.getAttribute('name')=='redshift':
                    redshift=float(item.childNodes[0].data)
            gala=Galaxy.Galaxy(objid,ra,dec,r,redshift)
            count+=1
            if count<=1:
                cluster.pop(0)
                cluster.append(gala)
            else:
                cluster.append(gala)

        if not hasGalaxy:
            cluster.pop(0)
        return cluster
