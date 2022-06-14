# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import scheduling
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Scheduling(GenericRedoxAbstractModel):
    _redox_module = scheduling


class AvailableSlots(_Scheduling):

    EndDateTime: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    StartDateTime: str = Field(...)
    Visit: generic.Visit = Field(None)


class AvailableSlotsResponse(_Scheduling):

    AvailableSlots: List[generic.AvailableSlot] = Field(...)
    Meta: generic.Meta = Field(...)


class Booked(_Scheduling):

    EndDateTime: Union[str, None] = Field(None)
    Meta: generic.Meta = Field(...)
    StartDateTime: str = Field(...)
    Visit: generic.Visit = Field(None)


class BookedResponse(_Scheduling):

    Meta: generic.Meta = Field(...)
    Visits: List[generic.Visit] = Field(...)


class Cancel(_Scheduling):

    AppointmentInfo: List[generic.AppointmentInfo] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(...)


class Modification(_Scheduling):

    AppointmentInfo: List[generic.AppointmentInfo] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(...)


class New(_Scheduling):

    AppointmentInfo: List[generic.AppointmentInfo] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(...)


class NoShow(_Scheduling):

    AppointmentInfo: List[generic.AppointmentInfo] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(...)


class PushSlots(_Scheduling):

    Meta: generic.Meta = Field(...)
    Slots: List[generic.Slot] = Field(...)


class Reschedule(_Scheduling):

    AppointmentInfo: List[generic.AppointmentInfo] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Visit: generic.Visit = Field(...)
