from database.database import Database
from database.models import CREATE_TABLE
from config.config import Config

class MonitoringRepository:

    def __init__(self):

        self.db = Database(
            Config.DATABASE_NAME
        )

        self.db.execute(CREATE_TABLE)
        self.ensure_schema()

    def ensure_schema(self):

        self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pipeline_monitor'")
        table_exists = self.db.fetchall()

        if not table_exists:
            self.db.execute(CREATE_TABLE)
            return

        self.db.execute("PRAGMA table_info(pipeline_monitor)")
        columns = [row[1] for row in self.db.fetchall()]

        if any(column in columns for column in ["serial_number", "file_name", "profile_name", "procedure_name", "blob_arrival_time", "status"]) or "File" in columns:
            self.migrate_legacy_table()
            return

        expected_columns = [
            ("File Serial Number", "INTEGER"),
            ("File Name", "TEXT"),
            ("Profile Name", "TEXT"),
            ("Procedure Name", "TEXT"),
            ("Status", "TEXT"),
            ("Blob Arrival Time", "TEXT"),
            ("Queue Movement Time", "TEXT"),
            ("Notebook Start Time", "TEXT"),
            ("Notebook End Time", "TEXT"),
            ("Duration(Notebook End Time - Notebook Start Time)", "TEXT"),
            ("Duration (Notebook End Time - Blob Arrival Time)", "TEXT"),
            ("File Size", "TEXT"),
            ("Instance", "TEXT"),
            ("Remark", "TEXT"),
        ]

        for column_name, data_type in expected_columns:
            if column_name not in columns:
                self.db.execute(
                    f'ALTER TABLE pipeline_monitor ADD COLUMN "{column_name}" {data_type}'
                )
                columns.append(column_name)

        if 'file_size' in columns and 'File Size' in columns:
            self.db.execute(
                'UPDATE pipeline_monitor SET "File Size" = file_size WHERE "File Size" IS NULL AND file_size IS NOT NULL'
            )

    def migrate_legacy_table(self):

        self.db.execute("ALTER TABLE pipeline_monitor RENAME TO pipeline_monitor_legacy")
        self.db.execute(CREATE_TABLE)

        self.db.execute("PRAGMA table_info(pipeline_monitor_legacy)")
        legacy_columns = [row[1] for row in self.db.fetchall()]

        def column_expr(*options):
            for option in options:
                if option in legacy_columns:
                    return f'"{option}"' if " " in option else option
            return "NULL"

        self.db.execute(f"""

            INSERT INTO pipeline_monitor(

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

            )

            SELECT

            {column_expr("File Serial Number", "serial_number")},

            {column_expr("File Name", "file_name")},

            {column_expr("Profile Name", "profile_name")},

            {column_expr("Procedure Name", "procedure_name")},

            {column_expr("Status", "status")},

            {column_expr("Blob Arrival Time", "blob_arrival_time")},

            {column_expr("Queue Movement Time", "queue_time")},

            {column_expr("Notebook Start Time", "notebook_start_time")},

            {column_expr("Notebook End Time", "notebook_end_time")},

            {column_expr("Duration(Notebook End Time - Notebook Start Time)", "notebook_duration")},

            {column_expr("Duration (Notebook End Time - Blob Arrival Time)", "total_duration")},

            {column_expr("File Size", "file_size")},

            {column_expr("Instance", "cluster_id")},

            {column_expr("Remark", "remarks")}

            FROM pipeline_monitor_legacy

        """)

        self.db.execute("DROP TABLE pipeline_monitor_legacy")

    def insert(self, values):

        query = """

        INSERT INTO pipeline_monitor(

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

        )

        VALUES(

        ?,?,?,?,?,?,?,?,?,?,?,?,?,?

        )

        """

        self.db.execute(query, values)

    def fetch_all(self):

        self.db.execute("""

            SELECT

                rowid AS id,

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

            FROM pipeline_monitor

        """)

        return self.db.fetchall()

    def file_exists(self, file_name):

        self.db.execute(

            'SELECT rowid FROM pipeline_monitor WHERE "File Name"=?',

            (file_name,)

        )

        result = self.db.fetchall()

        return len(result) > 0

    def get_next_serial(self):

        self.db.execute(

            'SELECT MAX("File Serial Number") FROM pipeline_monitor'

        )

        result = self.db.fetchall()[0][0]

        if result is None:
            return 1

        return result + 1

    def fetch_waiting_files(self):

        self.db.execute("""

        SELECT

               rowid AS id,

               "Blob Arrival Time" AS blob_arrival_time,

               "File Name" AS file_name

        FROM pipeline_monitor

        WHERE "Status"='WAITING'

        """)

        return self.db.fetchall()

    def update_pipeline(self,
                        record_id,
                        notebook_start,
                        queue_time,
                        notebook_end,
                        notebook_duration,
                        total_duration,
                        status,
                        instance):

        query = """

        UPDATE pipeline_monitor

        SET

        "Notebook Start Time"=?,

        "Queue Movement Time"=?,

        "Notebook End Time"=?,

        "Duration(Notebook End Time - Notebook Start Time)"=?,

        "Duration (Notebook End Time - Blob Arrival Time)"=?,

        "Status"=?,

        "Instance"=?

        WHERE rowid=?

        """

        values = (

            notebook_start,

            queue_time,

            notebook_end,

            notebook_duration,

            total_duration,

            status,

            instance,

            record_id

        )

        self.db.execute(query, values)