#!/usr/bin/python 
# -*- coding: utf-8 -*-
from enum import unique, Enum


@unique
class ContentTypeEnum(Enum):
	APPLICATION_JSON_UTF_8 = "application/json; charset=UTF-8"
	TEXT_XML_UTF_8 = "text/xml; charset=UTF-8"
	TEXT_PLAIN_UTF_8 = "text/plain; charset=UTF-8"
	APPLICATION_FORM_URLENCODED_UTF_8 = "application/x-www-form-urlencoded; charset=UTF-8"
	MULTIPART_FORM_DATA = "multipart/form-data; charset=UTF-8"