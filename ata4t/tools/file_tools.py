"""Contains functions for reading and writing files."""

import json

def read_credentials(credentials_json_file):
    """Reads a JSON file containing credentials and returns a dictionary. The keys returned are userID and password.
    
    Parameters
    ----------
    credentials_json_file : str
        The path to the JSON file containing the credentials.

    Returns
    -------
    dict
        A dictionary containing the credentials.

    Examples
    --------
    >>> import json
    >>> credentials_line = '{"userID":"123456","password":"pass1234"}'
    >>> with open('credentials.json', 'w') as file:
    ...     file.write(credentials_line)
    26
    >>> read_credentials('credentials.json')
    {'userID':"123456","password":"pass1234"}

    """
    with open(credentials_json_file, 'r') as file:
        credentials = json.load(file)
    return credentials

if __name__ == '__main__':
    credentials = read_credentials('credentials.json')
    print(credentials)
    