import unittest
from unittest.mock import Mock, patch

from Add_people_drink import add_people

class Test_Select_Person_From_Menu(unittest.TestCase):
    # When a function/class is imported using `from X import Y` the resolution path to the
    # target being patched is actually in the namespace where the import occurs instead of
    # where the target is defined.
    #
    # This means that if module z.py import Y using `from X import Y` syntax the patch target
    # path tto patch Y is z.Y instead of X.Y
    @patch("Add_people_drink.add_people")
    def test_when_add_more_is_no(self, mock_add_more):
    #     # Arrange
    #     add_more = input(Would you like to add a new person? Please type "Yes" or "No" \n')
    #     add_more = "Yes"
    #     input_mock_add_more.return_value = "No"
    #     # Act
    #     actual = select_person_from_menu(people)
    #     # Assert
        self.assertTrue
# provides a command-line interface to the test script
if __name__ == "__main__":
    unittest.main()