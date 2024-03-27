#!/bin/bash
# make directories to store the output data if they do not exist
mkdir -p /output_data/scripts

# logging
exec > >(tee -a /output_data/scripts/processing.log) 2>&1

# Start processing
echo "[$(date +%F\ %T)] Starting processing of HUEK250 hydrogeology data for the CAMELS-DE dataset..."

# Extract HUEK250 data
echo "[$(date +%T)] Extracting HUEK250 hydrogeological data..."
papermill /scripts/01_extract_huek250.ipynb /output_data/scripts/01_extract_huek250.ipynb --no-progress-bar
echo "[$(date +%T)] Saved extracted HUEK250 hydrogeological data for all CAMELS-DE stations with 01_extract_huek250.ipynb"

# Copy the output data to the camelsp output directory
echo "[$(date +%T)] Copying the extracted and postprocessed data to the camelsp output directory..."
mkdir -p /camelsp/output_data/raw_catchment_attributes/hydrogeo/huek250
cp -r /output_data/* /camelsp/output_data/raw_catchment_attributes/hydrogeo/huek250/
echo "[$(date +%T)] Copied the extracted and postprocessed data to the camelsp output directory"

# Copy scripts to /camelsp/output_data/scripts/hydrogeo/huek250/
mkdir -p /camelsp/output_data/scripts/hydrogeo/huek250/
cp /output_data/scripts/* /camelsp/output_data/scripts/hydrogeo/huek250/

# Change permissions of the output data
chmod -R 777 /camelsp/output_data/
chmod -R 777 /output_data/
chmod -R 777 /input_data/