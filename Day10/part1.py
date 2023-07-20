import re
from pprint import pprint
import json
import math

instructions = {"addx": {"cycles": 2, "do": sum}, "noop": {"cycles": 1, "do": None}}


class CPU:
    def __init__(self, data) -> None:
        self.commands = data
        self.clockcycle = 0
        self.register = 1
        pass

    def execute(self):
        signalStrength = 0
        command = True
        cyclesToComplete = 0
        do = None
        commandExecuted = 0
        while command:
            try:
                if self.clockcycle in [x for x in range(20, 221, 40)]:
                    signalStrength += self.register * (self.clockcycle)
                if cyclesToComplete == 0:
                    if do:
                        self.register = do([var, self.register])
                        commandExecuted += 1
                if cyclesToComplete == 0:
                    command = self.commands.pop(0).strip()
                    instruction = re.search(r"^[a-z]+", command).group(0)
                    cyclesToComplete = instructions.get(instruction).get("cycles")
                    do = instructions.get(instruction).get("do")
                    if "noop" not in command:
                        var = int(re.search(r"(-|)[\d]+$", command).group(0))
                self.clockcycle += 0.5
                cyclesToComplete += -0.5
            except:
                break
        print(signalStrength)


if __name__ == "__main__":
    with open("data") as f:
        data = f.readlines()
    cpu = CPU(data)
    cpu.execute()
