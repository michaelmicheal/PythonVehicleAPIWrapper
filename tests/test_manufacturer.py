import unittest
from unittest import mock
from unittest.mock import patch
import json
from requests import Session
from pvaw.manufacturer import (
    Manufacturer,
    get_manufacturer_details,
    get_manufacturers,
)


class TestManufacturer(unittest.TestCase):
    TEST_GET_MANUFACTURERS_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=3"
    )
    TEST_GET_MANUFACTURERS_WITH_M_TYPE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&ManufacturerType=Completed%20Vehicle%20Manufacturer&page=1"
    TEST_GET_MANUFACTURER_DETAILS_FROM_NAME_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetManufacturerDetails/honda?format=json"
    TEST_GET_MANUFACTURER_DETAILS_FROM_ID_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetManufacturerDetails/987?format=json"
    )

    def test_exceptions(self):

        with self.assertRaises(TypeError):
            get_manufacturers(1)

        with self.assertRaises(TypeError):
            get_manufacturers(page=1.0)

        with self.assertRaises(TypeError):
            get_manufacturer_details(1.0)

    @mock.patch("requests.get")
    def test_get_manufacturers(self, mock_get):
        with open("tests/responses/get_manufacturers_response.json") as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        manufacturers = get_manufacturers(page=3)

        self.assertTrue(
            mock.call(self.TEST_GET_MANUFACTURERS_URL) in mock_get.mock_calls
        )

        for m in manufacturers:
            self.assertTrue(isinstance(m, Manufacturer))

        first = manufacturers[0]

        self.assertEqual(first.common_name, "None")

        self.assertEqual(first.name, "3T MFG.")

        self.assertEqual(first.id, 1178)

        self.assertTrue("Trailer" in first.vehicle_types)

        self.assertTrue("Incomplete Vehicle" in first.vehicle_types)

        expected_results = expected_response["Results"]

        # testing get_results()
        self.assertEqual(expected_results, manufacturers.get_results())

        self.assertEqual(expected_results[0], first.get_results())

        # Making sure that get_df() doesn't error out
        manufacturers.get_df()

        manufacturers.get_df(raw=True)

        manufacturers.get_df(raw=True, drop_na=False)

        # Making sure that string and html reps don't error out
        str(manufacturers)
        manufacturers._repr_html_()
        str(first)
        first._repr_html_()

    @mock.patch("requests.get")
    def test_get_manufacturers_with_m_type(self, mock_get):
        with open("tests/responses/get_manufacturers_with_m_type_response.json") as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        manufacturers = get_manufacturers(m_type="Completed Vehicle Manufacturer")

        print(mock_get.mock_calls)

        self.assertTrue(
            mock.call(self.TEST_GET_MANUFACTURERS_WITH_M_TYPE_URL)
            in mock_get.mock_calls
        )

        for m in manufacturers:
            self.assertTrue(isinstance(m, Manufacturer))

        first = manufacturers[0]

        self.assertEqual(first.name, "SIGNALISATION VER-MAC INC.")

        self.assertEqual(first.id, 1410)

        self.assertTrue("Trailer" in first.vehicle_types)

    @mock.patch("requests.get")
    def test_get_manufacturer_details_from_name(self, mock_get):
        with open(
            "tests/responses/get_manufacturer_details_from_name_response.json"
        ) as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        manufacturers = get_manufacturer_details("honda")

        self.assertTrue(
            mock.call(self.TEST_GET_MANUFACTURER_DETAILS_FROM_NAME_URL)
            in mock_get.mock_calls
        )
        for m in manufacturers:
            self.assertTrue(isinstance(m, Manufacturer))

        first = manufacturers[0]

        self.assertEqual(first.name, "HONDA MOTOR CO., LTD")

        self.assertEqual(first.common_name, "Honda")

        self.assertEqual(first.id, 987)

        self.assertTrue("Motorcycle" in first.vehicle_types)

        self.assertTrue("Passenger Car" in first.vehicle_types)

        self.assertTrue("Multipurpose Passenger Vehicle (MPV)" in first.vehicle_types)

    @mock.patch("requests.get")
    def test_get_manufacturer_details_from_id(self, mock_get):
        with open(
            "tests/responses/get_manufacturer_details_from_id_response.json"
        ) as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        manufacturers = get_manufacturer_details(987)

        self.assertTrue(
            mock.call(self.TEST_GET_MANUFACTURER_DETAILS_FROM_ID_URL)
            in mock_get.mock_calls
        )

        for m in manufacturers:
            self.assertTrue(isinstance(m, Manufacturer))

        first = manufacturers[0]

        self.assertEqual(first.name, "HONDA MOTOR CO., LTD")

        self.assertEqual(first.common_name, "Honda")

        self.assertEqual(first.id, 987)

        self.assertTrue("Motorcycle" in first.vehicle_types)

        self.assertTrue("Passenger Car" in first.vehicle_types)

        self.assertTrue("Multipurpose Passenger Vehicle (MPV)" in first.vehicle_types)