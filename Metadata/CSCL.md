# CSCL


Geometry Type: point, line, polygon<br><br>![image](../Images/CSCL.png)

# Table of Contents 
- [Identification](#identification)
- [Data Quality and Specifications](#data-quality-and-specifications)
- [Feature Classes](#feature-classes) 


## Identification


|     |     |
| --- | --- |
**Purpose** |CSCL (Citywide Street Centerline) is a Geodatabase managed by the Department of City Planning (DCP) and the Office of Technology and Innovation (OTI). The CSCL database was developed subsequent to 9/11 to ensure that all the NYC public safety agencies were working with GIS data from a common source. CSCL data feeds the NYPD 911 call-takers maps as well as each of the unique dispatch systems used by NYPD, FDNY, and FDNY EMS. It also supplies city agencies and the public with an authoritative source for a variety of other GIS data. CSCL is used to produce the Dept. of City Planning’s Geosupport software, a geocoding system widely used by city agencies and the public.
**Description** |CSCL is governed by 7 city agencies: DCP, OTI, NYPD, FDNY, OEM, DOT, and DEP. CSCL centrally maintains database of street, address, common place, and additional location data to support public safety dispatching, serving as the authoritative source for New York City’s geographic data. The data is edited on a daily basis and updates are synchronized nightly to NYPD, FDNY, DOT, DSNY, OEM and OTI-PSGIS. The CSCL database contains 72 feature classes, 38 tables and 46 relationships that are described below.
**Publication Dates** |**Last Update**: Weekly<br>**Metadata**: 12/11/2024<br>**Update Frequency**: Features are updated daily by OTI staff and released publicly on [NYCMaps](https://nycmaps-nyc.hub.arcgis.com/). 
**Available Formats** | (zipped) ESRI File Geodatabase 
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |https://nyc.maps.arcgis.com/home/item.html?id=113249f31f994dde836f3617c9bca1e3
**Tags** |CSCL


## Data Quality and Specifications

|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot ([epsg:2263](https://spatialreference.org/ref/epsg/2263/))
**Resolution** |NA?
**Spatial Coverage** |New York City, NY
**Positional Accuracy** |NA? 
**Features Captured** |See individual feature classes listed below



## Feature Classes 

| Feature Class | Summary | Description |
| ---|---|---|
|AccessPoint|To provide Emergency Services with additional information on accessing locations.|Access points are primarily along the street and represent a point of access to one or more entrances of a building (mostly schools and gated building complexes).  In some cases, they are also in the interior of a building complex, because of internal fences or gates. In other cases, an access point represents access to an alley or walkway in the rear or side of a building. Access Points were originally field collected. There is no known source available to compare the field collected data, either for spatial location or attribute accuracy.|
|AddressPoint|Address points were developed to supplement the address information supplied by the CSCL centerline. Some computer aided dispatch systems use address points as the primary source for locating an address.|AddressPoints model actual addresses present in the field. AddressPoints are created approximately five feet inside building footprints along the correct street frontage. Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file.|
|AdjacentBoroughBoundary| |Polygon feature class that is used in a downstream process to alter the Borough for areas where FDNY and NYPD handle 911 calls differently. e.g. FDNY handles Roosevelt Island as Manhattan and NYPD handles Roosevelt Island as Queens. Polygons are drawn ad-hoc but using CSCL.Centerline and CSCL.Borough as a reference. Data is maintained by OTI-PSGIS group.|
|AlarmBox|FDNY Alarm Box locations.|This feature class can be used only by expressed permission from FDNY, City of New York only.|
|AlarmBoxArea|N/A|N/A|
|AssemblyDistrict|These districts were created by the Department of City Planning to aid city agencies in administering public services.|New York State assembly district boundaries for the City of New York. These districts were created by the Department of City Planning to aid city agencies in administering public services.|













