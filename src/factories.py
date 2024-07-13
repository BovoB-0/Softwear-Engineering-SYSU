from json_component import JSONComposite, JSONLeaf


class JSONFactory:
    def create(self, data, key='root'):
        if isinstance(data, dict):
            composite = JSONComposite(key)
            for k, v in data.items():
                composite.add(self.create(v, k))
            return composite
        else:
            return JSONLeaf(key, data)


class JSONTreeFactory(JSONFactory):
    pass


class JSONIndentedFactory(JSONFactory):
    pass


class JSONRectangleFactory(JSONFactory):
    pass
