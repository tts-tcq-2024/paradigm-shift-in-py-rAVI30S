# Constants for battery parameter thresholds
TEMPERATURE_MIN = 0
TEMPERATURE_MAX = 45
SOC_MIN = 20
SOC_MAX = 80
CHARGE_RATE_MAX = 0.8

def is_temperature_within_range(temperature):
    return TEMPERATURE_MIN <= temperature <= TEMPERATURE_MAX

def is_soc_within_range(soc):
    return SOC_MIN <= soc <= SOC_MAX

def is_charge_rate_within_range(charge_rate):
   return charge_rate <= CHARGE_RATE_MAX

def battery_is_ok(temperature, soc, charge_rate):
    if not is_temperature_within_range(temperature):
        return False, 'Temperature is out of range!'
    if not is_soc_within_range(soc):
        return False, 'State of Charge is out of range!'
    if not is_charge_rate_within_range(charge_rate):
        return False, 'Charge rate is out of range!'

    return True, 'Battery is OK.'

def main():
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)   

if __name__ == '__main__':
    main()
