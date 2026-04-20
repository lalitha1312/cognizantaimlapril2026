#create configuration for the project 

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.app_env = os.getenv("APP_ENV", "development")
        self.resource_path = self.get_resource_path("data")

    def get_resource_path(self, resource_name) -> str:
        if self.app_env == "production":
            return f"src/resources/data.json"
        elif self.app_env == "development":
            return f"src/resources/data.csv"
        elif self.app_env == "test":
            return f"src/resources/data.txt"
        else:
            raise ValueError(f"Invalid APP_ENV value. Must be 'production', 'development', or 'test': {self.app_env}")