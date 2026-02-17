formatcsv

A Linux-friendly Python CLI tool for formatting CSV datasets into clean, aligned tables for reporting and automation workflows.

The tool is designed for large datasets and automation pipelines where structured output is required without manual spreadsheet processing.

Installation
1. Clone repository
git clone https://github.com/yourusername/formatcsv.git
cd formatcsv

2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run CLI
python cli.py --help

Usage

Basic usage:

python cli.py format data/customers-100.csv --output data/customers_100_formatted.txt

CLI Commands
Format CSV file

Formats CSV data into aligned text output.

python cli.py format <input.csv> --output <output.txt>


Example:

python cli.py format data/test.csv --output data/formatted.txt

Validate CSV structure

Checks dataset integrity before processing.

python cli.py validate <input.csv>

Show help
python cli.py --help


Or per command:

python cli.py format --help

Automation Usage

Example cron or pipeline usage:

python cli.py format nightly.csv --output report.txt


Example script automation:

#!/bin/bash
python cli.py format data.csv --output result.txt
echo "Report generated"


Works well in:

cron jobs

CI/CD pipelines

automated reporting tasks

infrastructure automation workflows

Logs

Errors and execution details are logged automatically.

Typical logging behavior:

CLI errors are logged and printed

Supports automation-friendly output

Exit codes indicate success/failure

Example:

ERROR: Invalid CSV structure

Exit Codes
Code	Meaning
0	Success
1	General error
2	Input validation error

Useful for automation scripts.

Troubleshooting
Command not found

Run using:

python cli.py ...

or if you just want to try this for yourself 

py cli.py format data/customers-100.csv --output data/customers_100_formatted.txt

or ensure Python is installed:

python --version

Dependency errors

Reinstall dependencies:

pip install -r requirements.txt

Permission errors

Check file access:

chmod +r data.csv

Project Features

Streaming processing for large files

Automation-friendly CLI

Consistent logging and exit codes

Handles large datasets efficiently

Packaging-ready command structure

Structured modular codebase

Key Features

Automated dataset parsing and formatting

File output generation

Unit tests ensure reliable results

Repeatable automation workflows

Skills Demonstrated

Python scripting & automation

Workflow optimization

File handling & data processing

Unit testing

Structured, maintainable code design

CLI tool development

Automation pipeline thinking

This project reflects practical automation thinking transferable to IT operations, infrastructure, and system administration environments.

##Linux & Infrastructure Learning

I actively use Linux in virtualized environments to build hands-on experience with system administration and infrastructure operations.

Current Focus

Linux server setup and configuration

Command-line operations and scripting

Networking basics and troubleshooting

Automation and workflow efficiency

System administration fundamentals

This practice supports my transition toward infrastructure, automation, and security-oriented roles.
