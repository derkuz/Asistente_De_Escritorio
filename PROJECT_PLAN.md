# Asistente Pedagógico de Escritorio - Plan de Proyecto

**Versión:** 1.0
**Fecha:** 15 de marzo de 2026
**Project Manager:** Gemini Assistant

---

## 1. Resumen Ejecutivo 📜

Este documento define el plan de desarrollo para un asistente de escritorio interactivo ("Desktop Pet"). Su objetivo principal es actuar como un tutor de programación para estudiantes, ofreciendo soporte pedagógico mediante el análisis visual de la pantalla y la interacción con sistemas de IA. El asistente operará de forma transparente en el escritorio del usuario (Kubuntu), proporcionando ayuda en tiempo real sobre código y conceptos de programación.

---

## 2. Objetivos del Proyecto 🎯

### 2.1. Objetivo Principal
Crear un asistente de escritorio interactivo que brinde soporte pedagógico en programación mediante el análisis visual de la pantalla del usuario.

### 2.2. Objetivos Específicos
*   **Interfaz Gráfica:** Implementar una interfaz gráfica animada, transparente y no intrusiva en Kubuntu.
*   **Análisis Inteligente:** Integrar una IA multimodal (Gemini) para analizar capturas de pantalla y texto, y así explicar errores o lógica de programación.
*   **Resiliencia Offline:** Asegurar la continuidad del servicio mediante una IA local (Ollama) que se activa automáticamente ante la pérdida de conexión a internet.
*   **Experiencia de Usuario:** Diseñar una interacción fluida y amigable que fomente el aprendizaje y no interrumpa el flujo de trabajo del desarrollador.

---

## 3. Alcance del Proyecto 🗺️

### 3.1. Dentro del Alcance (In-Scope)
*   Desarrollo de dos personajes (Maid y Mayordomo) con 4 estados de animación definidos.
*   Funcionalidad de captura de pantalla activada por el usuario.
*   Integración con la API de Gemini para el análisis online.
*   Integración con Ollama para el análisis offline.
*   Sistema de detección de conectividad y switch automático entre proveedores de IA.
*   Visualización de las respuestas de la IA en la interfaz del asistente.

### 3.2. Fuera del Alcance (Out-of-Scope) para la v1.0
*   Creación de nuevas animaciones o personajes más allá de los definidos.
*   Soporte para sistemas operativos diferentes a Kubuntu.
*   Interacción por voz.
*   Capacidad de escribir o modificar código directamente en el IDE del usuario.

---

## 4. Requerimientos del Sistema ✅

### 4.1. Requerimientos Funcionales (RF)
| ID  | Requerimiento           | Descripción                                                                                                    |
|-----|-------------------------|----------------------------------------------------------------------------------------------------------------|
| RF-01 | Interfaz Animada        | El asistente mostrará los siguientes estados: Inactivo (saltando cuerda), Pensando (procesando), Hablando y Durmiendo (reposo). |
| RF-02 | Captura de Pantalla     | El usuario podrá solicitar ayuda, momento en el cual el sistema tomará una captura de pantalla del IDE activo.    |
| RF-03 | Análisis con IA         | La IA procesará la imagen y/o texto proporcionado para dar una explicación, sugerencia o resolver una duda.    |
| RF-04 | Modo Offline            | El sistema detectará la pérdida de conexión a internet, notificará al usuario y cambiará al proveedor de IA local (Ollama). |
| RF-05 | Modalidades de Respuesta| La respuesta de la IA se presentará en la interfaz del asistente, pudiendo incluir: texto (bocadillo de diálogo), foco visual (resaltar área en la captura) y sugerencias de código (bloque de código con opción de copia). |

### 4.2. Requerimientos No Funcionales (RNF)
| ID  | Requerimiento      | Descripción                                                                                                             |
|-----|--------------------|-------------------------------------------------------------------------------------------------------------------------|
| RNF-01| Arquitectura       | El sistema se basará en el patrón MVC (Modelo-Vista-Controlador). Se usará el patrón Estrategia para gestionar los proveedores de IA (Gemini, Ollama). |
| RNF-02| Rendimiento        | El consumo de CPU y RAM en estado inactivo o de reposo debe ser mínimo para no interferir con las tareas de desarrollo. |
| RNF-03| Plataforma         | La aplicación será desarrollada y probada para Kubuntu Linux con entorno de escritorio KDE Plasma.                      |
| RNF-04| Estilo Visual      | La interfaz será transparente y sin bordes, integrándose de forma natural en el escritorio.                             |

---

## 5. Activos y Diseño 🎨

### 5.1. Sprite Sheets
Se utilizarán dos hojas de sprites (Sprite Sheets) para los personajes de estilo anime (Maid, Mayordomo).

### 5.2. Animaciones Técnicas
1.  **Inactividad (Idle):** Ciclo de animación del personaje saltando a la cuerda.
2.  **Procesamiento (Thinking):** Pose estática o animación sutil con expresión de concentración (brazos cruzados).
3.  **Respuesta (Talking):** Animación de hablar, sincronizada con la aparición del texto de respuesta.
4.  **Reposo (Sleeping):** Animación del personaje durmiendo.

---

## 6. Plan de Desarrollo por Fases (Propuesta) 🚀

*   **Fase 1: Estructura y UI Base**
    *   [ ] Configurar el entorno de desarrollo.
    *   [ ] Crear la ventana principal transparente y sin bordes.
    *   [ ] Implementar el ciclo de animación básico (cargar sprite sheet y mostrar animación de inactividad).
    *   [ ] Definir la arquitectura MVC y el patrón Estrategia.

*   **Fase 2: Funcionalidad Central**
    *   [ ] Implementar la función de captura de pantalla.
    *   [ ] Crear la interfaz para que el usuario pueda introducir texto/preguntas.
    *   [ ] Implementar el cambio entre los diferentes estados de animación (idle, thinking, etc.).

*   **Fase 3: Integración IA Online**
    *   [ ] Desarrollar el conector para la API de Gemini (Estrategia A).
    *   [ ] Enviar la captura de pantalla y el texto a Gemini.
    *   [ ] Implementar la visualización de la respuesta en la UI (bocadillo de texto).

*   **Fase 4: Resiliencia y Modo Offline**
    *   [ ] Desarrollar el conector para Ollama (Estrategia B).
    *   [ ] Implementar el servicio de detección de conectividad.
    *   [ ] Orquestar el cambio automático entre la Estrategia A y B.
    *   [ ] Añadir notificación al usuario sobre el cambio de modo.

*   **Fase 5: Refinamiento y Entrega**
    *   [ ] Implementar las modalidades de respuesta avanzadas (foco visual, sugerencia de código).
    *   [ ] Optimizar el rendimiento.
    *   [ ] Realizar pruebas de usuario y empaquetar la aplicación.

---

## 7. Pila Tecnológica (Stack) 💻

| Componente              | Tecnología (Python)           | Justificación                                                                                                                              |
|-------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **Framework de GUI**    | `PySide6`                     | Es el binding oficial de Qt para Python. Ideal para Kubuntu, ya que KDE Plasma usa Qt. Garantiza integración nativa, y facilita la creación de ventanas transparentes y animaciones. |
| **Captura de Pantalla** | `mss`                         | Una librería rápida y multiplataforma para tomar capturas de pantalla, superior en rendimiento a otras alternativas para esta tarea específica. |
| **Cliente API Gemini**  | `google-generativeai`         | El SDK oficial de Google para interactuar con la API de Gemini. Simplifica la autenticación y el envío de datos multimodales (imagen y texto). |
| **Cliente API Ollama**  | `ollama`                      | La librería oficial de Python para Ollama. Abstrae las llamadas a la API local, haciendo la integración más limpia y sencilla.             |
| **Peticiones HTTP**     | `requests`                    | Se usará como respaldo o para comprobaciones de conectividad. Es el estándar de facto en Python para realizar peticiones HTTP.              |
| **Manejo de Imágenes**  | `Pillow` (PIL Fork)           | Necesaria para procesar, guardar y manipular las capturas de pantalla antes de enviarlas a las APIs.                                       |
| **Empaquetado**         | `PyInstaller` (a considerar)  | Al final del desarrollo, se puede usar para empaquetar la aplicación en un solo ejecutable, facilitando su distribución e instalación.      |
