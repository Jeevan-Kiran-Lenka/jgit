import argparse
import os

from . import data

# Main function that serves as the entry point for the command line interface.
# It parses the command line arguments and executes the function associated with the specified command.
def main():
    args = parse_args()  # Parse the command line arguments
    args.func(args)      # Execute the function associated with the parsed command

# Function to parse command line arguments and configure subcommands.
# It uses argparse to define a command line interface with subcommands.
def parse_args():
    parser = argparse.ArgumentParser()  # Create a new argument parser
    
    # Add subparsers for different commands
    commands = parser.add_subparsers(dest='command')
    commands.required = True  # Ensure a command is required
    
    # Define the 'init' command and associate it with the init function
    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    
    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func = hash_object)
    hash_object_parser.add_argument('file')
    
    return parser.parse_args()  # Return the parsed arguments

# Function to handle the 'init' command.
# It initializes a new jgit repository and prints the location.
def init(args):
    data.init()
    print(f'Initialized empty jgit repository in {os.getcwd()}/{data.GIT_DIR}')
    
def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))