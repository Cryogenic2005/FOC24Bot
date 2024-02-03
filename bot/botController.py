class BotStatus:
    '''
    Class for managing bot status.
    Note: No instances need to be created
    '''
    
    _is_bot_active = True
    
    ACTIVE = True
    INACTIVE = False

    @classmethod
    def isBotActive(cls):
        '''Check if bot is active'''
        return cls._is_bot_active

    @classmethod
    def setBotStatus(cls, status: bool):
        '''Set the status of the bot to be active (True) or inactive (False)'''
        cls._is_bot_active = status