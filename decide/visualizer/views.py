import json
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404



from base import mods

from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import activate


class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['voting'] = json.dumps(r[0])
        except:
            raise Http404

        return context
    
    

    def set_language(request, language):
        request.session[translation.LANGUAGE_SESSION_KEY] = language
        translation.activate(language)
        return redirect(request.META.get('HTTP_REFERER'))
