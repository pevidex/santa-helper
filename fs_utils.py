import json
from pathlib import Path
import os

from config import UserConfig

import logging

ROOT_FOLDER_PATH = Path.home().joinpath('.santa-helper')
CONFIG_FILE_PATH = ROOT_FOLDER_PATH.joinpath('config.json')

logger = logging.getLogger(__name__)


def _does_root_folder_exist():
    return os.path.exists(ROOT_FOLDER_PATH) and os.path.isdir(ROOT_FOLDER_PATH)


def _does_config_file_exist():
    return os.path.exists(CONFIG_FILE_PATH)


def _create_root_folder():
    os.makedirs(ROOT_FOLDER_PATH)


def _init_config_file(config_content=None):
    json_object = json.dumps(config_content or {'commands': []}, indent=4)

    with open(CONFIG_FILE_PATH, "w") as outfile:
        outfile.write(json_object)


def deserialize_config_file():
    if not _does_root_folder_exist():
        logger.debug("santa-helper root folder missing. Creating one...")
        _create_root_folder()
    if not _does_config_file_exist():
        logger.debug("santa-helper config file missing. Creating one...")
        _init_config_file()

    with open(CONFIG_FILE_PATH) as config_file:
        return UserConfig.from_json(json.load(config_file))


def serialize_config_file(user_config: UserConfig):
    with open(CONFIG_FILE_PATH, 'w') as f:
        json.dump(user_config.to_json(), f)
