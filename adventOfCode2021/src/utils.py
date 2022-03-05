from sys import stderr

def log_error(msg: str):
    print(msg + '\n', file=stderr)

def element_as_int(elem: str) -> int:
    return int(elem)

def element_as_tuple(elem: str, separator=' ') -> tuple:
    splitted_elem = elem.split(separator)
    return tuple(splitted_elem)