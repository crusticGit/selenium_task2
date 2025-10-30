import json

import os


class ConfigReader:
    _config = None

    @classmethod
    def _load_config(cls):
        if cls._config is None:
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
            with open(config_path, 'r', encoding='utf-8') as f:
                cls._config = json.load(f)

    @classmethod
    def get_url(cls, url_type):
        cls._load_config()
        return cls._config["urls"][url_type]

    @classmethod
    def get_timeout(cls):
        cls._load_config()
        return cls._config["timeout"]

    @classmethod
    def get_poll_frequency(cls):
        cls._load_config()
        return cls._config['poll_frequency']
