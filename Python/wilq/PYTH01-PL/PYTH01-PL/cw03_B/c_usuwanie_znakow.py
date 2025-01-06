from cw03_A.utils import execute

commands = [
    "'tattoo'.lstrip('at')"
]
execute(commands, globals(), "usuwanie znaków z początku...")

commands = [
    "'tattoo'.strip('ot')"
]
execute(commands, globals(), "usuwanie znaków z początku i końca...")

commands = [
    "'tattoo'.rstrip('ot')"
]
execute(commands, globals(), "usuwanie znaków z końca...")
