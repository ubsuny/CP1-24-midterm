"""
This module converts lengths in yards or feet to meters.
"""

def unit_converter(val, unit):
  """
  Takes in lengths in yards or feet and converts to meters.

  Parameters:
      val (float): magnitude of the length.
      unit (str): unit of length ('ft' or 'yd').

  Returns:
      float: Length converted to meters.
  """
  if unit == 'ft':
    val = val * 0.3048  # From Google Unit Converter
    return val
  elif unit == 'yd':
    val = val * 0.9144  # From Google Unit Converter
    return val
  else:
    raise ValueError("Only 'ft' or 'yd' please.")
