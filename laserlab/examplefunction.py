""" This is an example module for testing github actions"""
import numpy as np

def add(x,y):
  """ simple adder
  args:
    x: first value
    y: second value
  return:
    sum of both inputs
  """
  return x+y

def test_add():
  """ unit test for add function"""
  assert add(1,1) == 2
