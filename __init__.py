"""Team module exports."""

try:
    from .team01 import add
    from .team02 import bbellssem
    from .team04 import divisoin
    from .team_dongzoo import multiplication
except ImportError:
    from team01 import add
    from team02 import bbellssem
    from team04 import divisoin
    from team_dongzoo import multiplication

__all__ = ["add", "bbellssem", "divisoin", "multiplication"]
