CREATE_TABLE = """

CREATE TABLE IF NOT EXISTS pipeline_monitor(

    "File Serial Number" INTEGER,
    "File Name" TEXT,
    "Profile Name" TEXT,
    "Procedure Name" TEXT,
    "Status" TEXT,

    "Blob Arrival Time" TEXT,
    "Queue Movement Time" TEXT,

    "Notebook Start Time" TEXT,
    "Notebook End Time" TEXT,

    "Duration(Notebook End Time - Notebook Start Time)" TEXT,
    "Duration (Notebook End Time - Blob Arrival Time)" TEXT,

    "File Size" TEXT,
    "Instance" TEXT,
    "Remark" TEXT

)

"""