class DictSerializableMixin(object):
    serializable_fields = None

    def to_dict(self):
        if self.serializable_fields is None:
            raise NotImplementedError

        return dict(map(
            lambda key: (key, getattr(self, key)),
            self.serializable_fields
        ))
