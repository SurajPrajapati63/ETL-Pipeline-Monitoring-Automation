def fetch_waiting_files(self):

    self.db.execute("""

    SELECT id,

           blob_arrival_time,

           file_name

    FROM pipeline_monitor

    WHERE status='WAITING'

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
                    job_id,
                    run_id,
                    cluster_id):

    query = """

    UPDATE pipeline_monitor

    SET

    notebook_start_time=?,

    queue_time=?,

    notebook_end_time=?,

    notebook_duration=?,

    total_duration=?,

    status=?,

    job_id=?,

    run_id=?,

    cluster_id=?

    WHERE id=?

    """

    values = (

        notebook_start,

        queue_time,

        notebook_end,

        notebook_duration,

        total_duration,

        status,

        job_id,

        run_id,

        cluster_id,

        record_id

    )

    self.db.execute(query, values)