"""User content reporting."""

from typing import Optional

from comcatlib import User
from marketplace import Offer
from tenantcalendar import UserEvent
from tenantforum import Response, Topic

from reportlib.orm import OfferReport
from reportlib.orm import TopicReport
from reportlib.orm import ResponseReport
from reportlib.orm import UserEventReport


__all__ = [
    'report_offer',
    'report_topic',
    'report_response',
    'report_user_event'
]


def report_offer(
        reporter: User,
        offer: Offer,
        *,
        title: Optional[bool] = None,
        text: Optional[bool] = None,
        image: Optional[bool] = None
) -> OfferReport:
    """Report an offer."""

    try:
        report = OfferReport.get(
            (OfferReport.reporter == reporter) & (OfferReport.offer == offer)
        )
    except OfferReport.DoesNotExist:
        report = OfferReport(reporter=reporter, offer=offer)

    return report.update(title=title, text=text, image=image)


def report_topic(
        reporter: User,
        topic: Topic,
        *,
        title: Optional[bool] = None,
        text: Optional[bool] = None,
        image: Optional[bool] = None
) -> TopicReport:
    """Report a tenant forum topic."""

    try:
        report = TopicReport.get(
            (TopicReport.reporter == reporter) & (TopicReport.topic == topic)
        )
    except TopicReport.DoesNotExist:
        report = TopicReport(reporter=reporter, topic=topic)

    return report.update(title=title, text=text, image=image)


def report_response(
        reporter: User,
        response: Response,
        *,
        title: Optional[bool] = None,
        text: Optional[bool] = None,
        image: Optional[bool] = None
) -> ResponseReport:
    """Report a tenant forum response."""

    try:
        report = ResponseReport.get(
            (ResponseReport.reporter == reporter)
            & (ResponseReport.response == response)
        )
    except ResponseReport.DoesNotExist:
        report = ResponseReport(reporter=reporter, response=response)

    return report.update(title=title, text=text, image=image)


def report_user_event(
        reporter: User,
        user_event: UserEvent,
        *,
        title: Optional[bool] = None,
        text: Optional[bool] = None,
        image: Optional[bool] = None
) -> UserEventReport:
    """Report a tenant forum response."""

    try:
        report = UserEventReport.get(
            (UserEventReport.reporter == reporter)
            & (UserEventReport.user_event == user_event)
        )
    except UserEventReport.DoesNotExist:
        report = UserEventReport(reporter=reporter, user_event=user_event)

    return report.update(title=title, text=text, image=image)
