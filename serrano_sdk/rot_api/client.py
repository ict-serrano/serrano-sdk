import requests

class ROT:
    """
    Instantiate a ROT operation.

    :param parameter: parameter.
    :type parameter: int
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier
        self.session = requests.Session()

    def employ(self):
        """
        Employ ROT using a given parameter.

        :param parameter: The parameter to use.
        :type parameter: int

        :return: The result of calling telemetry.
        :rtype: object
        """
        response =self.session.get("http://api.open-notify.org/astros.json")
        return response

    def close(self):
        self.session.close()

