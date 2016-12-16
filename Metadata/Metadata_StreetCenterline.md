# Street Centerline
Filename: Centerline.shp<br>Geometry Type: polyline<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/StreetCenterline.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The Centerline file has been maintained as a major component of the Department of City Planning's Geosupport System and has been updated to meet the needs of the public safety agencies (NYPD & FDNY) for dispatch.
**Description** |The original source of geomtry for centerline was Linear Integrated Ordered Network (LION), which was maintained by the Department of City Planning. Centerline is a single line representation of New York City streets containing address ranges and other information such as traffic directions, road types, segment types. Street Centerline is part of the Citywide Street Centerline (CSCL) enterprise geospatial database and data maintenance system that supports multiple agencies, including the emergency 911 dispatching systems. 
**Source(s)** |Department of City Planning, Linear Integrated Ordered Network (LION)
**Publication Dates** |**Data**: 4/19/2014<br>**Last Update**: 11/17/2016<br>**Metadata**: 12/02/16<br>**Update Frequency**: Agency data is updated daily by Centerline Management Group (CMG). Public releases of this data are made X
**Available Formats** |Shapefile. Additional data formats are available for download on the [NYC Open Data Portal](https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/exjm-f27b).
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/exjm-f27b
**Tags** |New York, Manhattan, Staten Island, LION, Bronx, Transportation, Queens, centerline, Brooklyn, Highway, CSCL, Streets, Roads
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Data is current as of last update date.
**Positional Accuracy** |The dataset represents the roadbed centerline. 
**Features Captured** |The dataset includes information on traffic directions, road types, and segment types. 
**Features Excluded** |
**Capture and Update Notes** |The Centerline Maintenance Group (CMG) is the entity that is responsible for all updates to the CSCL centerline.  Agency users of CSCL use a "CSCL User Update Tracking System" to submit discrepancies and update requests. These requests are routed to the CMG group for update and review daily. The Department of City Planning (DCP) is responsible for segments whose SEGMENTID >-9000000 and are crated by CSCL.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| PHYSICALID | A unqiude ID assigned to intersection to intersection stretches of a street.  | double | No
| L_LOW_HN | Low value for the address range on the left side of the street segment, relative to the digitized direction of the segment. | text | No
| L_HIGH_HN | High value for the address range on the left side of the street segment, relative to the digitized direction of the segment. | text | No
| R_LOW_HN | Low value for the address range on the right side of the street segment, relative to the digitized direction of the segment. | text | No
| R_HIGH_HN | High value for the address range on the right side of the street segment, relative to the digitized direction of the segment. | text | No
| L_BLKFC_ID | A ten-digit number identifying the block face on the left hand side of a segment. Block Face is defined as one continuous side of a physical block that is intersected on that side by two other physical through streets. Blockface IDs were established by DoITT's consultants working on the planimetric feature classes for NYC and are not maintained by the Department of City Planning. | double | No
| R_BLKFC_ID | A ten-digit number identifying the block face on the right hand side of a segment. Block Face is defined as one continuous side of a physical block that is intersected on that side by two other physical through streets. Blockface IDs were established by DoITT's consultants working on the planimetric feature classes for NYC and are not maintained by the Department of City Planning. | double | No
| R_ZIP | Five-digit postal zip code for the right side of the street segment, relative to the digitized direction of the segment. | text | No
| L_ZIP | Five-digit postal zip code for the left side of the street segment, relative to the digitized direction of the segment. | text | No
| ST_NAME | Street Name added for cartographic labeling purposes. | text | No
| STATUS | Refers to the construction status of a street segment: Constructed, Paper, Under Construction, Demapped, or Paper Street Coincident with Boundary. <br>1 = Planned Private <br>2 = Constructed <br>3 = Paper <br>4 = Under Construction <br>5 = Demapped <br>9 = Paper Street Coincident with Boundary | text | No
| BIKE_LANE | Defines which segments are part of the bicycle network as defined by the NYC Department of Transportation. <br>1 = Class I <br>2 = Class II <br>3 = Class III <br>4 = Links <br>5 = Class I, II <br>6 = Class II, III <br>7 = Stairs <br>8 = Class I, III <br>9 = Class II, I <br>10 = Class III, I <br>11 = Class III, II | text | No
| BOROCODE | Numeric codes for NYC 5 boroughs. <br>1 = Manhattan<br>2 = Bronx<br>3 = Brooklyn<br>4 = Queens<br>5 = Staten Island | text | No
| ST_WIDTH | The width, in feet, of the paved area of the street | double | No
| CREATED | Date feature was created | date | No
| MODIFIED | Date the feature was last modified | date | No
| TRAFDIR | Traffic Direction. Code indicating the flow of traffic relative to the street segment's address range.<br>FT = With<br>TF = Against<br>TW = Two-Way<br>NV = Non-Vehicular | text | No
| RW_TYPE | Street Centerline roadway type.<br>1 = Street<br>2 = Highway<br>3 = Bridge<br>4 = Tunnel<br>5 = Boardwalk<br>6 = Path/Trail<br>7 = StepStreet<br>8 = Driveway<br>9 = Ramp<br>10 = Alley<br>11 = Unknown<br>12 = Non-Physical Street Segment<br>13 = U Turn<br>14 = Ferry Route | integer | No
| FRM_LVL_CO | Numeric value indicating the vertical position of the feature's "from" node relative to grade level. <br> 1 = Below Grade 1  <br> 2 = Below Grade 2  <br> 3 = Below Grade 3  <br> 4 = Below Grade 4  <br> 5 = Below Grade 5  <br> 6 = Below Grade 6  <br> 7 = Below Grade 7  <br> 8 = Below Grade 8 <br> 9 = Below Grade 9   <br> 10 = Below Grade 10  <br> 11 = Below Grade 11  <br> 12 = Below Grade 12  <br> 13 = At Grade <br> 14 = Above Grade 1  <br> 15 = Above Grade 2  <br> 16 = Above Grade 3 <br> 17 = Below Grade 4  <br> 18 = Below Grade 5  <br> 19 = Below Grade 6  <br> 20 = Below Grade 7  <br> 21 = Below Grade 8 <br> 22 = Below Grade 9   <br> 23 = Below Grade 10  <br> 24 = Below Grade 11  <br> 25 = Below Grade 12 <br> 25 = Below Grade 12<br> 26 = Below Grade 13<br> 99 = Not Applicable | integer | No
| TO_LVL_CO | Numeric value indicating the vertical position of the feature's "to" node relative to grade level. <br> 1 = Below Grade 1  <br> 2 = Below Grade 2  <br> 3 = Below Grade 3  <br> 4 = Below Grade 4  <br> 5 = Below Grade 5  <br> 6 = Below Grade 6  <br> 7 = Below Grade 7  <br> 8 = Below Grade 8 <br> 9 = Below Grade 9   <br> 10 = Below Grade 10  <br> 11 = Below Grade 11  <br> 12 = Below Grade 12  <br> 13 = At Grade <br> 14 = Above Grade 1  <br> 15 = Above Grade 2  <br> 16 = Above Grade 3 <br> 17 = Below Grade 4  <br> 18 = Below Grade 5  <br> 19 = Below Grade 6  <br> 20 = Below Grade 7  <br> 21 = Below Grade 8 <br> 22 = Below Grade 9   <br> 23 = Below Grade 10  <br> 24 = Below Grade 11  <br> 25 = Below Grade 12 <br> 25 = Below Grade 12<br> 26 = Below Grade 13<br> 99 = Not Applicable | integer | No
| SNOW_PRI | Department of Sanitation (DSNY) snow removal priority designation. V=Non-DSNY, C=Critical, H=Haulster, S=Sector | text | No
