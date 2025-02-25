# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import DevCenterDataplaneClientConfiguration
from .operations import ProjectOperations
from .operations import PoolOperations
from .operations import ScheduleOperations
from .operations import DevBoxOperations
from .operations import EnvironmentsOperations
from .operations import ArtifactsOperations
from .operations import CatalogItemsOperations
from .operations import CatalogItemVersionsOperations
from .operations import EnvironmentTypeOperations
from .operations import NotificationSettingOperations
from .. import models


class DevCenterDataplaneClient(object):
    """DevBox API.

    :ivar dev_center: DevCenterOperations operations
    :vartype dev_center: dev_center_dataplane_client.aio.operations.DevCenterOperations
    :ivar dev_boxes: DevBoxesOperations operations
    :vartype dev_boxes: dev_center_dataplane_client.aio.operations.DevBoxesOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: dev_center_dataplane_client.aio.operations.EnvironmentsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param project_name: The DevCenter Project upon which to execute operations.
    :type project_name: str
    :param endpoint: The DevCenter-specific URI to operate on.
    :type endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        project_name: str,
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}'
        self._config = DevCenterDataplaneClientConfiguration(credential, project_name, endpoint, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.project = ProjectOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pool = PoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.schedule = ScheduleOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dev_box = DevBoxOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.artifacts = ArtifactsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_item = CatalogItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_items = CatalogItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.catalog_item_versions = CatalogItemVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.environment_type = EnvironmentTypeOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.notification_setting = NotificationSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DevCenterDataplaneClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
