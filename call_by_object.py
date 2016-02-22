#!/usr/bin/env python
# _*_ coding: utf-8 _*_

u""" From first entry of https://github.com/taizilongxu/interview_python.
     Conditional call by object in python.
     Add id() function to illustrate if we are refering to the same or different objects in action.

     This is to show that Python is using pass by object with different behaviours for mutable or immutable
     parameters, which is different from call by value or call by reference.
"""


def call_by_object_immutable(a):
    u""" immutale example of integer argument.
         Python creates new immutable object in function namespace.
    """
    a = 2
    print "a in function id = {}".format(id(a))


def call_by_object_mutable(a):
    u""" http://effbot.org/zone/call-by-object.htm mutale example of list argument. """
    a.append(2)
    print "a in function id = {}".format(id(a))


if __name__ == "__main__":
    immu_a = 1
    print "before calling immu_a = {}, id = {}".format(immu_a, id(immu_a))
    call_by_object_immutable(immu_a)
    print "after calling immu_a = {}, id = {}".format(immu_a, id(immu_a))

    mu_a = [1, 2, 3]
    print "before calling mu_a = {}, id = {}".format(mu_a, id(mu_a))
    call_by_object_mutable(mu_a)
    print "after calling mu_a = {}, id = {}".format(mu_a, id(mu_a))
