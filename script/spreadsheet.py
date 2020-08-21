import gspread
from backend.settings import GAUTH_CREDS
import datetime


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

    def is_logged_in(self):
        current_date = datetime.datetime.now().date()
        sheet = self.client.open(self.filename).get_worksheet(1)
        row_count = len(sheet.get_all_records()) + 1
        row_value = sheet.row_values(row_count)
        print(row_value[0], row_count)
        if row_value[0] == "{0}-{1}-{2}".format(str(current_date.day).zfill(2), str(current_date.month).zfill(2),
                                                str(current_date.year).zfill(2)):
            return True, {"row_value": row_value, "row_count": row_count}
        else:
            return False, {"row_value": row_value, "row_count": row_count}

    def login(self):
        if not self.is_logged_in()[0]:
            now_datetime = datetime.datetime.now()
            current_date = now_datetime.date()
            current_time = now_datetime.time()
            sheet = self.client.open(self.filename).get_worksheet(1)
            return sheet.append_row(["{0}-{1}-{2}".format(str(current_date.day).zfill(2),
                                                          str(current_date.month).zfill(2),
                                                          str(current_date.year).zfill(2)),
                                     "{0}:{1}:{2}".format(str(current_time.hour).zfill(2),
                                                          str(current_time.minute).zfill(2),
                                                          str(current_time.second).zfill(2))])
        else:
            return False

    def logout(self):
        temp_data = self.is_logged_in()
        if temp_data[0]:
            now_datetime = datetime.datetime.now()
            current_time = now_datetime.time()
            col_count = len(temp_data[1]['row_value']) + 1
            sheet = self.client.open(self.filename).get_worksheet(1)
            return sheet.update_cell(temp_data[1]['row_count'], col_count, "{0}:{1}:{2}".format(str(current_time.hour).zfill(2),
                                                                                                str(current_time.minute).zfill(2),
                                                                                                str(current_time.second).zfill(2)))
        else:
            return False


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
