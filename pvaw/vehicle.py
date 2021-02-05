from typing import Dict, Union
import pandas as pd
import numpy as np
from pvaw.utils import value_or_none
from pvaw.results import Results


class Vehicle(Results):
    def __init__(
        self,
        full_or_partial_vin: str,
        year: Union[str, int],
        results_dict: Dict[str, str],
    ) -> None:
        super().__init__(results_dict)

        self.full_or_partial_vin = full_or_partial_vin
        self.year = year
        self.ABS = value_or_none(results_dict, "ABS")
        self.ActiveSafetySysNote = value_or_none(results_dict, "ActiveSafetySysNote")
        self.AdaptiveCruiseControl = value_or_none(
            results_dict, "AdaptiveCruiseControl"
        )
        self.AdaptiveDrivingBeam = value_or_none(results_dict, "AdaptiveDrivingBeam")
        self.AdaptiveHeadlights = value_or_none(results_dict, "AdaptiveHeadlights")
        self.AdditionalErrorText = value_or_none(results_dict, "AdditionalErrorText")
        self.AirBagLocCurtain = value_or_none(results_dict, "AirBagLocCurtain")
        self.AirBagLocFront = value_or_none(results_dict, "AirBagLocFront")
        self.AirBagLocKnee = value_or_none(results_dict, "AirBagLocKnee")
        self.AirBagLocSeatCushion = value_or_none(results_dict, "AirBagLocSeatCushion")
        self.AirBagLocSide = value_or_none(results_dict, "AirBagLocSide")
        self.AutoReverseSystem = value_or_none(results_dict, "AutoReverseSystem")
        self.AutomaticPedestrianAlertingSound = value_or_none(
            results_dict, "AutomaticPedestrianAlertingSound"
        )
        self.AxleConfiguration = value_or_none(results_dict, "AxleConfiguration")
        self.Axles = value_or_none(results_dict, "Axles")
        self.BasePrice = value_or_none(results_dict, "BasePrice")
        self.BatteryA = value_or_none(results_dict, "BatteryA")
        self.BatteryA_to = value_or_none(results_dict, "BatteryA_to")
        self.BatteryCells = value_or_none(results_dict, "BatteryCells")
        self.BatteryInfo = value_or_none(results_dict, "BatteryInfo")
        self.BatteryKWh = value_or_none(results_dict, "BatteryKWh")
        self.BatteryKWh_to = value_or_none(results_dict, "BatteryKWh_to")
        self.BatteryModules = value_or_none(results_dict, "BatteryModules")
        self.BatteryPacks = value_or_none(results_dict, "BatteryPacks")
        self.BatteryType = value_or_none(results_dict, "BatteryType")
        self.BatteryV = value_or_none(results_dict, "BatteryV")
        self.BatteryV_to = value_or_none(results_dict, "BatteryV_to")
        self.BedLengthIN = value_or_none(results_dict, "BedLengthIN")
        self.BedType = value_or_none(results_dict, "BedType")
        self.BlindSpotMon = value_or_none(results_dict, "BlindSpotMon")
        self.BodyCabType = value_or_none(results_dict, "BodyCabType")
        self.BodyClass = value_or_none(results_dict, "BodyClass")
        self.BrakeSystemDesc = value_or_none(results_dict, "BrakeSystemDesc")
        self.BrakeSystemType = value_or_none(results_dict, "BrakeSystemType")
        self.BusFloorConfigType = value_or_none(results_dict, "BusFloorConfigType")
        self.BusLength = value_or_none(results_dict, "BusLength")
        self.BusType = value_or_none(results_dict, "BusType")
        self.CAN_AACN = value_or_none(results_dict, "CAN_AACN")
        self.CIB = value_or_none(results_dict, "CIB")
        self.CashForClunkers = value_or_none(results_dict, "CashForClunkers")
        self.ChargerLevel = value_or_none(results_dict, "ChargerLevel")
        self.ChargerPowerKW = value_or_none(results_dict, "ChargerPowerKW")
        self.CoolingType = value_or_none(results_dict, "CoolingType")
        self.CurbWeightLB = value_or_none(results_dict, "CurbWeightLB")
        self.CustomMotorcycleType = value_or_none(results_dict, "CustomMotorcycleType")
        self.DaytimeRunningLight = value_or_none(results_dict, "DaytimeRunningLight")
        self.DestinationMarket = value_or_none(results_dict, "DestinationMarket")
        self.DisplacementCC = value_or_none(results_dict, "DisplacementCC")
        self.DisplacementCI = value_or_none(results_dict, "DisplacementCI")
        self.DisplacementL = value_or_none(results_dict, "DisplacementL")
        self.Doors = value_or_none(results_dict, "Doors")
        self.DriveType = value_or_none(results_dict, "DriveType")
        self.DriverAssist = value_or_none(results_dict, "DriverAssist")
        self.DynamicBrakeSupport = value_or_none(results_dict, "DynamicBrakeSupport")
        self.EDR = value_or_none(results_dict, "EDR")
        self.ESC = value_or_none(results_dict, "ESC")
        self.EVDriveUnit = value_or_none(results_dict, "EVDriveUnit")
        self.ElectrificationLevel = value_or_none(results_dict, "ElectrificationLevel")
        self.EngineConfiguration = value_or_none(results_dict, "EngineConfiguration")
        self.EngineCycles = value_or_none(results_dict, "EngineCycles")
        self.EngineCylinders = value_or_none(results_dict, "EngineCylinders")
        self.EngineHP = value_or_none(results_dict, "EngineHP")
        self.EngineHP_to = value_or_none(results_dict, "EngineHP_to")
        self.EngineKW = value_or_none(results_dict, "EngineKW")
        self.EngineManufacturer = value_or_none(results_dict, "EngineManufacturer")
        self.EngineModel = value_or_none(results_dict, "EngineModel")
        self.EntertainmentSystem = value_or_none(results_dict, "EntertainmentSystem")
        self.ErrorCode = value_or_none(results_dict, "ErrorCode")
        self.ErrorText = value_or_none(results_dict, "ErrorText")
        self.ForwardCollisionWarning = value_or_none(
            results_dict, "ForwardCollisionWarning"
        )
        self.FuelInjectionType = value_or_none(results_dict, "FuelInjectionType")
        self.FuelTypePrimary = value_or_none(results_dict, "FuelTypePrimary")
        self.FuelTypeSecondary = value_or_none(results_dict, "FuelTypeSecondary")
        self.GCWR = value_or_none(results_dict, "GCWR")
        self.GCWR_to = value_or_none(results_dict, "GCWR_to")
        self.GVWR = value_or_none(results_dict, "GVWR")
        self.GVWR_to = value_or_none(results_dict, "GVWR_to")
        self.KeylessIgnition = value_or_none(results_dict, "KeylessIgnition")
        self.LaneDepartureWarning = value_or_none(results_dict, "LaneDepartureWarning")
        self.LaneKeepSystem = value_or_none(results_dict, "LaneKeepSystem")
        self.LowerBeamHeadlampLightSource = value_or_none(
            results_dict, "LowerBeamHeadlampLightSource"
        )
        self.Make = value_or_none(results_dict, "Make")
        self.MakeID = value_or_none(results_dict, "MakeID")
        self.Manufacturer = value_or_none(results_dict, "Manufacturer")
        self.ManufacturerId = value_or_none(results_dict, "ManufacturerId")
        self.Model = value_or_none(results_dict, "Model")
        self.ModelID = value_or_none(results_dict, "ModelID")
        self.ModelYear = value_or_none(results_dict, "ModelYear")
        self.MotorcycleChassisType = value_or_none(
            results_dict, "MotorcycleChassisType"
        )
        self.MotorcycleSuspensionType = value_or_none(
            results_dict, "MotorcycleSuspensionType"
        )
        self.NCSABodyType = value_or_none(results_dict, "NCSABodyType")
        self.NCSAMake = value_or_none(results_dict, "NCSAMake")
        self.NCSAMapExcApprovedBy = value_or_none(results_dict, "NCSAMapExcApprovedBy")
        self.NCSAMapExcApprovedOn = value_or_none(results_dict, "NCSAMapExcApprovedOn")
        self.NCSAMappingException = value_or_none(results_dict, "NCSAMappingException")
        self.NCSAModel = value_or_none(results_dict, "NCSAModel")
        self.NCSANote = value_or_none(results_dict, "NCSANote")
        self.Note = value_or_none(results_dict, "Note")
        self.OtherBusInfo = value_or_none(results_dict, "OtherBusInfo")
        self.OtherEngineInfo = value_or_none(results_dict, "OtherEngineInfo")
        self.OtherMotorcycleInfo = value_or_none(results_dict, "OtherMotorcycleInfo")
        self.OtherRestraintSystemInfo = value_or_none(
            results_dict, "OtherRestraintSystemInfo"
        )
        self.OtherTrailerInfo = value_or_none(results_dict, "OtherTrailerInfo")
        self.ParkAssist = value_or_none(results_dict, "ParkAssist")
        self.PedestrianAutomaticEmergencyBraking = value_or_none(
            results_dict, "PedestrianAutomaticEmergencyBraking"
        )
        self.PlantCity = value_or_none(results_dict, "PlantCity")
        self.PlantCompanyName = value_or_none(results_dict, "PlantCompanyName")
        self.PlantCountry = value_or_none(results_dict, "PlantCountry")
        self.PlantState = value_or_none(results_dict, "PlantState")
        self.PossibleValues = value_or_none(results_dict, "PossibleValues")
        self.Pretensioner = value_or_none(results_dict, "Pretensioner")
        self.RearCrossTrafficAlert = value_or_none(
            results_dict, "RearCrossTrafficAlert"
        )
        self.RearVisibilitySystem = value_or_none(results_dict, "RearVisibilitySystem")
        self.SAEAutomationLevel = value_or_none(results_dict, "SAEAutomationLevel")
        self.SAEAutomationLevel_to = value_or_none(
            results_dict, "SAEAutomationLevel_to"
        )
        self.SeatBeltsAll = value_or_none(results_dict, "SeatBeltsAll")
        self.SeatRows = value_or_none(results_dict, "SeatRows")
        self.Seats = value_or_none(results_dict, "Seats")
        self.SemiautomaticHeadlampBeamSwitching = value_or_none(
            results_dict, "SemiautomaticHeadlampBeamSwitching"
        )
        self.Series = value_or_none(results_dict, "Series")
        self.Series2 = value_or_none(results_dict, "Series2")
        self.SteeringLocation = value_or_none(results_dict, "SteeringLocation")
        self.SuggestedVIN = value_or_none(results_dict, "SuggestedVIN")
        self.TPMS = value_or_none(results_dict, "TPMS")
        self.TopSpeedMPH = value_or_none(results_dict, "TopSpeedMPH")
        self.TrackWidth = value_or_none(results_dict, "TrackWidth")
        self.TractionControl = value_or_none(results_dict, "TractionControl")
        self.TrailerBodyType = value_or_none(results_dict, "TrailerBodyType")
        self.TrailerLength = value_or_none(results_dict, "TrailerLength")
        self.TrailerType = value_or_none(results_dict, "TrailerType")
        self.TransmissionSpeeds = value_or_none(results_dict, "TransmissionSpeeds")
        self.TransmissionStyle = value_or_none(results_dict, "TransmissionStyle")
        self.Trim = value_or_none(results_dict, "Trim")
        self.Trim2 = value_or_none(results_dict, "Trim2")
        self.Turbo = value_or_none(results_dict, "Turbo")
        self.VIN = value_or_none(results_dict, "VIN")
        self.ValveTrainDesign = value_or_none(results_dict, "ValveTrainDesign")
        self.VehicleType = value_or_none(results_dict, "VehicleType")
        self.WheelBaseLong = value_or_none(results_dict, "WheelBaseLong")
        self.WheelBaseShort = value_or_none(results_dict, "WheelBaseShort")
        self.WheelBaseType = value_or_none(results_dict, "WheelBaseType")
        self.WheelSizeFront = value_or_none(results_dict, "WheelSizeFront")
        self.WheelSizeRear = value_or_none(results_dict, "WheelSizeRear")
        self.Wheels = value_or_none(results_dict, "Wheels")
        self.Windows = value_or_none(results_dict, "Windows")

    def search_name(self):
        search_str = self.full_or_partial_vin
        if self.year is not None:
            search_str += f"{self.year}"
        return search_str

    # def get_dict(self) -> Dict[str, str]:
    #     return self.results_dict

    # def get_series(self):
    #     return pd.Series(self.results_dict).replace(
    #         to_replace=r"^\s*$", value=np.nan, regex=True
    #     )

    def get_df(self, drop_na: bool = False) -> pd.DataFrame:
        df = pd.DataFrame({self.full_or_partial_vin: self.get_series()})
        if drop_na:
            df.dropna(inplace=True)
        return df.T
