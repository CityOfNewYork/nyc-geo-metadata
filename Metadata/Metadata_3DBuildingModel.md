# 3-D Building Model
Geometry Type: Various. Depends on format. <br><br>![image](http://www1.nyc.gov/assets/doitt/images/content/pages/3d-buildings.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** | 3-D Building Models were developed to supplement the most recent [planimetric](https://github.com/ekamptner/nyc-planimetrics/blob/master/Capture_Rules.md) update. Examples of 3-D Building Model usage include: <br> [CESIUM (Open Source 3D rendering library)](https://cesiumjs.org/NewYork/index.html?view=-74.01881302800248%2C40.69114333714821%2C753.2406554180401%2C21.27879878293835%2C-21.343905508724625%2C0.0716951918898415)<br> [NY Times Shadow Study](http://www.nytimes.com/interactive/2016/12/21/upshot/Mapping-the-Shadows-of-New-York-City.html)
**Description** |3-D Building Models representing every NYC building present in the 2014 aerial survey. 
**Source(s)** |Department of Information Technology & Telecommunications (DOITT)
**Publication Dates** |**Data**: 04/18/2016<br>**Last Update**: 04/18/2016<br>**Metadata**: 12/28/2016<br>**Update Frequency**: The 3-D model was a one-time capture. Updates and extensions may be considered in the future. 
**Available Formats** |3-D Model data is available in the following formats: <br> [CityGML](http://maps.nyc.gov/download/3dmodel/DA_WISE_GML.zip)<br>[Multipatch (ESRI)](http://maps.nyc.gov/download/3dmodel/DA_WISE_Multipatch.zip)<br>[DGN (Microstation)](http://maps.nyc.gov/download/3dmodel/DA_Wise_DGN.zip)
**Use Limitations** |Open Data policies and restrictions apply. See [Terms of Use](http://www.nyc.gov/html/data/terms.html)
**Access Rights** |Public
**Contact Information** |**Name**: Colin Reilly, Director GIS Division, Department of Information Technology and Telecommunication (DOITT)<br>**Email**: creilly@doitt.nyc.gov
**Links** |https://data.cityofnewyork.us/City-Government/3-D-Building-Model/tnru-abg2
**Tags** |doitt, gis, 3d, buildings, model
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** | 1'=100''
**Spatial Coverage** |New York City, NY
**Temporal Coverage** | Data is based on 2014 aerial imagery. The source imagery for this dataset was captured on the following dates:<br> Manhattan - June 24, 2014<br> The Bronx, Brooklyn, Queens, Staten Island - April 1, 2014 - April 25, 2014<br>Final delivery of all imagery - April 10, 2015
**Positional Accuracy** |The Horizontal Accuracy (XY) of all planimetric feature classes captured is such that 95% of features are within (plus/minus) 1.25 ft of the actual horizontal location.	The Vertical Accuracy (Z) of all planimetric feature classes with elevation values is such that 95% of features captured are within (plus/minus) 1.6 ft of the actual elevation.
**Features Captured** |All major roof structures are modeled, including pitched roofs. 
**Features Excluded** |Domes and rounded roofs are not modeled. All roof appendages, such as chimneys, parapets, spindles, and antenna are also not included. 
**Capture and Update Notes** | The data was compiled by stereo compilation. Using the Open Geospatial Consortium's [CityGML](http://www.opengeospatial.org/standards/citygml) specification as the basis, the NYC 3-D Building Massing Model was developed to a hybrid specification combining elements from Level of Detail (LOD) 1 and 2. Approximately 100 iconic buildings provided herein were created in LOD 2 (per OGC specifications). Highlights of the model include the differentiation of building components including roof, facades and ground plane. <br><br> The model was a one-time capture. If the model is useful, future updates and extensions will be considered. 
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| BIN | Building identification number. Assigned by City Planning | numeric | No
| DOITT_ID | Unique identifier assigned by DOITT.  | numeric | No
| SOURCE_ID | Unique Feature Identification Number. | numeric | No
