class Colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class Bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


def execute(commands, globs, comment=''):
    if comment:
        print('\n\n>>>>>', comment.upper())
    width = max(map(len, commands))
    print('{:{width}}  {}'.format('POLECENIE:', 'WYNIK:', width=width))
    for command in commands:
        try:
            result = eval(command, globs)
        except Exception as e:
            result = e
        print(f'{Colors.Bg.lightgrey + Colors.bold + Colors.Fg.blue + command + Colors.reset:{width + 21}}'
              f'{Colors.Bg.lightgrey + Colors.bold + Colors.Fg.red}{result}{Colors.reset}')
