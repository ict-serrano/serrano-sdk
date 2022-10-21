import requests


class Telemetry:
    """
    Instantiate a Telemetry operation.

    :param parameter: parameter.
    :type parameter: int
    """

    def __init__(self, parameter):
        self.parameter = parameter
        self.session = requests.Session()

    def employ(self):
        """
        Employ telemetry using a given parameter.

        :param parameter: The parameter to use.
        :type parameter: int

        :return: The result of calling telemetry.
        :rtype: object
        """
        response = self.session.get("http://api.open-notify.org/astros.json")
        return response

    def close(self):
        self.session.close()

