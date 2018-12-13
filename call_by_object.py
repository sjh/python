#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

""" From first entry of https://github.com/taizilongxu/interview_python.
     Conditional call by object in python.
     Add id() function to illustrate if we are refering to the same or different objects in action.

     This is to show that Python is using pass by object with different behaviours for mutable or immutable
     parameters, which is different from call by value or call by reference.
"""


def call_by_object_immutable(a):
    """ immutale example of integer argument.
         Python creates new immutable object in function namespace.
    """

    a = 2
    print("a in function id = {}".format(id(a)))
    return id(a)


def call_by_object_mutable(a):
    """ http://effbot.org/zone/call-by-object.htm mutale example of list argument. """

    a.append(2)
    print("a in function id = {}".format(id(a)))
    return id(a)


def test_conditional_call_by_object():
    """ Test function to assert immutable and mutable parameters. """

    immu_a = 1
    id_of_a = id(immu_a)
    print("before calling immu_a = {}, id = {}".format(immu_a, id(immu_a)))
    assert id_of_a != call_by_object_immutable(immu_a)
    print("after calling immu_a = {}, id = {}".format(immu_a, id(immu_a)))

    mu_a = [1, 2, 3]
    print("before calling mu_a = {}, id = {}".format(mu_a, id(mu_a)))
    assert id(mu_a) == call_by_object_mutable(mu_a)
    print("after calling mu_a = {}, id = {}".format(mu_a, id(mu_a)))


if __name__ == "__main__":
    test_conditional_call_by_object()
