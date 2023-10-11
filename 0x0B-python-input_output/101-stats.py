#!/usr/bin/python3
"""Defines a script that reads stdin line by line"""


import sys
import signal


def print_metrics(metrics):
    print("File size: {:d}".format(metrics['total_size']))
    for status_code in sorted(metrics['status_codes']):
        print("{}: {}"
              .format(status_code, metrics['status_codes'][status_code]))

        def reset_metrics():
            return {
                    'total_size': 0,
                    'status_codes': {200: 0, 301: 0,
                                     400: 0, 401: 0,
                                     403: 0, 404: 0,
                                     405: 0, 500: 0}
                    }


metrics = reset_metrics()
line_count = 0


def process_line(line):
    """Print accumulared metrics"""
    global line_count
    global metrics

    parts = line.split()
    if len(parts) < 7:
        return

    status_code = int(parts[-2])
    file_size = int(parts[-1])

    if status_code in metrics['status_codes']:
        metrics['status_codes'][status_code] += 1

    metrics['total_size'] += file_size
    line_count += 1

    if line_count % 10 == 0:
        print_metrics(metrics)


def signal_handler(sig, frame):
    """Reads from standard input and computes metrics"""
    print_metrics(metrics)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line)
except KeyboardInterrupt:
    print_metrics(metrics)
