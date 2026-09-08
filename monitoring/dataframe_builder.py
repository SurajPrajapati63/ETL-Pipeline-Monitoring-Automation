import pandas as pd

from database.repository import MonitoringRepository


class DataFrameBuilder:

    def __init__(self):

        self.repo = MonitoringRepository()

    def build(self):

        rows = self.repo.fetch_all()

        columns = [

            "File Serial Number",

            "File Name",

            "Profile Name",

            "Procedure Name",

            "Status",

            "Blob Arrival Time",

            "Queue Movement Time",

            "Notebook Start Time",

            "Notebook End Time",

            "Duration(Notebook End Time - Notebook Start Time)",

            "Duration (Notebook End Time - Blob Arrival Time)",

            "File Size",

            "Instance",

            "Remark"


        ]

        if not rows:

            return pd.DataFrame(columns=columns)

        normalized_rows = []

        for row in rows:

            normalized_rows.append({

                "File Serial Number": row[1],
                "File Name": row[2],
                "Profile Name": row[3],
                "Procedure Name": row[4],
                "Status": row[5],
                "Blob Arrival Time": row[6],
                "Queue Movement Time": row[7],
                "Notebook Start Time": row[8],
                "Notebook End Time": row[9],
                "Duration(Notebook End Time - Notebook Start Time)": row[10],
                "Duration (Notebook End Time - Blob Arrival Time)": row[11],
                "File Size": row[12],
                "Instance": row[13],
                "Remark": row[14],
            })

        return pd.DataFrame(normalized_rows, columns=columns)