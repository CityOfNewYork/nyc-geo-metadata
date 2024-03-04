# Shoreline
Geometry Type: Shapefile (Polyline Z)<br><br>![image](https://github.com/CityOfNewYork/nyc-geo-metadata/blob/main/Images/TidalShoreline.PNG)

### Table of Contents<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**1. Identification**](#1-identification)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**2. Data Quality and Specifications**](#2-data-quality-and-specifications)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**3. Attribute Information**](#3-attribute-information)<br><br>
## 1. Identification
---------------------------------------------
|     |     |
| --- | --- |
**Purpose** |The 2017 shoreline dataset may be used with supplemental tidally coordinated shoreline datasets to assess shoreline change in New York City. 
**Description** |A dataset representing the shorelines of tidally influenced areas of New York City. This dataset derived from the 2017 Light Detection and Ranging (LiDAR) data capture. In most areas LiDAR was captured during low tide (defined here as a range between Mean Lower Low Water (MLLW) and MLLW + 30% of the mean tide range). All bathymetric LiDAR and most near-infrared (NIR) LiDAR was captured during low tide. Flights flown over NIR LiDAR shoreline areas that are largely made up of sea walls and riprap were not flown during low tide. See dataset attributes for which areas are tidally-coordinated. Tidal gauges used to determine low tide: Kings Point, Bergen West, Sandy Hook, and The Battery.
**Source(s)** |City of New York, Quantum Spatial Inc.
**Publication Dates** |**Data**: 10/2018<br>**Last Update**: 10/2018<br>**Metadata**: 11/20/2018<br>**Update Frequency**: As needed
**Available Formats** |Shapefile
**Use Limitations** |Not all areas of the city were captured during low tide. Areas such as along the Hudson and East Rivers that are lined with seawwalls and riprap were not captured at low tide. The attribute "Type" provides details on how each segment of the shoreline was captured. Because not areas of the shoreline were captured at the same tidal levels, the shoreline is not continous. 
**Access Rights** |Public
**Links** |[Tidally Coordinated Shoreline](https://data.cityofnewyork.us/Environment/Tidally-Coordinated-Shoreline/pawq-tjb4)
**Tags** |shoreline, water's edge, new york city, tidal coordination
## 2. Data Quality and Specifications
---------------------------------------------
|     |     |
| --- | --- |
**Horizontal Coordinate System** |New York State Plane Coordinates, Long Island East Zone, NAD83, US foot
**Resolution** |
**Spatial Coverage** |New York City, NY
**Temporal Coverage** |Topographic: 05/03/2017 - 05/17/2017<br>Bathymetric: 07/04/2017 - 07/26/2017
**Features Excluded** |Flights flown over NIR LiDAR shoreline areas that are largely made up of sea walls and riprap were not flown during low tide.

## 3. Attribute Information
---------------------------------------------
| Attribute | Description | Field Type | Sensitive Field (Y/N) | Notes| 
|------------ | ------------- | -------- | ----------- | ----------|
| SOURCE_ID | Unique Feature Identification Number. | double | No
| FEATURE_CODE | Type of feature.<br>3900 = Shoreline | integer | No
| SUB_FEATURE_CODE | A subset of features within a given Feature_Code set:<br>390000 = Shoreline | integer | No
| STATUS | Field indicating the feature status as it fits into one of the following categories:<br>NEW = A feature captured for the first time during the 2014 planimetrics update project.<br>UPDATED = The feature existed previously but has been updated during the 2014 planimetrics update project.<br>UNCHANGED = The feature is unchanged from the source planimetrics database. | text | No
| FID | Internal feature number. | Internal Feature Number | 
| Feature | Feature description (Shoreline) | String | 
| Type | Description field on how the shoreline was created. Bathymetric -low tide means the data was captured using the bathymetric (green) LiDAR data. NIR - low tide means the data was captured using the topographic (NIR) LiDAR data. NIR - not tidally coordinated means the data was captured with topographic LiDAR data but was not necessarily captured at low tide.  | String | 
