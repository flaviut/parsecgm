from abc import ABC, abstractmethod
from typing import Union


class Reader(ABC):
    @abstractmethod
    def next_byte(self) -> int:
        pass

    def next_word(self) -> int:
        return self.next_byte() << 8 | self.next_byte()


class BytesReader(Reader):
    def __init__(self, content: Union[bytes, bytearray]) -> None:
        self._content = content
        self._pos = 0

    def next_byte(self):
        byte = self._content[self._pos]
        self._pos += 1
        return byte
