# Open Space
Filename: OPEN_SPACE_NO_PARK<br>Geometry Type: polygon<br><br>![image](https://github.com/CityOfNewYork/nyc-planimetrics/raw/master/Images/FeatureViews/Cemetery.JPG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |This feature class is part of the planimetrics database used by the NYC DOITT GIS group to maintain and distribute an accurate 'basemap' for NYC. The basemap provides the foundation upon virtually all other geospatial data with New York. Digital planimetrics are derived using the imagery products delivered with the 2014 New York Statewide Flyover (see Summary for specific flight dates), which includes raw imagery collected to support the generation of 0.5 Ft Ground Sample Distance (GSD) natural color imagery. 
**Description** |This feature class contains various open areas (with no or few buildings), including:<br>CEMETERY OUTLINE = Boundary of cemetery.<br>RECREATIONAL AREA = areas used for picnic or other recreational use, NOT including NYC designated parks. Recreational areas must contain at least one of the following: Benches, Swings, Play area.<br>VACANT AREA = intended to be a vacant lot where a building could potentially be built and is associated with a tax lot polygon boundary.
**Source(s)** |Current imagery and previous planimetric database
**Publication Dates** |**Data**: 06/17/14<br>**Last Update**: 08/27/16<br>**Metadata**: 12/02/16<br>**Update Frequency**: 
**Available Formats** |File Geodatabase Feature Class as part of the Planimetrics geodatabase and individual shapefile on the [NYC Open Data Portal](https://data.cityofnewyork.us/Recreation/Open-Space-Parks-/g84h-jbjm)
**Use Limitations** |While all possible measures have been taken to ensure the accuracy of this data, the City of New York assumes no responsibility for the accuracy of the data for their purposes.
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Phone**: 718-403-8394<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/Recreation/Open-Space-Parks-/g84h-jbjm
**Tags** |structure, NYCMap, imageryBaseMapsEarthCover, Open Space, transportation, Landbase, Basemap, Cemetery, Planimetric
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |NA
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |For this dataset, the source imagery was captured on the following dates:<br>Manhattan - June 24, 2014<br>The Bronx, Brooklyn, Queens and Staten Island  - April 1st through April 25th, 2014<br>Final delivery of all imagery - April 10, 2015<br>Using this orthoimagery, the planimetric base layers were updated citywide starting in March 2015 and were completed in February 2016.
**Positional Accuracy** |The following features were captured for each subtype: <br>Cemetry Outline: Updated cemetery boundaries from new imagery.<br>Recreational Areas: Outline of recreational areas which may be used for picnic or other recreational activities. Recreational areas must contain at least one of the following:<br>a) Benches<br>b) Swings<br>c) Play area<br><br>Hardscape recreational areas were collected differently than softscape recreational areas, as follows:<br>Hardscape recreational areas have either hard surfaces or sand. These areas were captured as discrete polygons following the edges of these areas precisely.<br> Softscape recreational areas are grassy areas for football/baseball/other. These areas were captured as a single polygon (i.e., not discrete polygons) and snapped to other features (e.g. sidewalks, roadbed, hydro, etc.) where applicable.<br>When hardscapes and softscapes exists adjacent to one another, the entire area was captured by a single polygon.<br>Vacant Area: These features represent a vacant lot where a building could potentially be built and is associated with a tax lot polygon.
**Features Captured** |The following features were excluded from each subtype: <br>Recreational Area: Medians with either benches, swings, or play areas were captured as a median and not a recreational area.
**Features Excluded** |
**Capture and Update Notes** |The following capture notes for each subtype captured:<br>Cemetery Outline: Individual headstones, graves, or interior boundaries were not partitioned.<br>Recreational Area: These features are entirely outside of NYC designated parks.<br>Vacant Area: "Vacant" is defined herein as an area containing no structures.<br>The Digital Tax Map (DTM) and currently captured planimetrics (Building Footprints) were used to determine the location of the vacant areas.<br>The actual shape of each vacant aras was captured using physical features that typically form the boundary of a property such as fences, hedgerow, etc.<br>Vacant Areas extend to sidewalk or roadbed edge.<br>As a general rule of thumb, vacant lots were required to have roadway frontage, and not actively used for private or public entities (e.g., backyard or commmunity garden).
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Identification Number | double | No
| FEATURE_CODE | Type of feature. <br>2500 = Cemetery Outline<br>2510 = Recreational area (Not NYC designated parks)<br>2520 = Vacant Area containing no structures
 | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set. <br>250000 = Cemetery Outline <br>251000 = Recreational area (Not NYC designated parks) <br>252000 = Vacant Area containing no structures | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| NAME | Name of open space | text | No
