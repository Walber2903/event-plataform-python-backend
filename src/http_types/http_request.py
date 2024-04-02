from typing import Dict

class HttpRequest:
  def __init__(self, body: Dict, param: int) -> None:
    self.body = body
    self.param = param