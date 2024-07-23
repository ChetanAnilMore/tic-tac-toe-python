from __future__ import annotations
import enum

class Mark(enum.StrEnum):
  CROSS = "X"
  NAUGHT = "0"

  @property
  def other(self) -> Mark:
    return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT