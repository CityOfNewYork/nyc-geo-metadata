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
||ESINETAtomicLine|This polyline feature class used for the creation of Provisioning, PSAP, and Emergency Service Boundaries in a downstream process. Source is CSCL.Borough and CSCL.CityLimit. In some cases some line are drawn ad-hoc.|
||NonStreetFeature|NonStreetFeature is a single-line representation of non-street features. The subtypes of NonStreetFeature include:1) Census_block 2) District_Boundary 3) Election_District 4) Other 5) Physical_Non_ST_Feature 6) Pier_Outline 7) School_District.|
||Rail|Rail is a single line representation of New York City railroads containing route and other information.|
||Shoreline|Shoreline is a single line representation of New York City shorelines.|
||Subway|Subway is a single line representation of the New York City subway system.|
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

