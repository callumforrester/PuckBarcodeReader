import unittest
from dls_util.config import IntConfigItem, MultiValuesConfigItem

class TestIntConfigItem(unittest.TestCase):

    def test_item_is_initialised_correctly_without_units(self):
        # Arrange
        tag = "A tag"
        default_value = 5

        # Act
        item = IntConfigItem(tag, default_value)

        # Assert
        self.assertEqual(item.tag(), tag)
        self.assertIsNone(item.value())

    def test_valid_integer_value_is_set_correctly(self):
        # Arrange
        item = self._create_item()
        valid_value = 15

        # Act
        item.set(valid_value)

        # Assert
        self.assertEqual(item.value(), valid_value)

    def test_reset_sets_the_value_to_default(self):
        # Arrange
        expected_default = 12
        item = self._create_item(default_value=expected_default)
        new_value = 6
        item.set(new_value)

        # Act
        item.reset()

        # Assert
        self.assertEqual(item.value(), expected_default)

    def test_when_setting_double_value_then_value_is_rounded(self):
        # Arrange
        item = self._create_item()
        double_value = 1.9
        expected_value = int(double_value)

        # Act
        item.set(double_value)

        # Assert
        self.assertEqual(item.value(), expected_value)

    def test_value_can_be_set_from_string_of_integer(self):
        # Arrange
        item = self._create_item()
        string_value = "77"
        expected_value = 77

        # Act
        item.from_file_string(string_value)

        # Assert
        self.assertEqual(item.value(), expected_value)

    def test_when_setting_string_that_is_not_an_integer_then_value_is_set_to_default(self):
        # Arrange
        expected_default = 123
        item = self._create_item(default_value=expected_default)
        invalid_string = "456.4"

        # Act
        item.from_file_string(invalid_string)

        # Assert
        self.assertEqual(item.value(), expected_default)

    def _create_item(self, tag = "A tag", default_value = 5):
        return IntConfigItem(tag, default_value)


class TestMultiValuesConfigItems(unittest.TestCase):

    def test_item_is_initialised_correctly(self):
        # Arrange
        tag = "A tag"
        default_value = [1, 4]
        available_values = list(range(1, 5))

        # Act
        item = MultiValuesConfigItem(tag, default_value, available_values)

        # Assert
        self.assertEqual(item.tag(), tag)
        self.assertIsNone(item.value())
        self.assertEqual(item.available_values, available_values)

    def test_valid_value_is_set_correctly(self):
        # Arrange
        item = self._create_item()
        valid_value = [2, 9]

        # Act
        item.set(valid_value)

        # Assert
        self.assertEqual(item.value(), valid_value)

    def test_setting_value_ignores_entries_that_are_not_in_the_list_of_available_values(self):
        # Arrange
        available_entries = [1, 2, 3, 4, 9, 10]
        value_with_invalid_entries = [1, 3, 17, 4, 45]
        expected_value = [1, 3, 4]
        item = self._create_item(available_values=available_entries)

        # Act
        item.set(value_with_invalid_entries)

        # Assert
        self.assertEqual(item.value(), expected_value)

    def test_when_setting_value_with_no_valid_entries_then_value_defaults(self):
        # Arrange
        available_entries = [1, 2, 3, 4, 9, 10]
        default_value = [9, 10]
        value_with_invalid_entries = [123, 987]
        item = self._create_item(default_value=default_value, available_values=available_entries)

        # Act
        item.set(value_with_invalid_entries)

        # Assert
        self.assertEqual(item.value(), default_value)

    def test_reset_sets_the_value_to_default(self):
        # Arrange
        expected_default = [4, 6.1]
        item = self._create_item(default_value=expected_default)

        # Act
        item.reset()

        # Assert
        self.assertEqual(item.value(), expected_default)

    def test_string_representation_is_correct(self):
        # Arrange
        tag = "My Item"
        value = [1, 5, 10]
        item = self._create_item(tag=tag)
        item.set(value)
        expected_string = "My Item=[1, 5, 10]\n"

        # Act
        result = item.to_file_string()

        # Assert
        self.assertEqual(result, expected_string)

    def test_value_can_be_set_from_string_representation_of_list_of_values(self):
        # Arrange
        item = self._create_item()
        string_value = "[2, 4, 5]"
        expected_value = [2, 4, 5]

        # Act
        item.from_file_string(string_value)

        # Assert
        self.assertEqual(item.value(), expected_value)

    def test_setting_value_from_string_ignores_entries_that_are_not_in_the_list_of_available_values(self):
        # Arrange
        available_entries = [1, 2, 3, 4, 9, 10]
        string_value_with_invalid_entries = "[1, 3, 17, 4, 45]"
        expected_value = [1, 3, 4]
        item = self._create_item(available_values=available_entries)

        # Act
        item.from_file_string(string_value_with_invalid_entries)

        # Assert
        self.assertEqual(item.value(), expected_value)

    def test_when_setting_value_from_string_with_no_valid_entries_then_value_defaults(self):
        # Arrange
        available_entries = [1, 2, 3, 4, 9, 10]
        default_value = [9, 10]
        string_value_with_invalid_entries = "[123, 987]"
        item = self._create_item(default_value=default_value, available_values=available_entries)

        # Act
        item.from_file_string(string_value_with_invalid_entries)

        # Assert
        self.assertEqual(item.value(), default_value)

    def _create_item(self, tag = "A tag", default_value = [1, 4], available_values = range(1,11)):
        return MultiValuesConfigItem(tag, default_value, available_values)


