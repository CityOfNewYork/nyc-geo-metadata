# Highest Hit Digital Surface Model
Geometry Type: Raster (TIF)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/HighestHitModel.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The highest hit digital surface model may be used for a variety of analyses such as line of sight, shadow analysis, and creation of 3D building models. This model was used to help identify tree canopy and buildings in the 2017 Land Cover dataset. 
**Description** |The highest hit digital surface model (DSM) represents the earth's surface elevation with all natural and anthropogenic features included. It was derived from Green and NIR LiDAR data using the highest hit method. Green LiDAR was used within the water's edge breakline shape (provided as another deliverable) and NIR LiDAR was used everywhere outside of the water's edge breakline. Some elevation values have been interpolated across areas in the ground model where there is no elevation data (e.g. over water). 
**Source(s)** |City of New York, Quantum Spatial Inc. 
**Publication Dates** |**Data**: 2017<br>**Last Update**: 2018<br>**Metadata**: 09/12/2018<br>**Update Frequency**: As needed. This dataset was created as part of the 2017 LiDAR update
**Available Formats** |Topographic Mosaic
Topographic Tiled
Bathymetric Mosaic
Bathymetric Tiled
Topobathymetric Mosaic
Topobathymetric Tiled
**Use Limitations** |
**Access Rights** |Public
**Links** |Coming Soon
**Tags** |LiDAR, Light detection and ranging, highest hit, digital surface model, DSM, vegetation, anthropogenic structures, New York City, New York, NYC, Manhattan, Brooklyn, Queens, The Bronx, Staten Island
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |1 foot
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017 
Bathymetric: 07/04/2017 - 07/26/2017
**Positional Accuracy** |
**Features Captured** |
**Features Excluded** |
**Capture and Update Notes** |Elevation values for open water surfaces with no returns are derived from waters edge breaklines used in hydro-flattening the bare earth model. Triangles were created across water surfaces by interpolating from the nearest breakline elevation points.
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
