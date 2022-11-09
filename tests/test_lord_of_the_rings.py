import unittest
from lord_of_the_rings_sdk import LordOfTheRings 

class TestParameters(unittest.TestCase):

	def test_parameters(self):
		api = LordOfTheRings('fDCIpmKnesCL7xZEl4MN')
		self.assertEqual(api.parameters('', '', '', '', ''), '')

unittest.main()