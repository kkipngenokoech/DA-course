import pandas as pd

def apply_safety_standard(df, threshold=2.5):
    """
    Applies a WHO safety standard (Threshold).
    Returns a report on how many times we violated the standard.
    """
    # Create a copy to avoid messing up the original data
    report = df.copy()
    
    # The Policy:
    # If CO is greater than 'threshold', the air is UNSAFE.
    report['is_unsafe_TRUTH'] = report['CO(GT)'] > threshold
    
    # Our cheap sensor has a simple cutoff (e.g. raw value > 1200)
    
    report['is_unsafe_SENSOR'] = report['PT08.S1(CO)'] > 1200
    
    return report

def calculate_decision_impact(report):
    """
    Compares the Sensor's decision against the Truth.
    """
    # When did the Sensor panic, but the air was actually safe? (False Alarm)
    false_alarms = report[(report['is_unsafe_SENSOR'] == True) & (report['is_unsafe_TRUTH'] == False)]
    
    # When did the Sensor sleep, but the air was toxic? (Missed Danger)
    missed_dangers = report[(report['is_unsafe_SENSOR'] == False) & (report['is_unsafe_TRUTH'] == True)]
    
    return len(false_alarms), len(missed_dangers)