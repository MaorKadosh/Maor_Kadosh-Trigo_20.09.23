Prometheus Service Discovery Demo
This project demonstrates setting up Prometheus to discover targets using a custom inventory service.

Components
inventory_service: A simple Flask app that provides an endpoint to get the list of active targets
prometheus: The Prometheus server configured to scrape the inventory endpoint
update_targets.py: Python script to query inventory and update Prometheus target file
Usage

To start the services:
docker-compose up
This will start the inventory_service on port 1337 and Prometheus on port 9090.

Prometheus is configured to load scrape targets from inventory_targets.json.

To populate the targets file, run the script:
python update_targets.py
This will call the inventory service endpoint and write the targets to the JSON file.

Prometheus will automatically pick up the new targets and begin scraping them.

The targets can be viewed at http://localhost:9090/targets

Configuration
The Prometheus config file is located at ./prometheus/prometheus.yml. This defines the job to scrape the inventory endpoint.

Targets are loaded from ./prometheus/inventory_targets.json which is updated by the script.

Known Issues
Need to periodically run update script to refresh targets
Script needs error handling and logging
Prometheus scrape jobs need to be reloaded after update