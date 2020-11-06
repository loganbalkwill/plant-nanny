
""" Database-Related Dictionaries:  """

#Writing information to database
sql_insert={
    'soilsensor_trans'  :   "INSERT INTO soilsensor_trans (DateTime, plant_id, SoilTemp_DegC, SoilMoisture_val) VALUES (%s, %s, %s, %s)",
    'gassensor_trans'   :   "INSERT INTO `gassensor_trans` (`record_id`, `DateTime`, `plant_id`, `eCO2_ppm`, `TVOC_ppb`) VALUES (NULL, %s, %s, %s, %s)",
    'lightsensor_trans' :   "INSERT INTO `lightsensor_trans` (`record_id`, `DateTime`, `plant_id`, `colour_red`, `colour_green`, `colour_blue`, `colour_clear`) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
    'airsensor_trans'   :   "INSERT INTO `airsensor_trans` (`record_id`, `DateTime`, `plant_id`, `AirTemp_DegC`, `AirHumidity_percent`, `AirGas_ohms`, `AirPressure_hpa`) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
    'photo_trans'       :   "INSERT INTO `photo_trans` (`record_id`, `capture_datetime`, `plant_id`, `image_path`) VALUES (NULL, %s, %s, %s)",
    'log_trans'         :   "INSERT INTO `log_trans` (`record_id`, `datetime`, `log_type`, `log_message`) VALUES (NULL, %s, %s, %s)"
}           

#Retrieving information from database
sql_select={
    'air_temp'      :   "SELECT CAST(a.DateTime as Time) as Timestamp, a.AirTemp_DegC FROM airsensor_trans a WHERE a.DateTime >= '%s' AND a.DateTime < '%s' AND a.plant_id= '%s'",
    'air_humidity'  :   "SELECT CAST(a.DateTime as Time) as Timestamp, a.AirHumidity_percent FROM airsensor_trans a WHERE a.DateTime >= '%s' AND a.DateTime < '%s' AND a.plant_id= '%s'",
    'sensors'       :   "SELECT * FROM sensors",
    'sensor_freq'   :   "SELECT read_frequency_min FROM sensors",
    'plant_devices' :   "SELECT DISTINCT D_PD.id_plant AS Plant_ID, D_P.name AS Plant_Name, D_PD.id_device AS Device_ID, D_D.model AS Device_Name, COALESCE(D_PD.action_freq_mins, D_D.default_action_freq_mins) AS Action_Frequency FROM def_plant_devices AS D_PD INNER JOIN def_plants AS D_P ON D_PD.id_plant=D_P.id INNER JOIN def_devices AS D_D ON D_PD.id_device=D_D.id WHERE D_P.active=1 AND D_D.supported=1 AND D_PD.active=1"
}


""" Error Handling Dictionaries:    """

#Error Statements
err_statement={}    #TODO: Complete Dictionary

if __name__=="__main__":
    x=sql_select['air_humidity']
    print(x)