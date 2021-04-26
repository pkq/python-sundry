def remove_list_item(*, list_name, item_name):

  new_list = [ item for item in list_name if item != item_name]
  return new_list
