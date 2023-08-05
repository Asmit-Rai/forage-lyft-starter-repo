import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = self._extracted_from_test_engine_should_not_be_serviced_2(30001)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = self._extracted_from_test_engine_should_not_be_serviced_2(30000)
        self.assertFalse(car.needs_service())

    # TODO Rename this here and in `test_engine_should_be_serviced` and `test_engine_should_not_be_serviced`
    def _extracted_from_test_engine_should_not_be_serviced_2(self, arg0):
        last_service_date = datetime.now().date()
        current_mileage = arg0
        last_service_mileage = 0
        result = Calliope(last_service_date, current_mileage, last_service_mileage)


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = self._extracted_from_test_battery_should_not_be_serviced_2(5)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = self._extracted_from_test_battery_should_not_be_serviced_2(3)
        self.assertFalse(car.needs_service())

    # TODO Rename this here and in `test_battery_should_be_serviced` and `test_battery_should_not_be_serviced`
    def _extracted_from_test_battery_should_not_be_serviced_2(self, arg0):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - arg0)
        warning_light_is_on = False
        return Palindrome(last_service_date, warning_light_is_on)

    def test_engine_should_be_serviced(self):
        car = self._extracted_from_test_engine_should_not_be_serviced_2(True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = self._extracted_from_test_engine_should_not_be_serviced_2(False)
        self.assertFalse(car.needs_service())

    # TODO Rename this here and in `test_engine_should_be_serviced` and `test_engine_should_not_be_serviced`
    def _extracted_from_test_engine_should_not_be_serviced_2(self, arg0):
        last_service_date = datetime.now().date()
        warning_light_is_on = arg0
        return Palindrome(last_service_date, warning_light_is_on)


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Rorschach(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.now().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.now().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Thovex(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
