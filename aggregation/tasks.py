import csv
import pickle
from pathlib import Path

from celery import shared_task

from _base.cache import default_redis_pipeline
from aggregation.enums import RECEIVED_DATA_CACHE_KEY, RESULT_FILE_NAME
from aggregation.get_cached_data import get_cached_data


@shared_task(queue='result_maker')
def generate_result_csv(path):
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)  # to skip header
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            phone_number = row[2]
            stocks = int(row[3])
            default_redis_pipeline.hset(
                RECEIVED_DATA_CACHE_KEY, phone_number, pickle.dumps({
                    'first_name': first_name,
                    'last_name': last_name,
                    'stocks': stocks
                })
            )
        default_redis_pipeline.execute()
    data = get_cached_data()
    rows = [
        ['first_name', 'last_name', 'phone_number', 'stocks', ]
    ]
    for k, v in data.items():
        rows.append([
            v['first_name'], v['last_name'], k, v['stocks']
        ])
    Path(RESULT_FILE_NAME.rsplit('/', 1)[0]).mkdir(parents=True, exist_ok=True)
    with open(RESULT_FILE_NAME, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


