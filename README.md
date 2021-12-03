# King County House Sales Report and Dashboard using Power BI 

This is a project for the Microsoft MBKM program. In this project, a desktop-based report and dashboard was created using the Power BI desktop and Power BI service.

Original source of dataset : [GeoDa Data and Lab](https://geodacenter.github.io/data-and-lab/KingCounty-HouseSales2015/)

## Features

- 4 Page of Report Overview, City Performance, House Detail, Predict Price
- Predict house price interactively via power BI report

## Installation

This report need power BI dekstop and some python library to run.

- Install power BI dekstop [Download Power BI](https://powerbi.microsoft.com/en-us/downloads/)
- Install required python libraries
```sh
pip install pandas numpy request matplotlib
```
- Use azure autoML to build the machine learning model with maribisnistrain.csv dataset
- Deploy as a web service
- Change the Rest endpoint and key in power BI python script
