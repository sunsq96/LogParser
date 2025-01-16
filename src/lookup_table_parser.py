import csv
from typing import Dict, Tuple

class LookupTableParser:
    
    def parse(self, file_path: str) -> Dict[Tuple[str, str], str]:
        """
        Example:
            Input:
                dstport,protocol,tag
                25,tcp,sv_P1
                68,udp,sv_P2

            Output:
                {
                    ("25", "tcp"): "sv_P1",
                    ("68", "udp"): "sv_P2",
                }
        """
        lookup_table: Dict[Tuple[str, str], str] = {}
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            reader.fieldnames = [header.strip() for header in reader.fieldnames]

            for row in reader:
                port = row["dstport"].strip()
                protocol = row["protocol"].strip().lower()
                tag = row["tag"].strip()

                lookup_table[(port, protocol)] = tag

        return lookup_table