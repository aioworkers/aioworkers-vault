import json
import logging
from abc import ABC, abstractmethod
from urllib.request import urlopen

from aioworkers.core.base import LoggingEntity


logger = logging.getLogger(__package__)


class Server:
    def __init__(self, cfg: dict):
        self._cfg = cfg

    def request(self, path: str) -> dict:
        url = '{address}/v1/{namespace}/{path}'.format(
            address=self._cfg['address'],
            namespace=self._cfg['namespace'],
            path=path,
        )
        try:
            with urlopen(url) as r:
                data = json.loads(r)
        except json.JSONDecodeError:
            logger.exception('Error while request %s', url)

        if 'errors' in data:
            logger.error('Error while request', data)

        return data


class Engine(ABC):
    def __init__(self, server: Server, cfg: dict):
        self._cfg = cfg
        self._server = server

    @abstractmethod
    def get_config(self) -> dict:
        pass


class EngineKV(Engine):
    def get_path(self):
        return self._cfg['name']

    def get_config(self) -> dict:
        path = self.get_path()
        data = self._server.request(path)
        return self.get_values(data['data'])

    def get_values(self, data: dict) -> dict:
        result = {}
        for field, target in self._cfg['values'].items():
            result[target] = data[field]
        return result


class Vault(LoggingEntity):
    def set_config(self, config):
        cfg = config.new_parent(logger=__package__)
        super().set_config(cfg)
