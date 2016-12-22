# Points Of Interest
Filename: PointsOfInterest<br>Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/PointsOfInterest.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |Point of Interest (CommonPlace) is a point feature representation of points of interest throughout New York City. The primary intended purpose of CommonPlace is to help aid dispatch efforts to these points of interest throughout New York City.
**Description** |Point of Interest (aka Common Place) are point representations of locations that can be referred to by name and may or may not have an address. The data is a compilation of a variety of agency data and is a component of the CSCL database.
**Source(s)** |Department of Information Technology & Telecommunications (DOITT)
**Publication Dates** |**Data**: 8/30/2016<br>**Last Update**: Weekly<br>**Metadata**: 12/22/2016<br>**Update Frequency**: Agency data is updated daily by Centerline Management Group (CMG). Public releases of this data are made weekly. 
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/Points-Of-Interest/rxuy-2muj).
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Email**: 
**Links** |https://data.cityofnewyork.us/City-Government/Points-Of-Interest/rxuy-2muj
**Tags** |Manhattan, Brooklyn, Staten Island, New York City, Bronx, Common Place Name, complex, Queens, Common
Place
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY and areas of Nassau County, Westchester, and New Jersey. 
**Temporal Coverage** |Data is current as of last update date.
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SEGMENTID | Point is assigned the closest roadbed SegmentID. | double | 
| COMPLEXID | Point is assigned a ComplexID if it is a part of a Complex. | double | 
| SAFTYPE | Point is assigned a SAFTYPE if it is a part of a Complex<br>A = Alt Address - SAF record same as LION record<br>B = Alt Address - SAF record and LION record differ<br>C = Ruby Street on Brooklyn-Queens border<br>E = Neighborhood name<br>I = Named Intersection<br>N = NAP assigned to a Stand-alone feature<br>O = Out-of-Sequence Address or Opposite Parity Address<br>P = Addressable place name<br>S = Suffixed house numbers at an intersection<br>V = Vanity address<br>M = Multiple<br>G = Complex NAP<br>X = Constituent NAP<br>D = Duplicate or overlapping address ranges (real DAPS)<br>F = Duplicate or overlapping address ranges (Pseudo DAPS) | text | 
| SOS | Indicates which side of the street the CommonPlace is on. | text | 
| PLACEID | The unique identifier for each CommonPlace point. Links to the point to the FeatureName table. | double | 
| FACI_DOM | Facility Domain: <br>1 = Residential<br>2 = Education Facility<br>3 = Cultural Facility<br>4 = Recreational Facility<br>5 = Social Services<br>6 = Transportation Facility<br>7 = Commercial<br>8 = Government Facility (non public safety)<br>9 = Religious Institution<br>10 = Health Services<br>11 = Public Safety<br>12 = Water<br>13 = Miscellaneous | text | 
| BIN | BIN is an abbreviation of Building Identification Number. Point is assigned a BIN if it falls within a building. | double | 
| BOROUGH | Numeric codes for NYC 5 boroughs. <br>1 = Manhattan<br>2 = Bronx<br>3 = Brooklyn<br>4 = Queens<br>5 = Staten Island | text | 
| CREATED | Date feature was created | date | 
| MODIFIED | Date feature was modified | date | 
| FACILITY_T | This is a SubType field organizing the CommonPlace points into categories and sets up the domain values for the FACILITY_DOMAINS field.<br>1 = Residential<br>2 = Education Facility<br>3 = Cultural Facility<br>4 = Recreational Facility<br>5 = Social Services<br>6 = Transportation Facility<br>7 = Commercial<br>8 = Government Facility (non public safety)<br>9 = Religious Institution<br>10 = Health Services<br>11 = Public Safety<br>12 = Water<br>13 = Miscellaneous | integer | 
| SOURCE | Agency that defined the CommonPlace location.<br>DoITT = Department of Information Technology and Telecommunications<br>EMS = Fire Department Emergency Services (EMS)<br>FDNY = Fire Department (Fire)<br>DOB = Department of Buildings<br>DOF = Department of Finance<br>DOT = Department of Transportation<br>DCP = Department of City Planning<br>OEM = Office of Emergency Management<br>311 = 3-1-1<br>NYPD = Police Department<br>OTHER = Other<br>DPR = Department of Parks and Recreation<br>NOAA = National Oceanic and Atmospheric Administration<br>NYCHA = New York City Housing Authority<br>OSM = Open Street Map<br>DOE = NYC Dept. of Education | text | 
| B7SC | The Street Code assigned to a CommonPlace . | text | 
| PRI_ADD | The Addresspoint ID if the CommonPlace is related to any Addresspoint | double | 
| NAME | The name of the CommonPlace. Most name come from Feature name table. | text | 
