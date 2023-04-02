import os
from starbun.logger import logger

ENV_PREFIX = "STARBUN"
ENV_SEP = "_"

KEY_PROJECTS_PATH = "PROJECTS_PATH"

DEFAULT_VALUES = {
    KEY_PROJECTS_PATH: "./"
}

# Get a value, with the following hierarcy: value, env variable, default
def get_value(key, value=None, experiment_label=None, trial_label=None, run_label=None):

    # If value is given, return it
    if value is not None:
        logger.debug(f"Value for {key} given as override, returning '{value}'", experiment_label, trial_label, run_label)
        return value
    
    # If a value exists in environment variables, return it
    env_key = f"{ENV_PREFIX}{ENV_SEP}{key}"
    env_value = os.getenv(env_key)
    if env_value is not None and env_value != "":
        logger.debug(f"Value for {key} found as environment variable {env_key}, returning '{env_value}'", experiment_label, trial_label, run_label)
        return env_value
    
    # If a default value exists, return it
    try:
        default_value = DEFAULT_VALUES[key]
        logger.debug(f"Value for {key} found in defaults, returning '{default_value}'", experiment_label, trial_label, run_label)
        return default_value
    except KeyError:
        pass

    logger.warn(f"Tried to get value for {key}, but no override, environment variable or default existed. Returning None.", experiment_label, trial_label, run_label)
    return None





