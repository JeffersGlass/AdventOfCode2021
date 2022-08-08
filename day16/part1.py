from ast import operator, parse
from typing import Iterable
import pyparsing as pp

packet = pp.Forward()

version_token = pp.Group(pp.Char("01") * 3).set_name("version_token")

literal_packet_type = pp.Literal("100").set_name("literal_packet_type")
not_last_value_tokens = "1" + pp.Char("01") * 4
last_value_token = pp.Group("0" + pp.Char("01") * 4)

literal_packet = version_token("version") + literal_packet_type("literal") + \
    pp.Group(not_last_value_tokens[...])("not_last_packets") + last_value_token("last_packet")

operator_packet_type = pp.Group(pp.Char("01") * 3).set_name("operator_packet_type")
op_length_type_bitlength = pp.Char("0")
op_bitlength_field = pp.Char("01") * 15
op_length_type_subpacket = pp.Char("1")
op_subpacket_count = pp.Char("01") * 11

bitlength_packet = version_token("version") + operator_packet_type("operator_packet_type") + \
    pp.counted_array(pp.Char("01") , int_expr = op_bitlength_field)

subpacket_packet = version_token("version") + operator_packet_type("operator_packet_type") + \
    pp.counted_array(expr = pp.Char("01"),  int_expr = op_subpacket_count)

operator_packet = bitlength_packet | subpacket_packet

packet = literal_packet | operator_packet

#packet_string = multiple packets

def load_data(filename):
    with open(filename, 'r') as fp:
        raw = fp.read()
        return ''.join([bin(int(char, 16))[2:].rjust(4,"0") for char in raw]), raw

def value_of_literal_packet(packets: pp.ParseResults):
    """Given a (flat) list of parse results, get the value (as int) of literal tokens.
    """    
    raw_value_tokens = [''.join(v) for k, v in packets.items() if k in ("not_last_packets", "last_packet")]
    raw_value_string = ''.join(raw_value_tokens)
    stripped_string = ''.join(digit for i, digit in enumerate(raw_value_string) if i % 5 != 0)
    return int(stripped_string, 2)

def main():
    data, raw = load_data('input_test.txt')
    print(f"Parsed raw input data {raw} as {data}")

    parse_results = packet.parse_string(data)
    print(f"{parse_results= }")
    
    """ parse_results.pprint(indent=4)
    for label in ['version', 'literal', 'not_last_packets', 'last_packet']:
        print(f"{label}: {parse_results[label]}") """

if __name__ == "__main__":
    main()