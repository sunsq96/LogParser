import sys
from collections import defaultdict
from typing import DefaultDict, Dict, Tuple, List
from flow_log_parser import FlowLogParser
from lookup_table_parser import LookupTableParser

def get_counts(logs: List[Tuple[str, str]], lookup_table: Dict[Tuple[str, str], str]) -> Tuple[DefaultDict[str, int], DefaultDict[Tuple[str, str], int]]:
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    for dst_port, protocol in logs:
        tag = lookup_table.get((dst_port, protocol), 'Untagged')
        tag_counts[tag] += 1
        port_protocol_counts[(dst_port, protocol)] += 1

    return tag_counts, port_protocol_counts

def write_to_file(tag_counts: DefaultDict[str, int], port_protocol_counts: DefaultDict[Tuple[str, str], int], output_file_path: str) -> None:
    with open(output_file_path, 'w') as file:
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in sorted(tag_counts.items()):
            file.write(f"{tag},{count}\n")

        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            file.write(f"{port},{protocol},{count}\n")

def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python flow_log_parser.py <flow_log_file_path> <lookup_table_file_path> <output_file_path>")
        sys.exit(1)

    log_file = sys.argv[1]
    lookup_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    lookup_parser = LookupTableParser()
    lookup_table = lookup_parser.parse(lookup_file_path)
    flow_log_parser = FlowLogParser()
    logs = flow_log_parser.parse_flow_logs(log_file)

    tag_counts, port_protocol_counts = get_counts(logs, lookup_table)
    write_to_file(tag_counts, port_protocol_counts, output_file_path)

if __name__ == "__main__":
    main()
