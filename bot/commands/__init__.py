from .gameCommands import group
from .miscCommands import hello, help, enable, disable, start
from .permsManagementCommands import grant, demote, check_perms

commandList = [hello, help, enable, disable, start, group, grant, demote, check_perms]

__all__ = ['commandList']