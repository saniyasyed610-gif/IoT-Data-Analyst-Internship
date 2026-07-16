# Week 9 – Time-Series Analysis and Forecasting

## Overview

This project focuses on performing **Time-Series Analysis and Forecasting** on an IoT sensor dataset. The analysis includes data preprocessing, moving average calculation, trend analysis, and forecasting future temperature values using a Linear Regression model. The project demonstrates how historical sensor data can be analyzed to identify patterns and predict future trends.

---

## Objective

- Perform time-series analysis on IoT sensor data.
- Preprocess and prepare the dataset for analysis.
- Calculate and visualize the 7-day moving average.
- Analyze long-term temperature trends.
- Build a Linear Regression model for temperature forecasting.
- Visualize actual and predicted temperature values.

---

## Dataset

**Dataset Name:** Better_Dataset.csv

### Features

- Date
- Temperature
- Humidity
- Verdict

**Total Records:** 2311

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

---

## Methodology

1. Loaded the IoT sensor dataset.
2. Converted the Date column to datetime format.
3. Set the Date column as the dataset index.
4. Calculated the 7-day moving average.
5. Performed temperature trend analysis.
6. Built a Linear Regression forecasting model.
7. Visualized actual and predicted temperature values.

---

## Results and Visualizations

The following visualizations were generated:

- Temperature with 7-Day Moving Average
- Temperature Trend Over Time
- Temperature Forecast using Linear Regression

---

## Forecasting Model

**Algorithm Used:**
- Linear Regression

The model was trained using historical temperature data to predict future temperature trends and demonstrate basic time-series forecasting.

---

## Outcome

The project successfully demonstrated the application of time-series analysis techniques to IoT sensor data. Moving average analysis highlighted long-term trends, trend analysis revealed seasonal variations, and Linear Regression provided a simple forecasting model for predicting future temperature values.

---

## Files Included

- Better_Dataset.csv
- Week9_TimeSeries_Analysis.ipynb
- Week9_TimeSeries_Report.docx
- Week9_TimeSeries_Report.pdf
- README.md

---

## Conclusion

Time-series analysis is an effective approach for analyzing historical IoT sensor data and forecasting future observations. The techniques implemented in this project provide valuable insights into temperature patterns and demonstrate how predictive analytics can support intelligent IoT monitoring systems.
