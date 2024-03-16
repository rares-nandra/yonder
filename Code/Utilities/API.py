import requests

class API:
    def __init__(self, config: dict) -> None:
        self._url = config["url"]
        self._param_for_length = config["paramForLength"]
        self._expected_keys = config["expected"]["keys"]
        self._expected_data_types = config["expected"]["dataTypes"]

    def get_driver_licenses(self, length: int) -> dict | Exception:
        url = self._url
        params = {self._param_for_length: length}

        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        is_valid, error_message =  self._validate_json(data)

        if is_valid:
            return data
        
        raise ValueError("Eroare in formatul JSON-ului " + error_message)

    
    def _validate_json(self, data: dict) -> (bool, str):    
        for entry in data:
            if not isinstance(entry, dict):
                return False, "Format invalid de date"

            if set(self._expected_keys) != set(entry.keys()):
                return False, "keys neasteptate"

            for key, expected_type_str in zip(self._expected_keys, self._expected_data_types):
                expected_type = eval(expected_type_str)

                if not isinstance(entry[key], expected_type):
                    return False, "Format invalid pentru: " + key

            if not entry["dataDeEmitere"].count("/") == 2 or not entry["dataDeExpirare"].count("/") == 2:
                return False, "Format de date invalid, ar trebui sa fie: 'DD/MM/YYYY'"
    
        return True, "Datele sunt valide"