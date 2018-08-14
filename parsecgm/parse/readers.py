from abc import ABC, abstractmethod
from typing import Union, IO

from parsecgm.errors import InvalidFile


class Reader(ABC):
    @abstractmethod
    def next_byte(self) -> int:
        pass

    @abstractmethod
    def next_bytes(self, length=1) -> bytes:
        pass

    def next_word(self) -> int:
        if not self.is_word_aligned():
            raise RuntimeError('Reading off-aligned word. It\'s '
                               'unlikely you want this.')

        try:
            return self.next_byte() << 8 | self.next_byte()
        except InvalidFile:
            raise InvalidFile('Expected word, found EOF', self.pos)

    def is_word_aligned(self) -> bool:
        return self.pos % 2 == 0

    @property
    @abstractmethod
    def pos(self) -> int:
        """The current position in the input"""
        pass


class BytesReader(Reader):
    def __init__(self, content: Union[bytes, bytearray]) -> None:
        self._content = content
        self._pos = 0

    @property
    def pos(self):
        return self._pos

    def next_bytes(self, length=1) -> bytes:
        try:
            ret_bytes = self._content[self.pos:self.pos + length]
            self._pos += length
            return ret_bytes
        except IndexError:
            raise InvalidFile('Expected {} bytes, found EOL'.format(length),
                              self.pos)

    def next_byte(self):
        try:
            byte = self._content[self.pos]
        except IndexError:
            raise InvalidFile('Expected byte, found EOF', self.pos)
        self._pos += 1
        return byte


class IoReader(Reader):
    def __init__(self, stream: IO[bytes]) -> None:
        self._stream = stream
        self._pos = 0

    @property
    def pos(self):
        return self._pos

    def next_bytes(self, length=1) -> bytes:
        try:
            ret_bytes = self._stream.read(length)
            self._pos += length
            return ret_bytes
        except IndexError:
            raise InvalidFile(
                'Expected {} bytes, found EOL'.format(length), self.pos)

    def next_byte(self):
        try:
            byte = self._stream.read(1)[0]
        except IndexError:
            raise InvalidFile('Expected byte, found EOF', self.pos)
        self._pos += 1
        return byte
