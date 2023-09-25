import os
from jinja_compose_wrapper.libjinja_compose import JinjaComposeInject


class JinjaCompose(JinjaComposeInject):
    @staticmethod
    def is_leader():
        return False

