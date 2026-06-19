# Vertex Mobile Audit & Recon Framework (v1.3)

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Android-integer?style=for-the-badge&logo=android&color=101010&logoColor=3DDC84" alt="Platform Supported">
  <img src="https://img.shields.io/badge/Language-Python%203-integer?style=for-the-badge&logo=python&color=101010&logoColor=3776AB" alt="Language">
  <img src="https://img.shields.io/badge/Collective-Gateway-integer?style=for-the-badge&color=101010&labelColor=00FFFF" alt="Collective">
</p>

**Vertex Mobile** es un entorno portátil de auditoría táctica, reconocimiento de infraestructura y diagnóstico de red diseñado específicamente para operar en terminales móviles embebidas (Termux en Android). Desarrollado bajo el núcleo del colectivo **Gateway**, el framework combina el uso de sockets nativos en Python con la versatilidad de herramientas consagradas como `nmap` para ofrecer un mapa completo del entorno de red desde un smartphone.

La suite incluye un sistema integrado de alertas acústicas mediante síntesis de voz nativa del sistema (`termux-tts-speak`), facilitando la retroalimentación operativa durante los vectores de análisis en campo sin necesidad de mantener la vista fija en la consola.

---
## Capturas de Pantalla
<p align="center">
<img width="720" height="1612" alt="Menú Principal de Vertex OS" src="https://github.com/user-attachments/assets/2ab7f13c-6f7b-4f17-a0be-b700e1a248cf" />
<img width="720" height="1612" alt="Módulo 6: Escáner de Topología Local" src="https://github.com/user-attachments/assets/fcb23dcb-eb5b-4cfe-873e-ba636426c994" />
<img width="720" height="1612" alt="Módulo 7: Escáner de Puertos" src="https://github.com/user-attachments/assets/0b5bfe8b-31e8-48c7-9d45-237281df1c7f" />
</p>

## Arsenal Operativo (Módulos Integrados)

El sistema organiza sus funciones a través de módulos interactivos de ejecución inmediata:

1. **Escáner Fantasma de Nodos (Ping Sweeper):** Sonda de red local por sockets que lanza ráfagas de paquetes controladas a los primeros segmentos activos de la subred (`/24`), mapeando terminales encendidas de forma pasiva.
2. **Diagnóstico del Sistema (Core Monitor):** Intercepta la telemetría del hardware del dispositivo, parseando en tiempo real la energía de la batería, el almacenamiento asignado en el núcleo y el estado general de los sockets.
3. **Buscador de Paneles Administrativos (HTTP):** Herramienta de mapeo web encargada de rastrear rutas críticas de acceso (`/admin`, `/login`, `/config`) utilizando peticiones HTTP reales con temporizadores cortos para evitar bloqueos.
4. **Verificador de Filtraciones OSINT:** Consulta automatizada para auditar cuentas de correo electrónico y detectar si las credenciales han sido expuestas en brechas de datos masivas a nivel global (*Collection #1 Dump*).
5. **Escáner de Subdominios DNS:** Módulo de reconocimiento de infraestructura que interactúa con servidores DNS para resolver y comprobar la existencia de subdominios activos asociados a un dominio objetivo.
6. **Escáner de Topología Local:** Vector avanzado que procesa el segmento de red activo mediante barridos de descarte rápido (`nmap -sn`), aislando las direcciones físicas (MAC) y detectando el fabricante (Vendor) de cada terminal conectada.
7. **Escáner de Servicios y Puertos Real:** Inspector de sockets encargado de escanear los 100 puertos más comunes de una IP objetivo, interrogando los banners de software para auditar versiones de los servicios expuestos.

---

## Requisitos e Instalación

Para asegurar el correcto funcionamiento de las capacidades de red y voz en Termux, configure el entorno ejecutando:

```bash
# Actualizar el gestor de paquetes de la terminal
pkg update && pkg upgrade -y

# Instalar dependencias del sistema de auditoría y voz
pkg install nmap termux-api -y

# Instalar librería requerida de Python para peticiones web
pip install requests

Inicialización del Entorno
Para ejecutar la consola central del framework, navegue hasta la ubicación del script y use el intérprete nativo:
python Vertex_mobile.py
Al arrancar, Vertex cargará los diccionarios de reconocimiento, validará los sockets de conexión y establecerá el canal de comunicación del operador con el colectivo Gateway.
 Tablero de Control Interactivo (ASCII UI)
La interfaz presenta un diseño de bloques optimizado para pantallas móviles:
 ██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗
██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝
██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ 
██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  
╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   
 [ VERTEX OS v1.3 ] -------------- [ BY GATEWAY COLLECTIVE ]
=============================================================
 [1] ESCÁNER FANTASMA DE NODOS (Ping Sweeper Local de 10 IPs)
 [2] DIAGNÓSTICO DEL SISTEMA   (Core Monitor Hardware)
 [3] BUSCADOR DE PANELES WEB   (Admin Panel Finder REAL)
 [4] VERIFICADOR DE FILTRACIONES(Data Leak Checker OSINT)
 [5] ESCÁNER DE SUBDOMINIOS    (DNS Infrastructure Scan)
 [6] ESCÁNER DE TOPOLOGÍA LOCAL (Mapeo Completo Supermercados/QR)
 [7] ESCÁNER DE PUERTOS/SERVICIOS(Auditoría de Versiones e IPs)
 [0] DESCONECTAR SISTEMA       (Salir)
=============================================================

Uso Ético y Responsable
Este software ha sido diseñado con fines puramente académicos, auditorías de seguridad defensivas en laboratorios controlados y proyectos de investigación del colectivo. El uso del script para escaneos no autorizados en redes ajenas es responsabilidad exclusiva de la persona que opera la herramienta.

