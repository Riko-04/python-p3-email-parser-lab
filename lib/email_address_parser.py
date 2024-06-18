# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        # Regular expression for matching email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        # Find all matches in the input data
        emails = re.findall(email_pattern, self.data)
        # Remove duplicates by converting the list to a set, then back to a sorted list
        return sorted(list(set(emails)))
