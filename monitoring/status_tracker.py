class StatusTracker:

    @staticmethod
    def get_status(run):

        state = run.get("state", {})

        result = state.get("result_state")

        lifecycle = state.get("life_cycle_state")

        if lifecycle == "RUNNING":
            return "RUNNING"

        if result == "SUCCESS":
            return "SUCCESS"

        if result == "FAILED":
            return "FAILED"

        return "QUEUED"