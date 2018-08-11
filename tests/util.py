from typing import List


def ints_to_bytes(wordlist: List[int]) -> bytes:
    return b''.join(word.to_bytes(2, byteorder='big', signed=False)
                    for word in wordlist)
