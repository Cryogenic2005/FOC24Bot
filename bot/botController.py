class BotStatus:
    '''
    Class for managing bot status.
    Note: No instances need to be created
    '''
    
    _isBotActive = True
    
    ACTIVE = True
    INACTIVE = False

    @classmethod
    def isBotActive(cls):
        '''Check if bot is active'''
        return BotStatus._isBotActive

    @classmethod
    def setBotStatus(cls, status: bool):
        '''Set the status of the bot to be active (True) or inactive (False)'''
        BotStatus._isBotActive = status