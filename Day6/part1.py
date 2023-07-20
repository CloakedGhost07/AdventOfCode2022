import re
from pprint import pprint


class SignalProcessor:
    def __init__(self, signal):
        self.signal = list(signal)

    def detectFirstPacketIndicator(self):
        for packetEnd in range(4, len(self.signal)):
            packet = set(self.signal[packetEnd - 4 : packetEnd])
            if len(packet) == 4:
                return packetEnd


if __name__ == "__main__":
    score = 0
    with open("data") as f:
        line = f.readline()
    processor = SignalProcessor(line)
    firstPacketLoc = processor.detectFirstPacketIndicator()
    print(firstPacketLoc)
