#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from handler.base import BaseHandler, route


@route('/')
class Index(BaseHandler):
    def get(self):
        self.render()


@route('/introduction')
class Introduction(BaseHandler):
    def get(self):
        self.render()


@route('/notice')
class Notice(BaseHandler):
    def get(self):
        self.render()


@route('/course')
class Course(BaseHandler):
    def get(self):
        self.render()


@route('/contact')
class Contact(BaseHandler):
    def get(self):
        self.render()


@route('/teacher')
class Teacher(BaseHandler):
    def get(self):
        self.render()
