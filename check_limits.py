MIN_TEMP = 0
MAX_TEMP = 45
SOC_MIN = 20
SOC_MAX = 80
CHARGE_RATE_MAX = 0.8

def is_temperature_within_range(temperature):
    return MIN_TEMP <= temperature <= MAX_TEMP

def is_soc_within_range(soc):
    return SOC_MIN <= soc <= SOC_MAX

def is_charge_rate_within_range(charge_rate):
    return charge_rate <= CHARGE_RATE_MAX

def battery_is_ok(temperature, soc, charge_rate):

    if not is_temperature_within_range(temperature):
        print('Temperature is out of range!')
        return False
    if not is_soc_within_range(soc):
        print('State of Charge is out of range!')
        return False
    if not is_charge_rate_within_range(charge_rate):
        print('Charge rate is out of range!')
        return False

    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
