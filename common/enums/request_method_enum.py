#!/usr/bin/python 
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class RequestMethodEnum(Enum):
	POST = "post"
	GET = "get"