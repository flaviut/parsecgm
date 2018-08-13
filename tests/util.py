from typing import List

from parsecgm.readers import Reader, BytesReader


def ints_to_reader(wordlist: List[int]) -> Reader:
    return BytesReader(
        b''.join(word.to_bytes(2, byteorder='big', signed=False)
                 for word in wordlist))
