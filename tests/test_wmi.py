import unittest
from unittest import mock
from unittest.mock import patch
import json
from requests import Session
from pvaw.wmi import decode_wmi, get_wmis, WMIInfo


class TestWMI(unittest.TestCase):
    TEST_3_DIGIT_WMI_DECODE_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeWMI/1FD?format=json"
    )

    TEST_6_DIGIT_WMI_DECODE_URL = (
        "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeWMI/1G9340?format=json"
    )

    TEST_GET_WMIS_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/GetWMIsForManufacturer/honda?format=json"

    def test_wmi_exceptions(self):
        with self.assertRaises(TypeError):
            decode_wmi(1)
        with self.assertRaises(ValueError):
            decode_wmi("abcd")
        with self.assertRaises(TypeError):
            get_wmis(1)

    @patch.object(Session, "get")
    def test_decode_wmi_3_digit(self, mock_get):
        with open("tests/decode_3_digit_wmi_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        wmi_info = decode_wmi("1FD")
        self.assertTrue(
            mock.call(self.TEST_3_DIGIT_WMI_DECODE_URL) in mock_get.mock_calls
        )

        self.assertEqual(wmi_info.wmi, "1FD")
        self.assertEqual(wmi_info.manufacturer_name, "FORD MOTOR COMPANY, USA")
        self.assertEqual(wmi_info.vehicle_type, "Incomplete Vehicle")

    @patch.object(Session, "get")
    def test_decode_wmi_6_digit(self, mock_get):
        with open("tests/decode_6_digit_wmi_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        wmi_info = decode_wmi("1G9340")
        self.assertTrue(
            mock.call(self.TEST_6_DIGIT_WMI_DECODE_URL) in mock_get.mock_calls
        )

        self.assertEqual(wmi_info.wmi, "1G9340")
        self.assertEqual(wmi_info.manufacturer_name, "GRYPHON BIKES & CHOPPERS")
        self.assertEqual(wmi_info.vehicle_type, "Motorcycle")

    @patch.object(Session, "get")
    def test_get_wmis(self, mock_get):
        with open("tests/get_wmis_response.json") as f:
            expected_results = json.load(f)

        mock_get.return_value.json.return_value = expected_results

        wmi_infos = get_wmis("honda")

        self.assertTrue(mock.call(self.TEST_GET_WMIS_URL) in mock_get.mock_calls)

        for w in wmi_infos:
            self.assertTrue(isinstance(w, WMIInfo))

        first = wmi_infos[0]

        self.assertEqual(first.get_dict(), expected_results["Results"][0])

        self.assertEqual(first.wmi, "JHM")
        self.assertEqual(first.manufacturer_name, "HONDA MOTOR CO., LTD")
        self.assertEqual(first.vehicle_type, "Passenger Car")
