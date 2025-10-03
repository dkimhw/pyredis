from dataclasses import dataclass

@dataclass
class SimpleString:
  data: str

@dataclass
class Error:
  data: str

@dataclass
class Integer:
  data: int
