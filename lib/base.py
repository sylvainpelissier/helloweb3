from abc import *

import socketserver
import typing

from . import util


class ChallengeBase(util.TextStreamRequestHandler, ABC):
    @property
    @abstractmethod
    def metadata(self) -> dict[str, typing.Any]:
        """key value database to store instance information"""
        pass

    def handle(self) -> None:
        self.print("hello web3")

    @classmethod
    def make_handler_class(cls) -> type[socketserver.BaseRequestHandler]:
        metadata: dict[str, typing.Any] = {}  # global variable

        class RequestHandler(cls):
            @property
            def metadata(self):
                return metadata

        return RequestHandler
