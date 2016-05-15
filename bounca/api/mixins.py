'''
Created on 15 mei 2016

@author: Jeroen Arnoldus
'''
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers

class TrapDjangoValidationErrorCreateMixin(object):

    def perform_create(self, serializer):
        try:
            instance = serializer.save()
        except DjangoValidationError as detail:
            raise serializers.ValidationError(detail.messages)

class TrapDjangoValidationErrorUpdateMixin(object):

    def perform_update(self, serializer):
        try:
            instance = serializer.save()
        except DjangoValidationError as detail:
            raise serializers.ValidationError(detail.messages)
