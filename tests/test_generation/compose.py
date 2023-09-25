import os
from libjinja_compose import JinjaComposeInject


class JinjaCompose(JinjaComposeInject):
    @staticmethod
    def is_leader():
        return False

