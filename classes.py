class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False

    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def channel_up(self):
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1
            else:
                return self.__volume 

    def volume_down(self):
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1
            else:
                return self.__volume

    def __str__(self):
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
