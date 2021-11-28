from enum import Enum
from numbers import Real

from attr import attrs, attrib

from parsecgm.elements.common import cgm_element, CgmObjectParent, Element
from parsecgm.elements.types import StringFixed, Index, Point


@cgm_element(Element.BEGIN_METAFILE, Element.END_METAFILE)
@attrs(frozen=True)
class Metafile(CgmObjectParent):
    name: StringFixed = attrib()


@cgm_element(Element.BEGIN_PICTURE, Element.END_PICTURE)
@attrs(frozen=True)
class Picture(CgmObjectParent):
    name: StringFixed = attrib()


@cgm_element(Element.BEGIN_PICTURE_BODY)
@attrs(frozen=True)
class PictureBody(CgmObjectParent):
    pass


@cgm_element(Element.BEGIN_SEGMENT, Element.END_SEGMENT)
@attrs(frozen=True)
class Segment(CgmObjectParent):
    name: StringFixed = attrib()


@cgm_element(Element.BEGIN_FIGURE, Element.END_FIGURE)
@attrs(frozen=True)
class Figure(CgmObjectParent):
    pass


@cgm_element(Element.BEGIN_PROTECTION_REGION,
             Element.END_PROTECTION_REGION)
@attrs(frozen=True)
class ProtectionRegion(CgmObjectParent):
    index: Index = attrib()


@cgm_element(Element.BEGIN_COMPOUND_LINE, Element.END_COMPOUND_LINE)
@attrs(frozen=True)
class CompoundLine(CgmObjectParent):
    pass


@cgm_element(Element.BEGIN_COMPOUND_TEXT_PATH,
             Element.END_COMPOUND_TEXT_PATH)
@attrs(frozen=True)
class CompoundTextPath(CgmObjectParent):
    pass


class CellPathDirection(Enum):
    deg_0 = 0
    deg_90 = 1
    deg_180 = 2
    deg_270 = 3


class LineProgressionDirection(Enum):
    deg_90 = 0
    deg_270 = 1


@cgm_element(Element.BEGIN_TILE_ARRAY, Element.END_TILE_ARRAY)
@attrs(frozen=True)
class TileArray(CgmObjectParent):
    position: Point = attrib()
    cell_path_direction: CellPathDirection = attrib()
    line_progression_direction: LineProgressionDirection = attrib()
    tiles_in_path: int = attrib()
    tiles_in_line: int = attrib()
    cells_tiles_in_path: int = attrib()
    cells_tiles_in_line: int = attrib()
    cell_size_path: Real = attrib()
    cell_size_line: Real = attrib()
    image_offset_path: int = attrib()
    image_offset_line: int = attrib()
    num_cells_path: int = attrib()
    num_cells_line: int = attrib()


class InheritanceFlag(Enum):
    STATE_LIST = 0
    APPLICATION_STRUCTURE = 1


@cgm_element(Element.BEGIN_APPLICATION_STRUCTURE,
             Element.END_APPLICATION_STRUCTURE)
@attrs(frozen=True)
class ApplicationStructure(CgmObjectParent):
    identifier: StringFixed = attrib()
    typ: StringFixed = attrib()
    inheritance_flag: InheritanceFlag = attrib()
