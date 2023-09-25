from typing import LiteralString
class Properties:
    def __init__(self, fly_from=None, fly_to=None, date_from=None, date_to=None, sort=None):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.sort = sort

def updateDetails(input_list,defaultValue):
    if isinstance(input_list, list) and len(input_list) > 0:
        item = input_list[0]
        if isinstance(item, dict):
            return Properties(
                fly_from=item.get("fly_from"),
                fly_to=item.get("fly_to"),
                date_from=item.get("date_from"),
                date_to=item.get("date_to"),
                sort=item.get("sort")
            )
    return defaultValue
