class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the Television with default values.
        """
        self.__status = False  # TV power status is off by default
        self.__muted = False  # Mute status is off by default
        self.__volume = self.MIN_VOLUME  # Initial volume
        self.__channel = self.MIN_CHANNEL  # Initial channel

    def power(self) -> None:
        """Toggle the power status of the TV without changing status variable."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the TV if it is on by changing the value of the muted variable."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the TV channel by 1 when the TV is on. Comes back around to MIN_CHANNEL if MAX_CHANNEL value is exceeded."""
        if self.__status:
            self.__channel = (
                self.MIN_CHANNEL if self.__channel == self.MAX_CHANNEL else self.__channel + 1
            )

    def channel_down(self) -> None:
        """Decrease the TV channel by 1 when the TV is on. Comes back around to MAX_CHANNEL if MIN_CHANNEL value is exceeded."""
        if self.__status:
            self.__channel = (
                self.MAX_CHANNEL if self.__channel == self.MIN_CHANNEL else self.__channel - 1
            )

    def volume_up(self) -> None:
        """Increase the TV volume by 1 when the TV is on. Unmute the TV if it is muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the TV volume by 1 when the TV is on. Unmute the TV if it is muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the current state of the TV as a string, including power status, channel status, and volume level."""
        power_status = "True" if self.__status else "False"
        volume = 0 if self.__muted else self.__volume
        return f"Power: {power_status}, Channel: {self.__channel}, Volume: {volume}" 
