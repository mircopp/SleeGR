from datawrapper.value_wrapper import ValueWrapper
#from mapval import MappingValidator
from datetime import datetime
import FHIR_objects
from typing import Union, Optional, Dict, List


def value_list_validator(lst: List) -> bool:
    value_validator = FHIR_objects.MappingValidator(FHIR_objects.components_data)
    result = True
    for value in lst:
        result = result and value_validator.validate(value)
    return result

reference= {
    'Id': int,
    'Type': str,
    'Timestamp': str,
    'values': value_list_validator
}





class MeasureWrapper:
    def __init__(self, measurement_json):
        self._measuremet_json = measurement_json

    @property
    def id(self) -> int:
        return self._measuremet_json['Id']

    @property
    def type(self) -> str:
        return self._measuremet_json['Type']

    @property
    def time_stamp(self) -> datetime:
        return self._measuremet_json['Time_stamp']

    def __getitem__(self, key) -> ValueWrapper:
        if isinstance(key, int) and key >= 0:
            return ValueWrapper(self._measuremet_json['values'][key])
        else:
            raise KeyError

value_validator = FHIR_objects.MappingValidator(reference)
value_validator = FHIR_objects.MappingValidator(reference)


def measure_value_generator(json: Dict) -> Optional[MeasureWrapper]:
    validator = FHIR_objects.MappingValidator(FHIR_objects.observation)
    if validator.validate(json):
        return MeasureWrapper(json)
    else:
        return None

if __name__ == '__main__':
    date = datetime(2016, 1, 18, 11, 22, 55)
    date2 = datetime(2016, 1, 19, 11, 22, 55)
    measurements = {
        'arrayOfMeasurements': [
            {
                'Id': 1,
                'Type': 'bal',
                'Timestamp': '2016, 1, 18, 11, 22, 55',
                'values': [
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date,
                        "val2": 0,
                        "val1": 0,
                        "val0": 1111
                    },
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date,
                        "val2": 0,
                        "val1": 0,
                        "val0": 1112
                    },
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date,
                        "val2": 0,
                        "val1": date,
                        "val0": 1113
                    }]
            },
            {
                'Id': 2,
                'Type': 'bal',
                'Timestamp': '2016, 1, 19, 11, 22, 55',
                'values': [
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date2,
                        "val2": 0,
                        "val1": 0,
                        "val0": 1114
                    },
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date2,
                        "val2": 0,
                        "val1": 0,
                        "val0": 1115
                    },
                    {
                        "type": 4,
                        "email": "test@test.com",
                        "tag": "Idle",
                        "time_stamp": date2,
                        "val2": 0,
                        "val1": 0,
                        "val0": 1116
                    }]
            }
        ]

    }

    measures = measurements['arrayOfMeasurements']
    for measure in measures:
        res = measure_value_generator(measure)
        for elem in res:
            print(elem.time_stamp)

