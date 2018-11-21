# Points Of Interest
Geometry Type: point<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/PointsOfInterest.PNG)

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
**Links** |https://data.cityofnewyork.us/City-Government/Points-Of-Interest/rxuy-2muj
**Tags** |Manhattan, Brooklyn, Staten Island, New York City, Bronx, Common Place Name, complex, Queens, Common Place
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY and areas of Nassau County, Westchester, and New Jersey. 
**Temporal Coverage** |Data is current as of last update date.
**Usage Notes** | To query a specific point of interest, use both the FACILITY_T and FACI_DOM fields. For example, to find all police precincts -- FACILITY_T = 11 AND FACI_DOM = 1
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | 
|------------ | ------------- | -------- | 
| SEGMENTID | Point is assigned the closest roadbed SegmentID. | double | 
| COMPLEXID | Point is assigned a ComplexID if it is a part of a Complex. | double | 
| SAFTYPE | Point is assigned a SAFTYPE if it is a part of a Complex<br>N = NAP assigned to a Stand-alone feature<br>G = Complex NAP<br>X = Constituent NAP | text | 
| SOS | Indicates which side of the street the CommonPlace is on. | text | 
| PLACEID | The unique identifier for each CommonPlace point. Links to the point to the FeatureName table. | double | 
| FACI_DOM | Facility Domains are valid values for each FACILITY_TYPE: <br><br>Residential <br> 1 = Gated Development <br> 2 = Private Development <br> 3 = Public Housing Development <br> 4 = Constituent <br> 5 = Other<br><br>Education Facility<br> 1 = Public Elementary School <br> 2 = Public Junior High-Intermediate-Middle <br> 3 = Public High School <br> 4 = Private/Parochial Elementary School <br> 5 = Private/Parochial Junior/Middle School <br> 6 = Private/Parochial High School <br> 7 = Post Secondary Degree Granting Institution <br> 8 = Other <br> 9 = Public Early Childhood <br> 10 = Public K-8 <br> 11 = Public  K-12 all grades <br> 12 = Public Secondary School <br> 13 = Public School Building <br> 14 = Public School Annex <br> 15 = Private/Parochial Early Childhood <br> 16 = Private/Parochial K-8 <br> 17 = Private/Parochial K-12 all grades <br> 18 = Private/Parochial Secondary School <br><br>Cultural Facility<br> 1 = Center <br> 2 = Library <br> 3 = Theater/Concert Hall <br> 4 = Museum <br> 5 = Other<br><br>Recreational Facility<br> 1 = Park <br> 2 = Amusement Park <br> 3 = Golf Course <br> 4 = Beach <br> 5 = Botanical Garden <br> 6 = Zoo <br> 7 = Recreational Center <br> 8 = Sports <br> 9 = Playground <br> 10 = Other <br> 11 = Pool <br> 12 = Garden<br><br>Social Services<br> 1 = Residential Child Care <br> 2 = Day Care Center <br> 3 = Adult Day Care <br> 4 = Nursing Home/Assisted Living Facility <br> 5 = Homeless shelter <br> 6 = Other<br><br>Transportation Facility<br> 1 = Bus Terminal <br> 2 = Ferry landing/terminal <br> 3 = Transit/Maintenance Yard <br> 4 = Airport <br> 5 = Heliport <br> 6 = Marina <br> 7 = Pier <br> 8 = Bridge <br> 9 = Tunnel <br> 10 = Exit/Entrance <br> 11 = Water Navigation <br> 12 = Other<br><br>Commercial<br> 1 = Center <br> 2 = Business <br> 3 = Market <br> 4 = Hotel/Motel <br> 5 = Restaurant <br> 6 = Other<br><br>Government Facility (non public safety)<br> 1 = Government Office <br> 2 = Court of law <br> 3 = Post Office <br> 4 = Consulate <br> 5 = Embassy <br> 6 = Military <br> 7 = Other<br><br>Religious Institution<br> 1 Church <br> 2 Synagogue <br> 3 Temple <br> 4 Convent/Monastery <br> 5 Mosque <br> 6 Other<br><br>Health Services<br> 1 = Hospital <br> 2 = Inpatient care center <br> 3 = Outpatient care center/Clinic <br> 4 = Other<br><br>Public Safety<br> 1 = NYPD Precinct <br> 2 = NYPD Checkpoint <br> 3 = FDNY Ladder Company <br> 4 = FDNY Battalion <br> 5 = Correctional Facility <br> 6 = FDNY Engine Company <br> 7 = FDNY Special Unit <br> 8 = FDNY Division <br> 9 = FDNY Squad <br> 10 = NYPD Other <br> 11 = Other <br> 12 = FDNY Other<br><br>Water<br> 1 = Island <br> 2 = River <br> 3 = Lake <br> 4 = Stream <br> 5 = Other <br> 6 = Pond<br><br>Miscellaneous<br> 1 = Official Landmark <br> 2 = Point of Interest <br> 3 = Cemetery/Morgue <br> 4 = Other | text | 
| BIN | BIN is an abbreviation of Building Identification Number. Point is assigned a BIN if it falls within a building. | double | 
| BOROUGH | Numeric codes for NYC 5 boroughs. <br>1 = Manhattan<br>2 = Bronx<br>3 = Brooklyn<br>4 = Queens<br>5 = Staten Island | text | 
| CREATED | Date feature was created | date | 
| MODIFIED | Date feature was modified | date | 
| FACILITY_T | This is a SubType field organizing the CommonPlace points into categories and sets up the domain values for the FACILITY_DOMAINS field.<br>1 = Residential<br>2 = Education Facility<br>3 = Cultural Facility<br>4 = Recreational Facility<br>5 = Social Services<br>6 = Transportation Facility<br>7 = Commercial<br>8 = Government Facility (non public safety)<br>9 = Religious Institution<br>10 = Health Services<br>11 = Public Safety<br>12 = Water<br>13 = Miscellaneous | integer | 
| SOURCE | Agency that defined the CommonPlace location.<br>DoITT = Department of Information Technology and Telecommunications<br>EMS = Fire Department Emergency Services (EMS)<br>FDNY = Fire Department (Fire)<br>DOB = Department of Buildings<br>DOF = Department of Finance<br>DOT = Department of Transportation<br>DCP = Department of City Planning<br>OEM = Office of Emergency Management<br>311 = 3-1-1<br>NYPD = Police Department<br>OTHER = Other<br>DPR = Department of Parks and Recreation<br>NOAA = National Oceanic and Atmospheric Administration<br>NYCHA = New York City Housing Authority<br>OSM = Open Street Map<br>DOE = NYC Dept. of Education | text | 
| B7SC | The Street Code assigned to a CommonPlace . | text | 
| PRI_ADD | The Addresspoint ID if the CommonPlace is related to any Addresspoint | double | 
| NAME | The name of the CommonPlace. Most name come from Feature name table. | text | 
