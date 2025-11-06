from src.initialization import data
print("starting generation for 1200 datapoints:")
data.init_data(
    dataset_dir="data/",
    dataset_path="halfhourly_dataset/",
    file_pattern="block_{0}.csv",
    start_index=0,
    end_index=1,
    formatted_csv="formatted_data_1200.csv",
    weather_dataset_path="weather_hourly_darksky.csv",
    force_rebuild_data=True,
    data_cols=["LCLid", "tstp", "energy(kWh/hh)"],
    data_cols_out=["LCLid", "datetime", "energy(kWh/hh)"],
        weather_data=["temperature"],
    weather_time_col="time",
    data_points = 1200

)
print("finished generation for 1200 datapoints:")
print("starting generation for 600 datapoints:")
data.init_data(
    dataset_dir="data/",
    dataset_path="halfhourly_dataset/",
    file_pattern="block_{0}.csv",
    start_index=0,
    end_index=1,
    formatted_csv="formatted_data_600.csv",
    weather_dataset_path="weather_hourly_darksky.csv",
    force_rebuild_data=True,
    data_cols=["LCLid", "tstp", "energy(kWh/hh)"],
    data_cols_out=["LCLid", "datetime", "energy(kWh/hh)"],
        weather_data=["temperature"],
    weather_time_col="time",
    data_points = 600

)
print("finished generation for 600 datapoints:")
print("starting generation for 100 datapoints:")
data.init_data(
    dataset_dir="data/",
    dataset_path="halfhourly_dataset/",
    file_pattern="block_{0}.csv",
    start_index=0,
    end_index=1,
    formatted_csv="formatted_data_100.csv",
    weather_dataset_path="weather_hourly_darksky.csv",
    force_rebuild_data=True,
    data_cols=["LCLid", "tstp", "energy(kWh/hh)"],
    data_cols_out=["LCLid", "datetime", "energy(kWh/hh)"],
        weather_data=["temperature"],
    weather_time_col="time",
    data_points = 100

)
print("finished generation for 100 datapoints:")
