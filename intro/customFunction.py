def greet(lang) :
  if lang == 'es' :
    return "Hola"
  elif lang == 'fr' :
    return 'Bonjour'
  else :
    return "Hello"
  
print(greet('en'), 'Steve')
print(greet('es'), 'Andrea')
print(greet('fr'), 'Lilu')