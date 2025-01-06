from cw03_A.utils import execute

commands = [
    "'Japonia'.replace('J', 'L')",
    "'Sodoma'.translate(str.maketrans('dmS', 'mrG'))",
    "'_'.join('Python')"
]
execute(commands, globals())
