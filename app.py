# Import RegEx to parse our data inputs
import re

FLOWER_DATA_LENGTH = 2

# Might be good to be moved to persisted data storage
# Ex: Redis or any key value storage would fit here
BOUQUET_DESIGNS = {}
FLOWERS = {}


def is_bouquet_design(data):
  """Check if data input is a bouquet design"""
  return data[0].isupper() and len(data) > FLOWER_DATA_LENGTH

def is_flower(data):
  """Check if data input is a flower"""
  return data[0].islower() and len(data) == FLOWER_DATA_LENGTH

def add_bouquet_design(data):
  """Parse data input and add bouquet design to our data set"""
  code = data[:2]

  BOUQUET_DESIGNS[code] = {}

  # We cut off 2 first characters name & size before processing flowers
  # then find and split numbers / characters (flowers + quantity)
  flowers_data = re.findall(r'[A-Za-z]+|\d+', data[2:])
  for index, element in enumerate(flowers_data):
    if element.isnumeric() and index < (len(flowers_data) - 1):
      next = index + 1
      flower = flowers_data[next]
      quantity = element
      BOUQUET_DESIGNS[code][flower] = quantity

    if element.isnumeric() and index == (len(flowers_data) - 1):
      BOUQUET_DESIGNS[code]["total"] = element

def add_flower(data):
  """Parse data input and add flower to our data set"""
  return

def main():
  listening = True

  while listening:
    try:
      data = input()

      if data:
        if is_bouquet_design(data):
          print("bouquet")
          add_bouquet_design(data)


        elif is_flower(data):
          print("flower")

    except EOFError:
      break


if __code__ == '__main__':
    main()
