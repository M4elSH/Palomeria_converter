import yt_dlp
import sys
import os
import random

# Colores para la terminal
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
WHITE = "\033[97m"

def preparar_carpeta():
    if not os.path.exists('Convertidos'):
        os.makedirs('Convertidos')

def descargar_multimedia(url, tipo, calidad_video="1"):
    preparar_carpeta()
    
    formatos_video = {
        "1": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "2": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "3": "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    }
    
    frases_espera = [
        "Tate' quieto' que tamo' en eso...", 
        "Ta' desesperao'?", 
        "Que bobo con esa decalga' mio'...",
        "Dandole mambo a la descarga..."
    ]
    
    opciones = {
        'outtmpl': 'Convertidos/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [lambda d: print(f"{YELLOW}Descargando: {d['_percent_str']} - {d['_speed_str']}{RESET}", end='\r') if d['status'] == 'downloading' else None],
    }

    if tipo == "mp3":
        opciones.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        opciones.update({
            'format': formatos_video.get(calidad_video, "best[ext=mp4]"),
        })

    try:
        print(f"\n{CYAN}>> {random.choice(frases_espera)}{RESET}")
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print(f"\n\n{GREEN}¡Ya esta listo! Chequea la carpeta 'Convertidos'{RESET}")
    except Exception as e:
        print(f"\n{MAGENTA}Diantre, hubo un error: {e}{RESET}")

def mostrar_menu():
    print(f"\n{MAGENTA}" + "="*60 + f"{RESET}")
    print(f"{CYAN}           Palomeria converter{RESET}")
    print(f"{WHITE} No seas tan palomo y descarga tus videos y musicas desde aqui, PALOMO!{RESET}")
    print(f"{YELLOW}           Creado por: @Aniballl_13{RESET}")
    print(f"{MAGENTA}" + "="*60 + f"{RESET}")
    
    link = input(f"\n{GREEN}Enlace: {RESET} ").strip()
    if not link: return

    print(f"\n{CYAN}Que vas a bajar?{RESET}")
    print(f"a) Video MP4")
    print(f"b) Musica MP3")
    print(f"s) Modo Rapido (360p)")
    
    op = input(f"\n{YELLOW}Opcion: {RESET}").lower()

    if op == 'b':
        descargar_multimedia(link, "mp3")
    elif op == 's':
        descargar_multimedia(link, "video", "1")
    else:
        print(f"\n{CYAN}Calidad:{RESET} 1) 360p | 2) 720p | 3) 1080p")
        cal = input(f"{YELLOW}Elige (1-3): {RESET}")
        descargar_multimedia(link, "video", cal)

if __name__ == "__main__":
    try:
        mostrar_menu()
        print(f"\n{MAGENTA}Eso ta ready ya{RESET}\n")
    except KeyboardInterrupt:
        print(f"\n\n{MAGENTA}Saliendo...{RESET}\n")
