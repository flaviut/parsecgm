from enum import Enum, unique
from typing import Dict, NamedTuple, List

from attr import attrs, attrib


@unique
class Category(Enum):
    DELIMITER = 0
    METAFILE_DESCRIPTOR = 1
    PICTURE_DESCRIPTOR = 2
    CONTROL = 3
    GRAPHICAL_PRIMITIVE = 4
    ATTRIBUTE = 5
    ESCAPE = 6
    EXTERNAL = 7
    SEGMENT = 8
    APPLICATION_STRUCTURE_DESCRIPTOR = 9


class ElementId(NamedTuple):
    cls: int
    code: int


@unique
class Element(Enum):
    """Taken from ISO/IEC 8632-3:1999(E), Annex C, List of binary encoding metafile
    element codes"""
    # Delimiter Elements
    NO_OP = ElementId(0, 0)
    BEGIN_METAFILE = ElementId(0, 1)
    END_METAFILE = ElementId(0, 2)
    BEGIN_PICTURE = ElementId(0, 3)
    BEGIN_PICTURE_BODY = ElementId(0, 4)
    END_PICTURE = ElementId(0, 5)
    BEGIN_SEGMENT = ElementId(0, 6)
    END_SEGMENT = ElementId(0, 7)
    BEGIN_FIGURE = ElementId(0, 8)
    END_FIGURE = ElementId(0, 9)
    BEGIN_PROTECTION_REGION = ElementId(0, 13)
    END_PROTECTION_REGION = ElementId(0, 14)
    BEGIN_COMPOUND_LINE = ElementId(0, 15)
    END_COMPOUND_LINE = ElementId(0, 16)
    BEGIN_COMPOUND_TEXT_PATH = ElementId(0, 17)
    END_COMPOUND_TEXT_PATH = ElementId(0, 18)
    BEGIN_TILE_ARRAY = ElementId(0, 19)
    END_TILE_ARRAY = ElementId(0, 20)
    BEGIN_APPLICATION_STRUCTURE = ElementId(0, 21)
    BEGIN_APPLICATION_STRUCTURE_BODY = ElementId(0, 22)
    END_APPLICATION_STRUCTURE = ElementId(0, 23)

    # Metafile Descriptor Elements
    METAFILE_VERSION = ElementId(1, 1)
    METAFILE_DESCRIPTION = ElementId(1, 2)
    VDC_TYPE = ElementId(1, 3)
    INTEGER_PRECISION = ElementId(1, 4)
    REAL_PRECISION = ElementId(1, 5)
    INDEX_PRECISION = ElementId(1, 6)
    COLOUR_PRECISION = ElementId(1, 7)
    COLOUR_INDEX_PRECISION = ElementId(1, 8)
    MAXIMUM_COLOUR_INDEX = ElementId(1, 9)
    COLOUR_VALUE_EXTENT = ElementId(1, 10)
    METAFILE_ELEMENT_LIST = ElementId(1, 11)
    METAFILE_DEFAULTS_REPLACEMENT = ElementId(1, 12)
    FONT_LIST = ElementId(1, 13)
    CHARACTER_SET_LIST = ElementId(1, 14)
    CHARACTER_CODING_ANNOUNCER = ElementId(1, 15)
    NAME_PRECISION = ElementId(1, 16)
    MAXIMUM_VDC_EXTENT = ElementId(1, 17)
    SEGMENT_PRIORITY_EXTENT = ElementId(1, 18)
    COLOUR_MODEL = ElementId(1, 19)
    COLOUR_CALIBRATION = ElementId(1, 20)
    FONT_PROPERTIES = ElementId(1, 21)
    GLYPH_MAPPING = ElementId(1, 22)
    SYMBOL_LIBRARY_LIST = ElementId(1, 23)
    PICTURE_DIRECTORY = ElementId(1, 24)

    # Picture Descriptor Elements
    SCALING_MODE = ElementId(2, 1)
    COLOUR_SELECTION_MODE = ElementId(2, 2)
    LINE_WIDTH_SPECIFICATION_MODE = ElementId(2, 3)
    MARKER_SIZE_SPECIFICATION_MODE = ElementId(2, 4)
    EDGE_WIDTH_SPECIFICATION_MODE = ElementId(2, 5)
    VDC_EXTENT = ElementId(2, 6)
    BACKGROUND_COLOUR = ElementId(2, 7)
    DEVICE_VIEWPORT = ElementId(2, 8)
    DEVICE_VIEWPORT_SPECIFICATION_MODE = ElementId(2, 9)
    DEVICE_VIEWPORT_MAPPING = ElementId(2, 10)
    LINE_REPRESENTATION = ElementId(2, 11)
    MARKER_REPRESENTATION = ElementId(2, 12)
    TEXT_REPRESENTATION = ElementId(2, 13)
    FILL_REPRESENTATION = ElementId(2, 14)
    EDGE_REPRESENTATION = ElementId(2, 15)
    INTERIOR_STYLE_SPECIFICATION_MODE = ElementId(2, 16)
    LINE_AND_EDGE_TYPE_DEFINITION = ElementId(2, 17)
    HATCH_STYLE_DEFINITION = ElementId(2, 18)
    GEOMETRIC_PATTERN_DEFINITION = ElementId(2, 19)
    APPLICATION_STRUCTURE_DIRECTORY = ElementId(2, 20)

    # Control Elements
    VDC_INTEGER_PRECISION = ElementId(3, 1)
    VDC_REAL_PRECISION = ElementId(3, 2)
    AUXILIARY_COLOUR = ElementId(3, 3)
    TRANSPARENCY = ElementId(3, 4)
    CLIP_RECTANGLE = ElementId(3, 5)
    CLIP_INDICATOR = ElementId(3, 6)
    LINE_CLIPPING_MODE = ElementId(3, 7)
    MARKER_CLIPPING_MODE = ElementId(3, 8)
    EDGE_CLIPPING_MODE = ElementId(3, 9)
    NEW_REGION = ElementId(3, 10)
    SAVE_PRIMITIVE_CONTEXT = ElementId(3, 11)
    RESTORE_PRIMITIVE_CONTEXT = ElementId(3, 12)
    PROTECTION_REGION_INDICATOR = ElementId(3, 17)
    GENERALIZED_TEXT_PATH_MODE = ElementId(3, 18)
    MITRE_LIMIT = ElementId(3, 19)
    TRANSPARENT_CELL_COLOUR = ElementId(3, 20)

    # Graphical Primitive Elements
    POLYLINE = ElementId(4, 1)
    DISJOINT_POLYLINE = ElementId(4, 2)
    POLYMARKER = ElementId(4, 3)
    TEXT = ElementId(4, 4)
    RESTRICTED_TEXT = ElementId(4, 5)
    APPEND_TEXT = ElementId(4, 6)
    POLYGON = ElementId(4, 7)
    POLYGON_SET = ElementId(4, 8)
    CELL_ARRAY = ElementId(4, 9)
    GENERALIZED_DRAWING_PRIMITIVE = ElementId(4, 10)
    RECTANGLE = ElementId(4, 11)
    CIRCLE = ElementId(4, 12)
    CIRCULAR_ARC_3_POINT = ElementId(4, 13)
    CIRCULAR_ARC_3_POINT_CLOSE = ElementId(4, 14)
    CIRCULAR_ARC_CENTRE = ElementId(4, 15)
    CIRCULAR_ARC_CENTRE_CLOSE = ElementId(4, 16)
    ELLIPSE = ElementId(4, 17)
    ELLIPTICAL_ARC = ElementId(4, 18)
    ELLIPTICAL_ARC_CLOSE = ElementId(4, 19)
    CIRCULAR_ARC_CENTRE_REVERSED = ElementId(4, 20)
    CONNECTING_EDGE = ElementId(4, 21)
    HYPERBOLIC_ARC = ElementId(4, 22)
    PARABOLIC_ARC = ElementId(4, 23)
    NONUNIFORM_BSPLINE = ElementId(4, 24)
    NONUNIFORM_RATIONAL_BSPLINE = ElementId(4, 25)
    POLYBEZIER = ElementId(4, 26)
    POLYSYMBOL = ElementId(4, 27)
    BITONAL_TILE = ElementId(4, 28)
    TILE = ElementId(4, 29)

    # Attribute Elements
    LINE_BUNDLE_INDEX = ElementId(5, 1)
    LINE_TYPE = ElementId(5, 2)
    LINE_WIDTH = ElementId(5, 3)
    LINE_COLOUR = ElementId(5, 4)
    MARKER_BUNDLE_INDEX = ElementId(5, 5)
    MARKER_TYPE = ElementId(5, 6)
    MARKER_SIZE = ElementId(5, 7)
    MARKER_COLOUR = ElementId(5, 8)
    TEXT_BUNDLE_INDEX = ElementId(5, 9)
    TEXT_FONT_INDEX = ElementId(5, 10)
    TEXT_PRECISION = ElementId(5, 11)
    CHARACTER_EXPANSION_FACTOR = ElementId(5, 12)
    CHARACTER_SPACING = ElementId(5, 13)
    TEXT_COLOUR = ElementId(5, 14)
    CHARACTER_HEIGHT = ElementId(5, 15)
    CHARACTER_ORIENTATION = ElementId(5, 16)
    TEXT_PATH = ElementId(5, 17)
    TEXT_ALIGNMENT = ElementId(5, 18)
    CHARACTER_SET_INDEX = ElementId(5, 19)
    ALTERNATE_CHARACTER_SET_INDEX = ElementId(5, 20)
    FILL_BUNDLE_INDEX = ElementId(5, 21)
    INTERIOR_STYLE = ElementId(5, 22)
    FILL_COLOUR = ElementId(5, 23)
    HATCH_INDEX = ElementId(5, 24)
    PATTERN_INDEX = ElementId(5, 25)
    EDGE_BUNDLE_INDEX = ElementId(5, 26)
    EDGE_TYPE = ElementId(5, 27)
    EDGE_WIDTH = ElementId(5, 28)
    EDGE_COLOUR = ElementId(5, 29)
    EDGE_VISIBILITY = ElementId(5, 30)
    FILL_REFERENCE_POINT = ElementId(5, 31)
    PATTERN_TABLE = ElementId(5, 32)
    PATTERN_SIZE = ElementId(5, 33)
    COLOUR_TABLE = ElementId(5, 34)
    ASPECT_SOURCE_FLAGS = ElementId(5, 35)
    PICK_IDENTIFIER = ElementId(5, 36)
    LINE_CAP = ElementId(5, 37)
    LINE_JOIN = ElementId(5, 38)
    LINE_TYPE_CONTINUATION = ElementId(5, 39)
    LINE_TYPE_INITIAL_OFFSET = ElementId(5, 40)
    TEXT_SCORE_TYPE = ElementId(5, 41)
    RESTRICTED_TEXT_TYPE = ElementId(5, 42)
    INTERPOLATED_INTERIOR = ElementId(5, 43)
    EDGE_CAP = ElementId(5, 44)
    EDGE_JOIN = ElementId(5, 45)
    EDGE_TYPE_CONTINUATION = ElementId(5, 46)
    EDGE_TYPE_INITIAL_OFFSET = ElementId(5, 47)
    SYMBOL_LIBRARY_INDEX = ElementId(5, 48)
    SYMBOL_COLOUR = ElementId(5, 49)
    SYMBOL_SIZE = ElementId(5, 50)
    SYMBOL_ORIENTATION = ElementId(5, 51)

    # Escape Element
    ESCAPE = ElementId(6, 1)

    # External Elements
    MESSAGE = ElementId(7, 1)
    APPLICATION_DATA = ElementId(7, 2)

    # Segment Elements
    COPY_SEGMENT = ElementId(8, 1)
    INHERITANCE_FILTER = ElementId(8, 2)
    CLIP_INHERITANCE = ElementId(8, 3)
    SEGMENT_TRANSFORMATION = ElementId(8, 4)
    SEGMENT_HIGHLIGHTING = ElementId(8, 5)
    SEGMENT_DISPLAY_PRIORITY = ElementId(8, 6)
    SEGMENT_PICK_PRIORITY = ElementId(8, 7)

    # Application Structure Descriptor_Elements
    APPLICATION_STRUCTURE_ATTRIBUTE = ElementId(9, 1)


NO_END_ELEMENTS = {
    Element.BEGIN_PICTURE_BODY,
    Element.BEGIN_APPLICATION_STRUCTURE_BODY
}


@attrs(frozen=True)
class CgmObject:
    pass


@attrs(frozen=True)
class CgmObjectParent(CgmObject):
    children: List[CgmObject] = attrib()


element_types: Dict[Element, CgmObject] = dict()
begin_to_end: Dict[Element, Element] = dict()


def cgm_element(begin_el: Element, end_el: Element = None):
    def real_decorator(wrapped_class):
        assert begin_el not in element_types, 'Duplicate class declaration'
        element_types[begin_el] = wrapped_class
        if end_el is not None:
            begin_to_end_contents = (set(begin_to_end.keys()) |
                                     set(begin_to_end.values()))
            assert (begin_el not in begin_to_end_contents and
                    end_el not in begin_to_end_contents), \
                'Duplicate begin/end declaration'
            begin_to_end[begin_el] = end_el

        return wrapped_class

    return real_decorator
