# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegistrationAssignmentPropertiesRegistrationDefinition(Model):
    """Registration definition inside registration assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param properties: Properties of registration definition inside
     registration assignment.
    :type properties:
     ~azure.mgmt.managedservices.models.RegistrationAssignmentPropertiesRegistrationDefinitionProperties
    :param plan: Plan details for the managed services.
    :type plan: ~azure.mgmt.managedservices.models.Plan
    :ivar id: Fully qualified path of the registration definition.
    :vartype id: str
    :ivar type: Type of the resource
     (Microsoft.ManagedServices/registrationDefinitions).
    :vartype type: str
    :ivar name: Name of the registration definition.
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'RegistrationAssignmentPropertiesRegistrationDefinitionProperties'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, properties=None, plan=None, **kwargs) -> None:
        super(RegistrationAssignmentPropertiesRegistrationDefinition, self).__init__(**kwargs)
        self.properties = properties
        self.plan = plan
        self.id = None
        self.type = None
        self.name = None
