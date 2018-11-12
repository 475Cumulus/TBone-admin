#!/usr/bin/env python
# encoding: utf-8


class ModelAdminManager(object):
    def __init__(self, *args, **kwargs):
        self._registry = {}

    def register(self, name, model):
        self._registry[name] = model

    def get_model(self, name):
        if name in self._registry:
            return self._registry[name]
        raise KeyError('Model not registered')



model_manager = ModelAdminManager()
