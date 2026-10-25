from pathlib import Path
import re

Citibike_path = Path(r"C:\Users\renan\Downloads\Citibike_Dataset_12M")
divi_path = Path(r"C:\Users\renan\Downloads\Divvy_Dataset_12M")

inventory  = []
# Iterate through all CSV files in the Divvy dataset using glob as we have another inner folder outside our data file
# for item in divi_path.glob("*/*.csv"): 
#     # print(item.name)
#     # print(item.stem)
#     # print(item.suffix)  
#     file_name = item.name
#     trip_single_quarter = re.fullmatch(r"Divvy_Trips_(\d{4})_Q(\d)\.csv$", file_name)  # Regular expression to match the year and quarter in the file name
#     station_single_quarter = re.fullmatch(r"Divvy_Stations_(\d{4})_Q(\d)\.csv$", file_name)  # Regular expression to match the year and quarter in the file name
#     station_double_quarter = re.fullmatch(r"Divvy_Stations_(\d{4})_Q(\d)Q(\d)\.csv$", file_name)  # Regular expression to match the year and month in the file name
#     monthly_file = re.fullmatch(r"(\d{6})-divvy-tripdata\.csv$", file_name)

#     if trip_single_quarter or station_single_quarter:
#         year = trip_single_quarter.group(1) if trip_single_quarter else station_single_quarter.group(1)
#         quarter = trip_single_quarter.group(2) if trip_single_quarter else station_single_quarter.group(2)
#         if quarter.isdigit() and 1 <= int(quarter) <= 4:  # Check if the quarter is a valid number between 1 and 4
#             print(f"{year}-Q{quarter}")
#         else :
#             print(f"Needs review: {file_name}")
#     elif station_double_quarter:
#         year = station_double_quarter.group(1)
#         quarter1 = station_double_quarter.group(2)
#         quarter2 = station_double_quarter.group(3)
#         if quarter1.isdigit() and quarter2.isdigit() and 1 <= int(quarter1) <= 4 and 1 <= int(quarter2) <= 4:  # Check if both quarters are valid numbers between 1 and 4
#             if quarter1 < quarter2:
#                 print(f"{year}-Q{quarter1}Q{quarter2}")
#             else:
#                 print(f"Quaters are in wrong order: {file_name}")
#         else:
#             print(f"Needs review: {file_name}")
#     elif monthly_file : 
#         year = file_name[0:4]  # Extract the first four characters of the file name
#         month = file_name[4:6]  # Extract the next two characters of the file name
#         if month.isdigit() and 1 <= int(month) <= 12:  # Check if the month is a valid number between 1 and 12
#             print(f"{year}-{month}")
#         else:
#             print(f"Month and Year are invalid: {file_name}")
#     else:
#         print(f"Needs review: {file_name}")

for item in Citibike_path.rglob("*.csv"): 
    # print(item.name)
    # print(item.stem)
    # print(item.suffix)  
    file_name = item.name
    monthly_file_1 = re.fullmatch(r"(\d{6})-citibike-tripdata_(\d{1})\.csv$", file_name)
    monthly_file_2 = re.fullmatch(r"(\d{6})-citibike-tripdata.csv_(\d{1})\.csv$", file_name)
    monthly_file_3 = re.fullmatch(r"(\d{6})-citibike-tripdata\.csv$", file_name)
    monthly_file_4 = re.fullmatch(r"(\d{6})-citibike-tripdata-part(\d{1})\.csv$", file_name)
    files = []

    if monthly_file_1 or monthly_file_2 or monthly_file_3 or monthly_file_4:
        year = file_name[0:4]
        month = file_name[4:6]
        part = None
        if monthly_file_1:
            part = monthly_file_1.group(2)
        elif monthly_file_2:
            part = monthly_file_2.group(2)
        elif monthly_file_4:
            part = monthly_file_4.group(2)
        else:
            part = ""
        if part != "":
            source_period = f"{year}-{month}"
            files.append(file_name)
            
        else:
            source_period = f"{year}-{month}_{part}"
        if not inventory:
            inventory.append({
                            "source" : "CitiBike",
                            "file_name" : file_name,
                            "source_period" : source_period,
                            "status":"valid"
                        })
        elif not any(record["source_period"] == source_period for record in inventory):
            inventory.append({
                "source" : "CitiBike",
                "file_name" : file_name,
                "source_period" : source_period,
                "status":"valid"
            })
        else:
            print(f"Record already present for {source_period}")
    else:
        print(f"Needs review {file_name}")
    # if source_period not in file_record.values():
            
    # else:
    #     print(f"source oeriod already present{source_period}")
# 477

print(inventory)
# Iterate through all CSV files in the Citibike dataset
# for item in Citibike_path.rglob("*.csv"):
#     print(item.name)
#     print(item.stem)
#     print(item.suffix)

# print(folder.exists()) -- To check whether a Folder exists

# for folder1 in main_folder.iterdir():  -- To iterate through the subfolders of a main folder
#    for folder2 in folder1.iterdir():
#     for item in folder2.iterdir():
#         if item.glob("*.csv"):
#             print(item)

# print(list(folder.iterdir()))       -- To list all the subfolders of a main folder

# for item in Citibike_path.rglob("*.csv"):   --- To iterate through all the subfolders of a main folder and list all the files with a specific extension
#     print(item)
