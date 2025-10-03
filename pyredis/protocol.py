
from pyredis.types import Error, Integer, SimpleString


MSG_SEPARATOR = b"\r\n"
MSG_SEPARATOR_LENGTH = len(MSG_SEPARATOR)


def extract_frame_from_buffer(buffer):
  match chr(buffer[0]):
    case '+':
      separator = buffer.find(MSG_SEPARATOR)
      if separator != -1:
        return SimpleString(buffer[1:separator].decode()), separator + MSG_SEPARATOR_LENGTH
    case '-':
      separator = buffer.find(MSG_SEPARATOR)
      if separator != -1:
        return Error(buffer[1:separator].decode()), separator + MSG_SEPARATOR_LENGTH
    case ':':
      separator = buffer.find(MSG_SEPARATOR)


  return None, 0

print(extract_frame_from_buffer(b"-Syntax Error\r\n"))
