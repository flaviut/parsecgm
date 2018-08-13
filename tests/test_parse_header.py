import pytest

from parsecgm.errors import InvalidFile
from parsecgm.parse.parse_header import parse_command_header, CommandHeader
from tests.util import ints_to_reader


def test_single():
    #                          4321 7654321 54321
    reader = ints_to_reader([0b0001_0000001_11010])
    assert parse_command_header(reader) == CommandHeader(1, 1, 0b11010)
    reader = ints_to_reader([0b1010_1010101_01010])
    assert (parse_command_header(reader) ==
            CommandHeader(0b1010, 0b1010101, 0b01010))


def test_multiple():
    reader = ints_to_reader([
        # 4321 7654321 54321
        0b0001_0000001_11111,
        # 1 543210987654321
        0b0_101010101010101])
    assert (parse_command_header(reader) ==
            CommandHeader(1, 1, 0b101010101010101))
    reader = ints_to_reader([
        # 4321 7654321 54321
        0b0001_0000001_11111,
        # 1 543210987654321
        0b1_101010101010101,
        0b0_101001010110001])
    assert (parse_command_header(reader) ==
            CommandHeader(1, 1, 0b101010101010101_101001010110001))


def test_invalid():
    reader = ints_to_reader([
        # 4321 7654321 54321
        0b0001_0000001_11111,
        # 1 543210987654321
        0b1_101010101010101,
        0b1_101001010110001])
    with pytest.raises(InvalidFile):
        parse_command_header(reader)

    reader = ints_to_reader([
        0b0001_0000001_11111,
        0b1_101010101010101])
    with pytest.raises(InvalidFile):
        parse_command_header(reader)

    reader = ints_to_reader([0b0001_0000001_11111])
    with pytest.raises(InvalidFile):
        parse_command_header(reader)
