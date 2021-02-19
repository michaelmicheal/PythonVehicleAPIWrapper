import unittest
from unittest import mock
from unittest.mock import patch
import json
from requests import Session
from pvaw.make import get_makes, Make


class TestMake(unittest.TestCase):
    TEST_MANUFACTURER_NAME_MAKES_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakeForManufacturer/honda?format=json"
    TEST_MANUFACTURER_ID_MAKES_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakeForManufacturer/988?format=json"
    )
    TEST_MANUFACTURER_NAME_AND_YEAR_MAKES_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForManufacturerAndYear/honda?year=2004&format=json"
    TEST_VEHICLE_TYPE_MAKES_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetMakesForVehicleType/car?format=json"
    )

    def test_exceptions(self):

        with self.assertRaises(TypeError):
            get_makes(10.0)
        with self.assertRaises(TypeError):
            get_makes(manufacturer_name_or_id="honda", model_year=2005.0)
        with self.assertRaises(ValueError):
            get_makes(manufacturer_name_or_id="honda", model_year=1952)
        with self.assertRaises(TypeError):
            get_makes(vehicle_type=1)
        with self.assertRaises(ValueError):
            get_makes(manufacturer_name_or_id="honda", vehicle_type="PASSENGER CAR")
        with self.assertRaises(ValueError):
            get_makes(model_year=1999)

    @mock.patch("requests.get")
    def test_make_by_manufacturer_name(self, mock_get):
        with open("tests/get_makes_for_manufacturer_name_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        makes = get_makes("honda")

        self.assertTrue(
            mock.call(self.TEST_MANUFACTURER_NAME_MAKES_URL) in mock_get.mock_calls
        )

        for make in makes:
            self.assertTrue(isinstance(make, Make))

        first = makes[0]

        self.assertEqual(first.make_id, 474)
        self.assertEqual(first.make_name, "HONDA")
        self.assertEqual(first.manufacturer, "HONDA MOTOR CO., LTD")

    @mock.patch("requests.get")
    def test_make_by_manufacturer_id(self, mock_get):
        with open("tests/get_makes_for_manufacturer_id_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        makes = get_makes(988)

        self.assertTrue(
            mock.call(self.TEST_MANUFACTURER_ID_MAKES_URL) in mock_get.mock_calls
        )

        for make in makes:
            self.assertTrue(isinstance(make, Make))

        first = makes[0]

        self.assertEqual(first.make_id, 474)
        self.assertEqual(first.make_name, "HONDA")
        self.assertEqual(first.manufacturer, "HONDA OF AMERICA MFG., INC.")

    @mock.patch("requests.get")
    def test_make_by_manufacturer_name_and_year(self, mock_get):
        with open("tests/get_makes_for_manufacturer_name_and_year_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        makes = get_makes("honda", 2004)

        self.assertTrue(
            mock.call(self.TEST_MANUFACTURER_NAME_AND_YEAR_MAKES_URL)
            in mock_get.mock_calls
        )

        for make in makes:
            self.assertTrue(isinstance(make, Make))

        first = makes[0]

        self.assertEqual(first.make_id, 474)
        self.assertEqual(first.make_name, "HONDA")
        self.assertEqual(first.manufacturer, "HONDA MOTOR CO., LTD")

    @mock.patch("requests.get")
    def test_make_by_vehicle_type(self, mock_get):
        with open("tests/get_makes_for_vehicle_type_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        makes = get_makes(vehicle_type="car")

        self.assertTrue(
            mock.call(self.TEST_VEHICLE_TYPE_MAKES_URL) in mock_get.mock_calls
        )

        for make in makes:
            self.assertTrue(isinstance(make, Make))

        first = makes[0]

        self.assertEqual(first.make_id, 440)
        self.assertEqual(first.make_name, "ASTON MARTIN")
        self.assertEqual(first.vehicle_type, "Passenger Car")
