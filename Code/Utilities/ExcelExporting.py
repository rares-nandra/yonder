import os
import pandas as pd
import threading

class ExcelExporting:
    def __init__(self, config: dict) -> None:
        self._export_folder = config["exportFolder"]

        if not os.path.exists(self._export_folder):
            os.makedirs(self._export_folder)


    def generate_excel_file(self, driver_licenses: list, filename: str) -> None:
        def write_excel():
            filepath = os.path.join(self._export_folder, filename + ".xlsx")
            
            df = pd.DataFrame(driver_licenses)
            df.to_excel(filepath, index=False, engine="openpyxl")

        thread = threading.Thread(target=write_excel)
        thread.start()