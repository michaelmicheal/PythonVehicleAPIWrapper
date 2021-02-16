import unittest
from unittest import mock
from unittest.mock import patch
import json
from requests import Session
from pvaw.manufactuer import (
    Manufacturer,
    get_manufacturer_details,
    get_manufacturer_types,
    get_manufacturers,
)


class TestManufacturer(unittest.TestCase):
    TEST_GET_MANUFACTURERS_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=3"
    )
    TEST_GET_MANUFACTURERS_WITH_M_TYPE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&ManufacturerType=Intermediate&page=1"
    TEST_GET_MANUFACTURER_DETAILS_FROM_NAME_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetManufacturerDetails/honda?format=json"
    TEST_GET_MANUFACTURER_DETAILS_FROM_ID_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/GetManufacturerDetails/987?format=json"
    )

    def test_exceptions(self):

        with self.assertRaises(ValueError):
            get_manufacturers(1)

        with self.assertRaises(ValueError):
            get_manufacturers("test")

        with self.assertRaises(TypeError):
            get_manufacturers(page=1.0)

        with self.assertRaises(TypeError):
            get_manufacturer_details(1.0)

    @patch.object(Session, "get")
    def test_get_manufacturers(self, mock_get):
        with open("tests/get_manufacturers_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

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

    @patch.object(Session, "get")
    def test_get_manufacturers_with_m_type(self, mock_get):
        with open("tests/get_manufacturers_with_m_type_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        manufacturers = get_manufacturers(m_type="Completed Vehicle Manufacturer")

        self.assertTrue(
            mock.call(self.TEST_GET_MANUFACTURERS_WITH_M_TYPE_URL)
            in mock_get.mock_calls
        )

        for m in manufacturers:
            self.assertTrue(isinstance(m, Manufacturer))

        first = manufacturers[0]

        self.assertEqual(first.name, "UNIDAD DE VEHICULOS INDUSTRIALES, S.A.")

        self.assertEqual(first.id, 6577)

        self.assertTrue("Bus" in first.vehicle_types)

    @patch.object(Session, "get")
    def test_get_manufacturer_details_from_name(self, mock_get):
        with open("tests/get_manufacturer_details_from_name_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

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

    @patch.object(Session, "get")
    def test_get_manufacturer_details_from_id(self, mock_get):
        with open("tests/get_manufacturer_details_from_id_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

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