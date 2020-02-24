import importlib
from collections import namedtuple
from pathlib import Path

_modules = {}
_Option = namedtuple('BrisingrModule', ['name', 'func', 'help'])

for file in (Path(__file__).parent/'plugins').glob('*.py'):
    if file.stem != '__init__':
        _module = importlib.import_module(f'plugins.{file.stem}')
        _modules[file.stem] = _Option(
            name=_module.__name__,
            func=getattr(_module, 'fix'),
            help=_module.__doc__
        )

OPTIONS = {k: m.help for k, m in _modules.items()}

def update(path, mods):
    lines = path.read_text(errors='ignore').splitlines()
    for mod in mods:
        if mod in OPTIONS:
            lines = _modules[mod].func(lines=lines, filename=path.name)
    return '\n'.join(lines)