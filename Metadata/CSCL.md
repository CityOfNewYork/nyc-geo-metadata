# CSCL


Geometry Type: point, line, polygon<br><br>![image](../Images/CSCL.png)

# Table of Contents 
- [Identification](#identification)
- [Data Quality and Specifications](#data-quality-and-specifications)
- [Feature Classes](#feature-classes) 


## Identification


|     |     |
| --- | --- |
**Purpose** |The Citywide Street Centerline (CSCL) is a comprehensive and authoritative database for the City of New York. It comprises various geographic features and data, utilized by numerous city agencies, including Public Safety call centers, the Department of City Planning's Geosupport, and FDNY EMS dispatch systems. The CSCL is accessible to the public and will support the Next Generation 911 system.
**Description** |This CSCL database is an ESRI Enterprise geodatabase and consists of a feature dataset, more than 72 feature classes, 38 tables, and 46 relationship classes. The CSCL database is updated daily by the NYC Office of Technology and Innovation (OTI) and the Department of City Planning (DCP) and is governed by 8 city agencies.
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
| Feature Yype | Name | Description |
| ---|---|---|
|**Feature Dataset**|CSCL|The CSCL feature dataset is a collection of the following features and relationship classes: Atomic Polygon, Centerline, Median, Milepost, Node, Non-Street Feature, Rail, Reference Marker, Shoreline, Subway, CenterlineHaveAddresses, CenterlineHaveMileposts, and CenterlineHaveReference Markers.|
|**Points**|AccessPoint|Access points are primarily along the street and represent a point of access to one or more entrances of a building.|
||AddressPoint|AddressPoints are a data model that represents the actual addresses present in the field.|
||AlarmBox|Locatiosn of FDNY Alarm Boxs.|
||CellularCallBox|Locations of NYPD maintained call boxes.|
||CommonPlace|CommonPlace is a point feature dataset representing locations of various points of interest within the boundaries of New York City, such as schools, churches, parks, and museums.|
||ComplexAccessPoint|A reserved placeholder for future data.|
||EntrancePoint|Entrance Point is a point representation of New York City buildings that are associated with Access Points. The entrance point must be a physical entry at street level (i.e. rooftop entry will not be considered an entrance point). An entrance point does not have a posted address number.|
||ESINETAtomicPoint|This point feature class contains attribute data used for the creation of Provisioning, PSAP, and Emergency Service Boundaries in a downstream process. This point feature class is to be used by the Next Gen 911 system.|
||LinkNYC|LinkNYC kiosk point feature locations in New York City.|
||NYPDReferenceMarkers|This dataset represents the locations of New York State-maintained reference marker signs within New York City, situated along roads and highways. This data is utilized by the NYPD.|
||RailStation|Locations of all rail stations within New York City.|
||SubwayStation|Locations of all Subway stations within New York City.|
||TollBooth|New York City's tollbooth locations.|
||TrafficCamera|Locations of NYC DOT traffic cameras.|
||TransitBooth|Location of subway system transit booths.|
||TransitEmergencyExit|Location of MTA transit emergency exits.|
||TransitEntrance|Transit entrance is a point feature class identifying the location of MTA and LIRR station entrances.|
|**Lines**|Centerline|Centerline is a single line representation of New York City streets containing address ranges and other information such as traffic directions, road types, segment types.|
||NonStreetFeature|NonStreetFeature is a single-line representation of non-street features. The subtypes of NonStreetFeature include:1) Census_block 2) District_Boundary 3) Election_District 4) Other 5) Physical_Non_ST_Feature 6) Pier_Outline 7) School_District.|
||Rail|Rail is a single line representation of New York City railroads containing route and other information.|
||Shoreline|Shoreline is a single line representation of New York City shorelines.|
||VirtualCenterline|To represent NYPD virtual intersections.These represent centerline geometries unique to the police department, including streets, water features, and other spatial elements.|
|**Polygon**|AtomicPolygon|Atomic polygons serve as a set of basic building blocks for generating the polygons of many of the district types represented in the CSCL database.|
||Median|A reserved placeholder for future data.|
||AdjacentBoroughBoundary|Polygon feature class that is used in a downstream process to alter the Borough for areas where FDNY and NYPD handle 911 calls differently. Polygons are drawn ad-hoc but using Centerlines and Boroughs as a reference. Data is maintained by OTI-Public Safety GIS.|
||AlarmBoxArea||
||AssemblyDistrict|New York state assembly district boundaries for the City of New York. It is extracted by dissolving combined appropriate fields in atomic polygons.|
||Borough|Borough is a polygon representation of New York City boroughs.|
||BusinessImprovementDistrict|Dataset contains Business Improvement Districts (BIDs) Name and geographic boundaries.|
||CDTA2020|TBD|
||CensusBlock2000|The Census Blocks for the 2000 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been modified by dissolving combined appropriate fields in atomic polygons.|
||CensusBlock2010|The Census Blocks for the 2010 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been modified by dissolving combined appropriate fields in atomic polygons.|
||CensusBlock2020|The Census Blocks for the 2020 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been modified by dissolving combined appropriate fields in atomic polygons.|
||CensusTract1990|The Census Tracts for the 1990 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been geographically modified to fit the New York City base map. Because some census tract are under water not all census tracts are contained in this file, only census tracts that are partially or totally located on land have been mapped in this file.|
||CensusTract2000|The Census Tracts for the 2000 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been geographically modified to fit the New York City base map. Because some census tract are under water not all census tracts are contained in this file, only census tracts that are partially or totally located on land have been mapped in this file.|
||CensusTract2010|The Census Tracts for the 2010 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been geographically modified to fit the New York City base map. Because some census tract are under water not all census tracts are contained in this file, only census tracts that are partially or totally located on land have been mapped in this file.|
||CensusTract2020|The Census Tracts for the 2020 US Census. These boundary files are derived from the US Census Bureau's TIGER project and have been geographically modified to fit the New York City base map. Because some census tract are under water not all census tracts are contained in this file, only census tracts that are partially or totally located on land have been mapped in this file.|
||CityCouncilDistrict|The City Council Districts are the result of the recent redistricting process, which takes place every ten years to reflect population changes reported in the 2020 Census. These geographies were redrawn by the New York City Council Redistricting Commission.|
||CityLimit|A polygon defining the limits of New York City.|
||CommunityDistrict|Community Districts are mandated by the city charter to review and monitor quality of life issues for New York City neighborhoods. It is extracted by dissolving combined appropriate fields in atomic polygons.|
||Complex|Complex is a polygon representation of New York City complexes including colleges, hospitals, rail yards, parks, commercial centers, and other govermental buildings campuses.|
||CongressionalDistrict|US House of Representatives Congressional District boundaries for the City of New York. These district boundaries represent the redistricting as of the US Census 2020.|
||ElectionDistrict|New York City Board of Elections election districts for the City of New York. These district boundaries represent the redistricting as of the US Census 2020. It is extracted by dissolving combined appropriate fields in atomic polygons.|
||EMSAtom|The EMS Atoms provide map area coverage used by the EMSCAD software to determine the location and corresponding EMS_Atom of EMS units based on the locations reported via on-board vehicle location (GPS) systems. They are also used in the production of Geofiles for the EMSCAD dispatching system to resolve vehicle locations obtained through GPS location reports.|
||EMSBattalion|A reserved placeholder for future data.|
||EMSDispatchArea|A reserved placeholder for future data.|
||EMSDivision|A reserved placeholder for future data.|
||FireBattalion|The service area boundaries for New York's fire battalions.|
||FireCompany|The service area boundaries for New York City's fire companies.|
||FireDivision|The service area boundaries for New York City's fire divisions.|
||HealthArea|The boundaries for New York City's Health Areas.|
||HealthCenterDistrict|The boundaries for New York City's Health Center Areas.|
||HistoricDistrict|The boundaries of New York City's Historic Districts are defined by the Landmarks Preservation Commission.|
||HurricaneEvacuationZone|New York City's hurricane contingency plans are based on six evacuation zones. Hurricane evacuation zones are areas of the city that may be inundated by storm surge or isolated by storm surge waters. There are six zones, ranked by the risk of storm surge impact, with Zone 1 being the most likely to flood. In the event of a hurricane or tropical storm, residents in these zones may be ordered to evacuate.|
||MunicipalCourtDistrict|The New York City Municipal Court boundaries.|
||Neighborhood|An NYC Neighborhood, based on this, is a projection area created from census tracts within New York City's 55 PUMAs (Public Use Microdata Areas). These areas were designed for population projections from 2000 to 2030, with each having at least 15,000 people in 2000 to improve accuracy. The boundaries may not match historical neighborhoods, and the names are not definitive.|
||NTA2020|TBD|
||NYPDBeat|The service area boundaries for New York City's police posts.|
||NYPDPatrolBorough|The boundaries of New York City's NYPD Patrol Boroughs.|
||NYPDPrecinct|The service area boundaries for New York City's police precincts.|
||NYPDSector|The service area boundaries for New York City's police sectors. Created by dissolving beats.|
||NYPDTow|The service area boundaries for New York City's tow zones. Created by combining precincts.|
||QuarterSectionalMap||
||SchoolDistrict|The current NYC School District boundaries. It is extracted by dissolving combined appropriate fields in atomic polygons.|
||SectionalMap|TBD|
||StateSenateDistrict|New York State Senate district boundaries for the City of New York.|
||ZipCode|The boundaries for New York City’s ZIP Codes.|
||UrbanRenewalArea|A reserved placeholder for future data.|
|**Tables**|ADDRESSPOINTLGCS|The AddressPointLGCs table stores additional Local Group Codes (LGCs) to provide alternative street names for address points.|
||ADMINBOUNDARIES|A reserved placeholder for future data.|
||ALTSEGMENTDATA|The AltSegmentData table stores "alternative" data for CSCL centerline, rail, and shoreline segments.|
||BLOCKFACE|A reserved placeholder for future data.|
||CADSOURCEADDRESS|The CADSOURCEADDRESS file contains source records from EMSCAD, Starfire, SPRINT, and PCAD. It was created to store complete source records from public safety geofiles, specifically for commonplace records.|
||CENTERLINEHISTORY|This table records all edits made to centerline segments.|
||COMPLEXINTERSECTION|Complex intersections represent locations where roadbeds intersect with undivided streets or other roadbeds.|
||DELETEDSTREETCODES||
||ELEVATION|A reserved placeholder for future data.|
||EVENTROUTE|A reserved placeholder for future data.|
||FEATURENAME|The FeatureName table stores the names of common places and rail/subway features. It is used to associate one or more names with a CSCL common place point, complex, rail, or subway feature.|
||LASTWORD||
||NAMEDINTERSECTION|The named intersection table associates nodes (intersections) that have names in the City.|
||NEIGHBORHOODPUMACODES|Table that relates DCP neighborhoods to New York City's 55 Public Use Microdata Areas (PUMAs).|
||PARADEROUTE|A reserved placeholder for future data.|
||PERMIT|A reserved placeholder for future data.|
||PHYSICALRESTRICTION|A reserved placeholder for future data.|
||ROADBEDPOINTERLIST|The Roadbed Pointer List (RPL) is a table that relates generic segments to roadbed segments in the CSCL centerline.|
||SEDAT|The Split Election District Address Table (SEDAT) stores the address range data associated with segments split by Election Districts.|
||SEGMENT_LGC|The Segment_LGC table serves as the entry point for identifying the valid name(s) for a particular street segment. It stores the relationship between a centerline, rail, or shoreline segment and its 
||SPECIALDISASTER|A reserved placeholder for future data.|
||SPECIALINTERSECTIONS|The special intersection table store information relating to ambiguous intersections.|
||SPECIALSEDAT|The Special Split Election District Address Table (SEDAT) stores the address range data associated with segments split by Election Districts. The address information is associated with Special Address File records.|
||STREETNAME|The StreetName table stores street names. The street name is parsed into seven component parts according to National Emergency Number Association (NENA) standards.|
||STREETSHAVEINTERSECTIONS||
||STREETTYPE|The streettype table stores the various City agency values for street types (e.g. Avenue, Boulevard) and their abbreviations.|
||TRAFFICCALMINGDEVICE|A reserved placeholder for future data.|
||TRAVELRESTRICTION|A reserved placeholder for future data.|
||TRUCKROUTE|A reserved placeholder for future data.|
||TURNRESTRICTION|A reserved placeholder for future data.|
||TURNRESTRICTIONLIMITS|A reserved placeholder for future data.|
||UNIVERSALWORD||
||VIRTUALINTERSECTION||
||SUBADDRESS|A subaddress is a component of an address that further specifies a location within a larger building or complex. Subaddress records for New York City are added to the Citywide Street Centerline Geodatabase to support emergency response and post-emergency canvassing operations.|
||CDTAEquiv2020||
||NTAEquiv2020||
|**Relationship Class**|AccessPointToAddressPoint|This Attributed relationship class determines the relationship between Access Point and AddressPoint.|
||AccessPointsToEntrancePoints|Attributed|
||AddressPointHaveEntrancePoint||
||AddressPointsHaveLGCs||
||CenterlinesHaveAltSegmentData||
||CenterlinesHaveCommonPlaces||
||CenterlinesHaveRestrictions||
||CenterlinesHaveSegmentLGC||
||CenterlinesHaveTrafficCameras||
||CenterlinesHaveTransitEmergencyExits||
||CenterlinesHaveTravelRestrictions||
||CenterlinesToSEDAT||
||CenterlinesToStreetsHaveIntersections||
||CommonPlace_Streetname||
||CommonPlacesHaveAccessPoints|Attributed|
||CommonPlacesHaveAddressPoints|Attributed|
||CommonPlacesHaveFeatureNames|Attributed|
||ComplexIntersectionsHaveNodes||
||ComplexesHaveCommonPlaces||
||ComplexesHaveComplexAccessPoints||
||IntersectionsToBoundaries||
||NamedIntersectionsHaveStreetNames||
||NodesHaveNamedIntersections||
||NodesHaveSegments||
||NodesHaveSpecialIntersections||
||NodesHaveVirtualIntersections||
||NonStreetFeaturesHaveAltSegmentData
||NonStreetFeaturesHaveSegmentLGC||
||PostTypesHaveStreetTypes||
||PreTypesHaveStreetTypes||
||RailStationsHaveFeatureNames|Attributed|
||RailsHaveSegmentLGC||
||SegmentLGCsHaveFeatureNames||
||SegmentLGCsHaveStreetNames||
||ShorelinesHaveAltSegmentData||
||ShorelinesHaveSegmentLGC||
||SpecialSedatHaveCommonPlaces||
||SubwayStationsHaveFeatureNames|Attributed|
||SubwayStationsHaveStationEntrances||
||SubwayStationsHaveTransitBooths||
||SubwayStationsHaveTransitEmergencyExits||
||SubwaysHaveSegmentLGC||
||TurnRestrictionsHaveTurnRestrictionLimits||

<!--
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

-->







