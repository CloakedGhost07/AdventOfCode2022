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
        self.screen = []
        pass

    def execute(self):
        command = True
        cyclesToComplete = 0
        do = None
        commandExecuted = 0
        scanLine = []
        spritePosition = [False for _ in range(40)]
        spritePosition[0] = True
        spritePosition[1] = True
        spritePosition[2] = True
        while command:
            try:
                if self.clockcycle in range(241):
                    if spritePosition[int(self.clockcycle % 40)]:
                        scanLine.append("#")
                    else:
                        scanLine.append(".")
                if self.clockcycle in [x for x in range(0, 241, 40)]:
                    self.screen.append(scanLine)
                    scanLine = []
                if cyclesToComplete == 0:
                    if do:
                        self.register = do([var, self.register])
                        commandExecuted += 1
                        spritePosition = [False for x in range(0, 40)]
                        try:
                            spritePosition[self.register] = True
                        except:
                            pass
                        try:
                            spritePosition[self.register + 1] = True
                        except:
                            pass
                        try:
                            spritePosition[self.register + 2] = True
                        except:
                            pass

                if cyclesToComplete == 0:
                    command = self.commands.pop(0).strip()
                    instruction = re.search(r"^[a-z]+", command).group(0)
                    cyclesToComplete = instructions.get(instruction).get("cycles")
                    do = instructions.get(instruction).get("do")
                    if "noop" not in command:
                        var = int(re.search(r"(-|)[\d]+$", command).group(0))
                self.clockcycle += 0.5
                cyclesToComplete += -0.5
            except Exception as e:
                print(str(e))
                print(f"{command=} {self.register=} {self.clockcycle}")
                break
        self.printScreen()

    def printScreen(self):
        screen = ""
        for row in self.screen:
            for item in row:
                screen += item
            screen += "\n"
        print(screen)


if __name__ == "__main__":
    with open("data") as f:
        data = f.readlines()
    cpu = CPU(data)
    cpu.execute()
