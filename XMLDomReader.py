from xml.dom.minidom import parse
import xml.dom.minidom
import SpaceObejct
import Galaxy
class XmlDomReader(object):

    def __init__(self,filename):
        self.filename=filename

    def getDomTree(self):
        return xml.dom.minidom.parse(self.filename)

    def getClusterofGalaxies(self):
        tableWanted=None
        C