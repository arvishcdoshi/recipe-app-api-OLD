from rest_framework.renderers import JSONRenderer


class EmberJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        result = data
        if data is None:
            data = []
        if "success" not in data and "data" not in data:
            result = {'success': False, "data": data}

            if renderer_context["response"].status_code >= 400:
                result.update({'success': False})

            elif renderer_context["response"].status_code >= 100:
                result.update({'success': True})

        return super(EmberJSONRenderer, self).render(
            result, accepted_media_type, renderer_context
        )
