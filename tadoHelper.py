import logging
from PyTado.interface import Tado

_LOG_ = logging.getLogger(__name__)


class TadoHelper:

    def __init__(self, account, pwd):
        self.my_tado = Tado(account, pwd)

    def checkWindowState(self):
        zones = self.my_tado.getZones()

        for index, zone in enumerate(zones):
            if self.windowOpen(zone['id']):
                _LOG_.info('window open')
                self.my_tado.setOpenWindow(zone['id'])
            else:
                _LOG_.debug('window closed')

    def windowOpen(self, zone_id):
        window_open = self.my_tado.getOpenWindowDetected(zone_id)
        return window_open['openWindowDetected']

