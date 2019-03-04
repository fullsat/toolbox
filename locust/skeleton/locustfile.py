# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from locust import HttpLocust, TaskSet, task


class TaskSet(TaskSet):
#    def on_start(self):

    @task
    def index(self):
        self.client.get("/")


class Task(HttpLocust):
    task_set = TaskSet 
    min_wait = 0
    max_wait = 0
