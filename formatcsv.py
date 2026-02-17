#!/usr/bin/env python3
import argparse
import logging
import sys
from formatter_core import output_formatted_file
from colorama import init, Fore

init(autoreset=True)

def parse_args():
    parser = argparse.ArgumentParser(
        description=Fore.WHITE + "Format CSV datasets"
    )

    parser.add_argument("input", help="Input CSV file")
    parser.add_argument(
        "--output",
        default="output.txt",
        help=Fore.CYAN + "Output file name"
    )
    parser.add_argument(
        "--log",
        default="formatter.log",
        help="Log file"
    )

    return parser.parse_args()


def setup_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)  # <-- prints logs to terminal
        ]
    )


def log_and_print_error(message: str, exception: Exception = None, exit_code: int = 1):
    """
    Logs an error message and prints a colored message to the console.

    Parameters:
        message (str): The error message to log and print.
        exception (Exception, optional): Optional exception object for logging the stack trace.
        exit_code (int, optional): Exit code to terminate the program. Defaults to 1.
    """
    if exception:
        logging.exception(f"{message}: {exception}")  # Logs stack trace
        print(Fore.RED + f"{message}: {exception}")
    else:
        logging.error(message)
        print(Fore.RED + message)

    # Exit if running as main program
    import sys
    sys.exit(exit_code)

def main():
    args = parse_args()
    setup_logging(args.log)

    logging.info("Processing started")
    print(Fore.BLUE + "Processing started")

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            output_formatted_file(f, args.output)

        logging.info("Processing completed successfully")
        print(Fore.GREEN + "Processing completed successfully")

    except FileNotFoundError:
        logging.error("Input file not found")
        print(Fore.RED + "Input file not found")
        sys.exit(1)

    except Exception as e:
        logging.exception("Unexpected error occurred")
        print(Fore.RED + f"Unexpected error occurred: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()
