math_symbols_mapping = {
    'equal': '=',
    # ---- The following symbols are disable because are not matched correctly with the math skill ----.
    # 'open parentheses': '(',
    # 'close parentheses':  ')',
    'plus': '+',
    'minus': '-',
    'asterisk': '*',
    'divide': '/',
    'modulo': 'mod',
    'power': '**',
    'square root': '**(1/2)'
}

math_tags = ','.join(list(math_symbols_mapping.keys()))
