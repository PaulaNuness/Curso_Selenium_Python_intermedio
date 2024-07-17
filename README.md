# Curso_Selenium_Python_intermedio
* Curso hecho en la plataforma OpenWebinars

****************************************************************************************************************
## [PDF_POM](https://github.com/PaulaNuness/Curso_Selenium_Python_intermedio/blob/main/POM.pdf)

****************************************************************************************************************
## BDD
¿Qué es el BDD?
 
BDD, siglas de “Behavior Driven Development” (Desarrollo guiado por comportamiento), hace referencia a un proceso de desarrollo donde se busca la integración entre la parte técnica y la de negocio. Podemos verlo como una filosofía de desarrollo donde las pruebas se enfocan en flujos pequeños pero donde entran en juego varias partes de un sistema para llegar a un fin.

Si venimos del TDD, “Test Driven Development”, donde tratamos de desarrollar en base a unas pruebas básicas del software (como podrían ser pruebas unitarias), el BDD sería el siguiente escalón. Una capa por encima que abarca más que una prueba unitaria y que, además, involucra al equipo de negocio para expresar, mediante un lenguaje cercano al humano (Gherkin), la descripción de las pruebas que se deben realizar en la aplicación.

Puede que de primeras sea complicado de entender, pero a medida que se va desarrollando toma más sentido.

Para empezar basémonos en el lenguaje que hemos mencionado, Gherkin. Este lenguaje es común para los frameworks BDD que se aplican en distintos lenguajes como pueden ser Behave para el caso de Python, o Cucumber para el caso de Java (por ejemplo).

Partimos de la premisa de que disponemos de una serie de palabras clave que disponen una serie de acciones concretas. A saber:

Given -> Dada una situación inicial.

When -> Realización cierta acción.

Then -> Obtenemos un resultado concreto.

Para ser más concretos, vamos a suponer una situación hipotética donde tenemos una aplicación web donde nos logamos, pulsamos el botón de salir y comprobamos que se muestra un mensaje de despedida.

Esta situación se conocería como un escenario (Scenario). Si supusiésemos otra situación donde, por ejemplo, introdujésemos unas credenciales incorrectas y pulsásemos el botón login, y entonces obtendríamos un mensaje de error, esto sería otro “Scenario“.

El conjunto de escenarios relacionados entre sí para una funcionalidad en concreto de la aplicación, como podría en este caso ser la pantalla de login, se conoce como “Feature“ y se disponen en ficheros *.feature.

Así pues, un ejemplo práctico de lo anteriormente mencionado sería:

Feature: Pantalla de login
Se efectúan diversas pruebas para comprobar que el módulo de login funciona correctamente.

Scenario: El mensaje de logout aparece correctamente
      Given Estamos logados en la aplicación correctamente
      When Pulsamos el botón logout
      Then El sistema nos desloga y muestra un mensaje de despedida

Scenario: Al introducir credenciales incorrectas, el sistema muestra un mensaje de error
      Given Se introducen credenciales de usuario y contraseña incorrectas
      When Pulsamos el botón Login
      Then El sistema muestra un mensaje de error
No obstante, el presente curso sólo pretende dar unas pinceladas superficiales para comprender esta metodología de trabajo.

Si estáis interesados en saber más sobre el BDD, OpenWebinars dispone de un curso para ello en la siguiente URL:

URL del curso: https://openwebinars.net/academia/portada/testing-bdd/
Instalación de Behave y estructura de carpetas
Para instalar Behave, podemos ayudarnos de la herramienta Pip que nos provee Python:

$ pip install behave

Tras esto ya podremos importar la librería en nuestro script.

El objetivo de utilizar Behave es describir las pruebas de una manera más cercana al lenguaje humano. Pero a la hora de desarrollar las pruebas, hemos de establecer una relación entre dicha descripción y los métodos del código para que Selenium pueda interpretar nuestras acciones.

Si ya mencionamos que los ficheros .feature contienen la descripción de las pruebas, tendremos otros ficheros .py donde se describirán los pasos (steps) que actuarán de enlace entre la sentencia del scenario y la acción lógica de Selenium. Por ejemplo, si en el feature encontramos “When Pulsamos el botón logout“, en el fichero de steps encontraremos una función parecida a:

@when(u'Pulsamos el botón logout")
def pulsar_boton_logout(context):
      driver.find_element(boton_logout_locator).click()
De forma que cuando Behave llame a esa “frase” del feature, automáticamente se enlazará con esa función y ejecutará las sentencias de su interior.

Ahora bien, estos pasos pueden funcionar correctamente o no. Es decir, podemos tratar de hacer click sobre el botón, pero esta acción puede llevarse a cabo correctamente o derivar en un error.

Para este fin se utiliza lo que se conoce como “asserts“ (aserciones), donde se evalúa un dato que previamente proveemos (como por ejemplo un texto en pantalla que reza “accediendo a la página”), frente a una captura del elemento que debería estar mostrándolo. Siendo más prácticos, si sabemos que cuando pulsamos el botón login y va todo bien, aparece un elemento tipo “span“ con el texto “accediendo“ en su interior, nuestra aserción será algo similar a:

span_text = driver.find_element(span_element).text
assert "accediendo" == span_text
De forma que si el span_text contiene cualquier otro texto que no sea “accediendo”, o la ejecución falla, la prueba devolverá error. Pero si el elemento span contiene el string “accediendo”, la aserción devolverá True y por tanto este paso del escenario será satisfactorio.

* Pulsar - [BDD](https://github.com/PaulaNuness/Curso_Selenium_Python_intermedio/blob/main/Captura%20de%20pantalla%202024-07-17%20204222.png)

* Paos para instalar Behave en Python
  * no terminal en Visual Studio Code escribir: pip install behave
  * despues escribir: python.exe -m pip install --upgrade pip
* Estructura del proyecto:
  * crear carpeta features
  * dentro de la carpeta features, crear el archivo ejemplo.feature
  * y tambien dentro de la carpeta feature crear la carpeta spets
  * dentro de la carpeta steps, crear el archivo pasos.py
****************************************************************************************************************
