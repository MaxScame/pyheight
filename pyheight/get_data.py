class Height:
    def __init__(self, coord:dict) -> None:
        self.coord = coord
        self.lon, self.lat = '', '' # Names of columns with coords

    def set_cord_columns(self, cols:list) -> None:
        """
        Set name of columns with coordinates in WGS 84

        Args:
            cols (list): List of column names.
        """
        if len(cols) != 2:
            return
        self.lon, self.lat = cols

    def get(self) -> dict:
        pass
