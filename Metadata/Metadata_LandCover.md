# Land Cover
Geometry Type: Raster<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/LandCover.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The land cover dataset may be used to assess land cover types throughout the city or by specific geographies. 
**Description** |High resolution land cover dataset for New York City. Eight land cover classes were mapped: (1) Tree Canopy, (2) Grass\Shrubs, (3) Bare Soil, (4) Water, (5) Buildings, (6) Roads, (7) Other Impervious, and (8) Railroads. The primary sources used to derive this land cover layer were 2017 LiDAR (1-ft post spacing) and 2016 4-band orthoimagery (0.5-ft resolution). Ancillary data sources included GIS data (e.g., city boundary, building footprints, water, parking lots, roads, railroads, railroad structures, athletic facilities) provided by New York City. The tree canopy and buildings classes were considered current as of 2017; the remaining land-cover classes were considered current as of 2016. Object-based image analysis techniques (OBIA) were employed to extract land cover information using the best available remotely sensed and vector GIS datasets. OBIA systems work by grouping pixels into meaningful objects based on their spectral and spatial properties, while taking into account boundaries imposed by existing vector datasets. Within the OBIA environment. a rule-based expert system was designed to effectively mimic the process of manual image analysis by incorporating the elements of image interpretation (color/tone, texture, pattern, location, size, and shape) into the classification process. A series of morphological procedures were used to ensure that the end product was both accurate and cartographically pleasing. The dataset was also manually reviewed and corrected to eliminate non-systematic errors that would not be addressed by additional model refinement. Overall accuracy was 98%.Note that a 7-class map was produced for the year 2010 using similar mapping protocols. In this earlier map, roads and railroads were combined into a single class (6). For comparisons between 2010 and 2017, the Railroads class (8) in the 2017 map can be reassigned to the Roads class (6). 
**Source(s)** |University of Vermont Spatial Analysis Laboratory, in collaboration with New York City Department of Information Technology and Telecommunications (NYC DoITT), Applied Geographics (AppGeo), and Quantum Spatial
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed. This dataset was created as part of the 2017 LiDAR update
**Available Formats** |Raster
**Use Limitations** |
**Access Rights** |Public
**Links** |Coming Soon
**Tags** |Urban, New York, 2017, 2016, land cover, tree canopy, New York City, UTC
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |6 inch
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |05/03/2017 - 05/17/2017 
**Positional Accuracy** |This land-cover dataset was subjected to a thorough manual quality control (QC) that focused on correction of non-systematic errors that could not addressed by additional model refinement. A per-pixel accuracy assessment based on 8,493 random points indicated an overall accuracy of 98%.  User's and producer's accuracies for all classes except Bare Soil exceeded 94%; for bare soil, the user's and producer's accuracies were 89 and 82%, respectively.
**Features Captured** |Object based image analysis was used to automate land-cover features using LiDAR point clouds and derivatives, orthoimagery, and vector GIS datasets -- City Boundary (2017, NYC DoITT); Buildings (2017, NYC DoITT); Hydrography (2014, NYC DoITT); LiDAR Hydro Breaklines (2017, NYC DoITT); Transportation Structures (2014, NYC DoITT); Roadbed (2014, NYC DoITT); Road Centerlines (2014, NYC DoITT); Railroads (2014, NYC DoITT); Green Roofs (date unknown, NYC Parks); Parking Lots (2014, NYC DoITT); Parks (2016, NYC Parks), Sidewalks (2014, NYC DoITT), Synthetic Turf (2018, NYC Parks); Wetlands (2014, NYC Parks); Shoreline (2014, NYC DoITT), Plazas (2014, NYC DoITT), Utility Poles (2014, ConEdison via NYCEM); Athletic Facilities (2017, NYC Parks). <br><br> For the purposes of classification, only vegetation < 8 ft were classed as Tree Canopy. Vegetation below 8 ft was classed as Grass/Shrub. 

