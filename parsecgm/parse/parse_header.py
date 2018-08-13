from attr import attrs, attrib

from parsecgm.readers import Reader


@attrs
class CommandHeader:
    el_class: int = attrib()
    el_id: int = attrib()
    parameter_length: int = attrib()


def _parse_extended_param_length(reader: Reader):
    word = reader.next_word()
    has_more = word >> 15
    length = word & 0x7FFF

    if has_more:
        return length << 15 | _parse_extended_param_length(reader)

    return length


def parse_command_header(reader: Reader):
    word = reader.next_word()
    #                           4321
    el_class = (word >> 12) & 0b1111
    #                     7654321
    el_id = word >> 5 & 0b1111111
    #                           54321
    parameter_length = word & 0b11111
    if parameter_length == 0b11111:
        parameter_length = _parse_extended_param_length(reader)
    return CommandHeader(el_class, el_id, parameter_length)
