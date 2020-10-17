import os
from pathlib import Path

os.environ["absolute_log_location"] = str(Path.home()) + "/git/py_fy/dist/"

os.environ["newsapi_token"] = "a1b98f1264eb45308fd376809fcf7073"

os.environ["db_name"] = "postgres"
os.environ["db_username"] = "postgres"
os.environ["db_password"] = "password"