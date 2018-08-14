from decimal import Decimal
from numbers import Real
from struct import unpack

from parsecgm.parse.readers import Reader


def parse_int8(reader: Reader) -> int:
    return unpack('>b', reader.next_bytes())[0]


def parse_int16(reader: Reader) -> int:
    return unpack('>h', reader.next_bytes(2))[0]


def parse_int24(reader: Reader) -> int:
    val = parse_uint24(reader)
    sign = val >> 23
    if sign:
        return val - (1 << 24)
    return val


def parse_int32(reader: Reader) -> int:
    return unpack('>l', reader.next_bytes(4))[0]


def parse_uint8(reader: Reader) -> int:
    return unpack('>B', reader.next_bytes())[0]


def parse_uint16(reader: Reader) -> int:
    return unpack('>H', reader.next_bytes(2))[0]


def parse_uint24(reader: Reader) -> int:
    return (reader.next_byte() << 16 |
            reader.next_byte() << 8 |
            reader.next_byte())


def parse_uint32(reader: Reader) -> int:
    return unpack('>L', reader.next_bytes(4))[0]


def parse_fixed32(reader: Reader) -> Real:
    int_part = parse_int16(reader)
    dec_part = parse_uint16(reader)
    return Decimal(int_part) + (Decimal(dec_part) / 2 ** 16)


def parse_fixed64(reader: Reader) -> Real:
    int_part = parse_int32(reader)
    dec_part = parse_uint32(reader)
    return Decimal(int_part) + (Decimal(dec_part) / 2 ** 32)


def parse_float32(reader: Reader) -> Real:
    return unpack('>f', reader.next_bytes(4))[0]


def parse_float64(reader: Reader) -> Real:
    return unpack('>d', reader.next_bytes(4))[0]
