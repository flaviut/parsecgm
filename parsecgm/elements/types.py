from typing import Tuple, NewType

# comment following the type is the same as the "Abstract Symbol" in ISO/IEC
# 8632-3:1999(E), Table 1: Representation of abstract data types
StringFixed = NewType('StringFixed', str)  # SF
Name = NewType('Name', int)  # N
Index = NewType('Index', int)  # I
Point = Tuple[int, int]  # P
# Enum = int  # E
# int = int  # I
# Real = Real  # R
