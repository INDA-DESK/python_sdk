"""
    INDA DESK - INtelligent Data Analysis for document parsing

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is greater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.   Financial documents, invoices, taxes, and certifications are common documents  normally stored as Portable Document Format (PDF). Often such documents are used as financial approval or as input for next bureaucratic steps. These operations are commonly made by human beings where they should read the documents and make decision based on the information inside the document.      INDA DESK was born to automatize the operations of information extraction from commonly used financial documents  such as *single document of contribution regularity* (DURC), *single document of fiscal regularity* (DURF) or *visure camerali*.  The automatization provides scalability and the speeding up of the processes related with such documents.   The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is <span style=\"color:blue\">https<area>://api.inda.ai/desk/v1/</span>. We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@intervieweb.it
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import inda_desk
from inda_desk.model.base_file import BaseFile
globals()['BaseFile'] = BaseFile
from inda_desk.model.doc import Doc


class TestDoc(unittest.TestCase):
    """Doc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDoc(self):
        """Test Doc"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Doc()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()