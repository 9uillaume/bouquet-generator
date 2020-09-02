# Import RegEx to parse our data inputs
import re

FLOWER_DATA_LENGTH = 2

# Might be good to be moved to persisted data storage
# Ex: Redis or any key value storage would fit here

# Bouquet design object payload:
# <code (name + size)>: {
#   <flower N>: <quantity>, 
#   ..., 
#   <extra>: <quantity>
# }
BOUQUET_DESIGNS = {}

# Flower object payload:
# <code (name + size)>: <quantity>
FLOWERS = {}

BOUQUETS = []


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

  # We want to save how many extra flowers to reach total flowers
  base_design_quantity = 0

  # We cut off 2 first characters name & size before processing flowers
  # then find and split numbers / characters (flowers + quantity)
  flowers_data = re.findall(r'[A-Za-z]+|\d+', data[2:])
  for index, element in enumerate(flowers_data):
    if element.isnumeric() and index < (len(flowers_data) - 1):
      next = index + 1
      flower = flowers_data[next]
      quantity = int(element)
      base_design_quantity += quantity
      BOUQUET_DESIGNS[code][flower] = quantity

    if element.isnumeric() and index == (len(flowers_data) - 1):
      total = int(element)
      # Extra flowers to reach total flowers
      BOUQUET_DESIGNS[code]["extra"] = total - base_design_quantity


def add_flower(data):
  """Parse data input and add flower to our data set"""
  if data in FLOWERS:
    FLOWERS[data] += 1
  else:
    FLOWERS[data] = 1


def get_extra_flowers(size, extra):
  "Get extra flowers to complete a bouquet and reach total"
  global FLOWERS
  new_flowers = FLOWERS.copy()
  bouquet_extra = {}
  extra_added = 0

  for i in range(0, extra):
    for flower in new_flowers:
        flower_size = flower[1]
        flower_name = flower[0]
        quantity = new_flowers[flower]
        if flower_size == size and quantity >= extra and extra != 0:
          if bouquet_extra.get(flower_name):
            # print(f"yes {bouquet_extra[flower_name]}")
            bouquet_extra[flower_name] += 1
            new_flowers[flower] -= 1
            extra -= 1
          else:
            bouquet_extra[flower_name] = 1
            new_flowers[flower] -= 1
            extra -= 1

  FLOWERS = new_flowers.copy()
  return bouquet_extra


def get_bouquet_intent(size, bouquet_design):
  """Check if we have enough resources to create a bouquet and intent for it"""
  global FLOWERS
  new_flowers = FLOWERS.copy()
  # print(f"flw {FLOWERS}")
  # print(f"new {new_flowers}")
  bouquet_intent = {}

  for element in bouquet_design:
    # If not extra key, it's a flower
    if element != "extra":
      flower = element
      quantity = bouquet_design[element]

      wanted_flower = flower + size
      if new_flowers.get(wanted_flower):
        available_quantity = new_flowers[wanted_flower]
        if available_quantity >= quantity:
          # print("Proceed")
          new_flowers[wanted_flower] -= quantity
          bouquet_intent[flower] = quantity

        # Not enough flowers available => cancel intent
        else:
          return False
      # Not this flower in stock => cancel intent
      else:
        return False

  FLOWERS = new_flowers.copy()
  return bouquet_intent


def output_bouquet(code, bouquet_intent, bouquet_extra):
  """Display created bouquet on stdout and save it"""
  bouquet = str(code)
  size = code[0]
  for flower in bouquet_intent:
    quantity = bouquet_intent[flower]
    bouquet += str(quantity) + flower
  for extra_flower in bouquet_extra:
    extra_quantity = bouquet_extra[extra_flower]
    bouquet += str(extra_quantity) + extra_flower
  BOUQUETS.append(bouquet)
  print(bouquet)


def create_bouquet():
  """"Process of creating a bouquet from design"""
  if BOUQUET_DESIGNS:
    for code in BOUQUET_DESIGNS:
      size = code[1]
      bouquet_design = BOUQUET_DESIGNS[code]

      bouquet_intent = get_bouquet_intent(size, bouquet_design)
      if bouquet_intent:
        bouquet_extra = get_extra_flowers(size, bouquet_design['extra'])
        output_bouquet(code, bouquet_intent, bouquet_extra)


def main():
  listening = True

  while listening:
    try:
      data = input()

      if data:
        if is_bouquet_design(data):
          add_bouquet_design(data)

        elif is_flower(data):
          add_flower(data)

        create_bouquet()

    except EOFError:
      break


if __name__ == '__main__':
    main()
