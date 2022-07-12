from __future__ import annotations
from enum import Enum, auto
import logging
from multiprocessing.sharedctypes import Value

class PacketType(Enum):
    LITERAL = auto()
    OPERATOR = auto()

class LengthType(Enum):
    BIT_LENGTH = auto()
    SUBPACKET_LENGTH=auto()

class Packet():
    def __init__(self, version: int, type_id: int, data: str):
        self.version : int = version
        self.type_id : int = type_id
        self.data : str = data
        self.subpackets = []

    def __repr__(self):
        return(f"Packet(version={self.version}, type_id={self.type_id}, data=(0b){self.data})")
    
    @classmethod 
    def from_hex(cls, hex_string: str) -> Packet:
        logging.info(f"Creating new Packet from hex_string {hex_string}")
        data = ""
        for char in hex_string:
            bin_string = bin(int(char, 16))[2:].rjust(4,"0")
            data+= bin_string
            #logging.debug(f"Added characters {bin_string} from character {char}")
        #logging.debug(f"Final binary string is {data}")
        new_obj = cls(version = int(data[:3], 2), type_id = int(data[3:6], 2), data = data[6:])
        logging.debug(f"Created new Packet from Hex: {new_obj}")
        return new_obj

    @classmethod
    def from_bin(cls, bin_string: str) -> Packet:
        logging.info(f"Creating new packet from hex_string {bin_string}")
        return cls(version = int(bin_string[:3], 2), type_id = int(bin_string[3:6], 2), data = bin_string[6:])

    @property
    def packet_type(self) -> PacketType:
        if self.type_id == 4: return PacketType.LITERAL
        else: return PacketType.OPERATOR

    @property
    def length_type(self) -> LengthType:
        if self.packet_type != PacketType.OPERATOR: raise TypeError("Only Operator Packets have a length type")

        if self.data[0] == "0": return LengthType.BIT_LENGTH
        else: return LengthType.SUBPACKET_LENGTH

    @property
    def value(self) -> int:
        if self.type_id == 4: #Literal Value
            binary_data = str(bin(self.data))[2:]
            padded_data = binary_data.ljust((4 - len(binary_data) % 4) % 4, "0")
            bits = []
            while padded_data[0] == '1':
                bits.extend(padded_data[1:5])
                padded_data = padded_data[5:]

            #Capture one more group with first digit 0
            bits.extend(padded_data[1:5])
            padded_data = padded_data[5:]

            binary_string = "".join(bits)
            return int(binary_string, 2)
            
        else:
            raise NotImplementedError((f"No value computed for Packet with type_id {self.type_id}"))

    def get_subpackets(self) -> list[Packet] | None:
        if self.packet_type == PacketType.LITERAL:
            print("This is a literal packet, no subpackets to get")
            return None
        else:
            if self.length_type == LengthType.BIT_LENGTH:    
                subpacket_bit_length = int(self.data[1:16], 2) #skip first number as that's the length type ID
                subpacket_bits = self.data[16:16+subpacket_bit_length]
                logging.debug(f"This packet with length_type={self.length_type} has a subpacket length of {subpacket_bit_length}")
                return Packet.parse_subpackets_with_bitlength(subpacket_bits)
            elif self.length_type == LengthType.SUBPACKET_LENGTH:
                subpacket_number = int(self.data[1:12], 2)
                subpacket_bits = self.data[12:]
                logging.debug(f"This packet with length_type={self.length_type} has {subpacket_number} subpackets")
                return Packet.parse_subpackets_with_num(subpacket_bits, subpacket_number)
            else:
                raise ValueError(f"length_type must be a valid LengthType, was {self.length_type}")

    @staticmethod
    def parse_subpackets_with_num(data, num) -> list(Packet):
        logging.info(f"Parsing {num} subpackets from {data}")
        if num == 1:
            return [Packet.from_bin(data)]
        elif num > 0:
            pass
        else:
            raise ValueError("Number of subpackets must be 1 or greater")

    @staticmethod
    def parse_subpackets_with_bitlength(data) -> list(Packet):
        subpackets = []
        bits = data
        while len(bits) > 0:
            logging.debug(f"Looking for first packet in {bits}")
            if int(bits[:3], 2) == 4: #literal value
                logging.debug("Found a literal packet, parsing...")
                length_of_first_packet = Packet.find_length_of_literal_first_packet(bits)
            else: #operator packet
                if int(data[0], 2) == 0: #number of bits specified
                    logging.debug("Found a packet with a specified bitlength of subpackets, parsing...")
                    length_of_first_packet = int(data[1, 1+15], 2)
                    subpacket = Packet.from_bin(data[:length_of_first_packet])
                    logging.debug(f"Created new packet from {length_of_first_packet} bits")
                    logging.debug(subpacket)
                    subpackets.append(subpacket)
                    bits = bits[length_of_first_packet:]
                else:
                    logging.debug("Found a packet with specified number of subpackets, parsing...")
                    length_of_first_packet = len(bits)
                    num_subs = int(data[1:1+11], 2)
                    subpackets.append(Packet.parse_subpackets_with_num(data, num_subs))
                    break

        return subpackets

            

    @staticmethod
    def find_length_of_literal_first_packet(data):
        pass
               

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    data = "38006F45291200"

    p = Packet.from_hex(data)
    print(p.get_subpackets())