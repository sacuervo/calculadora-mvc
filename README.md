# IberoCalc - Calculadora con Arquitectura MVC

## Descripción

**IberoCalc** es una aplicación de calculadora sencilla construida utilizando la arquitectura Modelo-Vista-Controlador (MVC) en Python, con el uso de la biblioteca `tkinter` para la interfaz gráfica. Este proyecto separa las responsabilidades en tres componentes principales: 

- **Modelo**: Se encarga de manejar la lógica de los cálculos.
- **Vista**: Gestiona la interfaz gráfica y la interacción con el usuario.
- **Controlador**: Coordina la comunicación entre el modelo y la vista.

La aplicación está diseñada para ser fácilmente extensible, mantenible y escalable, aprovechando las ventajas que ofrece la arquitectura MVC.

## Estructura del Proyecto

El proyecto consta de los siguientes archivos:

- **`model.py`**: Contiene la lógica de negocio y cálculos de la calculadora.
- **`view.py`**: Se encarga de la interfaz gráfica de usuario utilizando `tkinter`.
- **`controller.py`**: Actúa como intermediario entre el modelo y la vista, gestionando las acciones del usuario y actualizando la interfaz.

## Requisitos

Para ejecutar esta aplicación, necesitas:

- **Python 3.x**
- La biblioteca `tkinter` (incluida en la mayoría de las distribuciones estándar de Python)

## Instalación y Ejecución

1. Clona este repositorio o descarga los archivos.

2. Asegúrate de tener Python instalado en tu máquina. Si no lo tienes, puedes descargarlo desde [aquí](https://www.python.org/downloads/).

3. No necesitas instalar bibliotecas adicionales, ya que `tkinter` viene preinstalado con Python en la mayoría de los casos.

4. Ejecuta el archivo principal del proyecto:

   ```bash
   python controller.py

## Créditos

- Proyecto basado en la [serie tutorial](https://www.youtube.com/playlist?list=PLtv1tL_708PBwQAsx4543wc7chepu0qYY) de 'Life In Code'
