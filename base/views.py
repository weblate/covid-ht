#
from django.conf import settings
from django.shortcuts import render

from data.forms import DataClassificationForm

from .models import NetworkNode
from .utils import (classification_tuple, get_current_classifier)


def home(request):
    classifier = get_current_classifier()
    nodes = NetworkNode.objects.filter(classification_request=True)
    example_data = getattr(settings, "EXAMPLE_DATA", False)
    (result, result_prob, classifier_error) = None, None, None
    if request.method == 'POST':
        dataform = DataClassificationForm(request.POST)
        if dataform.is_valid():
            try:
                (result, result_prob) = \
                    classification_tuple(classifier, dataform.cleaned_data)
            except Exception as e:
                classifier_error = str(e)
    else:
        dataform = DataClassificationForm()

    return render(
        request,
        'base/home.html',
        {
            'classifier': classifier,
            'nodes': nodes,
            'classifier_error': classifier_error,
            'example_data': example_data,
            'dataform': dataform,
            'result': result,
            'result_prob': result_prob
        }
    )


def about(request):
    return render(
        request,
        'base/about.html',
        {}
    )
