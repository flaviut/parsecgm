import sys
from typing import IO

from parsecgm.elements.common import Element
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

        el = Element((header.el_class, header.el_id))
        name = el.name
        if name.startswith('END_'):
            indent -= 2
        print('{}{:02d} {}'.format(' ' * indent, header.el_class, name))
        if name.startswith('BEGIN_') and not name.endswith('_BODY'):
            indent += 2

        if name == 'END_METAFILE':
            break


if __name__ == '__main__':
    parse_file(open(sys.argv[1], 'rb'))
