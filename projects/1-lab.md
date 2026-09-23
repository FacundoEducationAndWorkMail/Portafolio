# Configuración de HomeLab de Ciberseguridad

## 1. Visión General del Entorno
Para el desarrollo de pruebas de concepto (PoCs) y análisis de vulnerabilidades, configuré e implementé un entorno virtualizado aislado en **VirtualBox**. (*Algunas pruebas a lo largo del portafolio se realizaron con NAT).

## 2. Topología y Máquinas Virtuales
* **Atacante:** Kali Linux
  * IP: `192.168.56.102`
  * Rol: Estación de trabajo con suite de herramientas de auditoría (Nmap, Burp Suite, Metasploit).
* **Objetivos (Target):**
  * **Metasploitable2:** IP `192.168.56.104` (Entorno Linux vulnerable para pruebas de red y web).

## 3. Configuración de Red Virtual y Verificación de Aislamiento
Para garantizar que el tráfico malicioso no salga a la red doméstica ni a Internet, configuré una red de tipo **Host-Only**.

* Verificación de conectividad local entre Kali Linux y Metasploitable2 (ping exitoso) y prueba de aislamiento frente a Internet (Network is unreachable al probar 8.8.8.8).*![](lab-network-ping.png)
