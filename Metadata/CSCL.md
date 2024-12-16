# CSCL


Geometry Type: point, line, polygon<br><br>![image](../Images/CSCL.png)

# Table of Contents 
- [Identification](#identification)
- [Data Quality and Specifications](#data-quality-and-specifications)
- [Feature Classes](#feature-classes) 


## Identification


|     |     |
| --- | --- |
**Purpose** |CSCL (Citywide Street Centerline) is a geodatabase managed by the Department of City Planning (DCP) and the Office of Technology and Innovation (OTI). The CSCL database was created after 9/11 to ensure that all NYC public safety agencies use the same GIS data. CSCL data is used by NYPD 911 call-takers, NYPD, FDNY, and FDNY EMS dispatch systems. It is also an authoritative source for various other GIS data, used by city agencies and the public. CSCL helps produce the Dept. of City Planning’s Geosupport software, a widely used geocoding system.
**Description** |CSCL is managed by seven city agencies: DCP, OTI, NYPD, FDNY, OEM, DOT, and DEP. It maintains a central database of street, address, common place, and other location data to support public safety dispatching. This database is the main source of geographic data for New York City. The data is updated daily and synchronized every night with NYPD, FDNY, DOT, DSNY, OEM, and OTI-PSGIS. The CSCL database includes 72 feature classes, 38 tables, and 46 relationships.
**Publication Dates** |**Last Update**: Weekly<br>**Metadata**: 12/11/2024<br>**Update Frequency**: Features are updated daily by staff and released publicly on [NYCMaps](https://nycmaps-nyc.hub.arcgis.com/). 
**Available Formats** | (zipped) ESRI File Geodatabase 
**Use Limitations** |NYC Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Links** |https://nyc.maps.arcgis.com/home/item.html?id=113249f31f994dde836f3617c9bca1e3
**Tags** |CSCL


## Data Quality and Specifications

|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot ([epsg:2263](https://spatialreference.org/ref/epsg/2263/))
**Spatial Coverage** |New York City, NY
**Positional Accuracy** |Varies 
**Features Captured** |See individual feature classes listed below



## Feature Classes 

Some feature classes in the geodatabase are not described here because they are not actively maintained or used.

| Feature Class | Summary | Description |
| ---|---|---|
|AccessPoint|Provides Emergency Services with additional information on accessing locations.|Access points are primarily along the street and represent a point of access to one or more entrances of a building (mostly schools and gated building complexes).  In some cases, they are also in the interior of a building complex, because of internal fences or gates. In other cases, an access point represents access to an alley or walkway on the rear or side of a building. Access Points were originally field collected. There is no known source available to compare the field collected data, either for spatial location or attribute accuracy.|
|AddressPoint|Address points supplement the address information supplied by CSCL centerlines. Some computer aided dispatch systems use address points as the primary source for locating an address.|AddressPoints model actual addresses present in the field. AddressPoints are created approximately five feet inside building footprints along the correct street frontage. Address points were initially created from data in the Department of City Planning Property Address Directory (PAD) file.|
|AdjacentBoroughBoundary|Used internally by public safety systems. |Polygon feature class that is used in a downstream process to alter the Borough for areas where FDNY and NYPD handle 911 calls differently. e.g. FDNY handles Roosevelt Island as Manhattan and NYPD handles Roosevelt Island as Queens. Polygons are drawn ad-hoc but using Centerlines and Boroughs as a reference. Data is maintained by OTI-Public Safety GIS.|
|AlarmBox|FDNY Alarm Box locations.|***This feature class can be used only by expressed permission from FDNY, City of New York only.*** ?|
|AssemblyDistrict|Created by the Department of City Planning to aid city agencies in administering public services.|New York State assembly district boundaries for the City of New York. |
| AtomicPolygon         | Atomic polygons serve as a set of basic building blocks for generating the polygons of many of the district types represented in the CSCL database. Data is maintained by DCP.   |     |
|Borough |Depicts the coverage area for each borough | Borough is a polygon representation of New York City boroughs (Manhattan, Brooklyn, Bronx, Queens, and Staten Island) maintained by the Department of City Planning.|
| BusinessImprovementDistrict | Geographic boundaries of Business Improvement Districts (BID).                       | This dataset contains Business Improvement District (BID) Name and geographic boundaries. Data is provided by the BID Board of Directors.                                                                   |
| CellularCallBox             | Locations of NYPD maintained call boxes.           | Call box locations are determined through several methods, including manual placement based on orthophotography, field-collected coordinates, existing location data and automated geoprocessing.           |
| CensusBlock2020        | US Census polygons created by the Department of City Planning.             | 2020 US Census Block boundaries, derived from the US Census Bureau's TIGER database, and modified for use in New York City by dissolving appropriate fields within atomic polygons.      |
| CensusBlock2010        | US Census polygons created by the Department of City Planning.             | 2010 US Census block boundaries, derived from the US Census Bureau's TIGER database and modified for use in New York City by dissolving appropriate fields within atomic polygons.      |
| CensusBlock2000        | US Census polygons created by the Department of City Planning.             | 2000 US Census Block boundaries, derived from the US Census Bureau's TIGER database, and modified for use in New York City by dissolving appropriate fields within atomic polygons.      |
| CensusTract1990             | US Census polygons created by the Department of City Planning.             | 1990 US Census Tract boundary files, derived from the US Census Bureau's TIGER database. These boundaries have been geographically modified to align with the New York City base map.       |
| CensusTract2000             | US Census polygons created by the Department of City Planning.               | 2000 US Census Tract boundary files, derived from the US Census Bureau's TIGER database. These boundaries have been geographically modified to align with the New York City base map.       |
| CensusTract2010             | US Census polygons created by the Department of City Planning.              | 2010 US Census Tract boundary files, derived from the US Census Bureau's TIGER dtabase. These boundaries have been geographically modified to align with the New York City base map.       |
| CensusTract2020             | US Census polygons created by the Department of City Planning.               | 1990 US Census Tract boundary files, derived from the US Census Bureau's TIGER database. These boundaries have been geographically modified to align with the New York City base map.       |
| Centerline            | The Centerline file has been maintained as a major component of the Department of City Planning's Geosupport System and has been updated to meet the needs of the public safety agencies for dispatch. | Centerline is a single line representation of New York City streets containing address ranges and other information such as traffic directions, road types, segment types. Data is maintained by DCP.      |
| CityCouncilDistrict         | NYC council districts             | The City Council Districts are the result of the redistricting process, which takes place every ten years to reflect population changes reported in the latest Census. These geographies were redrawn by DCP. |
| CityLimit  | For use by CSCL users to define city limits.  | This feature class consists of a polygon defining the limits of New York City. It is maintained by DCP.        |
| CommonPlace       | CommonPlace is a point feature representation of points of interest throughout New York City.     | CommonPlace points are a compilation of what the different city agencies consider to be a Common Place or Place/Point of Interest. Data is maintained by OTI and DCP.           |
| CommunityDistrict    | NYC community districts           | Community Districts are mandated by the city charter to review and monitor quality of life issues for New York City neighborhoods. This feature class is maintained by DCP.  |
| Complex     | Areas that represent major complexes throughout the NYC.  | Complex polygons represent various New York City developments, encompassing colleges, hospitals, railyards, parks, commercial centers, public housing, and government campuses.            |
| CongressionalDistrict       | This feature class depicts the boundaries of United States Congressional Districts within NYC.    | This dataset provides a detailed representation of the legal boundaries for each US House of Representatives district within the NYC limits. It is maintained by DCP.      |
| ElectionDistrict         | NYC Board of Elections election districts       | These district boundaries represent the redistricting following each decennial US Census and subsequent redistricting processes. It is extracted by dissolving combined appropriate fields in atomic polygons. This feature class is maintained by the Department of City Planning. |
| EMSAtom      | This data is supplied to provide map area coverage used by EMSCAD software to determine the location and EMS_Atom of EMS Units based on locations reported via on-board vehicle location (GPS) system.    | EMS_Atoms v4 This is version '4' of the EMS Atoms series. Prepared 2009.04.10 Used in the production of Geofiles for the EMSCAD dispatching system to resolve vehicle locations obtained via GPS location reports. This version provides two levels of enhancement: 1) Updates and corrections to atom boundaries, 2) Edit boundaries to conform to LION 07C geometry (Initial CSCL base data) Refinements were made by Bowne Mgmnt under the direction of the HP/AVL and FDNY GIS team through April 2009. This feature class was originally created by FDNY GIS Unit and EMS AVL project team for use with EMSCAD systems. |            |
| EntrancePoint     | Secondary entrances to a building.         | Entrance Point is a point representation of New York City buildings that are associated with Access Points. The entrance point must be a physical entry at street level (i.e. rooftop entry will not be considered an entrance point). An entrance point does not have a posted address number. |
| ESINETAtomicLine       |    | Polyline feature class used for the creation of Provisioning, PSAP, and Emergency Service Boundaries in a downstream process. Source is CSCL.Borough and CSCL.CityLimit. In some cases, some lines are drawn ad-hoc. This feature class is maintained by OTI Public Safety GIS.      |
| ESINETAtomicPoint    |     | Point feature class containing attribute data used for the creation of Provisioning, PSAP, and Emergency Service Boundaries in a downstream process. Points are placed ad-hoc based on the Provisioning, PSAP, and Emergency Service Boundaries required.        |
| FireBattalion              | FDNY fire battalion boundaries      | The service area boundaries for New York's fire battalions. Data is maintained by DCP and provided by FDNY.       |
| FireCompany                | FDNY fire company boundaries    | The service area boundaries for New York City's fire companies. Data is maintained by DCP and provided by FDNY.      |
| FireDivision               | FDNY fire division boundaries      | The service area boundaries for New York City's fire divisions. Data is maintained by DCP and provided by FDNY.     |
| HealthArea                 | Boundaries for New York City’s health areas.       |          |
| HealthCenterDistrict       | Boundaries for New York City’s health center districts |  |
| HistoricDistrict           | Boundaries for New York City’s Historic Districts. | Maintained by OTI using data from the Landmarks Preservation Commission  |
| HurricaneEvacuationZone    | Hurricane evacuation zone category (1-6) for locations in New York City.  | New York City's hurricane contingency plans are based on six evacuation zones. Hurricane evacuation zones are areas of the city that may be inundated by storm surge or isolated by storm surge waters. There are six zones, ranked by the risk of storm surge impact, with Zone 1 being the most likely to flood. In the event of a hurricane or tropical storm, residents in these zones may be ordered to evacuate. Data is maintained by DCP.           |
| LinkNYC               | LinkNYC kiosk point feature locations in New York City.                  |  |
| MunicipalCourtDistrict| New York City's Municipal Court boundaries.      |       |
| Neighborhood          | Projection areas were created using whole census tracts that were exact subdivisions of NYC's PUMAs. | These 'Neighborhoods' are in essence projection areas created to project populations at a small area level, from 2000 to 2030. These aggregations were driven by population size in 2000. Data is maintained by the Department of City Planning.                                      |
| Node                  | Nodes represent the locations of any combination of linear features in CSCL (a topological junction). Data is maintained by DCP.    |  Nodes are useful for several reasons: 1) Assignment of a value to an intersection (e.g. reference an incident to an intersection, 2) Used to help assign location to other CSCSL datasets (e.g. Virtual Intersections, Special Intersections) and 3) Required for data editing to support Geosupport.     |
| NonStreetFeature      | NonStreetFeature is a single line representation of non-street features. The LION file includes some of these and are identified by Feature Type. Data is maintained by DCP.       |  The following are non-street feature subtypes: 1) Census_block 2) District_Boundary 3) Election_District 4) Other 5) Physical_Non_ST_Feature 6) Pier_Outline 7) School_District                                                                     |
| NTA2020               | Neighborhood tabulation areas | Created by DCP to be used with data from Census 2020.     |
| NYPDBeat              | The service area boundaries for New York City's police posts. |           |
| NYPDPatrolBorough     | NYPD patrol borough boundaries.    |    |
| NYPDPrecinct          | Service area boundaries for New York City's police precincts.       |  |
| NYPDSector            | Service area boundaries for New York City's police sector.                                    | This feature class represents area boundaries for New York City’s police sectors. Created by dissolving beats. The updated NYPD sector boundaries effective since July 1, 2013. Data is maintained by NYPD.  |
| NYPDTow               | Boundaries for New York City’s tow zones.     |    |
| Rail   | Rail is a single line representation of New York City railroads containing route and other information. Data is maintained by DCP.   |       |
| RailStation           | Location of rail stations with detailed attributes such as subway type, division, line.|  |
| ReferenceMarker       |  Reference markers are small signs that are positioned systematically at points along state-maintained roads and highways. NYS DOT maintains a system of reference markers affixed to posts, walls, railings, and other prominent physical features. Data is maintained by DCP. | Reference markers are positioned approximately every one-tenth of a mile along arterials. The reference marker panel legends contain up to twelve alphanumeric characters of identifying information, consisting of a NYS DOT route identification code, identifiers of the county/locality, and a reference marker sequencing number. Reference markers are part of CSCL to assist in identifying a location along an arterial highway.  |
| SchoolDistrict        | NYC School District boundaries.   |     |
| Shoreline             | Shoreline is a single line representation of New York City shorelines.| |
| StateSenateDistrict   | New York State Senate district boundaries for the City of New York.   |     |
| Subway                |  Subway is a single line representation of the New York City subway system. Data is maintained by OTI and includes attributes such as subway type, division, line name, and route.  |     |
| SubwayStation         | Subway stations with detailed attributes such as subway type, division, line.|    |
| TollBooth             | New York City's tollbooth locations. | |
| TrafficCamera         | New York City's traffic camera locations. |          |
| TransitBooth          | Location of subway system transit booths.|     |
| TransitEmergencyExit  | Location of transit emergency exits. |                     |
| TransitEntrance       | Transit entrance is a point feature class identifying the location of MTA and LIRR station entrances.|   
| VirtualCenterline     | NYPD virtual intersections | Virtual centerline was created by importing street segments from NYPD PCAD geodatabases where the classes are equal to "VI" or "CPK". These represent centerline geometries that are unique to the police department which may include streets, water features, and other spatial features.       |
| ZipCode               | New York City’s ZIP Codes.                                                | This feature class was originally created by the City Planning Department, and it is now updated periodically by OTI. |









