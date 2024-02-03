from .gameCommands import group
from .miscCommands import hello, help, enable, disable, start, register
from .permsManagementCommands import grant, demote, check_perms

command_list = [hello, help, enable, disable, start, group, grant, demote, check_perms, register]

__all__ = ['command_list']