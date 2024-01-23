class BotStatus:
    '''
    Class for managing bot status.
    Note: No instances need to be created
    '''
    
    _BOT_ACTIVE = False

    @classmethod
    def isBotActive(cls):
        '''Check if bot is active'''
        return BotStatus._BOT_ACTIVE

    @classmethod
    def setBotStatus(cls, status: bool):
        '''Set the status of the bot to be active (True) or inactive (False)'''
        BotStatus._BOT_ACTIVE = status