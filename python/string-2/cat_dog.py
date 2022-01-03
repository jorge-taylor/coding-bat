def cat_dog(str):
  cats = 0
  dogs = 0
  for i in range(len(str)-2):
    if str[i:i+3] == "cat":
      cats += 1
    elif str[i:i+3] == "dog":
      dogs += 1
  if cats == dogs:
    return True
  else:
    return False
