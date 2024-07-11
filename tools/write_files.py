import json
import os

import requests
from langchain.tools import tool

class WriteFiles:

    @tool("Write to a file ")
    def write_jokes_to_file(jokes):
        """Useful for writing jokes down to files"""
        with open("jokes.txt", 'w') as file:
            file.write(jokes)