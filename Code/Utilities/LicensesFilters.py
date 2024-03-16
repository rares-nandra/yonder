from datetime import datetime

class LicensesFilters:
    def __init__(self, config: dict) -> None:
        self._categories = config["categories"]

    def suspended(self, driver_licenses: list) -> list:
        suspended_licenses = []

        for driver_license in driver_licenses:
            if driver_license["suspendat"]:
                suspended_licenses.append(driver_license)
        
        return suspended_licenses


    def valid(self, driver_licenses: list) -> list:
        today = datetime.today().strftime('%d/%m/%Y')
        valid_licenses = []

        for driver_license in driver_licenses:
            expiration_date = datetime.strptime(driver_license["dataDeExpirare"], "%d/%m/%Y")
            issued_date = datetime.strptime(driver_license["dataDeEmitere"], "%d/%m/%Y")
            
            if expiration_date >= datetime.strptime(today, "%d/%m/%Y") and issued_date <= datetime.strptime(today, "%d/%m/%Y"):
                valid_licenses.append(driver_license)

        return valid_licenses


    def licenses_by_category(self, driver_licenses: list, category: str) -> list:
        if category not in self._categories:
            raise ValueError("Categorie de permis invalida: " + category)

        licenses_with_category = []

        for driver_license in driver_licenses:
            if driver_license["categorie"] == category:
                licenses_with_category.append(driver_license)

        return licenses_with_category