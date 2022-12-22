import re

inputRe = re.compile("^value (\d+) goes to bot (\d+)$")
propagateRe = re.compile(
    "^bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)")


class Bots:
    def __init__(self):
        self.srcForBot = {}
        self.srcForOutput = {}
        self.destForValue = {}
        self.loDestForBot = {}
        self.hiDestForBot = {}

        self.valuesForBot = {}
        self.valuesForOutput = {}

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
            loDestType = propagateRe.match(instruction).groups()[1]
            loDestIndex = int(propagateRe.match(instruction).groups()[2])
            hiDestType = propagateRe.match(instruction).groups()[3]
            hiDestIndex = int(propagateRe.match(instruction).groups()[4])
            if loDestType == 'bot':
                if loDestIndex not in self.srcForBot:
                    self.srcForBot[loDestIndex] = []
                self.srcForBot[loDestIndex].append(('bot', sourceBot))
            else:
                self.srcForOutput[loDestIndex] = sourceBot
            self.loDestForBot[sourceBot] = (loDestType, loDestIndex)

            if hiDestType == 'bot':
                if hiDestIndex not in self.srcForBot:
                    self.srcForBot[hiDestIndex] = []
                self.srcForBot[hiDestIndex].append(('bot', sourceBot))
            else:
                self.srcForOutput[hiDestIndex] = sourceBot
            self.hiDestForBot[sourceBot] = (hiDestType, hiDestIndex)

    def populateBots(self):
        for botId in self.srcForBot:
            self.populateValueForBot(botId)

    def populateValueForBot(self, botId):
        if botId in self.valuesForBot:
            return
        values = []
        for src in self.srcForBot[botId]:
            if src[0] == 'value':
                values.append(src[1])
            else:
                srcBot = src[1]
                self.populateValueForBot(srcBot)
                srcBotLowDest = self.loDestForBot[srcBot]
                srcBotHighDest = self.hiDestForBot[srcBot]
                if srcBotLowDest[0] == 'bot' and srcBotLowDest[1] == botId:
                    values.append(min(self.valuesForBot[srcBot]))
                elif srcBotHighDest[0] == 'bot' and srcBotHighDest[1] == botId:
                    values.append(max(self.valuesForBot[srcBot]))
        self.valuesForBot[botId] = values

    def getBotWithValue(self, values):
        for botId in self.srcForBot:
            if tuple(sorted(self.valuesForBot[botId])) == values:
                return botId

    def getOutput(self, outputId):
        srcBot = self.srcForOutput[outputId]
        srcBotLowDest = self.loDestForBot[srcBot]
        srcBotHighDest = self.hiDestForBot[srcBot]
        if srcBotLowDest[0] == 'output' and srcBotLowDest[1] == outputId:
            return min(self.valuesForBot[srcBot])
        elif srcBotHighDest[0] == 'output' and srcBotHighDest[1] == outputId:
            return max(self.valuesForBot[srcBot])


def part1():
    with open('input') as f:
        b = Bots()
        for line in f.readlines():
            b.consume(line.strip())
        b.populateBots()
        print(b.getBotWithValue((17, 61)))

def part2():
    with open('input') as f:
        b = Bots()
        for line in f.readlines():
            b.consume(line.strip())
        b.populateBots()
        print(b.getOutput(0) * b.getOutput(1) * b.getOutput(2))

part1()
part2()
