"""
Main driver for program  execution, interpreter should point to this file for project execution
"""
import os

from ui.application import Application


def main():
    # Set working directory, relatively, to root of project
    this_path = os.path.abspath(os.path.dirname(__file__))
    this_path += '/../'
    os.chdir(this_path)

    # Instantiate UI
    Application()


if __name__ == "__main__":
    main()
