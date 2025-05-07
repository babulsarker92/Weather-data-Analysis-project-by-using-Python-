
# Weather Trends Analysis and Visualization

This project analyzes hourly weather data from a CSV file to uncover patterns and trends in temperature, humidity, wind speed, visibility, and weather conditions over a year.

## 📁 Project Structure

```
weather-trends-analysis/
│
├── data/
│   └── file.csv                # Original dataset
│
├── notebooks/
│   └── weather_analysis_notebook.ipynb  # Jupyter notebook with code and visualizations
│
├── images/
│   └── *.png                   # Saved plots and visualizations
│
├── reports/
│   └── summary_report.pdf      # Final report (optional)
│
├── README.md                   # Project overview and documentation
└── requirements.txt            # Python packages used
```

## 🎯 Objectives

- Clean and preprocess hourly weather data.
- Explore trends in temperature, humidity, and weather conditions.
- Visualize seasonal and monthly variations.
- Identify patterns linked to low visibility or extreme weather.
- Provide summary insights and visualizations.

## 🛠️ Tools and Technologies

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## 📊 Key Analyses

- Line plots of temperature trends over time.
- Bar charts of monthly average temperatures.
- Heatmaps showing correlations between weather variables.
- Weather condition frequency analysis.

## 🧹 Data Cleaning & Preprocessing

- Converted `Date/Time` to datetime format.
- Renamed columns for clarity.
- Added derived features like `Month`, `Hour`, and `DayOfWeek`.

## 🔍 Data Insights

- Clear seasonal variation in temperature trends.
- Higher relative humidity associated with lower temperatures.
- Fog and freezing drizzle are common causes of reduced visibility.

## 📈 Visualizations

All key trends are visualized using line plots, histograms, and heatmaps. These help to quickly interpret the underlying data patterns.

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 📌 Usage

Run the Jupyter Notebook in the `notebooks/` folder to reproduce the analysis:

```bash
jupyter notebook notebooks/weather_analysis_notebook.ipynb
```

## 📝 Conclusion

This project demonstrates how historical weather data can provide meaningful insights through data analysis and visualization. The outcomes can be useful for planning, forecasting, and climate research.

