import sys
from typing import IO

from parsecgm.elements import ELEMENT_NAMES
from parsecgm.parse.parse_header import parse_command_header
from parsecgm.parse.readers import IoReader


def parse_file(file: IO[bytes]) -> None:
    reader = IoReader(file)
    indent = 0
    while True:
        header = parse_command_header(reader)
        needs_padding = header.parameter_length % 2
        padded_length = header.parameter_length + needs_padding
        reader.next_bytes(padded_length)

        name = ELEMENT_NAMES[(header.el_class, header.el_id)]
        if name.startswith('END_'):
            indent -= 2
        print(' ' * indent + name)
        if name.startswith('BEGIN_') and not name.endswith('_BODY'):
            indent += 2

        if name == 'END_METAFILE':
            break


if __name__ == '__main__':
    parse_file(open(sys.argv[1], 'rb'))
