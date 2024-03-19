import json
from rest_framework.renderers import JSONRenderer


class PropertiesJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders the error message in the JSON form.
        If no error occurs, it renders the output in JSON format.
        """
        if 'ErrorDetail' in data:
            response = json.dumps({'errors': data})
        else:
            response = json.dumps(data)

        return response
