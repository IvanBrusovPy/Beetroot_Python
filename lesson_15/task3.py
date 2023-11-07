CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    current_channel_num = 0

    def __init__(self, channels_list):
        self.channels_list = channels_list

    def first_channel(self):
        return self.channels_list[0]

    def last_channel(self):
        return self.channels_list[-1]

    def turn_channel(self, channel_num):
        self.current_channel_num = channel_num - 1
        return self.channels_list[self.current_channel_num]

    def next_channel(self):
        self.current_channel_num += 1
        if self.current_channel_num > len(self.channels_list):
            self.current_channel_num = 0
        return self.channels_list[self.current_channel_num]

    def previous_channel(self):
        self.current_channel_num -= 1
        return self.channels_list[self.current_channel_num]

    def current_channel(self):
        return self.channels_list[self.current_channel_num]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return "Yes" if channel in range(len(self.channels_list)) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels_list else "No"


controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")
