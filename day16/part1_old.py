from dataclasses import dataclass

def packetVersion(packetData):
    dataBits = packetData[:3]
    return int(dataBits, 2)

def packetID(packetData):
    idBits = packetData[3:6]
    return int(idBits, 2)

def lengthTypeID(packetData):
    id = int(packetData[6])
    if id not in [0,1]: raise ValueError(f"Expected length type id 0 or 1, calculated {id= }")
    return id

def getBitLength(packetData): #assumes lengthTypeID == 0
    return int(packetData[7:7+15], 2)

def numSubPackets(packetData): #assumes lengthTypeID == 1
    return int(packetData[7:7+11], 2)

def packetLiteralValue(packetData):
    valueBits = packetData[6:]
    #print(f"Translating binary chunks with full string {valueBits= }")
    if len(valueBits) %5 != 0: valueBits = valueBits[:-1* (len(valueBits)%5)] #chop off trailing bits
    #print(f"After truncation this is {valueBits= }")
    valueString = ""
    for chunk in range(int(len(valueBits)/5)):
        newChunk = valueBits[(chunk*5)+1:(chunk*5)+5]
        valueString += newChunk
        #print(f"After adding {newChunk= } to value, {valueString=}")
    return int(valueString, 2)

#TODO: split using inital bit of packets data
def splitPacketsByBitCount(packetData, numBits):
    packetList = []
    chunkIndex = 0
    while len(packetData) > 0:
        header, tempData = packetData[:6], packetData[6:]
        #while tempData[0]
    return packetList

#TODO: split using inital bit of packets data
def splitPacketsByPacketNum(packetData, numPackets):
    packetStartIndices = [0]
    trackingIndex = 0
    while len(packetStartIndices) < numPackets:
        trackingIndex += 7
        chunkIndex = 0
        if int(packetData[trackingIndex + chunkIndex]) == 0:
            packetStartIndices += trackinGIndex + chunkIndex
        else:
            pass

    return packetList

class Packet():
    def __init__(self, data):
        self.version = packetVersion(data)
        self.typeID = packetID(data)
        self.content = data[6:]
     
    def __str__(self):
        return f"{self.__class__} object at {id(self)} {self.version= } {self.typeID= } {self.content= }"

class operatorPacket(Packet):
    def __init__(self, data):
        super().__init__(data)

        self.lengthTypeID = int(self.content[0])
        if self.lengthTypeID == 0:
            self.length = int(self.content[1:1+15], 2)
        elif self.lengthTypeID == 1:
            self.length = int(self.content[1:1+11], 2)
        else: raise ValueError(f"Expected length type ID 0 or 1, got {self.lengthTypeID}")

        self.subPackets = list()

    def __str__(self):
        return super().__str__() + f" {self.lengthTypeID= } {self.length= }"



def parseMainPacket(s):
    firstPacketType = packetID(s)
    if firstPacketType == 4: return Packet(s)
    else:
        p = operatorPacket(s)
        if p.lengthTypeID == 1:
            while len(p.subPackets) < p.length:


    return p
        
if __name__ == '__main__':
    with open("input_test.txt", "r", encoding="utf-8") as infile:
        data = infile.read().strip()

    numString = int(data, 16)
    size = len(data) * 4
    binaryData = f'{numString:0>{size}b}'

    basePacket = parseMainPacket(binaryData)
    print(basePacket)