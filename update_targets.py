import requests
import time
import json
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INVENTORY_URL = "http://172.17.0.2:1337/inventory"
OUTPUT_FILE = "/tmp/inventory_targets.json"
MAX_RETRIES = 5
RETRY_DELAY = 1


def fetch_inventory():

    for i in range(MAX_RETRIES):

        try:
            response = requests.get(INVENTORY_URL)
            response.raise_for_status()
            break

        except requests.exceptions.RequestException as e:
            logger.error(f"Request #{i+1} failed: {e}")
            time.sleep(RETRY_DELAY)

    else:
        logger.error(f"Inventory API failed after {MAX_RETRIES} retries")
        sys.exit(1)

    sensors = response.json()

    targets = [{"labels": {"job": "sensor"}, "targets": [sensor]} for sensor in sensors]

    try:
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(targets, f)

    except IOError as e:
        logger.error(f"Error writing targets file: {e}")
        sys.exit(1)


def run(interval):

    while True:

        logger.info("Fetching targets")
        fetch_inventory()

        logger.info(f"Updated targets file {OUTPUT_FILE}")

        time.sleep(interval)


if __name__ == "__main__":

    interval = int(sys.argv[1]) if len(sys.argv) > 1 else 60

    run(interval)