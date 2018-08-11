from parsecgm.parse_header import parse_command_header, CommandHeader
from parsecgm.readers import BytesReader
from tests.util import ints_to_bytes


def test_header_parse_single():
    #                                     4321 7654321 54321
    reader = BytesReader(ints_to_bytes([0b0001_0000001_11010]))
    assert parse_command_header(reader) == CommandHeader(1, 1, 0b11010)
    reader = BytesReader(ints_to_bytes([0b1010_1010101_01010]))
    assert (parse_command_header(reader) ==
            CommandHeader(0b1010, 0b1010101, 0b01010))


def test_header_parse_multiple():
    reader = BytesReader(ints_to_bytes([
        # 4321 7654321 54321
        0b0001_0000001_11111,
        # 1 543210987654321
        0b0_101010101010101]))
    assert (parse_command_header(reader) ==
            CommandHeader(1, 1, 0b101010101010101))
    reader = BytesReader(ints_to_bytes([
        # 4321 7654321 54321
        0b0001_0000001_11111,
        # 1 543210987654321
        0b1_101010101010101,
        0b0_101001010110001]))
    assert (parse_command_header(reader) ==
            CommandHeader(1, 1, 0b101010101010101_101001010110001))
