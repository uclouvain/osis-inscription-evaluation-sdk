"""
    Evaluation enrollments service

    A set of API endpoints that allow you to enroll students to evaluations  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.model.contact_faculte import ContactFaculte
from osis_inscription_evaluation_sdk.model.periode_inscription import PeriodeInscription
globals()['ContactFaculte'] = ContactFaculte
globals()['PeriodeInscription'] = PeriodeInscription
from osis_inscription_evaluation_sdk.model.inscription_formation import InscriptionFormation


class TestInscriptionFormation(unittest.TestCase):
    """InscriptionFormation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInscriptionFormation(self):
        """Test InscriptionFormation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InscriptionFormation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
