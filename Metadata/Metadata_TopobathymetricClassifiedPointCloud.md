# Topobathymetric Classified Point Cloud
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
**Links** | Coming Soon
**Tags** |classified point cloud, lidar
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |Data was collected with QL1 specifications (8 pulses/m2). Actual first return densities for this dataset are: <br>Topographic (NIR): 10.75 pts/m2<br>Bathymetric (Green): 15.24 pts/m2
**Spatial Coverage** |New York City, plus an additional 100 m buffer around the city
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017<br>Bathymetric: 07/04/2017 - 07/26/2017
**Positional Accuracy** |**Topographic**<br>Non-Vegetated Vertical Accuracy (95% confidence level): 0.242 ft (0.074 m)<br>Vegetated Vertical Accuracy (95th percentile): 0.517 ft (0.158 m)<br>Relative Vertical Accuracy: 0.085 ft (0.026 m)<br><br>**Bathymetric**<br>Non-Vegetated Vertical Accuracy (95% confidence level): 0.208 ft (0.064 m)
**Features Captured** |The topobathymetric point cloud was classified as follows: <br><br>1 - Default/Unclassified<br> 1 WO - Default/Unclassified Withheld Overlap<br> 2 - Ground<br> 7 W - Noise Withheld<br> 9 - Water<br> 10 - Ignored Ground (Water's Edge)<br> 17 - Bridge<br> 25 - Subway Stairs<br> 40 - Bathymetric Bottom<br> 41 - Water Surface<br> 45 - Water Column
**Capture and Update Notes** |For more information on data acquisition, processing, and accuracy assessments of the 2017 LiDAR data, see the [Topobathymetric LiDAR Technical Data Report](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/master/Supplemental/New_York_City_2017_Topobathymetric_LiDAR_Report.pdf)
## 3. Attribute Information
---------------------------------------------

| Attribute | Description |
|------------ | ------------- |
| X | The X, Y, and Z values are used in conjunction with the scale values and the offset values to determine the coordinate for each point. Units are based on the coordinate reference system (US ft).  |  | 
| Y | The X, Y, and Z values are used in conjunction with the scale values and the offset values to determine the coordinate for each point. Units are based on the coordinate reference system (US ft).  |  | 
| Z | The X, Y, and Z values are used in conjunction with the scale values and the offset values to determine the coordinate for each point. Units are based on the coordinate reference system (US ft).  |  | 
| Intensity | The intensity value is the integer representation of the pulse return magnitude. |  | 
| Return Number | The Return Number is the pulse return number for a given output pulse. A given output laser pulse can have many returns, and they must be marked in sequence of return. The first return will have a Return Number of one, the second a Return Number of two, and so on up to fifteen returns. The Return Number must be between 1 and the Number of Returns, inclusive. |  | 
| Number of Returns | The Number of Returns is the total number of returns for a given pulse. For example, a laser data point may be return two (Return Number) within a total number of up to fifteen returns. |  | 
| Classification Flag | Classification flags are used to indicate special characteristics associated with the point. <br>Withheld - This point is should no be included in processing <br>Overlap - The point is within the overlap region of 2 or more swaths.  |  | 
| Scanner Channel | Scanner Channel is used to indicate the channel (scanner head) of a multichannel system. Channel 0 is used for single scanner systems.  |  | 
| Scan Direction Flag | The Scan Direction Flag denotes the direction at which the scanner mirror was traveling at the time of the output pulse. |  | 
| Edge of Flight Line | The Edge of Flight Line data bit has a value of 1 only when the point is at the end of a scan. |  | 
| Classification | This field represents the "class" attributes of a point.<br>1  - Default / Unclassified<br>2  - Ground<br>9 - Water<br>10 - Ignored Ground<br>17 - Bridge Decks<br>25 - Subway/Transit stairwells<br>40 - Bathymetric Bottom<br>41 - Green Near Water Surface<br>45 - Water Column |  | 
| Scan Angle | The Scan Angle represents the rotational position of the emitted laser pulse with respect to the vertical of the coordinate system of the data |  | 
| Scan Angle Rank | The Scan Angle Rank is the angle (rounded to the nearest integer in the absolute value sense) at which the laser point was output from the laser system including the roll of the aircraft.  The scan angle is within 1 degree of accuracy from +90 to -90 degrees. The scan angle is an angle based on 0 degrees being nadir, and -90 degrees to the left side of the aircraft in the direction of flight. |  | 
| Point Source ID | This value indicates the file from which this point originated. |  | 
| GPS Time | The GPS Time is the double floating point time tag value at which the point was acquired. |  | 
