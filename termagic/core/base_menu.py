# termagic/core/base_menu.py

class BaseMenu:
    def __init__(self, title, options=[], style=None, exit_key='0'):
        """
        :param title: Título del menú.
        :param options: Lista de opciones del menú.
        :param style: Estilo del menú.
        """
        self.title = title
        self.options = options
        self.style = style

    def add_option(self, name, action, description=None):
        """
        :param name: Nombre de la opción.
        :param action: Acción asociada a la opción (una función).
        :param description: Descripción de la opción.
        """
        option = {
            'name': name,
            'action': action,
            'description': description
        }
        self.options.append(option)

    def remove_option(self, name):
        """
        :param name: Nombre de la opción a eliminar.
        """
        self.options = [option for option in self.options if option['name'] != name]

    def display(self):
        """
        Método para mostrar el menú. Debe ser implementado por las subclases.
        """
        raise NotImplementedError("El método display() debe ser implementado por las subclases.")

    def execute(self, option_name):
        """
        :param option_name: Nombre de la opción a ejecutar.
        """
        for option in self.options:
            if option['name'] == option_name:
                option['action']()
                return
        print(f"Opción '{option_name}' no encontrada.")
