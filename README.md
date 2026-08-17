# Security Log Analyzer

A Python-based security log analysis tool that reads authentication logs and identifies failed login activity, suspicious users, suspicious IP addresses, critical activity, and high-frequency User/IP combinations.

This project was built incrementally from V1 to V6 as part of my hands-on Python and cybersecurity learning.

## Features

- Count total log events
- Count failed login attempts
- Count successful logins
- Count logout events
- Track failed login attempts by user
- Track failed login attempts by IP address
- Track failed login attempts by User/IP combination
- Detect suspicious users
- Detect suspicious IP addresses
- Detect critical users
- Detect critical IP addresses
- Identify the user with the most failed login attempts
- Identify the IP with the most failed login attempts
- Identify the User/IP combination with the most failed login attempts
- Generate a final suspicious and critical activity report

## Detection Rules

The analyzer currently uses the following thresholds:

| Failed Attempts | Classification |
|---|---|
| 1–2 | Normal |
| 3–4 | Suspicious |
| 5+ | Critical |

These thresholds are educational rules used for this project and are not intended to represent production security policies.

## Project Evolution

### V1
Basic security log reading and event detection.

### V2
Added event counters and basic statistics.

### V3
Added failed-login tracking by user and IP address.

### V4
Added suspicious activity detection and reporting.

### V5
Added User/IP combination tracking using Python tuples and dictionaries.

### V6
Added critical activity detection and identification of the most frequently failing users, IPs, and User/IP combinations.

## Technologies

- Python 3
- File handling
- Lists
- Dictionaries
- Tuples
- Loops
- Conditional statements
- String manipulation
- Basic security-log analysis

## Learning Objectives

Learning Objectives

This project was created to strengthen practical Python skills through a cybersecurity-related problem.

The main concepts practiced include:

Reading and processing files
Parsing structured log data
Working with dictionaries
Using tuples as dictionary keys
Counting occurrences
Building simple detection rules
Finding maximum values in dictionaries
Organizing security-related data
Producing readable security reports
Disclaimer

This project is an educational security-log analysis tool.

It does not replace a production SIEM, IDS, EDR, or other professional security monitoring system. The detection thresholds and log format are simplified for learning purposes.

Future Improvements

Possible future versions may include:

Better error handling
More flexible log parsing
Timestamp analysis
Time-based attack detection
Detection of brute-force patterns
Configurable detection thresholds
Exporting reports to JSON or CSV
Automated security alerts
Modularizing the analyzer into functions and classes