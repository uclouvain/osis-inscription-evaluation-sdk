"""
    Evaluation enrollments service

    A set of API endpoints that allow you to enroll students to evaluations  # noqa: E501

    The version of the OpenAPI document: 1.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.api.mes_programmes_api import MesProgrammesApi  # noqa: E501


class TestMesProgrammesApi(unittest.TestCase):
    """MesProgrammesApi unit test stubs"""

    def setUp(self):
        self.api = MesProgrammesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_liste_inscriptions_programmes(self):
        """Test case for liste_inscriptions_programmes

        """
        pass


if __name__ == '__main__':
    unittest.main()
