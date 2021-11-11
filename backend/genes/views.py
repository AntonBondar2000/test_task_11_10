from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from genes.find_codone_services import method_kmp
from genes.validators import validator_codon


class CheckCodonView(viewsets.ViewSet):
    def create(self, request):
        codon = request.data['codon'].lower()
        error = validator_codon(codon)  # validation
        if error:
            return Response({
                'error': error
            })
        is_find = method_kmp(codon, settings.GENE)
        return Response({
            'result': is_find,
        })
