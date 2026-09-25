Portafolio Técnico — IT, Help Desk & Ciberseguridad

¡Hola! Bienvenido a mi portafolio técnico y bitácora de laboratorios prácticos. Este espacio es utilizado con el fin de documentar mi experiencia de aprendizaje en **administración de sistemas, diagnóstico de redes, resolución de incidencias (Troubleshooting) y ciberseguridad defensiva/ofensiva**.

Mi objetivo es aplicar estas competencias en roles de entrada como **Soporte Técnico Jr., Mesa de Ayuda (Help Desk) o Analista SOC Trainee / Junior**, aportando capacidad analítica, automatización y buenas prácticas de seguridad.

---

## 🛠️ Competencias Técnicas Clave

- **Sistemas Operativos & Scripting:** Administración y navegación avanzada en Linux (Debian/Ubuntu/Kali) y Windows. Nociones básicas de Bash Scripting, gestión de permisos y verificación de integridad de archivos via SHA-256.
- **Diagnóstico de Redes & Conectividad:** Inspección profunda de paquetes con Wireshark, diagnóstico de capa de red/transporte, resolución de problemas de conectividad local/remota y mapeo de infraestructura con Nmap.
- **Soporte Web & Protocolos:** Comprensión de arquitecturas cliente-servidor, análisis de cabeceras HTTP/HTTPS, interpretación de códigos de estado (200, 301, 403, 500) e intercepción de tráfico mediante proxies.
- **Seguridad Operacional & Hardening:** Diseño de entornos virtualizados aislados, gestión de credenciales, análisis de vulnerabilidades (PoCs) y mitigación de riesgos de exposición de datos.

---

## 📋 Estructura del Portafolio y Laboratorios Prácticos

A continuación se detallan los laboratorios desarrollados, organizados paso a paso con sus respectivas metodologías y evidencias:

### 👤 Información Personal & Perfil
* [**Sobre Mí e Información de Contacto**](about/profile.md) — Resumen profesional, habilidades y vías de contacto.

---

### 🧪 Proyectos y Laboratorios Técnicos

1. [**Configuración de HomeLab Seguro**](projects/1-lab.md)
   * **Descripción:** Diseño e implementación de un laboratorio de pruebas virtualizado (Kali Linux y objetivo Metasploitable2) utilizando redes *Host-Only* para garantizar aislamiento total y seguridad operacional.

1. [**Scripting en Bash e Integridad de Datos**](projects/2-bash-scripting.md)
   * **Descripción:** Automatización de tareas de administración en Linux mediante Bash Scripts. Implementación de controles de integridad de archivos mediante hashing con algoritmo **SHA-256**.

1. [**Prueba de Concepto: Análisis de Tráfico y Riesgos HTTP vs. HTTPS**](projects/3-wireshark-poc.md)
   * **Descripción:** Captura e inspección de paquetes con **Wireshark**. Demostración práctica del peligro de credenciales viajando en texto plano e importancia del cifrado SSL/TLS.

1. [**Fuzzing y Enumeración Web con Feroxbuster**](projects/4-feroxbuster.md)
   * **Descripción:** Descubrimiento activo de directorios y archivos ocultos en servidores web. Análisis de respuestas HTTP para identificación de superficies de ataque y políticas de control de acceso.

1. [**Escaneo de Red y Reconocimiento con Nmap**](projects/5-nmap-basics.md)
   * **Descripción:** Auditoría de puertos abiertos, fingerprinting de sistemas operativos y detección de versiones de servicios para diagnóstico de red y evaluación de vulnerabilidades.

1. [**Intercepción e Inspección Web con Burp Suite**](projects/6-burp-suite.md)
   * **Descripción:** Configuración de proxy local y certificados CA para análisis de tráfico HTTP/HTTPS, inspección de peticiones/respuestas y evaluación de controles de seguridad (MFA, Rate Limiting).

1. [**Prueba de Concepto: Explotación vsftpd Backdoor**](projects/7-poc-vsftpd-backdoor.md)
   * **Descripción:** Análisis y validación técnica de la vulnerabilidad crítica en `vsftpd v2.3.4` mediante Metasploit. Aplicación de medidas de remediación, hardening y actualización de servicios.
   
1. [**Prueba de Concepto y Reporte: Análisis de Tráfico y Simulación de UDP Flood**](projects/8-UDPflood.md)
   * **Descripción:** Simulación de tráfico UDP no solicitado en un entorno virtualizado Host-Only para el análisis de comportamiento de la capa de transporte. Identificación de patrones de fragmentación IP en Wireshark y definición de medidas defensivas (Rate Limiting, Hardening e IDS/IPS).



---

## 🚀 Enlaces de Interés

- 🌐 **Portfolio Web (Vercel):** [En proceso]
- 💼 **LinkedIn:** [En proceso]
- ✉️ **Contacto:** Facundoeducwork@protonmail.com