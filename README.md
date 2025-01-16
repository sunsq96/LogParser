## AWS VPC Flow Log Processor

### Description
This program parses a file containing AWS VPC flow log data and generates a txt file with:
1. Count of matches for each tag.
2. Count of matches for each port/protocol combination.

### Assumptions
- The program **only supports the default log format**, not custom formats, and the **only supported version is 2**. ([AWS VPC Flow Logs Reference](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html))
- Input files are **plain text (ASCII) files**.
- Unsupported log versions or malformed logs (e.g., logs with missing fields) will be **skipped**.
- The lookup table csv contains the following columns: **Port, Protocol, Tag**.
- Supported protocols are limited to **icmp**, **tcp**, and **udp** for simplicity.
- Output file is in txt format.

### Instructions
To run the program, use the following command:
```bash
python flow_log_processor.py <flow_log_file_path> <lookup_table_file_path> <output_file_path>
```
Example:
```bash
python ./src/flow_log_processor.py ./data/flow_logs.txt ./data/lookup_table.csv ./output.txt
```

### Testing scenarios
- Unit tests
- Flow log file tests: empty file, malformed/unsupported logs
- Look up csv tests: empty file, multiple tags map to more than one port, duplicate entries
- Load testing: test the performance with a 10MB log file and mapping csv with 10K records

### Future Enhancements
- Add error handing for invalid file/logs
- Add logging
- Support for more versions of flow logs and additional protocols by enhancing the FlowLogParser