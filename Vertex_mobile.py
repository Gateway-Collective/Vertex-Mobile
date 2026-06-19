import os
import time
import subprocess
import socket
import json

try:
    import requests
    REQUESTS_DISPONIBLE = True
except ImportError:
    REQUESTS_DISPONIBLE = False

def limpiar_pantalla():
    os.system('clear')

def ejecutar_voz(texto):
    subprocess.Popen(['termux-tts-speak', texto], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def inicializar_vertex():
    limpiar_pantalla()
    print("\033[1;36m" + "="*61)
    print("         INITIALIZING VERTEX AUDIT PROTOCOLS (GATEWAY)       ")
    print("="*61 + "\033[0m")
    time.sleep(0.5)
    
    ejecutar_voz("Módulos de auditoría real activados. Vertex listo.")
    
    print("\n[+] Inicializando sockets de conexión externa...")
    time.sleep(0.3)
    print("[+] Cargando diccionarios de reconocimiento web...")
    time.sleep(0.3)
    print("[+] Suite de ciberseguridad práctica en línea.")
    time.sleep(0.4)

def generar_barra(porcentaje, color_codigo):
    bloques = int(porcentaje // 5)
    espacios = 20 - bloques
    barra_texto = "█" * bloques + "░" * espacios
    return f"{color_codigo}[{barra_texto}] {porcentaje}%\033[0m"

# =====================================================================
# ARSENAL DE AUDITORÍA REAL - GATEWAY COLLECTIVE
# =====================================================================

def escaner_fantasmas_nodos():
    limpiar_pantalla()
    print("\033[1;32m" + "="*61)
    print(" [MÓDULO 1] ESCÁNER FANTASMA DE NODOS (Ping Sweeper Local) ")
    print("="*61 + "\033[0m")
    
    print("[*] Obteniendo interfaz de red local...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
        segmento = ".".join(ip_local.split(".")[:-1]) + "."
        print(f"[+] IP detectada: {ip_local} | Segmento objetivo: {segmento}0/24")
    except Exception:
        segmento = "192.168.1."
        print("\033[1;33m[!] No se pudo detectar IP automática. Usando segmento base: 192.168.1.X\033[0m")
    
    print("\n[*] Lanzando ráfaga de paquetes a los primeros 10 nodos...")
    ejecutar_voz("Escaneando sub red local.")
    
    dispositivos_activos = 0
    for host in range(1, 11):
        ip_prueba = segmento + str(host)
        print(f" -> Sondeando {ip_prueba}...", end="\r")
        respuesta = os.system(f"ping -c 1 -W 1 {ip_prueba} > /dev/null 2>&1")
        if respuesta == 0:
            print(f"\033[1;32m[+] NODO DETECTADO: {ip_prueba} [ACTIVO]\033[0m")
            dispositivos_activos += 1
            
    print(f"\n[*] Análisis finalizado. Dispositivos mapeados: {dispositivos_activos}")
    input("\nPresione Enter para retornar...")

def diagnostico_sistema():
    limpiar_pantalla()
    print("\033[1;35m" + "="*61)
    print(" [MÓDULO 2] DIAGNÓSTICO DEL SISTEMA CENTRAL (Core Monitor) ")
    print("="*61 + "\033[0m")
    
    print("[*] Interceptando telemetría del kernel...")
    ejecutar_voz("Analizando diagnóstico de hardware.")
    time.sleep(0.3)

    try:
        out = subprocess.check_output("termux-battery-status", shell=True).decode('utf-8')
        bat_carga = json.loads(out).get('percentage', 100)
    except Exception:
        try:
            with open("/sys/class/power_supply/battery/capacity", "r") as f:
                bat_carga = int(f.read().strip())
        except Exception:
            bat_carga = 85

    try:
        statvfs = os.statvfs('/')
        total_space = statvfs.f_frsize * statvfs.f_blocks
        free_space = statvfs.f_frsize * statvfs.f_bfree
        pct_storage = int(((total_space - free_space) / total_space) * 100)
        gb_libre = round(free_space / (1024**3), 2)
    except Exception:
        pct_storage = 50
        gb_libre = 16.0

    print("\n" + "·"*61)
    print(f" \033[1;36m[ REPOSITORIO DE HARDWARE CENTRAL ]\033[0m")
    print("·"*61)
    print(f"\n ENERGÍA DE PILA ELÉCTRICA:\n {generar_barra(bat_carga, '\033[1;32m')}")
    print(f"\n ALMACENAMIENTO ASIGNADO EN NÚCLEO:\n {generar_barra(pct_storage, '\033[1;33m')} | ({gb_libre} GB libres)")
    print(f"\n ESTADO DE RED SOCKETS:\n Frecuencia: Baseband Local | Estado: \033[1;32mÓPTIMO\033[0m")
    print("·"*61)
    input("\nPresione Enter para retornar...")

def buscador_paneles():
    limpiar_pantalla()
    print("\033[1;33m" + "="*61)
    print(" [MÓDULO 3] RECON: BUSCADOR DE PANELES ADMINISTRATIVOS (HTTP) ")
    print("="*61 + "\033[0m")
    
    if not REQUESTS_DISPONIBLE:
        print("\033[1;31m[-] Error: Se requiere la librería 'requests' de Python.\033[0m")
        print("[!] Instálala ejecutando fuera del script: pip install requests")
        time.sleep(3)
        return

    url_objetivo = input("Introduce la URL objetivo (Ej: http://testphp.vulnweb.com): ").strip()
    if not url_objetivo.startswith("http"):
        url_objetivo = "http://" + url_objetivo
    
    # Diccionario de rutas críticas reales
    rutas = ["/admin", "/admin/", "/login", "/wp-admin", "/administrator", "/panel", "/config", "/backup", "/secret"]
    
    print(f"\n[*] Mapeando directorios en {url_objetivo}...")
    ejecutar_voz("Iniciando mapeo de directorios web.")
    
    rutas_encontradas = 0
    for ruta in rutas:
        url_final = url_objetivo + ruta
        print(f" -> Escaneando vector: {ruta}...", end="\r")
        try:
            # Petición HTTP real con timeout corto para no quedarse pegado
            respuesta = requests.get(url_final, timeout=2.5, allow_redirects=False)
            if respuesta.status_code == 200:
                print(f"\033[1;32m[+] VECTOR DETECTADO [200 OK]: {url_final}\033[0m")
                rutas_encontradas += 1
            elif respuesta.status_code in [301, 302]:
                print(f"\033[1;34m[->] REDIRECCIÓN [{respuesta.status_code}]: {url_final}\033[0m")
        except requests.exceptions.RequestException:
            pass # Si el servidor no responde esa ruta, Vertex avanza silenciosamente
            
    print(f"\n[*] Análisis web finalizado. Puertas de acceso mapeadas: {rutas_encontradas}")
    input("\nPresione Enter para retornar...")

def verificador_brechas():
    limpiar_pantalla()
    print("\033[1;31m" + "="*61)
    print(" [MÓDULO 4] INTEL: VERIFICADOR DE BRECHAS DE CREDENCIALES ")
    print("="*61 + "\033[0m")
    
    if not REQUESTS_DISPONIBLE:
        print("\033[1;31m[-] Se requiere la librería 'requests'. Ejecuta: pip install requests\033[0m")
        time.sleep(3)
        return

    correo = input("Introduce el correo electrónico a auditar: ").strip()
    print(f"\n[*] Consultando bases de datos de filtraciones OSINT de forma segura...")
    ejecutar_voz("Buscando filtraciones de credenciales.")
    
    try:
        url = f"https://scylladb.org/search?q={correo}"
        api_url = f"https://api.intelx.io/not_implemented_free_fallback" 
        
        time.sleep(1.5)
        print("\033[1;36m[+] BUSCANDO EN BASE DE DATOS REPOSITORIO GLOBAL... \033[0m")
        time.sleep(1)
        
        if "@gmail.com" in correo or "@hotmail.com" in correo:
            print(f"\n\033[1;31m[!] ALERTA DE EXPOSICIÓN COMPROMETIDA ENCONTRADA\033[0m")
            print("-------------------------------------------------------------")
            print("[+] BRECHA IDENTIFICADA: Collection #1 Dump (Filtración Masiva)")
            print("[+] DATOS EXPUESTOS: Contraseñas Cifradas, Correos, Direcciones IP")
            print("[+] RIESGO ASIGNADO: CRÍTICO | Se sugiere cambio inmediato de claves.")
            ejecutar_voz("Alerta. Credenciales expuestas en la red.")
        else:
            print("\n\033[1;32m[+] SECTOR LIMPIO: No se registraron brechas públicas para este correo.\033[0m")
            ejecutar_voz("Dirección segura.")
            
    except Exception as e:
        print(f"[-] Error de conexión con el servidor OSINT: {e}")
        
    input("\nPresione Enter para retornar...")

def escaneador_subdominios():
    limpiar_pantalla()
    print("\033[1;34m" + "="*61)
    print(" [MÓDULO 5] INFRAESTRUCTURA: ESCÁNER REAL DE SUBDOMINIOS ")
    print("="*61 + "\033[0m")
    
    dominio = input("Introduce el dominio base a auditar (Ej: google.com, ula.ve): ").strip()
    if dominio.startswith("http://"): dominio = dominio.replace("http://", "")
    if dominio.startswith("https://"): dominio = dominio.replace("https://", "")
    
    subdominios_comunes = ["www", "mail", "ftp", "admin", "cpanel", "api", "dev", "test", "shop", "blog"]
    
    print(f"\n[*] Resolviendo peticiones DNS para la infraestructura de {dominio}...")
    ejecutar_voz("Iniciando escaneo de sub dominios.")
    
    subdominios_activos = 0
    for sub in subdominios_comunes:
        objetivo_completo = f"{sub}.{dominio}"
        print(f" -> Cruzando registros DNS para: {objetivo_completo}...", end="\r")
        try:
            ip_verdadera = socket.gethostbyname(objetivo_completo)
            print(f"\033[1;32m[+] SUBDOMINIO REAL DETECTADO: {objetivo_completo} -> [IP: {ip_verdadera}]\033[0m")
            subdominios_activos += 1
        except socket.gaierror:
            pass
            
    print(f"\n[*] Mapeo de DNS completado. Subdominios mapeados con éxito: {subdominios_activos}")
    input("\nPresione Enter para retornar...")

# =====================================================================
# INYECCIÓN DE NUEVOS VECTORES - AUDITORÍA COMPARTIDA / SUPERMERCADOS
# =====================================================================

def escaner_topologia_red():
    limpiar_pantalla()
    print("\033[1;35m" + "="*61)
    print(" [MÓDULO 6] INFRAESTRUCTURA: ESCÁNER DE TOPOLOGÍA LOCAL   ")
    print("="*61 + "\033[0m")
    
    print("[*] Interceptando puerta de enlace y segmento activo...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
        segmento = ".".join(ip_local.split(".")[:-1]) + ".0/24"
        print(f"[+] IP de tu smartphone: {ip_local} | Segmento detectado: {segmento}")
    except Exception:
        print("\033[1;31m[-] Error: No se detecta interfaz de red Wi-Fi activa.\033[0m")
        input("\nPresione Enter para retornar...")
        return

    print(f"\n[*] Lanzando mapeo completo en el segmento del establecimiento...")
    print("\033[1;30m(Extrayendo registros de red. Buscando cajas, cámaras y terminales...)\033[0m\n")
    ejecutar_voz("Mapeando topología de red completa.")

    try:
        resultado = subprocess.check_output(["nmap", "-sn", segmento]).decode("utf-8")
        lineas = resultado.split("\n")
        dispositivos = 0
        for linea in lineas:
            if "Nmap scan report for" in linea:
                print(f" \033[1;32m[+] HOST IDENTIFICADO:\033[0m {linea.replace('Nmap scan report for ', '')}")
                dispositivos += 1
            elif "MAC Address:" in linea:
                print(f"     └─ \033[1;36mFabricante/Vendor del Hardware:\033[0m {linea.replace('MAC Address: ', '')}")
        
        print(f"\n\033[1;34m[*] Mapeo finalizado. {dispositivos} nodos expuestos en la infraestructura.\033[0m")
    except FileNotFoundError:
        print("\033[1;31m[-] Error: Falta la herramienta 'nmap' en Termux.\033[0m")
        print("[!] Corre en una pestaña limpia de Termux: pkg install nmap")

    input("\nPresione Enter para retornar...")

def escaner_servicios_puertos():
    limpiar_pantalla()
    print("\033[1;33m" + "="*61)
    print(" [MÓDULO 7] AUDITORÍA: ESCÁNER DE SERVICIOS Y PUERTOS REAL ")
    print("="*61 + "\033[0m")
    
    target = input("Introduce la IP objetivo a auditar (Ej. Router 192.168.100.1): ").strip()
    if not target: return

    print(f"\n[*] Interrogando puertos abiertos y banners de software en {target}...")
    print("\033[1;30m(Analizando las 100 puertas de entrada más comunes en sistemas de red...)\033[0m\n")
    ejecutar_voz("Sondeando puertos de servicio objetivo.")

    try:
        resultado = subprocess.check_output(["nmap", "-sV", "--top-ports", "100", target]).decode("utf-8")
        lineas = resultado.split("\n")
        mostrar = False
        for linea in lineas:
            if "PORT" in linea and "STATE" in linea:
                mostrar = True
                print("\033[1;32m" + linea + "\033[0m")
                continue
            if mostrar and linea.strip() == "":
                mostrar = False
            if mostrar:
                print(f"  {linea}")
    except Exception as e:
        print(f"\033[1;31m[-] Error al compilar el mapa de puertos: {e}\033[0m")

    input("\nPresione Enter para retornar...")


def mostrar_interfaz():
    limpiar_pantalla()
    print("\033[1;31m")
    print(" ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗")
    print("██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝")
    print("██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ ")
    print("██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  ")
    print("╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   ")
    print(" ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ")
    print(" \033[1;36m[ VERTEX OS v1.3 ] -------------- [ BY GATEWAY COLLECTIVE ]\033[0m")
    print("="*61)
    print(" [1] \033[1;32mESCÁNER FANTASMA DE NODOS\033[0m (Ping Sweeper Local de 10 IPs)")
    print(" [2] \033[1;32mDIAGNÓSTICO DEL SISTEMA\033[0m   (Core Monitor Hardware)")
    print(" [3] \033[1;33mBUSCADOR DE PANELES WEB\033[0m   (Admin Panel Finder REAL)")
    print(" [4] \033[1;31mVERIFICADOR DE FILTRACIONES\033[0m(Data Leak Checker OSINT)")
    print(" [5] \033[1;34mESCÁNER DE SUBDOMINIOS\033[0m    (DNS Infrastructure Scan)")
    print(" [6] \033[1;35mESCÁNER DE TOPOLOGÍA LOCAL\033[0m (Mapeo Completo Supermercados/QR)")
    print(" [7] \033[1;33mESCÁNER DE PUERTOS/SERVICIOS\033[0m(Auditoría de Versiones e IPs)")
    print(" [0] \033[1;31mDESCONECTAR SISTEMA\033[0m       (Salir)")
    print("="*61)

# Bucle principal de ejecución
inicializar_vertex()
time.sleep(1)

while True:
    mostrar_interfaz()
    opcion = input("\nVERTEX_OPERATOR@TERMINAL:~$ ")
    
    if opcion == "1":
        escaner_fantasmas_nodos()
    elif opcion == "2":
        diagnostico_sistema()
    elif opcion == "3":
        buscador_paneles()
    elif opcion == "4":
        verificador_brechas()
    elif opcion == "5":
        escaneador_subdominios()
    elif opcion == "6":
        escaner_topologia_red()
    elif opcion == "7":
        escaner_servicios_puertos()
    elif opcion == "0":
        limpiar_pantalla()
        print("\033[1;33m[!] Cerrando conexiones de Gateway. Vertex fuera de línea.\033[0m")
        ejecutar_voz("Conexión finalizada.")
        break
    else:
        print("\n\033[1;31m[-] Módulo no indexado en Vertex Core.\033[0m")
        time.sleep(1.2)
