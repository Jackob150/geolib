import logging.config
import pytest

from tests.test_logger import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

@pytest.fixture
def test_manager():
    test_status = {}
    yield test_status, logger
