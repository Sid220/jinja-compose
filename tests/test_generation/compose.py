import os
from jinja_compose.libjinja_compose import JinjaComposeInject


class JinjaCompose(JinjaComposeInject):
    @staticmethod
    def is_leader():
        return False

