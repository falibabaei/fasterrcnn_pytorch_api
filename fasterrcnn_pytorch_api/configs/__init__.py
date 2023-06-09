"""Configuration loader for rnacontactmap."""
import configparser
import os
import pathlib
from importlib.metadata import metadata as _metadata

#from webdav4.client import Client

# Get configuration from user env and merge with pkg settings
SETTINGS_FILE = pathlib.Path(__file__).parent / "settings.ini"
SETTINGS_FILE = os.getenv("fasterrcnn-pytorch-training-pipeline_SERRING", default=SETTINGS_FILE)
settings = configparser.ConfigParser()
settings.read(SETTINGS_FILE)

try:  # Configure model metadata from pkg metadata 
    MODEL_NAME = os.getenv("MODEL_NAME", default=settings['model']['name'])
    MODEL_METADATA = _metadata(MODEL_NAME).json
except KeyError as err:
    raise RuntimeError("Undefined configuration for [model]name") from err

try:  # Configure input files for testing and possible training
    DATA_PATH = os.getenv("DATA_PATH", default=settings['data']['path'])
    # Selbstaufsicht requires currently the setup of DATA_PATH env variable
    os.environ["DATA_PATH"] = DATA_PATH
except KeyError as err:
    raise RuntimeError("Undefined configuration for [data]path") from err

try:  # Local path for caching   sub/models
    MODEL_DIR = os.getenv("MODEL_DIR", settings['model_dir']['path'])
    os.environ["MODEL_DIR"] = MODEL_DIR 
except KeyError as err:
    raise RuntimeError("Undefined configuration for model path") from err
 

try:  # Local path for caching   sub/models
    REMOT_URL = os.getenv("REMOT", settings['remote']['url'])
    os.environ["REMOT_URL"] = REMOT_URL 
except KeyError as err:
    raise RuntimeError("Undefined configuration for url") from err


