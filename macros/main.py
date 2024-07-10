import yaml
from pathlib import Path


def define_env(env):
    @env.macro
    def load_data(filename):
        data_path = Path(env.project_dir) / "data" / filename
        with open(data_path, "r") as f:
            return yaml.safe_load(f)
