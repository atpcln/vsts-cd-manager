# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BuildConfiguration(Model):
    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
    }

    def __init__(self, type=None):
        self.type = type
