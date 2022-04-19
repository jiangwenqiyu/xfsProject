# !/usr/bin/env python
# coding: utf-8

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import qtawesome as qta

# ==============================
# =           Button           =
# ==============================
"""

    TODO:
    - Hacer los botones primarios, secundarios, etc poniendo como default el custom         | Hecho
    - Soportar iconos en los botones y iconos con texto                                     | Hecho
    - Soportar largo, alto, ancho, top, rileft (right left) y asignar un tamaño default     | Hecho
    - El border-radius de los botones debe ser relativo (height / 2)                        | Hecho
    - Soportar fuentes personalizadas y tipo de letra bold, italic, underline, strikeout, 
    y antialiasing                                                                          | Hecho
    - Remover el focus                                                                      | Hecho
    - Soportar estilos CSS                                                                  | Hecho

    - Borrar el font-size de los estilos primary, secundary, success, etc.

"""
class Button(QPushButton):
    def __init__(self, parent=None, **kwargs):
      super(Button, self).__init__(parent=parent)
      self.setFocusPolicy(Qt.NoFocus)

      # -----------  Posicion y tamaño del boton  -----------
      """
        
         Primero verificar que el arreglo recibido contenga numeros si no es así mostrar en el boton
         el mensaje de error. De lo contrario establece la geometria del boton escrita por el usuario
         y si no se recibe el parametro "pos" entonces asignar el tamaño default.
        
      """
      if "pos" in kwargs:
        size = 0
        for key in kwargs['pos']:
          try:
            value = int(kwargs['pos'][key])

            # Valores por default
            rileft = top = 0
            width = 95
            height = 40

            # Si los valores recibidos son diferentes a los default modificarlos y establecerlos en geometry
            if 'rileft' in kwargs['pos']:rileft = kwargs['pos']['rileft']                    
            if 'top' in kwargs['pos']:top = kwargs['pos']['top']
            if 'width' in kwargs['pos']:width = kwargs['pos']['width']
            if 'height' in kwargs['pos']: height = kwargs['pos']['height']

            self.setGeometry(rileft,top,width,height)
                        
          except ValueError as e:
            self.error = QLabel("{}".format(e), self)
            self.error.setGeometry(0, size, 380, 20)
            self.setGeometry(0,0,380, 80)
            size +=20
      else:
        # Asignar valores por default y usarlos en setGeometry
        rileft = top = 0
        width = 95
        height = 40
        self.setGeometry(rileft,top,width,height)

        # -----------  Diseño del boton  -----------
        """
        
           Establecer los diferentes diseños de boton y si no se recibe ningun diseño entonces dejarlo 
           como default
        
        """
      
      # -----------  Diseño del boton  -----------
      """
      
         Si se recibe el parametro btn validarlo con la lista de la condicional y si existe llamar a su
         funcion
      
      """
      
      if "btn" in kwargs and kwargs['btn'].lower() in ["primary", "secundary", "success", "danger", "warning"]:
        {'primary': self.btn_primary,
        'secundary': self.btn_secundary,
        'success': self.btn_success,
        'danger': self.btn_danger,
        'warning': self.btn_warning}[kwargs['btn'].lower()](height=height)

      # -----------  Estilos CSS  -----------
      """
      
         Advertencia: Los estilos pueden afectar a los botones con clase btn ya que sobreescriben los estilos
         predefinidos
      
      """
      if "stylesheet" in kwargs:
        self.setStyleSheet(kwargs['stylesheet'])

      # -----------  Iconos  -----------
      """
      
         El color del icono activo por default es blanco, por alguna razon el color active falla y el tamaño por
         default es 12 

         Iconos gracias a QtAwesome
         https://pypi.org/project/QtAwesome/
      
      """
      if "icon" in kwargs:

        # valores por default
        color = "white"
        active_color = "green"
        icon_size = 12

        # Si los valores recibidos son diferentes a los default modificarlos
        if "color" in kwargs['icon']:color = kwargs['icon']['color']
        if "color active" in kwargs['icon']: active_color = kwargs['icon']['color active']
        if "icon size" in kwargs['icon']: icon_size = kwargs['icon']['icon size']

        styling_icon = qta.icon(kwargs['icon']['icon'], color=color, color_active=active_color)
        self.setIcon(styling_icon)
        self.setIconSize(QSize(icon_size, icon_size))

      # -----------  Fuente  -----------
      """
      
         El path de la fuente no es necesario en caso de ser diferente a none aplicar una configuracion diferente
      
      """
      if "font" in kwargs:

        # Valores por default
        font_path = None
        font_size = 12
        default_font = "Sans Serif"

        if "font size" in kwargs['font']: font_size = kwargs['font']['font size']
        if "font" in kwargs['font']: default_font = kwargs['font']['font']
        
        # -----------  Si no hay fuente predeterminada aplicar una por default  -----------

        if "font path" in kwargs['font']:
          font_db = QFontDatabase()
          font_id = font_db.addApplicationFont(kwargs['font']['font path'])
          families = font_db.applicationFontFamilies(font_id)
          font = QFont(families[0])
        else:
          font = QFont()
          font.setFamily(default_font)

        #Iterar en cada dato recibido por font type y compararlo con el dict y ejecutarlo si existe

        if "font type" in kwargs['font']:
          for element in kwargs['font']['font type'].lower().split():
            result = {"bold": self.font_bold,
            "italic": self.font_italic,
            "underline": self.font_underline,
            "strikeout": self.font_strikeout
            }[element]()

            exec(result)

        # -----------  Aplicar cambios a la fueente  -----------
            
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setPointSize(font_size)
        self.setFont(font)
      # -----------  Text  -----------
      """
      
         Si se recibe el parametro text entonces establecer el texto escrito por el usuario
      
      """
      
      if "text" in kwargs:
        self.setText(kwargs['text'])
      

    # -----------  Estilos de los botones  -----------
    """
      
       Mantener el border radius independientemente el tamaño que pueda tener el boton
       para eso se divide el tamaño entre 2 y se convierte en px
      
    """
    def btn_primary(self, height):
      self.setStyleSheet("""QPushButton{background:#20C1F7;color:#fff;border:none;border-radius:""" + str(height/2) + """px;} 
        QPushButton:hover{background:#09bbf6;}""")
      
    def btn_secundary(self, height):
      self.setStyleSheet("""QPushButton{background:#424242;color:#fff;border:none;border-radius:""" + str(height/2) + """px;} 
        QPushButton:hover{background:#333;}""")

    def btn_success(self, height):
      self.setStyleSheet("""QPushButton{background:#2bff37;color:#fff;border:none;border-radius:""" + str(height/2) + """px;} 
        QPushButton:hover{background:#00ff0d;}""")
    
    def btn_danger(self, height):
      self.setStyleSheet("""QPushButton{background:#ff3c13;color:#fff;border:none;border-radius:""" + str(height/2) + """px;} 
        QPushButton:hover{background:#ff2b00;}""")

    def btn_warning(self, height):
      self.setStyleSheet("""QPushButton{background:#ff901a;color:#fff;border:none;border-radius:""" + str(height/2) + """px;} 
        QPushButton:hover{background:#FF8300;}""")

    # -----------  diseños de fuente como bold, italic, underline, etc  -----------
    def font_bold(self):
      return "font.setBold(True)"
    def font_italic(self):
      return "font.setItalic(True)"
    def font_underline(self):
      return "font.setUnderline(True)"
    def font_strikeout(self):
      return "font.setStrikeOut(True)"
    
        
# ======  End of Button  =======


if __name__ == "__main__":
    print("Error: este archivo debe ser requerido.")
