import logging
from datetime import timedelta
from itertools import islice

import click
import pandas as pd
import requests
import yaml
from prefect import flow, task
from sqlalchemy import create_engine
from yaml import SafeLoader

logging.basicConfig(level=logging.INFO)


def batched(iterable, n):
    """Batch data into tuples of length n. The last batch may be shorter."""
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


def config(file_path: str) -> dict:
    with open(file_path) as infile:
        configuration = yaml.load(infile, Loader=SafeLoader)
    return configuration


@task
def extract_data(configuration: dict) -> pd.DataFrame:
    con = create_engine(configuration["datasource_url"])
    sql = """select * from cars"""
    return pd.read_sql(sql, con)


@task
def transform_data(data: pd.DataFrame) -> list:
    luxury_brands = {
        "Lexus",
        "Volvo",
        "Aston Martin",
        "Infiniti",
        "BMW",
        "Land Rover",
        "Maserati",
        "Ferrari",
        "Acura",
        "Lincoln",
        "Genesis",
        "Chrysler",
        "Tesla",
        "Audi",
        "Bugatti",
        "Alfa Romeo",
        "Jaguar",
        "Cadillac",
        "Pontiac",
        "Mercedes-Benz",
        "Oldsmobile",
        "Porsche",
        "Mini",
    }
    data["segment"] = [
        "luxury" if name in luxury_brands else "economy" for name in data["brand"]
    ]

    groups = data.groupby("company_id")["segment"].value_counts(normalize=True)
    res = groups.groupby(groups.index.get_level_values(0)).idxmax()
    return [
        {"company_id": str(company_id), "segment": segment}
        for company_id, segment in res
    ]


@flow
def load_data(configuration: dict, data: list):
    for batch in batched(data, 10):
        batch_update(configuration, batch)


def cache_key_from_batch(context, parameters):
    return "-".join(f"{di['company_id']}{di['segment']}" for di in parameters["data"])


@task(retries=2,
      retry_delay_seconds=60,
      cache_key_fn=cache_key_from_batch,
      cache_expiration=timedelta(days=1))
def batch_update(configuration, data):
    requests.put(configuration["url"], json=list(data))


@flow
def main(configuration_path: str):
    configuration = config(configuration_path)
    df = extract_data(configuration)
    data_to_load = transform_data(df)
    load_data(configuration, data_to_load)


@click.command()
@click.argument("configuration_path", type=click.Path(exists=True))
def command(configuration_path: str):
    main(configuration_path)


if __name__ == "__main__":
    command()
