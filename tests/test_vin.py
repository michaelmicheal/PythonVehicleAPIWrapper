import unittest
from unittest import mock
from unittest.mock import patch
import json
from requests import Session
from pvaw.vin import Vin, decode_vins, Vehicle


class TestVin(unittest.TestCase):
    TEST_VIN_DECODE_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/5UXWX7C5*BA?format=json"
    TEST_VIN_DECODE_WITH_YEAR_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/5UXWX7C5*BA?format=json&modelyear=2011"
    TEST_BATCH_VIN_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/"
    TEST_BATCH_VIN_POST = {"format": "json", "data": "5UXWX7C5*BA,2011;5YJSA3DS*EF"}

    def setUp(self):
        self.TEST_VIN = Vin("5UXWX7C5*BA")
        self.TEST_VIN_2 = Vin("5YJSA3DS*EF")
        self.TEST_MODEL_YEAR_VIN = Vin("5UXWX7C5*BA", 2011)

    def test_Vin_exceptions(self):
        with self.assertRaises(TypeError):
            Vin(1)
        with self.assertRaises(ValueError):
            Vin("123456789012345678")
        with self.assertRaises(TypeError):
            Vin("5UXWX7C5*BA", 2005.0)
        with self.assertRaises(ValueError):
            Vin("5UXWX7C5*BA", 1941)

    @mock.patch("requests.get")
    def test_decode_vin(self, mock_get):
        with open("tests/responses/decode_vin_response.json") as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        vehicle = self.TEST_VIN.decode()

        self.assertTrue(mock.call(self.TEST_VIN_DECODE_URL) in mock_get.mock_calls)

        self.assertEqual(vehicle.results_dict, expected_response["Results"][0])
        self.assertEqual(vehicle.model_year, 2011)
        self.assertEqual(vehicle.make, "BMW")
        self.assertEqual(
            vehicle.manufacturer, "BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA"
        )
        self.assertEqual(vehicle.model, "X3")
        self.assertEqual(vehicle.full_or_partial_vin, "5UXWX7C5*BA")
        self.assertEqual(vehicle.vehicle_type, "MULTIPURPOSE PASSENGER VEHICLE (MPV)")

        expected_results = expected_response["Results"]

        # testing get_results()
        self.assertEqual(expected_results[0], vehicle.get_results())

        # Making sure that get_df() doesn't error out
        vehicle.get_df()

        vehicle.get_df(raw=True)

        vehicle.get_df(raw=True, drop_na=False)

        # Making sure that string and html reps don't error out
        str(vehicle)
        vehicle._repr_html_()

    @mock.patch("requests.get")
    def test_decode_vin_model_year(self, mock_get):
        with open("tests/responses/decode_vin_response_with_year.json") as f:
            expected_response = json.load(f)

        mock_get.return_value.json.return_value = expected_response

        vehicle = self.TEST_MODEL_YEAR_VIN.decode()

        self.assertTrue(
            mock.call(self.TEST_VIN_DECODE_WITH_YEAR_URL) in mock_get.mock_calls
        )

        self.assertEqual(vehicle.results_dict, expected_response["Results"][0])
        self.assertEqual(vehicle.model_year, 2011)
        self.assertEqual(vehicle.make, "BMW")
        self.assertEqual(
            vehicle.manufacturer, "BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA"
        )
        self.assertEqual(vehicle.model, "X3")
        self.assertEqual(vehicle.full_or_partial_vin, "5UXWX7C5*BA")
        self.assertEqual(vehicle.vehicle_type, "MULTIPURPOSE PASSENGER VEHICLE (MPV)")

    def test_decode_vins_exceptions(self):
        with self.assertRaises(TypeError):
            decode_vins(1)
        with self.assertRaises(TypeError):
            decode_vins([1])
        with self.assertRaises(ValueError):
            decode_vins([])

    @mock.patch("requests.post")
    def test_decode_vins(self, mock_post):
        with open("tests/responses/decode_vin_batch_reponse.json") as f:
            expected_response = json.load(f)

        mock_post.return_value.json.return_value = expected_response
        vehicles = decode_vins([self.TEST_MODEL_YEAR_VIN, self.TEST_VIN_2])

        self.assertTrue(
            mock.call(self.TEST_BATCH_VIN_URL, self.TEST_BATCH_VIN_POST)
            in mock_post.mock_calls
        )
        # testing iteration
        for vehicle in vehicles:
            self.assertTrue(isinstance(vehicle, Vehicle))

        # testing indexing
        vehicle_1 = vehicles[0]

        self.assertEqual(vehicle_1.results_dict, expected_response["Results"][0])
        self.assertEqual(vehicle_1.model_year, 2011)
        self.assertEqual(vehicle_1.make, "BMW")
        self.assertEqual(
            vehicle_1.manufacturer, "BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA"
        )
        self.assertEqual(vehicle_1.model, "X3")
        self.assertEqual(vehicle_1.full_or_partial_vin, "5UXWX7C5*BA")
        self.assertEqual(vehicle_1.vehicle_type, "MULTIPURPOSE PASSENGER VEHICLE (MPV)")

        vehicle_2 = vehicles[1]

        self.assertEqual(vehicle_2.results_dict, expected_response["Results"][1])
        self.assertEqual(vehicle_2.model_year, 2014)
        self.assertEqual(vehicle_2.make, "TESLA")
        self.assertEqual(vehicle_2.manufacturer, "TESLA, INC.")
        self.assertEqual(vehicle_2.model, "Model S")
        self.assertEqual(vehicle_2.full_or_partial_vin, "5YJSA3DS*EF")
        self.assertEqual(vehicle_2.vehicle_type, "PASSENGER CAR")

        expected_results = expected_response["Results"]

        # testing get_results()
        self.assertEqual(expected_results, vehicles.get_results())

        self.assertEqual(expected_results[0], vehicle_1.get_results())

        # Making sure that get_df() doesn't error out
        vehicles.get_df()

        vehicles.get_df(raw=True)

        vehicles.get_df(raw=True, drop_na=False)

        # Making sure that string and html reps don't error out
        str(vehicles)
        vehicles._repr_html_()
        str(vehicle_1)
        vehicle_1._repr_html_()


if __name__ == "__main__":
    unittest.main()