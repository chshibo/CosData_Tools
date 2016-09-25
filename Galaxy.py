import SpaceObejct



class Galaxy(SpaceObejct):
    """basic data about a galaxy"""
    def __init__(self,objid,ra,dec,r=None,l_to_sun=None,redshift=None):
        SpaceObejct.__init__(self,objid,ra,dec,redshift)
        self.r=r
        self.l_to_sun=l_to_sun
        self.redshift=redshift


