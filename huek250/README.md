# HUEK250

## Description

Dockerized tool to extract and process data from the HUEK250 shapefile for CAMELS-DE.  
A folder is created in the `output_data` folder for the results of each catchment, in which a .csv file is saved for each of the superclasses with the variables listed below. In addition, plots of the superclasses in the catchment area are also generated. Extracted variables are copied to the camelsp `output_data` directory, where other tools process the data further and organize it in the folder structure.

## Container

### Build the container

```bash
docker build -t huek250 .
```

### Run the container

Follow the instructions in `input_data/README.md` to add the necessary input data to run the tool. 

To run the container, the local `input_data`, `output_data` and `camelsp/output_data` directories have to be mounted inside the container:

```bash
docker run -v ./input_data:/input_data -v ./output_data:/output_data -v /path/to/local/camelsp/output_data:/camelsp/output_data -it --rm huek250
```

## Output variables

All variables represent the area percentage of the various HUEK250 classes of the total catchment area.  

**Permeability**:
- kf_very_high_perc [%]
- kf_high_perc [%]
- kf_medium_perc [%]
- kf_moderate_perc [%]
- kf_low_perc [%]
- kf_very_low_perc [%]
- kf_extremely_low_perc [%]
- kf_very_high_to_high_perc [%]
- kf_medium_to_moderate_perc [%]
- kf_low_to_extremely_low_perc [%]
- kf_highly_variable_perc [%]
- kf_moderate_to_low_perc [%]
- kf_no_data_perc [%]
- kf_water_body_perc [%]

**Aquifer media type**:
- aquitard_perc [%]
- aquifer_perc [%]
- aquifer_aquitard_mixed_perc [%]
- aquifer_waterbody_perc [%]
- aquifer_no_data_perc [%]

**Cavity type**:
- cavity_fissure_perc [%]
- cavity_pores_perc [%]
- cavity_fissure_karst_perc [%]
- cavity_fissure_pores_perc [%]
- cavity_waterbody_perc [%]
- cavity_no_data_perc [%]

**Consolidation**:
- consolidation_solid_rock_perc [%]
- consolidation_unconsolidated_rock_perc [%]
- consolidation_waterbody_perc [%]
- consolidation_no_data_perc [%]

**Rock type**:
- rocktype_sediment_perc [%]
- rocktype_metamorphite_perc [%]
- rocktype_magmatite_perc [%]
- rocktype_waterbody_perc [%]
- rocktype_no_data_perc [%]

**Geochemical rock type**:
- geochemical_rocktype_silicate_perc [%]
- geochemical_rocktype_silicate_carbonatic_perc [%]
- geochemical_rocktype_carbonatic_perc [%]
- geochemical_rocktype_sulfatic_perc [%]
- geochemical_rocktype_silicate_organic_components_perc [%]
- geochemical_rocktype_anthropogenically_modified_through_filling_perc [%]
- geochemical_rocktype_sulfatic_halitic_perc [%]
- geochemical_rocktype_halitic_perc [%]
- geochemical_rocktype_waterbody_perc [%]
- geochemical_rocktype_no_data_perc [%]
