import logging
from io import StringIO
import pytest
import allure


"""
Create a fixture - logger object, logs will be attached into each test as a post condition of allure report
"""


@pytest.fixture
def custom_logger(request):
    custom_logger = logging.getLogger(request.function.__name__)
    custom_logger.setLevel(logging.DEBUG)

    # Create string_io object to store log data
    string_io = StringIO()

    console_handler = logging.StreamHandler()

    stream_handler = logging.StreamHandler(stream=string_io)

    console_handler_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler_format = logging.Formatter('%(asctime)s == %(process)d == %(name)s == %(levelname)s: %(message)s')

    console_handler.setFormatter(fmt=console_handler_format)
    stream_handler.setFormatter(fmt=stream_handler_format)

    custom_logger.addHandler(hdlr=console_handler)
    custom_logger.addHandler(hdlr=stream_handler)

    # Return a logger object as a fixture
    yield custom_logger

    # Attach our log string_io value into each test case in a post condition (tear down)
    allure.attach(string_io.getvalue(), name="Logs file", attachment_type=allure.attachment_type.TEXT)
