from abc import ABC, abstractmethod


class Closeable(ABC):
    @abstractmethod
    def close(self):
        pass
