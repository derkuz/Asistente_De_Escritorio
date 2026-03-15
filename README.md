# Asistente Pedagógico de Escritorio

Este proyecto es un "Desktop Pet" o asistente de escritorio interactivo, diseñado para actuar como un tutor de programación. Utiliza inteligencia artificial para analizar la pantalla del usuario y ofrecer ayuda pedagógica sobre el código.

---

## 🚀 Puesta en Marcha para Desarrolladores

Sigue estos pasos para configurar tu entorno de desarrollo local.

### Prerrequisitos

*   [Python 3.10+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads/)
*   **xdotool**: Necesario para el movimiento programático de la ventana en entornos Wayland como KDE Plasma.
    *   En **Arch Linux / CachyOS**:
        ```bash
        sudo pacman -S xdotool
        ```
*   (Opcional pero recomendado) [GitHub CLI](https://cli.github.com/)

### Pasos de Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/derkuz/Asistente_De_Escritorio.git
    cd Asistente_De_Escritorio
    ```

2.  **Crea un entorno virtual:**
    ```bash
    python3 -m venv .venv
    ```

3.  **Activa el entorno virtual:**
    *   En **Linux/macOS**:
        ```bash
        source .venv/bin/activate
        ```
    *   En **Windows (Git Bash/PowerShell)**:
        ```bash
        . .venv/Scripts/activate
        ```

4.  **Instala las dependencias:**
    Una vez activado el entorno, instala todas las librerías necesarias con un solo comando.
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Cómo Ejecutar la Aplicación

Una vez que la configuración esté completa, podrás ejecutar la aplicación con el siguiente comando:

```bash
# (Asegúrate de que tu entorno virtual esté activado)
# Para Wayland (ej. KDE Plasma), es necesario ejecutar con Xwayland para el movimiento de la ventana:
QT_QPA_PLATFORM=xcb python main.py
# Para entornos X11, o si QT_QPA_PLATFORM=xcb no es necesario:
# python main.py
```
*(Nota: El archivo `main.py` será el punto de entrada principal que crearemos).*

---

## 📚 Documentación del Proyecto

Para entender la visión, arquitectura y decisiones tecnológicas, consulta los siguientes documentos:

*   `PROJECT_PLAN.md`: La hoja de ruta completa del proyecto, objetivos y fases.
*   `tecnologias.md`: Una guía de introducción a PySide6 y cómo se utiliza en este proyecto.
