# PVAW: Python Vehicle API Wrapper

A Python wrapper for the **National Highway Traffic Saftey Association** (NHTSA) [Vehicle API](https://vpic.nhtsa.dot.gov/api/)

# License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Documentation

## Importing Python Vehicle API Wrapper

```python
import pvaw as pv
```

# Vin Decoding

The NHTSA Vehicle API supports individual and batch decoding.

## Vin Class

### class pvaw.Vin(full_or_partial_vin, model_year=None)

**Parameters:**

**full_or_partial_vin:** string representing a Vehicle Identification Number (VIN). It can be either the full VIN (e.g. "3C6JR7AT4EG248404"), or be a subset of the VIN with missing characters replaced by the '\*' character (e.g. "5YJSA3DS\*EF")

**model_year:** string or integer representing the model year of the vehicle. Defaults to None.

#### Constructing a Vin

```python
# creating a Vin object from partial vin
vin_1 = pv.Vin("5YJSA3DS*EF")

# creationg a Vin object from partial vin and year
vin_2 = pv.Vin("5UXWX7C5*BA", 2011)
```

## Decoding a Vin

### pvaw.Vin.decode()

**Returns:** A Vehicle object with information about the Vin's associated vehicle

```python
vehicle = vin_1.decode()
vehicle
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>2014</td>
      <td>TESLA</td>
      <td>TESLA, INC.</td>
      <td>Model S</td>
      <td>5YJSA3DS*EF</td>
      <td>PASSENGER CAR</td>
    </tr>
  </tbody>
</table>
</div>

**Getting Key Attributes**

```python
print(vehicle.model_year)
print(vehicle.make)
print(vehicle.manufacturer)
print(vehicle.model)
print(vehicle.full_or_partial_vin)
print(vehicle.vehicle_type)
```

    2014
    TESLA
    TESLA, INC.
    Model S
    5YJSA3DS*EF
    PASSENGER CAR

**Getting JSON Results**

```python
vehicle.get_results()
```

    {'ABS': '',
     'ActiveSafetySysNote': '',
     'AdaptiveCruiseControl': '',
     'AdaptiveDrivingBeam': '',
     'AdaptiveHeadlights': '',
     'AdditionalErrorText': 'The error positions are indicated by ! in Suggested VIN. In the Possible values section, each pair of parenthesis indicate information about each error position in VIN . The Numeric value before the : indicates the position in error and the values after the : indicate the possible values that are allowed in this position Unused position(s): 8;',
     'AirBagLocCurtain': '',
     'AirBagLocFront': '1st Row (Driver & Passenger)',
     ...

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
vehicle.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>2014</td>
      <td>TESLA</td>
      <td>TESLA, INC.</td>
      <td>Model S</td>
      <td>5YJSA3DS*EF</td>
      <td>PASSENGER CAR</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Getting full raw data df not dropping nan
vehicle.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ABS</th>
      <th>ActiveSafetySysNote</th>
      <th>AdaptiveCruiseControl</th>
      <th>AdaptiveDrivingBeam</th>
      <th>AdaptiveHeadlights</th>
      <th>AdditionalErrorText</th>
      <th>AirBagLocCurtain</th>
      <th>AirBagLocFront</th>
      <th>AirBagLocKnee</th>
      <th>AirBagLocSeatCushion</th>
      <th>...</th>
      <th>VIN</th>
      <th>ValveTrainDesign</th>
      <th>VehicleType</th>
      <th>WheelBaseLong</th>
      <th>WheelBaseShort</th>
      <th>WheelBaseType</th>
      <th>WheelSizeFront</th>
      <th>WheelSizeRear</th>
      <th>Wheels</th>
      <th>Windows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>The error positions are indicated by ! in Sugg...</td>
      <td>NaN</td>
      <td>1st Row (Driver &amp; Passenger)</td>
      <td>1st Row (Driver &amp; Passenger)</td>
      <td>NaN</td>
      <td>...</td>
      <td>5YJSA3DS*EF</td>
      <td>NaN</td>
      <td>PASSENGER CAR</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 145 columns</p>
</div>

## Batch Decoding

### pvaw.decode_vins(vins)

**Parameters:** **vins:** list of Vin objects

**Returns:** ResultsList object which stores a list of Vehicle objects

```python
vehicles = pv.decode_vins([vin_1, vin_2])
vehicles
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>2014</td>
      <td>TESLA</td>
      <td>TESLA, INC.</td>
      <td>Model S</td>
      <td>5YJSA3DS*EF</td>
      <td>PASSENGER CAR</td>
    </tr>
    <tr>
      <td>5UXWX7C5*BA,2011</td>
      <td>2011</td>
      <td>BMW</td>
      <td>BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA</td>
      <td>X3</td>
      <td>5UXWX7C5*BA</td>
      <td>MULTIPURPOSE PASSENGER VEHICLE (MPV)</td>
    </tr>
  </tbody>
</table>
</div>

**Accessing each Vehicle**

```python
# Iterating through vehicles
for vehicle in vehicles:
    display(vehicle)

# Indexing Vehicles
first = vehicles[0]
last = vehicles[len(vehicles) - 1]
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>2014</td>
      <td>TESLA</td>
      <td>TESLA, INC.</td>
      <td>Model S</td>
      <td>5YJSA3DS*EF</td>
      <td>PASSENGER CAR</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5UXWX7C5*BA,2011</td>
      <td>2011</td>
      <td>BMW</td>
      <td>BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA</td>
      <td>X3</td>
      <td>5UXWX7C5*BA</td>
      <td>MULTIPURPOSE PASSENGER VEHICLE (MPV)</td>
    </tr>
  </tbody>
</table>
</div>

**Getting JSON Results**

```python
vehicles.get_results()
```

    [{'ABS': '',
      'ActiveSafetySysNote': '',
      'AdaptiveCruiseControl': '',
      'AdaptiveDrivingBeam': '',
      'AdaptiveHeadlights': '',
      'AdditionalErrorText': 'The error positions are indicated by ! in Suggested VIN. In the Possible values section, each pair of parenthesis indicate information about each error position in VIN . The Numeric value before the : indicates the position in error and the values after the : indicate the possible values that are allowed in this position Unused position(s): 8;',
      'AirBagLocCurtain': '',
      'AirBagLocFront': '1st Row (Driver & Passenger)',
      'AirBagLocKnee': '1st Row (Driver & Passenger)',
      'AirBagLocSeatCushion': '',
      ...

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
vehicles.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>model_year</th>
      <th>make</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>full_or_partial_vin</th>
      <th>vehicle_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>2014</td>
      <td>TESLA</td>
      <td>TESLA, INC.</td>
      <td>Model S</td>
      <td>5YJSA3DS*EF</td>
      <td>PASSENGER CAR</td>
    </tr>
    <tr>
      <td>5UXWX7C5*BA,2011</td>
      <td>2011</td>
      <td>BMW</td>
      <td>BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA</td>
      <td>X3</td>
      <td>5UXWX7C5*BA</td>
      <td>MULTIPURPOSE PASSENGER VEHICLE (MPV)</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Getting full raw data df not dropping nan
vehicles.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ABS</th>
      <th>ActiveSafetySysNote</th>
      <th>AdaptiveCruiseControl</th>
      <th>AdaptiveDrivingBeam</th>
      <th>AdaptiveHeadlights</th>
      <th>AdditionalErrorText</th>
      <th>AirBagLocCurtain</th>
      <th>AirBagLocFront</th>
      <th>AirBagLocKnee</th>
      <th>AirBagLocSeatCushion</th>
      <th>...</th>
      <th>VIN</th>
      <th>ValveTrainDesign</th>
      <th>VehicleType</th>
      <th>WheelBaseLong</th>
      <th>WheelBaseShort</th>
      <th>WheelBaseType</th>
      <th>WheelSizeFront</th>
      <th>WheelSizeRear</th>
      <th>Wheels</th>
      <th>Windows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJSA3DS*EF</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>The error positions are indicated by ! in Sugg...</td>
      <td>NaN</td>
      <td>1st Row (Driver &amp; Passenger)</td>
      <td>1st Row (Driver &amp; Passenger)</td>
      <td>NaN</td>
      <td>...</td>
      <td>5YJSA3DS*EF</td>
      <td>NaN</td>
      <td>PASSENGER CAR</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>5UXWX7C5*BA,2011</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1st Row (Driver &amp; Passenger)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>5UXWX7C5*BA</td>
      <td>NaN</td>
      <td>MULTIPURPOSE PASSENGER VEHICLE (MPV)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 145 columns</p>
</div>

# WMI Methods

The NHTSA Vehicle API supports wmi decoding

## WMI Decoding

#### pvaw.decode_wmi(wmi)

**Parameters: wmi:** str of length 3 representing VIN position 1-3 (e.g. "1FD") or 6 representing VIN positions 1-3 & 12-14 (e.g. "1G9340")

**Returns:** WMIInfo object with information on wmi

```python
wmi_info = pv.decode_wmi("JTL")
wmi_info
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JTL</td>
      <td>JTL</td>
      <td>Multipurpose Passenger Vehicle (MPV)</td>
      <td>TOYOTA MOTOR NORTH AMERICA, INC</td>
    </tr>
  </tbody>
</table>
</div>

**Getting Key Attributes**

```python
print(wmi_info.wmi)
print(wmi_info.manufacturer)
print(wmi_info.vehicle_type)
```

    JTL
    TOYOTA MOTOR NORTH AMERICA, INC
    Multipurpose Passenger Vehicle (MPV)

**Getting JSON Results**

```python
wmi_info.get_results()
```

    {'CommonName': 'Toyota',
     'CreatedOn': '2015-05-04',
     'DateAvailableToPublic': '2015-01-01',
     'Make': 'TOYOTA',
     'ManufacturerName': 'TOYOTA MOTOR NORTH AMERICA, INC',
     'ParentCompanyName': 'TOYOTA MOTOR CORPORATION',
     'URL': 'http://www.toyota.com',
     'UpdatedOn': None,
     'VehicleType': 'Multipurpose Passenger Vehicle (MPV)',
     'WMI': 'JTL'}

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
wmi_info.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JTL</td>
      <td>JTL</td>
      <td>Multipurpose Passenger Vehicle (MPV)</td>
      <td>TOYOTA MOTOR NORTH AMERICA, INC</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Getting full raw data df not dropping nan
wmi_info.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CommonName</th>
      <th>CreatedOn</th>
      <th>DateAvailableToPublic</th>
      <th>Make</th>
      <th>ManufacturerName</th>
      <th>ParentCompanyName</th>
      <th>URL</th>
      <th>UpdatedOn</th>
      <th>VehicleType</th>
      <th>WMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>JTL</td>
      <td>Toyota</td>
      <td>2015-05-04</td>
      <td>2015-01-01</td>
      <td>TOYOTA</td>
      <td>TOYOTA MOTOR NORTH AMERICA, INC</td>
      <td>TOYOTA MOTOR CORPORATION</td>
      <td>http://www.toyota.com</td>
      <td>None</td>
      <td>Multipurpose Passenger Vehicle (MPV)</td>
      <td>JTL</td>
    </tr>
  </tbody>
</table>
</div>

## Finding WMIs by Manufacturer

### pvaw.get_wmis(manufacturer_search)

**Parameters: manufacturer_search:** a str representing part or all of the name of a Manufacturer (e.g. "Honda")

**Returns:** ResultsList object which stores a list of WMIInfo objects

```python
wmi_infos = pv.get_wmis("Tesla")
wmi_infos
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJ</td>
      <td>5YJ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
    <tr>
      <td>SFZ</td>
      <td>SFZ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
  </tbody>
</table>
</div>

**Accessing Each WMI**

```python
# Iterating through vehicles
for wmi_info in wmi_infos:
    display(wmi_info)

# Indexing Vehicles
first = wmi_infos[0]
last = wmi_infos[len(vehicles) - 1]

# Getting Key Attributes
print(first.wmi)
print(first.manufacturer)
print(first.vehicle_type)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJ</td>
      <td>5YJ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SFZ</td>
      <td>SFZ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
  </tbody>
</table>
</div>

    5YJ
    TESLA, INC.
    Passenger Car

**Getting JSON Results**

```python
wmi_infos.get_results()
```

    [{'Country': 'UNITED STATES (USA)',
      'CreatedOn': '2015-03-04',
      'DateAvailableToPublic': '2015-01-01',
      'Id': 955,
      'Name': 'TESLA, INC.',
      'UpdatedOn': None,
      'VehicleType': 'Passenger Car',
      'WMI': '5YJ'},
     {'Country': 'UNITED STATES (USA)',
      'CreatedOn': '2015-04-16',
      'DateAvailableToPublic': '2015-01-01',
      'Id': 955,
      'Name': 'TESLA, INC.',
      'UpdatedOn': None,
      'VehicleType': 'Passenger Car',
      'WMI': 'SFZ'}]

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
wmi_infos.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wmi</th>
      <th>vehicle_type</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJ</td>
      <td>5YJ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
    <tr>
      <td>SFZ</td>
      <td>SFZ</td>
      <td>Passenger Car</td>
      <td>TESLA, INC.</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Getting full raw data df not dropping nan
wmi_infos.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>CreatedOn</th>
      <th>DateAvailableToPublic</th>
      <th>Id</th>
      <th>Name</th>
      <th>UpdatedOn</th>
      <th>VehicleType</th>
      <th>WMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>5YJ</td>
      <td>UNITED STATES (USA)</td>
      <td>2015-03-04</td>
      <td>2015-01-01</td>
      <td>955</td>
      <td>TESLA, INC.</td>
      <td>None</td>
      <td>Passenger Car</td>
      <td>5YJ</td>
    </tr>
    <tr>
      <td>SFZ</td>
      <td>UNITED STATES (USA)</td>
      <td>2015-04-16</td>
      <td>2015-01-01</td>
      <td>955</td>
      <td>TESLA, INC.</td>
      <td>None</td>
      <td>Passenger Car</td>
      <td>SFZ</td>
    </tr>
  </tbody>
</table>
</div>

## Make Methods

### pvaw.get_makes(manufacturer_name_or_id=None, model_year=None, vehicle_type=None)

Finding Makes by Manufacturer and Year or Vehicle Type

**Parameters: manufacturer_name_or_id:** a str representing part or all of the name of a manufacturer (e.g. "Honda") or an integer representing the manufacturer ID

**model_year:** a str or int representing the year makes must exist in (e.g. 2005)

**vehicle_type:** a str representing the type of vehicle that a make produces (e.g. "car")

**NOTE**: For this method, you can filter either by manufacturer_name_or_id or by vehicle_type, you cannot filter by both. Additionally, model_year can be passed in with manufacturer_name_or_id, but not with vehicle_type.

**Returns:** ResultsList object which stores a list of Make objects

```python
# getting makes for manufacturer name search
makes = pv.get_makes("hyundai")

# getting makes for manufacturer name search and model year
makes_2 = pv.get_makes("tesla", 2020)

# getting makes for manufacturer ID and model year
makes_3 = pv.get_makes(988, 2005)

# getting makes by vehicle_type search
makes_4 = pv.get_makes(vehicle_type="car")
```

```python
# displaying makes
makes_3
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>make_id</th>
      <th>make_name</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>474-HONDA OF AMERICA MFG., INC.</td>
      <td>474</td>
      <td>HONDA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
    <tr>
      <td>475-HONDA OF AMERICA MFG., INC.</td>
      <td>475</td>
      <td>ACURA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
  </tbody>
</table>
</div>

**Accessing Each Make**

```python
# Iterating through makes
for m in makes_3:
    display(m)

# Indexing makes
first = makes_3[0]
last = makes_3[len(makes_3) - 1]

# Getting Key Attributes
print(first.make_id)
print(first.make_name)
print(first.manufacturer)
print(first.vehicle_type)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>make_id</th>
      <th>make_name</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>474-HONDA OF AMERICA MFG., INC.</td>
      <td>474</td>
      <td>HONDA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>make_id</th>
      <th>make_name</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>475-HONDA OF AMERICA MFG., INC.</td>
      <td>475</td>
      <td>ACURA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
  </tbody>
</table>
</div>

    474
    HONDA
    HONDA OF AMERICA MFG., INC.
    None

**Getting JSON Results**

```python
makes_3.get_results()
```

    [{'MakeId': 474,
      'MakeName': 'HONDA',
      'MfrId': 988,
      'MfrName': 'HONDA OF AMERICA MFG., INC.'},
     {'MakeId': 475,
      'MakeName': 'ACURA',
      'MfrId': 988,
      'MfrName': 'HONDA OF AMERICA MFG., INC.'}]

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
makes_3.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>make_id</th>
      <th>make_name</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>474-HONDA OF AMERICA MFG., INC.</td>
      <td>474</td>
      <td>HONDA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
    <tr>
      <td>475-HONDA OF AMERICA MFG., INC.</td>
      <td>475</td>
      <td>ACURA</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
  </tbody>
</table>
</div>

```python
# Getting full raw data df not dropping nan
makes_3.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>MakeId</th>
      <th>MakeName</th>
      <th>MfrId</th>
      <th>MfrName</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>474-HONDA OF AMERICA MFG., INC.</td>
      <td>474</td>
      <td>HONDA</td>
      <td>988</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
    <tr>
      <td>475-HONDA OF AMERICA MFG., INC.</td>
      <td>475</td>
      <td>ACURA</td>
      <td>988</td>
      <td>HONDA OF AMERICA MFG., INC.</td>
    </tr>
  </tbody>
</table>
</div>

# Manufacturer Methods

## Getting Manufacturers

### pvaw.get_manufacturers(m_type=None, page=1)

**Parameters: m_type:** a str representing part or all of the manufacturer type (e.g. "Intermediate")

**page:** int representing the api page number. Each page returns 100 manufacturers

**Returns:** ResultsList object which stores a list of Manufacturer objects

```python
# getting manufacturers by api page number
manufacturers = pv.get_manufacturers(page=5)

# getting manufacturers by manufacturer type
manufacturers_2 = pv.get_manufacturers(m_type="complete", page=1)
```

## Searching for Specific Manufacturers

### pvaw.get_manufacturer_details(manufacturer_name_or_id)

**Parameters: manufacturer_name_or_id:** a str representing manufacturer name or an int representing the manufacturer ID

**Returns:** ResultsList object which stores a list of Manufacturer objects matching the manufacturer search

```python
# getting manufacturer(s) from manufacturer name search
manufacturers_3 = pv.get_manufacturer_details("Toyota")

# getting manufacturer from manufacturter id
manufacturers_4 = pv.get_manufacturer_details(988)
```

**Accessing Each Manufacturer**

```python
# Iterating through manufacturers
for m in manufacturers[:4]:
    display(m)

# Indexing manufacturers
first = manufacturers[0]
last = manufacturers[len(manufacturers) - 1]

# Getting Key Attributes
print(first.id)
print(first.common_name)
print(first.name)
print(first.vehicle_types)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>vehicle_types</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1387</td>
      <td>WOOPYONG MOTOR WHEEL LTD</td>
      <td>[]</td>
      <td>1387</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>vehicle_types</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1388</td>
      <td>WORCESTER TANK &amp; EQUIPMENT CO., INC</td>
      <td>[]</td>
      <td>1388</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>vehicle_types</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1389</td>
      <td>WORCESTER WHITE AUTOCAR, INC.</td>
      <td>[]</td>
      <td>1389</td>
    </tr>
  </tbody>
</table>
</div>

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>vehicle_types</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1390</td>
      <td>WORKBENCH, INC.</td>
      <td>[Trailer]</td>
      <td>1390</td>
    </tr>
  </tbody>
</table>
</div>

    1387
    None
    WOOPYONG MOTOR WHEEL LTD
    []

**Getting JSON Results**

```python
manufacturers.get_results()
```

    [{'Country': '',
      'Mfr_CommonName': None,
      'Mfr_ID': 1387,
      'Mfr_Name': 'WOOPYONG MOTOR WHEEL LTD',
      'VehicleTypes': []},
     {'Country': 'UNITED STATES (USA)',
      'Mfr_CommonName': None,
      'Mfr_ID': 1388,
      'Mfr_Name': 'WORCESTER TANK & EQUIPMENT CO., INC',
      'VehicleTypes': []},
     ...

**Getting DataFrame**

```python
# Getting key attribute df dropping nan
manufacturers.get_df()
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>vehicle_types</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1387</td>
      <td>WOOPYONG MOTOR WHEEL LTD</td>
      <td>[]</td>
      <td>1387</td>
    </tr>
    <tr>
      <td>1388</td>
      <td>WORCESTER TANK &amp; EQUIPMENT CO., INC</td>
      <td>[]</td>
      <td>1388</td>
    </tr>
    <tr>
      <td>1389</td>
      <td>WORCESTER WHITE AUTOCAR, INC.</td>
      <td>[]</td>
      <td>1389</td>
    </tr>
    <tr>
      <td>1390</td>
      <td>WORKBENCH, INC.</td>
      <td>[Trailer]</td>
      <td>1390</td>
    </tr>
    <tr>
      <td>1391</td>
      <td>U-SCREEN U.S.A., INC.</td>
      <td>[Trailer]</td>
      <td>1391</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>1479</td>
      <td>TAZZARI GL SPA</td>
      <td>[Low Speed Vehicle (LSV)]</td>
      <td>1479</td>
    </tr>
    <tr>
      <td>1480</td>
      <td>CHANGZHOU CITY WENMING VEHICLE ACCESSORIES FAC...</td>
      <td>[]</td>
      <td>1480</td>
    </tr>
    <tr>
      <td>1481</td>
      <td>SALSCO, INC.</td>
      <td>[Trailer]</td>
      <td>1481</td>
    </tr>
    <tr>
      <td>1482</td>
      <td>LIFT N LOCK, LLC</td>
      <td>[]</td>
      <td>1482</td>
    </tr>
    <tr>
      <td>1483</td>
      <td>CONTINENTAL BIOMASS INDUSTRIES, INC.</td>
      <td>[]</td>
      <td>1483</td>
    </tr>
  </tbody>
</table>
<p>92 rows × 3 columns</p>
</div>

```python
# Getting full raw data df not dropping nan
manufacturers.get_df(raw=True, drop_na=False)
```

<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Mfr_CommonName</th>
      <th>Mfr_ID</th>
      <th>Mfr_Name</th>
      <th>VehicleTypes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1387</td>
      <td>NaN</td>
      <td>None</td>
      <td>1387</td>
      <td>WOOPYONG MOTOR WHEEL LTD</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1388</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1388</td>
      <td>WORCESTER TANK &amp; EQUIPMENT CO., INC</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1389</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1389</td>
      <td>WORCESTER WHITE AUTOCAR, INC.</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1390</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1390</td>
      <td>WORKBENCH, INC.</td>
      <td>[{'IsPrimary': False, 'Name': 'Trailer'}]</td>
    </tr>
    <tr>
      <td>1391</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1391</td>
      <td>U-SCREEN U.S.A., INC.</td>
      <td>[{'IsPrimary': False, 'Name': 'Trailer'}]</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>1479</td>
      <td>ITALY</td>
      <td>None</td>
      <td>1479</td>
      <td>TAZZARI GL SPA</td>
      <td>[{'IsPrimary': True, 'Name': 'Low Speed Vehicl...</td>
    </tr>
    <tr>
      <td>1480</td>
      <td>CHINA</td>
      <td>None</td>
      <td>1480</td>
      <td>CHANGZHOU CITY WENMING VEHICLE ACCESSORIES FAC...</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1481</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1481</td>
      <td>SALSCO, INC.</td>
      <td>[{'IsPrimary': True, 'Name': 'Trailer'}]</td>
    </tr>
    <tr>
      <td>1482</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1482</td>
      <td>LIFT N LOCK, LLC</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>1483</td>
      <td>UNITED STATES (USA)</td>
      <td>None</td>
      <td>1483</td>
      <td>CONTINENTAL BIOMASS INDUSTRIES, INC.</td>
      <td>[]</td>
    </tr>
  </tbody>
</table>
<p>92 rows × 5 columns</p>
</div>
