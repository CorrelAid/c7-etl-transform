from sshtunnel import SSHTunnelForwarder
from pathlib import Path
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

load_dotenv(Path(__file__).resolve().parents[1].joinpath(".env"))
server = SSHTunnelForwarder(
    os.environ["LIMESURVEY_SSH_IP"],
    ssh_username=os.environ["LIMESURVEY_SSH_USER"],
    ssh_password=os.environ["LIMESURVEY_SSH_PASSWORD"],
    remote_bind_address=('127.0.0.1', 3306),
    local_bind_address=('localhost', 5555)
)

server.start()

print(server.local_bind_port)

engine = create_engine(f"mariadb+pymysql://{os.environ['LIMESURVEY_SQL_USER']}:"
                       f"{os.environ['LIMESURVEY_SQL_PASSWORD']}@localhost:5555/ve_limesurvey_test?charset=utf8mb4")

results=engine.execute("SELECT * FROM lime_answers")
query_data = [entry for entry in results]