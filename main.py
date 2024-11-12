from ui.app import main_window
from utils.db_utils import create_table

# Crear la base de datos y la tabla al iniciar el programa
create_table()

# Iniciar la ventana principal
if __name__ == "__main__":
    main_window()