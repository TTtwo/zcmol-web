from .default import DefaultConfig
from .development import DevelopmentConfig

configs = {
    "default": DefaultConfig(),
    "development": DevelopmentConfig()
}