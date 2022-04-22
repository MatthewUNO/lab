class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Method to set default configuration
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self):
        """
        Function to validate the television is powered on/off
        :param Test if power is off
        :param Change power status to on
        :return power status
        """
        if self.__status == False:
            self.__status = True        #turn power on
        else:
            self.__status = False       #keep power off

    def channel_up(self):
        """
        Function to increase television channel
        :param increase channel.
        :return to lowest channel
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1         #increase current channel by 1
            else:
                self.__channel = Television.MIN_CHANNEL     #return channel to 0

    def channel_down(self):
        """
        Function to decrease television channel
        :param adjust channel.
        :return to lowest channel
        """
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1         #decrease current channel by 1
            else:
                self.__channel = Television.MAX_CHANNEL     #return to channel 3

    def volume_up(self):
        """
        Function to increase television volume
        :param increase volume.
        :return volume level
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1   #increase current volume by 1
            else:
                return self.__volume                #return current volume

    def volume_down(self):
        """
        Function to decrease television volume
        :param decrease volume.
        :return volume level
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1   #decrease volume by 1
            else:
                return self.__volume                 #return current volume

    def __str__(self):
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
