# Guía Rápida de PySide6 para el Asistente de Escritorio

Este documento está dirigido a los desarrolladores del proyecto "Asistente Pedagógico de Escritorio" y sirve como una introducción conceptual a PySide6, el framework de GUI que hemos elegido. El objetivo no es ser un tutorial exhaustivo, sino explicar **cómo** aplicaremos sus características clave para cumplir con los requisitos de nuestro proyecto.

---

## ¿Qué es PySide6 y por qué lo usamos?

PySide6 es un conjunto de "bindings" de Python para el framework **Qt**. Qt es un conjunto de herramientas multiplataforma muy potente y maduro para crear interfaces gráficas.

**Razón de la elección:** Lo elegimos porque nuestro objetivo es Kubuntu, cuyo entorno de escritorio (KDE Plasma) está construido sobre Qt. Esto nos da una **integración visual perfecta** y acceso directo a las funcionalidades que necesitamos, como la transparencia y la gestión de ventanas.

---

## Conceptos Clave para Nuestro Proyecto

### 1. La Estructura Base: `QApplication` y `QWidget`

Todo programa en PySide6 tiene dos componentes fundamentales:

-   `QApplication`: Es el corazón de la aplicación. Solo puede haber **una** instancia. Gestiona el bucle de eventos (ver más abajo), el portapapeles, los estilos, etc. Se inicializa al principio y se ejecuta al final.
-   `QWidget`: Es la clase base para **todo** lo que se ve en pantalla: ventanas, botones, etiquetas, etc. Nuestra ventana principal del "Desktop Pet" será una clase que **herede** de `QWidget`.

```python
# Pseudo-código de la estructura principal
import sys
from PySide6.QtWidgets import QApplication, QWidget

# 1. Creamos nuestra clase para la ventana principal
class AsistenteWindow(QWidget):
    def __init__(self):
        super().__init__()
        # ... aquí configuraremos la ventana

# 2. El punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv) # Solo una instancia
    window = AsistenteWindow()
    window.show()
    sys.exit(app.exec()) # Inicia el bucle de eventos
```

### 2. La Magia Visual: Ventanas Transparentes y Sin Bordes

Este es un requisito crítico (RNF-04). PySide6 lo hace sorprendentemente sencillo usando "flags" y "atributos" de la ventana. Dentro del `__init__` de nuestra `AsistenteWindow`, añadiremos:

-   `setWindowFlag(Qt.FramelessWindowHint)`: Esto le dice al sistema operativo que no dibuje la barra de título, los bordes, ni los botones de minimizar/maximizar/cerrar.
-   `setAttribute(Qt.WA_TranslucentBackground)`: Esto permite que la ventana tenga un fondo transparente. Las partes del widget donde no dibujemos nada serán completamente invisibles, dejando ver el escritorio.

### 3. El Corazón: El Bucle de Eventos y los "Signals & Slots"

Una aplicación de GUI no se ejecuta de arriba a abajo como un script. Se queda esperando a que ocurran "eventos". El `app.exec()` inicia un **bucle infinito** que procesa eventos como:

-   El usuario mueve el ratón.
-   El usuario hace clic.
-   Un temporizador se dispara.
-   Llegan datos de la red.

Para reaccionar a estos eventos, Qt usa un mecanismo muy potente llamado **Signals y Slots**:
-   **Signal (Señal):** Es una notificación que un objeto emite cuando algo sucede. Ejemplo: un botón emite la señal `clicked()`.
-   **Slot (Ranura):** Es una función que se ejecuta cuando una señal es recibida.

**En nuestro proyecto:**
> Un `QTimer` emitirá una señal `timeout()` cada X milisegundos. Conectaremos esa señal a un *slot* (una función nuestra) que cambie la imagen del sprite para crear la animación.

### 4. Dando Vida al Personaje: Animación de Sprites

Tenemos dos enfoques principales, ambos viables:

1.  **Opción Sencilla (`QLabel` y `QMovie`):** Si nuestras animaciones son GIFs animados, podemos usar un `QLabel` y asignarle un `QMovie`. Es la forma más rápida de tener una animación en bucle. Ideal para la Fase 1.

2.  **Opción Avanzada (`QPainter`):** Para un control total (necesario para la física del salto de cuerda), sobreescribiremos el método `paintEvent(self, event)` de nuestro widget. Dentro de este método, usaremos un `QPainter` para dibujar una porción específica de nuestra hoja de sprites (sprite sheet) en las coordenadas que queramos. El `QTimer` que mencionamos antes se encargará de decirnos cuándo cambiar de frame y recalcular la posición.

### 5. Evitando Congelamientos: Tareas en Segundo Plano con `QThread`

**IMPORTANTE:** El bucle de eventos se ejecuta en un único hilo (el "hilo de la GUI"). Si realizamos una tarea larga en este hilo (como una llamada a la API de Gemini o Ollama), la aplicación entera **se congelará** hasta que la tarea termine.

**Solución:** Usaremos `QThread`. Moveremos el objeto que hace la llamada a la API a un hilo secundario.

**Flujo de trabajo:**
1.  La GUI (hilo principal) le dice al objeto del hilo secundario que empiece a trabajar (ej. "analiza esta imagen").
2.  El hilo secundario hace la llamada a la API (la GUI sigue respondiendo perfectamente).
3.  Cuando el hilo secundario recibe la respuesta de la API, emite una **señal** con los datos.
4.  La GUI (hilo principal) tiene un **slot** conectado a esa señal, recibe los datos y actualiza la interfaz de forma segura para mostrar la respuesta.
