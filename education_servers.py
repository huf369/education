# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.escape
import models.grade
import models.exam
from utils.strutil import strutil
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ExamHandler(tornado.web.RequestHandler):
    def post(self):
        if strutil.is_json(self.request.body):
            data = json.loads(self.request.body)
            models.exam.exam.generateResult(data)
            self.write('')
    def get(self):
        if strutil.is_json(self.request.body):
            data = json.loads(self.request.body)
            print(data)
        values = models.exam.exam.getAllRecord()
        self.write(json.dumps(values,ensure_ascii=False))

class ExamResultHandler(tornado.web.RequestHandler):
    def get(self):
        values = models.exam.exam.getExamResult()
        self.write(json.dumps(values,ensure_ascii=False))

class GetCourseHandler(tornado.web.RequestHandler):
    def get(self):
        values = models.grade.grade.getAllRecord()
        # self.write(tornado.escape.json_encode(values))
        self.write(json.dumps(values,ensure_ascii=False))

class GetGradeHandler(tornado.web.RequestHandler):
    def get(self):
        values = models.grade.grade.getAllRecord()
        # self.write(tornado.escape.json_encode(values))
        self.write(json.dumps(values,ensure_ascii=False))

Handlers=[
    (r"/", MainHandler),
    (r"/exam", ExamHandler),
    (r"/examresult", ExamResultHandler),
    (r"/courses", GetCourseHandler),
    (r"/grades", GetGradeHandler),
]
application = tornado.web.Application(Handlers)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()