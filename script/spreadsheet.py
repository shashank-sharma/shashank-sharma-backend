import gspread
from backend.settings import GAUTH_CREDS


# TODO: Model validate for url and other stuff
class SpreadsheetModel(object):

    AVAILABLE_DOCUMENT = ["TOREAD"]

    LINK_DOCUMENT = [{"name": "source", "type": "str", "limit": 80},
                     {"name": "type", "type": "str", "limit": 80},
                     {"name": "link", "type": "str", "limit": 200},
                     {"name": "status", "type": "str", "limit": 80},
                     {"name": "priority", "type": "str", "limit": 80},
                     {"name": "description", "type": "str", "limit": 400},
                     {"name": "created_at", "type": "str", "limit": 80},
                     {"name": "updated_at", "type": "str", "limit": 80}]


# If spreadsheet is false, then give error
class SpreadsheetBuilder(object):

    def __init__(self, filename, json_data):
        self.client = gspread.authorize(GAUTH_CREDS)
        self.filename = filename
        self.data = json_data
        self.final_data = []

        # TODO: Support for custom sheet names

    def valid(self):
        if self.filename not in SpreadsheetModel.AVAILABLE_DOCUMENT:
            print("FILENAME")
            return False
        for model in SpreadsheetModel.LINK_DOCUMENT:
            check = self.data[model["name"]] if model["name"] in self.data else False
            if check == False or type(check).__name__ != model["type"] or len(check) > model["limit"]:
                print("Error with", model)
                return False
            else:
                self.final_data.append(self.data[model["name"]])
        return True

    def get_all(self):
        sheet = self.client.open(self.filename).sheet1
        return sheet.get_all_records()

    def append(self):
        sheet = self.client.open(self.filename).sheet1
        return sheet.append_row(self.final_data)
