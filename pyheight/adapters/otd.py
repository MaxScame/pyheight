import requests

from pyheight.get_data import Height


class OpenTopoData(Height):
    """
    https://www.opentopodata.org/
    """
    def __init__(self, coord:dict) -> None:
        super().__init__(coord)
        self.source = 'aster30m' # ASTER GDEM
        self.batch_size = 100 # Count of points in one request

    def set_cord_columns(self, cols: list) -> None:
        return super().set_cord_columns(cols)

    def get(self) -> dict:
        res = requests.get(url=f'https://api.opentopodata.org/v1/{self.source}?locations={self.coord}')
