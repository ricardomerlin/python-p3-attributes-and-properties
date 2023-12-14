#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Joe", job = "Admin" ):
        self.name = name
        if job not in APPROVED_JOBS:
            print('Job must be in list of approved jobs.')
        else:
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 < len(name) < 25:
            poo = name.title()
            self._name = poo
        else:
            print('Name must be string between 1 and 25 characters.')