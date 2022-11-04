#!/usr/bin/python 
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TLogin(Base):
    __tablename__ = 't_login'

    id = Column(BIGINT(20), primary_key=True, comment='主键')
    user_gid = Column(String(64), index=True, comment='用户唯一标识')
    user_name = Column(String(64), index=True, comment='登录名')
    user_password = Column(String(64), comment='登陆密码')
    source_channel = Column(String(64), comment='注册渠道')
    source_type = Column(String(2), comment='注册类型：00-经销商')
    x_id = Column(String(128))
    raw_add_time = Column(TIMESTAMP, comment='添加数据的数据')
    raw_update_time = Column(TIMESTAMP)




