
"""
Simple String "+OK\r\n"

Error "-Error message\r\n"

Integers ":100\r\n"

Bulk String "*2\r\n$4\r\necho\r\n$5\r\nhello world\r\n"

Arrays "*2\r\n:1\r\n :2\r\n"
"""
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from project import resp

# def test_read_frame_simple_string_incomplete_frame():
#   buffer = b"+Par"
#   frame, frame_size = resp.extract_frame_from_buffer(buffer)
#   assert frame == None
#   assert frame_size == 0

from project import resp

def test_greet():
    assert resp.greet("Alice") == "Hello, Alice!"
