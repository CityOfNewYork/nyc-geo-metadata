# Street Centerline (CSCL)
Centerline.shp <br>
Geometry Type: Polyline

![image](https://github.com/ekamptner/test-repo/blob/master/Images/StreetCenterline.PNG)

### Table of Contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Organization**](#2-data-quality-and-organization)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)

## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** | The Centerline file has been maintained as a major component of the Department of City Planning's Geosupport System and has been updated to meet the needs of the public safety agencies for dispatch.
**Description** | Centerline is a single line representation of New York City streets containing address ranges and other information such as traffic directions, road types, segment types.
**Source(s)** |	Department of City Planning
**Publication  Dates** | **Data**:  <br>**Last Update**: Today <br> **Metadata**: 11/14/2016 <br> **Update Frequency**: Daily
**Spatial Coverage** | New York City, NY
**Temporal Coverage** | Data is current as of last update date. 
**Available Formats** | shapefile. Additional data formats are available for download on the OpenData Portal.
**Use Limitations** | While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** | Public
**Contact Information** | **Name**: Department of Information Technology and Telecommunication (DOITT), GIS <br>**Phone**: ###-###-#### <br> **Email**: gis-group@doitt.nyc.gov
**Links** | The street centerline data layer is available for download on NYC Open Data Portal -- https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL
**Tags** | LION, CSCL, Highway, Staten Island, Manhattan, Queens, Bronx, New York, Streets, Transportation, Brooklyn, Roads, transportation, centerline
	
## 2. Data Quality and Organization
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** | New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** | NA	
**Features Captured** |	--
**Features Excluded** | --
**Positional Accuracy** | --
**Capture and Update Notes** | --

## 3. Attribute Information
-----------------------------------
Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes
------------ | ------------- | -------- | ----------- | ----------
FID | Unique feature Identification Number. | Integer | N | NA
SHAPE | Geometry Field | Geometry | N  | NA
PHYSICALID | A unique ID assigned in order to aggregate granular geometry to represent a Physical View of the city's street network. In CSCL, segmentation is very granular in order to accommodate many types of physical and non-physical geometry. The PHYSICALID is a unique number used to identify a physically existing piece of geometry that may or may not be comprised of several SEGMENTIDs. For example, E 28 Street between 2nd Ave and 3rd Ave in Manhattan would have 1 PHYSICALID although there are 3 segments defining that block face, with 3 separate SEGMENTIDs. | Integer | N  | NA
L_LOW_HN | Low value for the address range on the left side of the street segment, relative to the digitized direction of the segment.  | Text | N  | NA
L_HIGH_HN | High value for the address range on the left side of the street segment, relative to the digitized direction of the segment. | Text | N  | NA
R_LOW_HN | Low value for the address range on the right side of the street segment, relative to the digitized direction of the segment.  | Text | N  | NA
R_HIGH_HN | High value for the address range on the right side of the street segment, relative to the digitized direction of the segment. | Text | N  | NA
L_ZIP | Five digit postal zip code for the left side of the street segment, relative to the digitized direction of the segment.  | Text | N  | NA
R_ZIP | Five digit postal zip code for the right side of the street segment, relative to the digitized direction of the segment.  | Text | N  | NA
L_BLKFC_ID | A ten digit number identifying the block face on the left hand side of a segment. Block Face is defined as one continuous side of a physical block that is intersected on that side by two other physical through streets. Blockface IDs were established by DoITT’s consultants working on the planimetric feature classes for NYC and are not maintained by the Department of City Planning. | Text | N  | NA
R_BLKFC_ID |A ten digit number identifying the block face on the right hand side of a segment. Block Face is defined as one continuous side of a physical block that is intersected on that side by two other physical through streets. Blockface IDs were established by DoITT’s consultants working on the planimetric feature classes for NYC and are not maintained by the Department of City Planning. | Text | N  | NA
ST_NAME | Street Name added for cartographic labeling purposes. | Text | N  | NA
STATUS | Refers to the construction status of a street segment: Constructed, Paper, Under Construction, Demapped, or Paper Street Coincident With Boundary. | Text | N  | NA
BIKE_LANE | Defines which segments are part of the bicycle network as defined by the NYC Department of Transportation. | Text | N  | NA
BOROCODE | A 1-digit code identifying the borough the feature is located in. | Integer | N  | NA
ST_WIDTH | The width, in feet, of the paved area of the street. | Integer | N  | NA
CREATED | Date record was created | Date | N  | NA
MODIFIED | Date record was modified | Date | N  | NA
TRAFDIR | Traffic Direction Code indicating the flow of traffic relative to the street segment's digitized direction. | Text | N  | NA
RW_TYPE | ? | Integer | N  | NA
FRM_LVL_CO | ? | Text | N  | NA
TO_LVL_CO | ? | Text | N  | NA
SNO_PRI | ?| Integer | N  | NA
SHAPE_Leng | Physical ID | Integer | N  | NA