# CSCL Pub

Geometry Type: point, line, polygon<br><br>![image](../Images/CSCL.png)

# Table of Contents 
- [Identification](#identification)
- [Data Quality and Specifications](#data-quality-and-specifications)
- [Feature Classes](#feature-classes) 


## Identification


|     |     |
| --- | --- |
**Purpose** |The Published Citywide Street Centerline (CSCL) is a comprehensive and authoritative spatial database for the City of New York. It contains the published version of geographic features and data. It is used by many city agencies including Public Safety call centers, the Department of City Planning's Geosupport, and FDNY EMS dispatch systems. The published CSCL database is accessible to the public and will support the Next Generation 911 system.
**Description** |This published CSCL database is an [ESRI file geodatabase](https://en.wikipedia.org/wiki/Geodatabase_(Esri)) and includes a feature dataset, 40 feature classes, 3 tables, and 2 relationship classes. The source data for the published CSCL database is updated daily by the NYC Office of Technology and Innovation (OTI) and the Department of City Planning (DCP) and is governed by 8 city agencies.
**Publication Dates** |**Last Update**: Weekly<br>**Metadata**: 01/16/2025<br>**Update Frequency**: Features are updated daily by staff and released publicly on [NYCMaps](https://nycmaps-nyc.hub.arcgis.com/). 
**Available Formats** | (zipped) ESRI File Geodatabase 
**Use Limitations** |NYC Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |https://nyc.maps.arcgis.com/home/item.html?id=9163b04952354da2bf748abe1788e985
**Tags** |CSCL Pub


## Data Quality and Specifications

|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot ([epsg:2263](https://spatialreference.org/ref/epsg/2263/))
**Spatial Coverage** |New York City, NY
**Positional Accuracy** |Varies 
**Features Captured** |See feature classes listed below

----

## Feature Classes 

Some feature classes in the geodatabase are not described here because they are not actively maintained or used.
| Feature Type | Name | Description |
| ---|---|---|
|**Feature Dataset**|CSCL|The CSCL feature dataset is a collection of the following features and relationship classes: Centerline, Milepost, Node, NonStreetFeature, Rail, ReferenceMarker, Shoreline, Subway, CenterlineHaveAddresses, CenterlineHaveNames.|
|**Points**|AddressPoint||
| |CommonPlace| |
| |FerryLanding| |
| |MilePost| |
| |NamedIntersection| |
| |Node| |
| |RailStation| |
| |ReferenceMarker| |
| |SubwayStation| |
| |TollBooth| |
|**Lines**|Centerline|Centerline is a single line representation of New York City streets containing address ranges and other information such as traffic directions, road types, segment types.|
| |NonStreetFeature| |
| |Rail| |
| |Shoreline| |
| |Subway| |
|**Polygon**|AssemblyDistrict||
| |Borough| |
| |BusinessImprovementDistrict|
| |CensusBlock2000| |
| |CensusBlock2010| |
| |CensusBlock2020| |
| |CensusTract2000| |
| |CensusTract2010| |
| |CensusTract2020| |
| |CityCouncilDistrict| |
| |CommunityDistrict| |
| |Complex| |
| |CongressionalDistrict| |
| |ElectionDistrict| |
| |FireCompany| |
| |HealthArea| |
| |HealthCenterDistrict| |
| |HistoricDistrict| |
| |HurricaneEvacuationZone| |
| |MunicipalCourtDistrict| |
| |Neighborhood| |
| |NYPDPrecinct| |
| |SchoolDistrict| |
| |StateSenateDistrict| |
| |ZipCode| |
|**Tables**|ALTSEGMENTDATA| |
| | FEATURENAME | |
| | StreetName | |
|**Relationship Classes**|The CSCL feature dataset includes 2 [ESRI Relationship classes](https://pro.arcgis.com/en/pro-app/latest/help/data/relationships/geodatabase-relationship-class-fundamentals.htm) to manage the associations between objects in one feature class or table and objects in another. |<ul><li>CenterlinesHaveAltAddresses</li><li>CenterlinesHaveNames</li></ul> |


