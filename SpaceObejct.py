class SpaceObject(object):
    """Objects contained in our universe including blackholes, galaxies,star,planets etc."""
    def __init__(self,objid,ra,dec,redshift=None):
        self.objid=objid
        self.ra=ra
        self.dec=dec
        self.redshift=redshift