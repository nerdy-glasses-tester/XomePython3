import unittest
from tests.webtests.login_test import LoginTests
from tests.webtests.search_test import SearchTests
from tests.webtests.filterResultsBySqFeet_test import FilterResultsBySqFeetTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(FilterResultsBySqFeetTests)
#tc4 = unittest.TestLoader().loadTestsFromTestCase()

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])
#smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#pytest -s -v tests/test_suite_web_sanity.py --browser chrome --os none --html=htmlreport.html
