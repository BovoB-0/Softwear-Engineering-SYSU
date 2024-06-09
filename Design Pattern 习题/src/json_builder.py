from json_component import JSONComposite, JSONLeaf

class JSONBuilder:
    def build(self, data):
        if isinstance(data, dict):
            composite = JSONComposite("root")
            for key, value in data.items():
                composite.add(self._build_component(key, value))
            return composite
        raise ValueError("Data must be a dictionary")

    def _build_component(self, key, value):
        if isinstance(value, dict):
            composite = JSONComposite(key)
            for k, v in value.items():
                composite.add(self._build_component(k, v))
            return composite
        else:
            return JSONLeaf(key, value)
