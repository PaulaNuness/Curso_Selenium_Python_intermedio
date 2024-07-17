# BDD(Behavior Driven Development) Desarrollo Guiado po Coportamento es un proceso de desarrollo de software
# Si en TDD buscamos la validación de una acción concreta, en BDD tratamos de abstraernos un poco más y validar un flujo mínimo concreto.
# ● Nos ofrece un lenguaje común (Gherkin) entre la parte de negocio y la parte técnica.
# ● Se ha de seguir siempre el ciclo Given-When-Then:
#   ○ Given: Dada una situación inicial
#   ○ When: Realizando una acción en concreto
#   ○ Then: Obtenemos un resultado esperado
# ● Para ahondar más en este tema tenéis disponible un curso en OpenWebinars relativo a esto:
#   ○ URL del curso: https://openwebinars.net/academia/portada/testing-bdd

############################################################################################

#EJEMPLO DE PRUEBA EN GHERKIN
 
# Feature: Comprobacion de login en pagina web
#    Scenario: Realizar Login exitosamente
#        Given Un usuario y password válidos
#        When Realizo login en el sistema
#        Then El sistema muestra mi cuenta de usuario

#    Scenario: Relaizar Login fallido
#        Given Un usuario y password inválidos
#        When Relaizo login en el sistema
#        Then El sistema muestra un mensaje de error

############################################################################################