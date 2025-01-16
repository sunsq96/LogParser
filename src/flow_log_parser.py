from typing import List, Tuple

class FlowLogParser:

    FIELD_MAPPING: dict[str, int] = {
        "version": 0,
        "account-id": 1,
        "interface-id": 2,
        "srcaddr": 3,
        "dstaddr": 4,
        "srcport": 5,
        "dstport": 6,
        "protocol": 7,
        "packets": 8,
        "bytes": 9,
        "start": 10,
        "end": 11,
        "action": 12,
        "log-status": 13,
    }

    PROTOCOL_MAPPING: dict[str, str] = {
        "1": "icmp",
        "6": "tcp",
        "17": "udp",
    }

    def parse_flow_logs(self, file_path: str) -> List[Tuple[str, str]]:
        """
        Example:
            Input:
                2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK
                2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK

            Output:
                [('443', 'tcp'), ('23', 'tcp')]
        """
        logs = []
        with open(file_path, 'r') as file:
            for line in file:
                fields = line.split()
                if len(fields) < len(self.FIELD_MAPPING):
                    continue
                version = fields[self.FIELD_MAPPING["version"]]
                if version == '2':
                    logs.append(self._parse_flow_log(fields))
        return logs

    def _parse_flow_log(self, fields: List[str]) -> Tuple[str, str]:
        dst_port = fields[self.FIELD_MAPPING["dstport"]]
        protocol_number = fields[self.FIELD_MAPPING["protocol"]]
        protocol = self.PROTOCOL_MAPPING.get(protocol_number, 'other')
        return dst_port, protocol