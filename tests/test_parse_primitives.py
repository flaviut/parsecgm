from decimal import Decimal

from parsecgm.parse.parse_primitives import (
    parse_int8, parse_int16, parse_int24, parse_int32, parse_uint32,
    parse_uint8, parse_uint16, parse_uint24, parse_fixed32, parse_fixed64)
from tests.util import ints_to_reader


def test_int8():
    reader = ints_to_reader([0xFF_0F])
    assert parse_int8(reader) == -1
    assert parse_int8(reader) == 0x0F


def test_int16():
    reader = ints_to_reader([0xFF0F, 643])
    assert parse_int16(reader) == -0xf1
    assert parse_int16(reader) == 643


def test_int24():
    reader = ints_to_reader([0x7FFF, 0x0FA0, 0xF0F0])
    assert parse_int24(reader) == 0x7FFF0F
    assert parse_int24(reader) == -6229776


def test_int32():
    reader = ints_to_reader([0xF0F0, 0xF0F0,
                             0x7AFE, 0x7A21])
    assert parse_int32(reader) == -0xF0F0F10
    assert parse_int32(reader) == 0x7AFE7A21


def test_uint8():
    reader = ints_to_reader([0xFF_0F])
    assert parse_uint8(reader) == 0xFF
    assert parse_uint8(reader) == 0x0F


def test_uint16():
    reader = ints_to_reader([0xFF0F, 643])
    assert parse_uint16(reader) == 0xFF0F
    assert parse_uint16(reader) == 643


def test_uint24():
    reader = ints_to_reader([0x7FFF, 0x0FA0, 0xF0F0])
    assert parse_uint24(reader) == 0x7FFF0F
    assert parse_uint24(reader) == 0xA0F0F0


def test_uint32():
    reader = ints_to_reader([0xF0F0, 0xF0F0,
                             0x7AFE, 0x7A21])
    assert parse_uint32(reader) == 0xF0F0F0F0
    assert parse_uint32(reader) == 0x7AFE7A21


def test_fixed32():
    reader = ints_to_reader([32321, 0xF0F0,
                             0xFAFE, 0x7A21])
    assert parse_fixed32(reader) == Decimal('32321.941162109375')
    assert parse_fixed32(reader) == Decimal('-1281.5229339599609375')


def test_fixed64():
    reader = ints_to_reader([0xF0F0, 0xF0F0, 0xFAFE, 0x7A21])
    assert parse_fixed64(reader) == Decimal('-252645135.0195544881280511618')
