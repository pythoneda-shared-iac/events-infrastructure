# vim: set fileencoding=utf-8
"""
pythoneda/shared/iac/events/infrastructure/dbus/dbus_infrastructure_removal_requested.py

This file declares the DbusInfrastructureRemovalRequested event.

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
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.iac.events import InfrastructureRemovalRequested
from pythoneda.shared.iac.events.infrastructure.dbus import DBUS_PATH
from typing import List, Type


class DbusInfrastructureRemovalRequested(DbusEvent):
    """
    Represents the moment removal of infrastructure resources has been requested.

    Class name: DbusInfrastructureRemovalRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusInfrastructureRemovalRequested instance.
        """
        super().__init__("Pythoneda_Iac_InfrastructureRemovalRequested", DBUS_PATH)

    @signal()
    def InfrastructureRemovalRequested(
        self,
        stackName: "s",
        projectName: "s",
        location: "s",
    ):
        """
        Defines the InfrastructureRemovalRequested d-bus signal.
        :param stackName: The name of the stack.
        :type stackName: str
        :param projectName: The name of the project.
        :type projectName: str
        :param location: The location.
        :type location: str
        """
        pass

    @classmethod
    def transform(cls, event: InfrastructureRemovalRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.shared.iac.events.InfrastructureRemovalRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.stack_name,
            event.project_name,
            event.location,
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: InfrastructureRemovalRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.shared.iac.events.InfrastructureRemovalRequested
        :return: The signature.
        :rtype: str
        """
        return "sssss"

    @classmethod
    def parse(cls, message: Message) -> InfrastructureRemovalRequested:
        """
        Parses given d-bus message containing a InfrastructureRemovalRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The InfrastructureRemovalRequested event.
        :rtype: pythoneda.shared.iac.events.InfrastructureRemovalRequested
        """
        stack_name,
        project_name,
        location,
        prev_event_ids,
        event_id = message.body
        return InfrastructureRemovalRequested(
            stack_name,
            project_name,
            location,
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
        return InfrastructureRemovalRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
