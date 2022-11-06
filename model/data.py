from dataclasses import dataclass

@dataclass
class Request:
    number: str
    message: str

@dataclass
class Response:
    message : str
    request : Request
