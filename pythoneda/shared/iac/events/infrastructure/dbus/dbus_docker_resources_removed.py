# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/infrastructure/dbus/docker_resources_removed.py

This file declares the DockerResourcesRemoved event.

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
from dbus_next.service import signal
import json
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.iac.events import DockerResourcesRemoved
from pythoneda.shared.iac.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusDockerResourcesRemoved(DbusEvent):
    """
    Represents the moment Docker resources have not been removal.

    Class name: DbusDockerResourcesRemoved

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusDockerResourcesRemoved instance.
        """
        super().__init__("Pythoneda_Iac_DockerResourcesRemoved")

    @signal()
    def DockerResourcesRemoved(
        self,
        stackName: "s",
        projectName: "s",
        location: "s",
        imageName: "s",
        imageVersion: "s",
        imageUrl: "s",
    ):
        """
        Defines the DockerResourcesRemoved d-bus signal.
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
    def transform(cls, event: DockerResourcesRemoved) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.iac.events.DockerResourcesRemoved
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
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: DockerResourcesRemoved) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.iac.events.DockerResourcesRemoved
        :return: The signature.
        :rtype: str
        """
        return "ssssssss"

    @classmethod
    def parse(cls, message: Message) -> DockerResourcesRemoved:
        """
        Parses given d-bus message containing a DockerResourcesRemoved event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The DockerResourcesRemoved event.
        :rtype: pythoneda.shared.iac.events.DockerResourcesRemoved
        """
        stack_name,
        project_name,
        location,
        image_name,
        image_version,
        image_url,
        prev_event_ids,
        event_id = message.body
        return DockerResourcesRemoved(
            stack_name,
            project_name,
            location,
            image_name,
            image_version,
            image_url,
            json.loads(prev_event_ids),
            event_id,
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return DockerResourcesRemoved


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
