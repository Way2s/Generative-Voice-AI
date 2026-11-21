def pad_cell(text: str, width: int, align: str = 'left') -> str:
    s = str(text)
    if align == 'right':
        return s.rjust(width)
    if align == 'center':
        return s.center(width)
    return s.ljust(width)
