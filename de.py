import os
import subprocess

def get_desktop_environment_and_version():
    desktop_environment = 'unknown'
    version = "Версия не определена"

    if os.environ.get('DESKTOP_SESSION'):
        desktop_session = os.environ.get('DESKTOP_SESSION').lower()
        if desktop_session in ['gnome', 'unity', 'cinnamon', 'mate', 'xfce4', 'lxde', 'kde', 'plasma']:
            desktop_environment = desktop_session
        elif desktop_session == 'pantheon':
            desktop_environment = 'pantheon'  
    elif os.environ.get('XDG_CURRENT_DESKTOP'):
        desktop_environment = os.environ.get('XDG_CURRENT_DESKTOP').lower()
    elif os.environ.get('XDG_SESSION_DESKTOP'):
        desktop_environment = os.environ.get('XDG_SESSION_DESKTOP').lower()

    try:
        if desktop_environment == 'gnome':
            result = subprocess.run(['gnome-shell', '--version'], capture_output=True, text=True)
            version = result.stdout.strip()
        elif desktop_environment == 'kde' or desktop_environment == 'plasma':
            result = subprocess.run(['plasmashell', '--version'], capture_output=True, text=True)
            version = result.stdout.strip()
        elif desktop_environment == 'xfce4':
            result = subprocess.run(['xfce4-session', '--version'], capture_output=True, text=True)
            version = result.stdout.strip()
        elif desktop_environment == 'cinnamon':
            result = subprocess.run(['cinnamon', '--version'], capture_output=True, text=True)
            version = result.stdout.strip()
        elif desktop_environment == 'mate':
            result = subprocess.run(['mate-session', '--version'], capture_output=True, text=True)
            version = result.stdout.strip()
    except FileNotFoundError:
        version = "Команда не найдена"
    except Exception as e:
        version = f"Ошибка: {e}"

    return version

