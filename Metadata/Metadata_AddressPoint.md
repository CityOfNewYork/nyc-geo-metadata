# Address Point
Filename: AddressPoint.shp<br>Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/AddressPoint.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |Address points were developed to supplement the address information supplied by street centerline data (CSCL). Some computer aided dispatch systems use address points as the primary source for locating an address.
**Description** |Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file. Points were created approximately five feet inside building footprints along the correct street frontage. A field collection/verification process was undertaken to validate "multi-valued" addresses contained in the PAD file (i.e. those locations with a range of addresses). Additionally, a statistical sample of PAD single valued addresses was field checked. Approximately 100,000 locations were visited (about 10% of the total).
**Source(s)** |Department of City Planning Property Address Directory (PAD), DOITT
**Publication Dates** |**Data**: 4/27/2015<br>**Last Update**: 11/17/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: As needed
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/NYC-Address-Points/g6pj-hd8k).
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/NYC-Address-Points/g6pj-hd8k
**Tags** |address, BIN, New York City, NYC, Brooklyn, Bronx, Manhattan, Queens, Staten Island, gis, doitt
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Data is current as of last update date.
**Positional Accuracy** |Points were created approximately five feet inside building footprints along the correct street frontage.
**Features Captured** |All possible measures have been taken to ensure all registered address points are collected.
**Features Excluded** |Only registered address points are included in the dataset.
**Capture and Update Notes** |Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file. A field collection/verification process was undertaken to validate "multi-valued" addresses contained in the PAD file (i.e. those locations with a range of addresses). Additionally, a statistical sample of PAD single valued addresses was field checked. Approximately 100,000 locations were visited (about 10% of the total).
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| ADDRESS_ID | Unique identifer for address | double | No
| BIN | Building Identification Number (BIN) associated with the address point | double | No
| H_NO | The address number. The field supports hyphenated and range based addresses.  | text | No
| HNO_SUFFIX | For address points representing suffixed range-type addresses, this value is the upper range for the address suffix. | text | No
| HYPHEN_TYP | The Address Point Feature Class will support the storage of hyphenated addresses. <br>R = Building Range <br>Q = Queens Type <br>X = Range of Queens Style <br>N = No Hyphen Type <br>U = Unit | text | No
| SIDE_OF_ST | Indicates which side of the street the point is located on relative to the digitized direction of the associated Centerline street segment. <br>1 = Left <br>2 = Right | text | No
| SPECIAL_CO | This data element is used to store conditions identified in the DCP Special Address File (SAF) and from other sources. <br>A = Alt Address  = SAF record same as LION record <br>B = Alt Address  = SAF record and LION record differ <br>C = Ruby Street on Brooklyn-Queens border <br>E = Neighborhood name <br>I = Named Intersection <br>N = NAP assigned to a Stand-alone feature <br>O = Out-of-Sequence Address or Opposite Parity Address <br>P = Addressable place name <br>S = Suffixed house numbers at an intersection <br>V = Vanity address <br>M = Multiple <br>G = Complex NAP <br>X = Constituent NAP <br>D = Duplicate or overlapping address ranges (real DAPS) <br>F = Duplicate or overlapping address ranges (Pseudo DAPS) | text | No
| BOROCODE | Numeric codes for NYC 5 boroughs. <br>1 = Manhattan<br>2 = Bronx<br>3 = Brooklyn<br>4 = Queens<br>5 = Staten Island | text | No
| ZIPCODE | Five-digit postal zip code. | text | No
| CREATED | Date feature was created | date | No
| MODIFIED | Date the feature was last modified | date | No
| ST_NAME | Street name | text | No
| HN_RNG | For address points representing range-type addresses, this value is the upper range for the address.  | text | No
| HN_RNG_SUF | For address points representing suffixed rang-type addresses, this value is the upper range for the address suffix. | text | No
| PHYSICALID | A unique ID assigned to intersection to intersection stretches of a street.  | double | No
