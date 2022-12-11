import re

inputRe = re.compile("^value (\d+) goes to bot (\d+)$")
propagateRe = re.compile(
    "^bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)")


class Bots:
    def __init__(self):
        self.srcForBot = {}
        self.srcForOutput = {}
        self.destForValue = {}
        self.lowDestForBot = {}
        self.highDestForBot = {}
        self.valuesForBot = {}

    def consume(self, instruction):
        if inputRe.match(instruction):
            value = int(inputRe.match(instruction).groups()[0])
            destBot = int(inputRe.match(instruction).groups()[1])
            if destBot not in self.srcForBot:
                self.srcForBot[destBot] = []
            self.srcForBot[destBot].append(('value', value))
            self.destForValue[value] = destBot

        elif propagateRe.match(instruction):
            sourceBot = int(propagateRe.match(instruction).groups()[0])
            lowDestType = propagateRe.match(instruction).groups()[1]
            lowDestIndex = int(propagateRe.match(instruction).groups()[2])
            highDestType = propagateRe.match(instruction).groups()[3]
            highDestIndex = int(propagateRe.match(instruction).groups()[4])
            if lowDestType == 'bot':
                if lowDestIndex not in self.srcForBot:
                    self.srcForBot[lowDestIndex] = []
                self.srcForBot[lowDestIndex].append(('bot', sourceBot))
            else:
                self.srcForOutput[lowDestIndex] = sourceBot
            self.lowDestForBot[sourceBot] = (lowDestType, lowDestIndex)

            if highDestType == 'bot':
                if highDestIndex not in self.srcForBot:
                    self.srcForBot[highDestIndex] = []
                self.srcForBot[highDestIndex].append(('bot', sourceBot))
            else:
                self.srcForOutput[highDestIndex] = sourceBot
            self.highDestForBot[sourceBot] = (highDestType, highDestIndex)

    def pushInputValue(self, value):
        self.populateValueForBot(self.destForValue[value])

    def populateValueForBot(self, botId):
        if botId in self.valuesForBot:
            return
        values = []
        for src in self.srcForBot[botId]:
            if src[0] == 'value':
                values.append(src[1])
            else:
                self.populateValueForBot(src[1])


def part1():
    with open('input') as f:
        b = Bots()
        for line in f.readlines():
            b.consume(line.strip())
        b.pushInputValue(61)
        b.pushInputValue(17)
        #print(b.getBotWithValue((17, 61)))


part1()
