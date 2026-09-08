# Pipeline Monitoring System

This project monitors Azure SQL, Databricks jobs, clusters, notebooks, and blob storage activities for pipeline health and operational alerts.

## Features

- Azure SQL health monitoring
- Databricks cluster and job monitoring
- Notebook status tracking
- Blob storage monitoring
- Alerting via Microsoft Teams
- Scheduled execution using Python schedulers
- Report generation in Excel format

## Project Structure

```text
.
├── alerts/
├── blob_monitor/
├── config/
├── database/
├── databricks_monitor/
├── logs/
├── monitoring/
├── reports/
├── scheduler/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10+
- Azure access and SQL credentials
- Databricks access token and workspace URL
- Microsoft Teams webhook URL (for alerts)

Install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Update configuration values in the files under the `config/` folder before running the application.

Typical settings may include:

- Azure SQL connection details
- Databricks workspace URL and token
- Blob storage credentials
- Alert webhook URLs
- Scheduler intervals

## Run the Application

```bash
python main.py
```

## Notes

- Make sure your environment variables or configuration files contain valid credentials.
- Review logs in the `logs/` directory for troubleshooting.
- The project may require cloud-specific permissions and network access.

## License

This project is intended for internal monitoring and operational use.
