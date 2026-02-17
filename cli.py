#!/usr/bin/env python3
import argparse
import sys
import logging
import os
from colorama import init, Fore
from formatter_core import output_formatted_file, output_html_file
from formatcsv import setup_logging, log_and_print_error

init(autoreset=True)


def choose_output() -> int:
    """Ask the user whether they want a text file or HTML output."""
    while True:
        try:
            choice = int(input(Fore.BLUE + "Choose output, enter 1 for file, 2 for HTML page: "))
            if choice in (1, 2):
                return choice
            else:
                print(Fore.RED + "Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number (1 or 2).")


def format_command(args: argparse.Namespace) -> None:
    """Format CSV dataset interactively (text or HTML)."""
    
    print(Fore.BLUE + f"Processing input: {args.input}")
    logging.info(f"Processing started: {args.input}")
    input_path = args.input
    try:
        with open(args.input, "r", encoding="utf-8") as f:
            choice = choose_output()
            if choice == 1:
                # Output to text file
                output_file = args.output or args.input.rsplit('.', 1)[0] + "_formatted.txt"
                output_formatted_file(f, output_file)
                print(Fore.GREEN + f"Processing completed. Formatted file saved as {output_file}")
                logging.info(f"Formatted file saved as {output_file}")
           
           
            elif choice == 2:
                # Use the HTML version in the same folder as CSV
                output_html = os.path.splitext(args.input)[0] + ".html"
                from formatter_core import output_html_file
                output_html_file(f, output_html=output_html)
                logging.info(Fore.GREEN + f"Formatted HTML saved: {output_html}")
                print(Fore.GREEN + f"Formatted HTML saved: {output_html}")

            else:
                print(Fore.RED + "Invalid choice, exiting.")
                sys.exit(1)

    except FileNotFoundError:
        log_and_print_error(f"Input file not found: {input_path}", exit_code=1)

    except Exception as e:
        log_and_print_error("Unexpected error during formatting", e, exit_code=2)


    except FileNotFoundError:
        log_and_print_error(f"Input file not found: {args.input}")
    except Exception as e:
        log_and_print_error("Unexpected error occurred during formatting", e)



def validate_command(args: argparse.Namespace) -> None:
    """Validate a CSV dataset."""
    logging.info(Fore.YELLOW + f"Validation command executed on '{args.input}'")
    # Placeholder implementation
    log_and_print_error("Validation not implemented yet.", None)
    sys.exit(1)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Dataset Formatter CLI (interactive)")
    parser.add_argument("--log", default="formatter.log", help="Log file path")
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # FORMAT subcommand
    format_parser = subparsers.add_parser("format", help="Format a CSV dataset interactively")
    format_parser.add_argument("input", help="Input CSV file")
    format_parser.add_argument("--output", default=None, help="Optional text output file (if choosing 1)")
    format_parser.set_defaults(func=format_command)

    return parser


def main() -> None:
    """Entry point for CLI execution."""
    parser = build_parser()
    args = parser.parse_args()

    # Centralized logging
    setup_logging(args.log)

    # Execute the chosen subcommand
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
