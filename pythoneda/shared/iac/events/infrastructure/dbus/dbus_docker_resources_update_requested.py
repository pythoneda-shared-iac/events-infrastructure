# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/infrastructure/dbus/docker_resources_update_requested.py

This file declares the DockerResourcesUpdateRequested event.

Copyright (C) 2024-today pythoneda-shared-iac/events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import BusType, Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject, Event
from pythoneda.shared.iac.events import DockerResourcesUpdateRequested
from pythoneda.shared.iac.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusDockerResourcesUpdateRequested(BaseObject, ServiceInterface):
    """
    Represents the moment Docker resources have not been updated.

    Class name: DbusDockerResourcesUpdateRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerResourcesUpdateRequested instance.
        """
        super().__init__("Pythoneda_Iac_DockerResourcesUpdateRequested")

    @signal()
    def DockerResourcesUpdateRequested(
        self,
        stackName: "s",
        projectName: "s",
        location: "s",
        imageName: "s",
        imageVersion: "s",
        imageUrl: "s",
    ):
        """
        Defines the DockerResourcesUpdateRequested d-bus signal.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        :param imageName: The image name.
        :type imageName: str
        :param imageVersion: The version.
        :type imageVersion: str
        :param imageUrl: The url of the image.
        :type imageUrl: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + event.image_name.replace("-", "_")

    @property
    def bus_type(self) -> str:
        """
        Retrieves the d-bus type.
        :return: Such value.
        :rtype: str
        """
        return BusType.SYSTEM

    @classmethod
    def transform(cls, event: DockerResourcesUpdateRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.iac.events.DockerResourcesUpdateRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.stack_name,
            event.project_name,
            event.location,
            event.image_name,
            event.image_version,
            event.image_url,
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: DockerResourcesUpdateRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.iac.events.DockerResourcesUpdateRequested
        :return: The signature.
        :rtype: str
        """
        return "ssssssss"

    @classmethod
    def parse(cls, message: Message) -> DockerResourcesUpdateRequested:
        """
        Parses given d-bus message containing a DockerResourcesUpdateRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DockerResourcesUpdateRequested event.
        :rtype: pythoneda.shared.iac.events.DockerResourcesUpdateRequested
        """
        stack_name,
        project_name,
        location,
        image_name,
        image_version,
        image_url,
        event_id,
        prev_event_ids = message.body
        return DockerResourcesUpdateRequested(
            stack_name,
            project_name,
            location,
            image_name,
            image_version,
            image_url,
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End: