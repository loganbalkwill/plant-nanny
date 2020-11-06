
sql_insert={
            'soilsensor_trans'  :   "INSERT INTO soilsensor_trans (DateTime, plant_id, SoilTemp_DegC, SoilMoisture_val) VALUES (%s, %s, %s, %s)",
            'gassensor_trans'   :   "INSERT INTO `gassensor_trans` (`record_id`, `DateTime`, `plant_id`, `eCO2_ppm`, `TVOC_ppb`) VALUES (NULL, %s, %s, %s, %s)",
            'lightsensor_trans' :   "INSERT INTO `lightsensor_trans` (`record_id`, `DateTime`, `plant_id`, `colour_red`, `colour_green`, `colour_blue`, `colour_clear`) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
            'airsensor_trans'   :   "INSERT INTO `airsensor_trans` (`record_id`, `DateTime`, `plant_id`, `AirTemp_DegC`, `AirHumidity_percent`, `AirGas_ohms`, `AirPressure_hpa`) VALUES (NULL, %s, %s, %s, %s, %s, %s)",
            'photo_trans'       :   "INSERT INTO `photo_trans` (`record_id`, `capture_datetime`, `plant_id`, `image_path`) VALUES (NULL, %s, %s, %s)",
            'log_trans'         :   "INSERT INTO `log_trans` (`record_id`, `datetime`, `log_type`, `log_message`) VALUES (NULL, %s, %s, %s)"
}           

