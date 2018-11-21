# Classified Point Cloud
Geometry Type: Point (LAS 1.4)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Images/TopobathymetricClassifiedPointCloud.png)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The topobathymetric classified point cloud may be used for creating 3D building models, tree canopy models, or may be further classified. See [LiDAR and Derived Products](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Metadata/Metadata_LiDAR_Summary.md) for a summary of derived products created from this classified point cloud. 
**Description** |In May 2017, Quantum Spatial (QSI) was contracted by Applied Geographics to collect topographic and topobathymetric Light Detection and Ranging (LiDAR) data for the City of New York (NYC) in the spring and summer of 2017 for the New York City LiDAR project site in New York. QSI collected and processed traditional (near infrared wavelength) LiDAR over the topographic AOI, and spliced together NIR and bathymetric LiDAR (green wavelength) for the topobathymetric AOI. Topographic data was collected for the entire city, plus an additional 100 meter buffer, using a Leica ALS80 sensor equipped to capture at least 8 pulse/m2. Dates of capture for topographic data were between 05/03/2017 and 05/17/2017 during 50% leaf-off conditions. Bathymetric data was collected in select areas of the city (where bathymetric data capture was expected) using a Riegl VQ-880-G sensor equipped to capture approximately 15 pulses/m2 (1.5 Secchi depths). Dates of capture for bathymetric were between 07/04/2017 - 07/26/2017. LiDAR data was tidally-coordinated and captured between mean lower low water (+30% of mean tide) ranges. 
**Source(s)** |City of New York, Quantum Spatial Inc.
**Publication Dates** |**Data**: <br>**Last Update**: 10/2018<br>**Metadata**: 11/20/2018<br>**Update Frequency**: As needed
**Available Formats** |LAS 1.4
**Use Limitations** |
**Access Rights** |Public
**Links** |Coming Soon
**Tags** |classified point cloud, lidar
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |Data was collected with QL1 specifications (8 pulses/m2). Actual first return densities for this dataset are: <br>
Topographic (NIR): 10.75 pts/m2<br>
Bathymetric (Green): 15.24 pts/m2
**Spatial Coverage** |New York City, plus an additional 100 m buffer around the city
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017 
Bathymetric: 07/04/2017 - 07/26/2017
**Positional Accuracy** |**Topographic**<br>Non-Vegetated Vertical Accuracy (95% confidence level): 0.242 ft (0.074 m)<br>Vegetated Vertical Accuracy (95th percentile): 0.517 ft (0.158 m)<br>Relative Vertical Accuracy: 0.085 ft (0.026 m)<br><br>**Bathymetric**<br>Non-Vegetated Vertical Accuracy (95% confidence level): 0.208 ft (0.064 m)

**Features Captured** |The topobathymetric point cloud was classified as follows: <br><br>
 1 - Default/Unclassified<br>
 1 WO - Default/Unclassified Withheld Overlap<br>
 2 - Ground<br>
 7 W - Noise Withheld<br>
 9 - Water<br>
 10 - Ignored Ground (Water's Edge)<br>
 17 - Bridge<br>
 25 - Subway Stairs<br>
 40 - Bathymetric Bottom<br>
 41 - Water Surface<br>
 45 - Water Column
**Features Excluded** |
**Capture and Update Notes** |For more information on data acquisition, processing, and accuracy assessments of the 2017 LiDAR data, see the [Topobathymetric LiDAR Technical Data Report](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Supplemental/New_York_City_2017_Topobathymetric_LiDAR_Report.pdf)
## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
