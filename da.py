from info import *
from pystyle import Colors , Colorate , Add
logo = f'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⣀⣠⣶⣾⣿⣿⣿⣿⣷⣦⣤⣀⡀⢠⣾⣿⣿⣷⣦⣄⣀⣀⣀⣠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣶⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣷⣄⠉⠙⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⢆⡾⣿⡟⣿⣿⣿⣿⡟⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⢀⣼⣿⣿⣿⣿⣿⣾⣿⡿⢠⣿⣿⣿⣿⣶⣶⣤⣧⡀⡈⠁⠀⠈⠉⠉⠉⠉⠀⠀⠙⢛⢿⣷⢹⣿⣿⣿⣿⣝⡿⠛⠋⣿⣆⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠊⢰⣶⣶⣯⣆⡀⠀⣴⣿⣿⣿⢸⣿⣿⣿⣿⣿⡇⣴⣿⣿⣿⣧⡀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣼⣿⣿⣿⣿⣿⣧⣽⣿⣿⣿⡸⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣧⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⠛⣿⡿⢿⣿⣿⡿⠋⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢻⣟⡇⣼⠋⣰⣿⣿⣿⣿⣶⡎⢿⣿⣿⣿⣿⣿⡿⢿⢸⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣦⣼⠸⠃⠀⠈⣿⣇⣾⠋⢻⡿⠧⠸⢿⡯⢿⣿⣿⣷⡘⡄⢳⣿⢻⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠀⠀⠀⠈⣿⡿⠻⡲⣚⡃⠀⠀⠀⠀⠀⠹⣿⣿⡄⢻⠀⠛⠸⣿⣿⣿⡏⠘⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⡟⣿⣿⢻⡗⠢⢄⠀⠈⣷⣉⠉⡉⠀⠀⠀⠀⠀⠀⢰⣿⡷⠀⡈⠀⠀⢀⣿⣿⡿⠀⢀⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⣸⣿⣿⣿⡿⣱⣿⣿⣸⣧⠀⠀⠑⣠⣷⣍⠉⠀⠠⣄⠀⠀⢀⡀⠀⢸⡇⠀⠀⠀⢠⣾⣿⣿⠁⠀⣸⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⣰⠟⣿⣿⣿⣿⣿⣿⣿⠟⣿⠀⠀⢀⣿⡇⠉⣷⣦⠀⠈⠓⠚⠋⣀⣴⢾⡇⠀⠀⢠⣿⣿⣿⠃⠀⢠⣿⣿⣿⣿⣿⢇⣿⠅⠀
⡀⠀⡠⡾⢋⣠⣿⣿⣿⣿⣿⡟⠁⠀⡿⠀⢀⢶⣿⡇⢰⡿⠛⢻⡶⠤⠾⣿⡏⠀⠈⣷⢀⠤⢸⣿⡿⠉⠀⠀⢸⣿⣟⢿⣿⣿⡾⢋⠀⠀
⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⠏⢀⠂⢠⠇⠀⠨⡾⢿⣷⣞⡀⠀⣀⡇⣀⣀⣀⣹⢦⡀⠸⡇⠀⠀⢻⡄⢄⠀⠀⢸⣿⣿⡌⢿⡏⠁⠙⠗⠀
⠀⣀⡔⠒⠒⠛⠿⢿⣿⣋⣀⣀⣠⡿⠀⢀⣃⡷⠊⠉⠯⠿⣿⣿⣿⣿⠞⠛⠛⠀⠉⠙⢣⢠⠀⠀⣷⡈⠆⠀⠀⠹⣿⣿⣶⣳⣀⠀⠀⠀
⣤⣷⡀⠀⠀⠀⠀⠀⠀⠈⠉⣹⣿⠁⠀⠜⢸⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠸⡌⢇⠀⠘⢿⣿⣿⠿⠟⠛⠛⠛⠿⣿⣿⣶⣶
⠿⠿⠷⣦⡀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠠⠂⣾⠀⠀⠀⢠⢟⣿⣿⡏⣿⠀⠀⠀⠀⠀⠀⠀⢳⠈⡆⠀⠈⢻⡁⢀⣀⠀⠀⠀⠀⠀⣰⣿⡟
⠀⠀⢰⡏⠁⠔⠀⠁⣀⠄⢠⡏⠀⠀⠀⠠⡏⠀⠀⠀⡞⣸⣿⡿⣧⣽⠀⠀⠀⠀⠀⠀⢀⣼⡆⠘⠀⠀⠈⣇⠰⠄⠉⣐⡤⠴⢾⣿⣿⣿
⠀⠀⠀⠙⠿⠤⣤⠞⢳⣠⡟⠀⠀⠀⠀⢸⠛⠦⠀⣾⣿⣿⠊⠉⣿⣿⡧⠀⠀⠀⠀⣀⣾⣿⢿⡀⡄⠀⠀⠙⣷⡈⠀⣹⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣦⣩⠏⠀⠀⠀⠀⠀⣾⠀⠀⣾⣿⣿⡟⠀⠈⢻⣿⣽⡀⠀⠀⣴⣿⣿⡇⠘⣧⠱⡀⠀⠀⠘⣷⠾⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⢠⠀⢠⣿⣦⡼⠋⠸⠿⠃⠀⠀⢸⣿⠟⢿⣀⣼⣿⣿⣿⣧⡀⢸⠀⢣⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣇⠀⠀⠠⠃⠀⣼⣧⣿⠆⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢹⣟⣿⣿⣿⣿⡿⣿⡆⠈⢆⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⠁⠀⣸⣿⣿⣿⣦⣀⢀⡀⠀⢰⡇⢀⣤⣤⣤⣼⣿⣿⣿⣿⣿⡇⠘⣿⠀⠀⠳⣀⠀⣸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠁⢀⣴⣿⠿⠿⢻⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠳⣄⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⣴⠋⣸⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⣛⣻⣿⡏⠀⠀⠀⠀⢘⢷⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⢿⣿⣿⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⢽⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⢻⠞⣻⣿⣿⣿⢛⠛⠿⣿⣿⣿⣿⣿⣿⢫⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠘⣿⣦⣾⣿⣿⣿⣿⡐⠀⠀⣿⣿⡿⣿⣏⡏⢉⣽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

info = f'''
    {get_info_name_pc()}
    ─════════════════════════════════════════════════════─
    Дистрибутив    ▶ {get_distro()}
    Ядро           ▶ {get_kernel()}
    Граф.Окружение ▶ {get_de()}
    Оболочка       ▶ {get_shell()}
    GTK Тема       ▶ {get_gtk_theme()}
    Расширение     ▶ {get_resolution()}
    Память         ▶ {get_memory()}
    Процессор      ▶ {get_cpu()}
    ─════════════════════════════════════════════════════─
'''
full_info = Add.Add(logo, info)

print(Colorate.Vertical(Colors.blue_to_purple,full_info,1))
