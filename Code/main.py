from Utilities import ConfigReader
from Utilities import API
from Utilities import LicensesFilters
from Utilities import ExcelExporting

def print_licenses(licenses: list) -> None:
    for driver_license in licenses:
        for key in driver_license:
            print(key, driver_license[key])
        print("")

if __name__ == "__main__":
    config = ConfigReader.ConfigReader().config
    api = API.API(config["api"])
    exporting = ExcelExporting.ExcelExporting(config["exporting"])
    filters = LicensesFilters.LicensesFilters(config["filters"])

    licenses = api.get_driver_licenses(150)

    Command = ""

    while True:
        print("1. Permise suspendate")
        print("2. Permise valide")
        print("3. Permise dupa categorie")
        print("4. Iesire")
        Command = input("Comanda: ")

        try:
            if Command == "1":
                filtered_licenses = filters.suspended(licenses)
                print_licenses(filtered_licenses)
                filename = input("Numele fisiereului excel: ")
                exporting.generate_excel_file(filtered_licenses, filename)
            elif Command == "2":
                filtered_licenses = filters.valid(licenses)
                print_licenses(filtered_licenses)
                filename = input("Numele fisiereului excel: ")
                exporting.generate_excel_file(filtered_licenses, filename)
            elif Command == "3":
                category = input("Categorie: ")
                filtered_licenses = filters.licenses_by_category(licenses, category)
                print_licenses(filtered_licenses)
                filename = input("Numele fisiereului excel: ")
                exporting.generate_excel_file(filtered_licenses, filename)
            elif Command == "4":
                exit()
            else:
                print("Comanda invalida")
        except Exception as e:
            print(e)
