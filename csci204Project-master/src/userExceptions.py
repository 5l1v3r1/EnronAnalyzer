"""
File that will keep a list of all user exceptions
"""


class OurInFileException(Exception):
    """
    Will be used when we have a problem with our in files
    """
    pass


class OurOutFileException(Exception):
    """
    Will be used when we have a problem withou our out files
    """
    pass


class NoDataException(Exception):
    """
    Will be used if trying to compute something we have no data for
    """
    pass

