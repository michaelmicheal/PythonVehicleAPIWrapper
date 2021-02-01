from . import session
from typing import Dict, List
from pvaw.constants import VEHICLE_API

class WMI:
    def __init__(self, wmi_dict: Dict[str, str]) -> None:
        self.wmi_dict = wmi_dict
        self.wmi = wmi_dict['WMI']
        self.CreatedOn = wmi_dict['CreatedOn']
        self.DateAvailableToPublic = wmi_dict['DateAvailableToPublic']
        self.ManufacturerName = wmi_dict['ManufacturerName']
        self.UpdatedOn = wmi_dict['UpdatedOn']
        self.VehicleType = wmi_dict['VehicleType']

class WMIInfo(WMI):
    def __init__(self, wmi_dict: Dict[str, str]) -> None:
        self.wmi_dict = wmi_dict
        self.wmi = wmi_dict['WMI']
        self.CreatedOn = wmi_dict['CreatedOn']
        self.DateAvailableToPublic = wmi_dict['DateAvailableToPublic']
        self.ManufacturerName = wmi_dict['ManufacturerName']
        self.UpdatedOn = wmi_dict['UpdatedOn']
        self.VehicleType = wmi_dict['VehicleType']
        self.CommonName = wmi_dict['CommonName']
        self.Make = wmi_dict['Make']
        self.ParentCompanyName = wmi_dict['ParentCompanyName']
        self.URL = wmi_dict['URL']

class WMISearchResult(WMI):
    def __init__(self, wmi_dict: Dict[str, str]) -> None:
        self.wmi_dict = wmi_dict
        self.wmi = wmi_dict['WMI']
        self.CreatedOn = wmi_dict['CreatedOn']
        self.DateAvailableToPublic = wmi_dict['DateAvailableToPublic']
        self.ManufacturerName = wmi_dict['Name']
        self.UpdatedOn = wmi_dict['UpdatedOn']
        self.VehicleType = wmi_dict['VehicleType']
        self.Country = wmi_dict['Country']

def decode_wmi(wmi: str) -> WMI:
    ## TODO: Error handle the parameters
    path = f'{VEHICLE_API}DecodeWMI/{wmi}?format=json'
    response = session.get(path)
    wmi_dict = response.json()['Results'][0]
    wmi_dict['WMI'] = wmi
    return WMIInfo(wmi_dict)


def get_manufacturer_wmis(search: str) -> List[WMI]:
    path = f'{VEHICLE_API}GetWMIsForManufacturer/{search}?format=json'
    response = session.get(path)
    results = response.json()['Results']
    print(response.json())
    return [WMISearchResult(result) for result in results]
