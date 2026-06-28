from pathlib import Path
import yaml

from etl.paths import CONFIG_PATH

def load_config():

    project_root = (
        Path(__file__)
        .resolve()
        .parent
        .parent
    )

    config_path = (
        project_root
        / "config"
        / "config.yaml"
    )
    
    with open(CONFIG_PATH, "r") as file:

        return yaml.safe_load(file)



