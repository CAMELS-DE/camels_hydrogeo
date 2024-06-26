import os
from datetime import datetime as dt

import geopandas as gpd

from json2args import get_parameter
from json2args.data import get_data_paths

from extract_functions import extract_hydrogeology_attributes_huek


# parse parameters
parameter = get_parameter()
id_field_name = parameter["id_field_name"]

# get data paths
data_paths = get_data_paths()

# read data
huek = gpd.read_file(data_paths["huek"])
catchments = gpd.read_file(data_paths["catchments"])

# check if a toolname was set in env
toolname = os.environ.get("TOOL_RUN", "").lower()

# if no toolname was set, raise an error
if toolname == "":
    raise ValueError("No toolname was set in the environment variable TOOL_RUN")

# if the toolname is valid, run the corresponding tool
elif toolname == "hydrogeology_attributes_huek":
    # extract hydrogeology attributes
    hydrogeology_attributes = extract_hydrogeology_attributes_huek(huek, catchments, id_field_name)

    # write the results to csv file
    hydrogeology_attributes.to_csv("/out/hydrogeology_attributes.csv")

    # set user permissions for the output directory
    os.system("chmod -R 777 /out")

# if the toolname is not valid, write an error log
else:
    with open('/out/error.log', 'w') as f:
        f.write(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
