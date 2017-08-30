import unittest
import os
import pypin

class TestPypinExceptions(unittest.TestCase):

    def setUp(self):
        # TODO: Don't use a live pin request between each test, store in cassete and make sure it
        # matches the one that comes back from the api in another test so we only make one request.
        self.api = pypin.API(access_token=os.environ['PIN_TOKEN'])

    def test_content_not_found_exception(self):
        with self.assertRaises(pypin.exceptions.PyPinContentNotFoundError):
            self.api.get_public_pin('this_is_a_garbage_pin_number')

if __name__ == '__main__':
    unittest.main()
