import geopandas as gpd
import pandas as pd
from numpy.testing import assert_almost_equal


def check_extracted_values(df: pd.DataFrame, category: str) -> None:
    """
    Check that the sum of the values in the category columns sum to 100
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with the extracted data.
    category : str
        Category name to check.

    """
    # check that category sums to 100
    sum_category = df[[col for col in df.columns if col.startswith(category)]].sum(axis=1).iloc[0]
    
    # assert that the sum is approximately 100
    assert_almost_equal(sum_category, 100, decimal=1, err_msg=f"Sum of {category} categories is not 100 but {sum_category}")


def extract_kf_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 permeability (kf) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["kf_very_high_perc"] = (clipped[clipped["kf_bez"] == "sehr hoch (>1E-2)"].area.sum() / clipped.area.sum()) * 100
    df["kf_high_perc"] = (clipped[clipped["kf_bez"] == "hoch (>1E-3 - 1E-2)"].area.sum() / clipped.area.sum()) * 100
    df["kf_medium_perc"] = (clipped[clipped["kf_bez"] == "mittel (>1E-4 - 1E-3)"].area.sum() / clipped.area.sum()) * 100
    df["kf_moderate_perc"] = (clipped[clipped["kf_bez"] == "mäßig (>1E-5 - 1E-4)"].area.sum() / clipped.area.sum()) * 100
    df["kf_low_perc"] = (clipped[clipped["kf_bez"] == "gering (>1E-7 - 1E-5)"].area.sum() / clipped.area.sum()) * 100
    df["kf_very_low_perc"] = (clipped[clipped["kf_bez"] == "sehr gering (>1E-9 - 1E-7)"].area.sum() / clipped.area.sum()) * 100
    df["kf_extremely_low_perc"] = (clipped[clipped["kf_bez"] == "äußerst gering (<1E-9)"].area.sum() / clipped.area.sum()) * 100
    df["kf_very_high_to_high_perc"] = (clipped[clipped["kf_bez"] == "sehr hoch bis hoch (>1E-3)"].area.sum() / clipped.area.sum()) * 100
    df["kf_medium_to_moderate_perc"] = (clipped[clipped["kf_bez"] == "mittel bis mäßig (>1E-5 - 1E-3)"].area.sum() / clipped.area.sum()) * 100
    df["kf_low_to_extremely_low_perc"] = (clipped[clipped["kf_bez"] == "gering bis äußerst gering (<1E-5)"].area.sum() / clipped.area.sum()) * 100
    df["kf_highly_variable_perc"] = (clipped[clipped["kf_bez"] == "stark variabel"].area.sum() / clipped.area.sum()) * 100
    df["kf_moderate_to_low_perc"] = (clipped[clipped["kf_bez"] == "mäßig bis gering (>1E-6 - 1E-4)"].area.sum() / clipped.area.sum()) * 100
    df["kf_waterbody_perc"] = (clipped[clipped["kf_bez"] == "Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["kf_no_data_perc"] = (clipped[clipped["kf_bez"] == "keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 100
    check_extracted_values(df, "kf")

    return df
    

def extract_ch_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 aquifer media type (ch) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["aquitard_perc"] = (clipped[clipped["LChar_bez"]=="Grundwasser-Geringleiter"].area.sum() / clipped.area.sum()) * 100
    df["aquifer_perc"] = (clipped[clipped["LChar_bez"]=="Grundwasser-Leiter"].area.sum() / clipped.area.sum()) * 100
    df["aquifer_aquitard_mixed_perc"] = (clipped[clipped["LChar_bez"]=="Grundwasser-Leiter/Geringleiter"].area.sum() / clipped.area.sum()) * 100
    df["aquifer_waterbody_perc"] = (clipped[clipped["LChar_bez"]=="Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["aquifer_no_data_perc"] = (clipped[clipped["LChar_bez"]=="keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 1
    check_extracted_values(df, "aqui")

    return df


def extract_ha_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 cavity type (ha) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["cavity_fissure_perc"] = (clipped[clipped["HA_bez"]=="Kluft"].area.sum() / clipped.area.sum()) * 100
    df["cavity_pores_perc"] = (clipped[clipped["HA_bez"]=="Poren"].area.sum() / clipped.area.sum()) * 100
    df["cavity_fissure_karst_perc"] = (clipped[clipped["HA_bez"]=="Kluft/Karst"].area.sum() / clipped.area.sum()) * 100
    df["cavity_fissure_pores_perc"] = (clipped[clipped["HA_bez"]=="Kluft/Poren"].area.sum() / clipped.area.sum()) * 100
    df["cavity_waterbody_perc"] = (clipped[clipped["HA_bez"]=="Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["cavity_no_data_perc"] = (clipped[clipped["HA_bez"]=="keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 1
    check_extracted_values(df, "cavity")

    return df


def extract_vf_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 consolidation (vf) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["consolidation_solid_rock_perc"] = (clipped[clipped["VF_bez"]=="Festgestein"].area.sum() / clipped.area.sum()) * 100
    df["consolidation_unconsolidated_rock_perc"] = (clipped[clipped["VF_bez"]=="Lockergestein"].area.sum() / clipped.area.sum()) * 100
    df["consolidation_waterbody_perc"] = (clipped[clipped["VF_bez"]=="Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["consolidation_no_data_perc"] = (clipped[clipped["VF_bez"]=="keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 1
    check_extracted_values(df, "consolidation")

    return df


def extract_ga_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 rock type (ga) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["rocktype_sediment_perc"] = (clipped[clipped["GA_bez"]=="Sediment"].area.sum() / clipped.area.sum()) * 100
    df["rocktype_metamorphite_perc"] = (clipped[clipped["GA_bez"]=="Metamorphit"].area.sum() / clipped.area.sum()) * 100
    df["rocktype_magmatite_perc"] = (clipped[clipped["GA_bez"]=="Magmatit"].area.sum() / clipped.area.sum()) * 100
    df["rocktype_waterbody_perc"] = (clipped[clipped["GA_bez"]=="Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["rocktype_no_data_perc"] = (clipped[clipped["GA_bez"]=="keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 1
    check_extracted_values(df, "rocktype")

    return df


def extract_gc_from_huek(huek: gpd.GeoDataFrame, catchment: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 geochemical rock type (ga) data for the given catchment.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchment : gpd.GeoDataFrame
        The catchment GeoDataFrame, same projection as huek.
    id_field_name : str
        The name of the field containing the catchment ID in catchment.

    Returns
    -------
    df : pd.DataFrame
        DataFrame with the extracted data.
        
    """
    # clip huek to catchment boundary
    clipped = huek.clip(catchment)

    # initialize pandas DataFrame to store results
    df = pd.DataFrame()
    df["gauge_id"] = catchment[id_field_name]
    df.set_index("gauge_id", inplace=True)

    # calculate area percentage for each category
    df["geochemical_rocktype_silicate_perc"] = (clipped[clipped["GC_bez"]=="silikatisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_silicate_carbonatic_perc"] = (clipped[clipped["GC_bez"]=="silikatisch/karbonatisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_carbonatic_perc"] = (clipped[clipped["GC_bez"]=="karbonatisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_sulfatic_perc"] = (clipped[clipped["GC_bez"]=="sulfatisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_silicate_organic_components_perc"] = (clipped[clipped["GC_bez"]=="silikatisch mit organischen Anteilen"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_anthropogenically_modified_through_filling_perc"] = (clipped[clipped["GC_bez"]=="durch Auffüllung anthropogen verändert"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_sulfatic_halitic_perc"] = (clipped[clipped["GC_bez"]=="sulfatisch/halitisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_halitic_perc"] = (clipped[clipped["GC_bez"]=="halitisch"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_waterbody_perc"] = (clipped[clipped["GC_bez"]=="Gewässer"].area.sum() / clipped.area.sum()) * 100
    df["geochemical_rocktype_no_data_perc"] = (clipped[clipped["GC_bez"]=="keine Angaben"].area.sum() / clipped.area.sum()) * 100

    # check if extracted categories sum to 1
    check_extracted_values(df, "geochemical_rocktype")

    return df


def extract_hydrogeology_attributes_huek(huek: gpd.GeoDataFrame, catchments: gpd.GeoDataFrame, id_field_name: str) -> pd.DataFrame:
    """
    Extract the huek250 hydrogeology attributes for all catchments.

    Parameters
    ----------
    huek : gpd.GeoDataFrame
        The huek250 data.
    catchments : gpd.GeoDataFrame
        The catchments GeoDataFrame for which to extract the data.
    id_field_name : str
        The name of the field containing the catchment ID in catchments.

    Returns
    -------
    df_all : pd.DataFrame
        DataFrame with the extracted data.

    """
    # reproject catchments to huek
    catchments = catchments.to_crs(huek.crs)

    # initialize pandas DataFrame to store results
    df_all = pd.DataFrame()
    
    # loop through all catchments
    for _, catchment in catchments.iterrows():
        # make catchment a GeoDataFrame
        catchment = gpd.GeoDataFrame([catchment], geometry="geometry", crs=huek.crs)

        # extract ch data
        df_ch = extract_ch_from_huek(huek, catchment, id_field_name)
        # extract kf data
        df_kf = extract_kf_from_huek(huek, catchment, id_field_name)
        # extract ha data
        df_ha = extract_ha_from_huek(huek, catchment, id_field_name)
        # extract ga data
        df_ga = extract_ga_from_huek(huek, catchment, id_field_name)
        # extract vf data
        df_vf = extract_vf_from_huek(huek, catchment, id_field_name)
        # extract gc data
        df_gc = extract_gc_from_huek(huek, catchment, id_field_name)
        
        # merge all dataframes
        df = pd.concat([df_kf, df_ch, df_ha, df_vf, df_ga, df_gc], axis=1)

        # check that all waterbody columns have the same value
        waterbody_cols = [col for col in df.columns if "waterbody" in col]
        assert len(set(df[waterbody_cols].values.flatten().tolist())) == 1

        # make one waterbody column
        df["waterbody_perc"] = df[waterbody_cols[0]]
        df.drop(waterbody_cols, axis=1, inplace=True)

        # check that all no_data columns have the same value
        no_data_cols = [col for col in df.columns if "no_data" in col]
        assert len(set(df[no_data_cols].values.flatten().tolist())) == 1

        # make one no_data column
        df["no_data_perc"] = df[no_data_cols[0]]
        df.drop(no_data_cols, axis=1, inplace=True)
        
        # add to df_all
        df_all = pd.concat([df_all, df], axis=0)

    # round to 2 decimal places
    df_all = df_all.round(2)

    return df_all
