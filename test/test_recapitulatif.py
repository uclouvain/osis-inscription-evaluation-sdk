"""
    Evaluation enrollments service

    A set of API endpoints that allow you to enroll students to evaluations  # noqa: E501

    The version of the OpenAPI document: 1.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_inscription_evaluation_sdk
from osis_inscription_evaluation_sdk.model.contact_faculte import ContactFaculte
from osis_inscription_evaluation_sdk.model.etudiant import Etudiant
from osis_inscription_evaluation_sdk.model.formation import Formation
from osis_inscription_evaluation_sdk.model.recapitulatif_inscriptions import RecapitulatifInscriptions
from osis_inscription_evaluation_sdk.model.session_de_travail import SessionDeTravail
globals()['ContactFaculte'] = ContactFaculte
globals()['Etudiant'] = Etudiant
globals()['Formation'] = Formation
globals()['RecapitulatifInscriptions'] = RecapitulatifInscriptions
globals()['SessionDeTravail'] = SessionDeTravail
from osis_inscription_evaluation_sdk.model.recapitulatif import Recapitulatif


class TestRecapitulatif(unittest.TestCase):
    """Recapitulatif unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecapitulatif(self):
        """Test Recapitulatif"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Recapitulatif()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
