# Constants for battery parameter thresholds
THRESHOLDS = {
    'temperature': (0, 45),
    'soc': (20, 80),
    'charge_rate': (0, 0.8)
}

def is_within_range(value, min_val, max_val):
    
    if value < min_val:
        return False, f'value is below the minimum threshold of {min_val}.'
    elif value > max_val:
        return False, f'value is above the maximum threshold of {max_val}.'
    return True, 'Value is within range.'

def battery_is_ok(temperature, soc, charge_rate, reporter):
    
    parameters = {
        'temperature': temperature,
        'soc': soc,
        'charge_rate': charge_rate
    }
    
    for param, value in parameters.items():
        min_val, max_val = THRESHOLDS[param]
        is_ok, message = is_within_range(value, min_val, max_val)
        if not is_ok:
            reporter(param, value, message)
            return False
    
    reporter('Battery', 'All parameters', 'Battery is OK.')
    return True

def console_reporter(parameter, value, message):
    
    print(f'{parameter.capitalize()} ({value}): {message}')

def main():
    
    assert battery_is_ok(25, 70, 0.7, console_reporter) is True
    assert battery_is_ok(50, 85, 0, console_reporter) is False
    assert battery_is_ok(0, 20, 0.8, console_reporter) is True
    assert battery_is_ok(-1, 50, 0.5, console_reporter) is False
    assert battery_is_ok(30, 81, 0.5, console_reporter) is False
    assert battery_is_ok(30, 50, 0.9, console_reporter) is False
    assert battery_is_ok(45, 80, 0.8, console_reporter) is True
    assert battery_is_ok(45.1, 80, 0.8, console_reporter) is False
    assert battery_is_ok(45, 80.1, 0.8, console_reporter) is False
    assert battery_is_ok(45, 80, 0.81, console_reporter) is False

if __name__ == '__main__':
    main()
