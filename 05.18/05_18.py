import unittestfrom unittest.mock
import patchfrom main 
import register_userfrom modules 
import Userclass


@patch('builtins.input')
@patch('database.SqliteDatabase')
def test_register_user(self, mock_database, mock_input):
     mock_database.get_user_by_email.return_value = User(id=1, name="a", surname="b", email="c", password="d")
     mock_input.side_effect = ["a", "b", "c", "d"]
     user = register_user(mock_database)
     assert user.name == "a" 
     assert user.surname == "b" 
     assert mock_database.create_user.call_count == 1 
     assert mock_database.create_user.call_args.kwargs == {'name': 'a', 'surname': 'b', 'email': 'c', 'password': 'd'}
     assert mock_database.get_user_by_email.call_count == 1 
     assert mock_database.get_user_by_email.call_args.args[0] == "c"

if __name__ == "__main__":
    unittest.main()