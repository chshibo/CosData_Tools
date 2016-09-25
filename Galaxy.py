import SpaceObejct



class Galaxy(SpaceObejct.SpaceObject):
    """basic data about a galaxy"""
    def __init__(self,objid,ra,dec,r=None,redshift=None,l_to_sun=None):
        SpaceObejct.SpaceObject.__init__(self,objid,ra,dec,redshift)
        self.r=r
        self.l_to_sun=l_to_sun


