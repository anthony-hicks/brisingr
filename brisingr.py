import importlib
from collections import namedtuple
from pathlib import Path

_modules = {}
_Module = namedtuple('Module', ['name', 'func', 'help'])
_Plugins = namedtuple('Plugins', ['active', 'inactive'])


for file in (Path(__file__).parent/'plugins').glob('*.py'):
    if file.stem != '__init__':
        _module = importlib.import_module(f'plugins.{file.stem}')
        _modules[file.stem] = _Module(
            name=_module.__name__,
            func=getattr(_module, 'fix'),
            help=_module.__doc__
        )


class Brisingr:
    def __init__(self):
        self.args = None
        self.parser = None
        self.plugins = None

    def set_parser(self, parser):
        self.parser = parser
        for name, plugin in _modules.items():
            parser.add_argument(f'--{name}', action='store_true', help=plugin.help)

    def parse_args(self):
        self.args = self.parser.parse_args()

        active = [k for k in _modules if k in self.args]
        inactive = [k for k in _modules if k not in self.args]

        self.plugins = _Plugins(active=active, inactive=inactive)

        return self.args

    def update(self, path):
        lines = path.read_text(errors='ignore').splitlines()
        for plugin in self.plugins.active:
            lines = _modules[plugin].func(lines=lines, filename=path.name)
        return '\n'.join(lines)