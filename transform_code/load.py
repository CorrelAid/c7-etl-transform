"""Connects to the Limesurvey database through an SSH tunnel (see README.md for setting env variables)"""  # noqa : E401
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder

if __name__ == "__main__":
    load_dotenv(Path(__file__).resolve().parents[1].joinpath(".env"))
    server = SSHTunnelForwarder(
        os.environ["LIMESURVEY_SSH_IP"],
        ssh_username=os.environ["LIMESURVEY_SSH_USER"],
        ssh_password=os.environ["LIMESURVEY_SSH_PASSWORD"],
        remote_bind_address=("127.0.0.1", 3306),
        local_bind_address=("localhost", 5555),
    )

    server.start()

    engine = create_engine(
        f"mariadb+pymysql://{os.environ['LIMESURVEY_SQL_USER']}:"
        f"{os.environ['LIMESURVEY_SQL_PASSWORD']}@localhost:5555"
        f"/ve_limesurvey_test?charset=utf8mb4"
    )

    for table in engine.table_names():
        results = engine.execute(f"SELECT * FROM {table}")
        query_data = [entry for entry in results]
        pd.DataFrame(query_data).to_csv(
            Path(__file__).resolve().parents[1].joinpath(f"data/raw/{table}.csv")
        )
