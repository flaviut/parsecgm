from numbers import Real
from typing import Tuple, Union, List

from attr import attrs, attrib

from parsecgm.parse.parse_primitives import parse_fixed32, parse_fixed64, \
    parse_float32, parse_int8, parse_int16, parse_int24, parse_int32, \
    parse_uint32, parse_uint8, parse_uint16, parse_uint24
from parsecgm.parse.readers import Reader

RealPrecision = Tuple[str, int]

ColorExtent = Tuple[str, List[Union[int, Real]],
                    List[Union[int, Real]]]

IntPrecision = int


def _bit_validator(bits: IntPrecision) -> bool:
    return bits in [8, 16, 24, 32]


def _real_validator(real_spec: RealPrecision) -> bool:
    return (len(real_spec) == 2 and
            real_spec[0] in ['float', 'fixed'] and
            real_spec[1] in [32, 64])


def _color_extent_validator(extent: ColorExtent) -> bool:
    if not (len(extent) == 3 and
            len(extent[1]) == 3 and len(extent[2]) == 3):
        return False
    if extent[0] == 'minmax':
        return (all(255 >= v >= 0 for v in extent[1]) and
                all(255 >= v >= 0 for v in extent[2]))
    elif extent[0] == 'scaleoffset':
        return (all(1.0 >= v >= 0.0 for v in extent[1]) and
                all(1.0 >= v >= 0.0 for v in extent[2]))


def _parse_real(reader: Reader, precision: RealPrecision) -> Real:
    if precision == ('fixed', 32):
        return parse_fixed32(reader)
    elif precision == ('fixed', 64):
        return parse_fixed64(reader)
    elif precision == ('float', 32):
        return parse_float32(reader)
    elif precision == ('float', 64):
        return parse_fixed64(reader)
    raise ValueError('Invalid precision passed')


def _parse_int(reader: Reader, precision: IntPrecision) -> int:
    if precision == 8:
        return parse_int8(reader)
    elif precision == 16:
        return parse_int16(reader)
    elif precision == 24:
        return parse_int24(reader)
    elif precision == 32:
        return parse_int32(reader)


def _parse_uint(reader: Reader, precision: IntPrecision) -> int:
    if precision == 8:
        return parse_uint8(reader)
    elif precision == 16:
        return parse_uint16(reader)
    elif precision == 24:
        return parse_uint24(reader)
    elif precision == 32:
        return parse_uint32(reader)


@attrs()
class BinaryCgmDescriptors:
    """
    Structure containing settings for how the file should be parsed.

    See ISO/IEC 8632-3:1999(E):
      - § 9 Defaults
      - § 8.3 Metafile descriptor elements
    """
    real_precision: RealPrecision = attrib(('fixed', 32), _real_validator)
    int_precision: IntPrecision = attrib(16, _bit_validator)

    color_precision: IntPrecision = attrib(8, _bit_validator)  # per component
    color_index_precision: IntPrecision = attrib(8, _bit_validator)

    index_precision: IntPrecision = attrib(16, _bit_validator)

    vdc_real_precision: RealPrecision = attrib(('fixed', 32), _real_validator)
    vdc_int_precision: IntPrecision = attrib(16, _bit_validator)

    color_extent: ColorExtent = attrib(validator=_color_extent_validator)

    name_precision: IntPrecision = attrib(16, _bit_validator)

    def parse_real(self, reader: Reader) -> Real:
        return _parse_real(reader, self.real_precision)

    def parse_int(self, reader: Reader) -> int:
        return _parse_int(reader, self.int_precision)

    def parse_uint(self, reader: Reader) -> int:
        return _parse_uint(reader, self.int_precision)

    def parse_vdc_real(self, reader: Reader) -> Real:
        return _parse_real(reader, self.vdc_real_precision)

    def parse_vdc_int(self, reader: Reader) -> int:
        return _parse_int(reader, self.vdc_int_precision)

    def parse_vdc_uint(self, reader: Reader) -> int:
        return _parse_uint(reader, self.vdc_int_precision)
