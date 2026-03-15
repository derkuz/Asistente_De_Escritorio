import sys
import pdb
import os
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QMenu
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QAction, QRegion

class AsistenteWindow(QWidget):
    """
    La ventana principal de nuestro Asistente de Escritorio (Desktop Pet).
    """
    def __init__(self):
        super().__init__()

        # --- CONFIGURACIÓN DE LA VENTANA ---
        self.setWindowTitle("Asistente de Escritorio")
        self.setGeometry(100, 100, 300, 300)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color:rgba(100, 150, 255, 180);")

        self.offset = QPoint() # Para almacenar el desplazamiento del ratón al arrastrar

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.position().toPoint() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = QPoint()

    def contextMenuEvent(self, event):
        """
        Este evento se activa al hacer clic derecho en la ventana.
        Aquí creamos y mostramos nuestro menú de posicionamiento.
        """
        menu = QMenu(self)
        
        # Crear las 4 acciones para el menú
        action_tl = QAction("Anclar a la Esquina Superior Izquierda", self)
        action_tr = QAction("Anclar a la Esquina Superior Derecha", self)
        action_bl = QAction("Anclar a la Esquina Inferior Izquierda", self)
        action_br = QAction("Anclar a la Esquina Inferior Derecha", self)

        # Conectar cada acción a su respectiva función
        action_tl.triggered.connect(self.snap_to_top_left)
        action_tr.triggered.connect(self.snap_to_top_right)
        action_bl.triggered.connect(self.snap_to_bottom_left)
        action_br.triggered.connect(self.snap_to_bottom_right)

        # Añadir las acciones al menú
        menu.addAction(action_tl)
        menu.addAction(action_tr)
        menu.addAction(action_bl)
        menu.addAction(action_br)

        # Mostrar el menú en la posición del cursor
        menu.exec(event.globalPos())

    def snap_window(self, x_func, y_func):
        """Función genérica para mover la ventana."""
        # --- ¡AQUÍ NOS DETENDREMOS A INVESTIGAR! ---
        # pdb.set_trace() # Comentado para depuración automática

        screen_rect = QApplication.primaryScreen().geometry()
        window_rect = self.frameGeometry()
        target_point = QPoint(x_func(screen_rect, window_rect), y_func(screen_rect, window_rect))

        print(f"screen_rect: {screen_rect}")
        print(f"window_rect: {window_rect}")
        print(f"target_point: {target_point}")

        # Intentar mover con xdotool
        try:
            # winId() devuelve el ID de ventana nativo, que en Xwayland debería ser el ID X11.
            window_id = str(self.winId())
            command = ['xdotool', 'windowmove', window_id, str(target_point.x()), str(target_point.y())]
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Ventana movida con xdotool: {' '.join(command)}")
        except Exception as e:
            print(f"Error al mover con xdotool: {e}. Fallback a PySide6.")
            self.windowHandle().setPosition(target_point)
            self.update() # Asegurarse de que se actualice visualmente

    def snap_to_top_left(self):
        self.snap_window(lambda s, w: s.left(), lambda s, w: s.top())

    def snap_to_top_right(self):
        self.snap_window(lambda s, w: s.right() - w.width(), lambda s, w: s.top())

    def snap_to_bottom_left(self):
        self.snap_window(lambda s, w: s.left(), lambda s, w: s.bottom() - w.height())

    def snap_to_bottom_right(self):
        self.snap_window(lambda s, w: s.right() - w.width(), lambda s, w: s.bottom() - w.height())

    def resizeEvent(self, event):
        """Define la forma circular de la ventana."""
        # Aplicar la máscara solo si la ventana no tiene marco.
        # Si tiene marco, el setMask puede causar problemas visuales.
        if self.windowFlags() & Qt.FramelessWindowHint: # Asegurarse de que esta condición sea verdadera.
            mask = QRegion(self.rect(), QRegion.Ellipse)
            self.setMask(mask)


def main():
    """Función principal que inicializa y ejecuta la aplicación."""
    app = QApplication(sys.argv)
    window = AsistenteWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


