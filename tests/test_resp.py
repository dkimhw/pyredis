
from pyredis.protocol import extract_frame_from_buffer
from pyredis.types import (
    Error,
    Integer,
    SimpleString,
)
import pytest

@pytest.mark.parametrize("buffer, expected", [
  (b"+Par", (None, 0)),
  (b"+OK\r\n", (SimpleString("OK"), 5)),
  (b"+OK\r\n+Next", (SimpleString("OK"), 5))
])
def test_read_frame_simple_string_incomplete_frame(buffer, expected):
  actual = extract_frame_from_buffer(buffer)
  assert actual == expected

@pytest.mark.parametrize("buffer, expected", [
  (b"-Syntax Error\r\n", (Error("Syntax Error"), 15))
])
def test_read_frame_error(buffer, expected):
  actual = extract_frame_from_buffer(buffer)
  print(actual)
  assert actual == expected
