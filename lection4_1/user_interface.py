import data_provider as dp
import logger as log

def temperature_view(senson):
    data = dp.get_temperature(senson)
    log.temperature_logger(data)
    return data

def pressuse_view(senson):
    data = dp.get_pressure(senson)
    log.pressure_logger(data)
    return data

def wind_speed_view(senson):
    data = dp.get_wind_speed(senson)
    log.wind_speed_logger(data)
    return data