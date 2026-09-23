# Escaneo Activo y Reconocimiento de Red con Nmap

## 1. Objetivo
Identificar la superficie de ataque del objetivo `192.168.0.240` mediante el descubrimiento de puertos abiertos, identificación de servicios, detección de versiones, evaluación de vulnerabilidades conocidas y la generación de reportes estructurados en formato XML/HTML.

---

## 2. Ejecución Técnica

### Escaneo de Vulnerabilidades Directo
```bash
nmap -sV -T 5 --top-ports 100 --script vuln 192.168.0.240
```

![](nmap-vuln-scan.png)
*Detección del servicio FTP (vsftpd 2.3.4) e identificación de vulnerabilidades críticas y exploits asociados (CVE-2011-2523 / Backdoor).


### Escaneo Estructurado con Exportación XML

```bash
cd Desktop && mkdir Reporte-Escaneo && cd Reporte-Escaneo
```

```bash
nmap -p 21-80 -sS -sV -vvv -T 5 -oX reporte.xml --stylesheet="[https://svn.nmap.org/nmap/docs/nmap.xsl](https://svn.nmap.org/nmap/docs/nmap.xsl)" 192.168.0.240
```

![](nmap-command-xml.png)
*Ejecución del escaneo SYN sigiloso con nivel alto de verbosidad (-vvv) y generación del reporte estilizado.

#### Desglose de Parámetros

- `-p 21-80`: Define el rango específico de puertos a auditar (del 21 al 80).
    
- `-sS`: _TCP SYN Scan_ (escaneo sigiloso o _half-open_). Evalúa el estado del puerto sin completar el _handshake_ de tres vías.
    
- `-sV`: _Service Version Detection_. Interroga a los puertos abiertos para determinar el software exacto y su versión.
    
- `-vvv`: _Triple Verbosity_. Muestra los resultados y cambios de estado de los puertos en tiempo real en la terminal.
    
- `-T 5`: _Timing Template_ (Insane). Ajusta la velocidad del escaneo al máximo, óptimo para entornos de laboratorio. (Solo apto en entornos seguros y controlados de práctica)
    
- `--script vuln`: Ejecuta la categoría de scripts de NSE (_Nmap Scripting Engine_) orientada a la detección de vulnerabilidades conocidas.
    
- `-oX reporte.xml`: Exporta la salida estructurada en un documento XML.
    
- `--stylesheet=...`: Vincula la hoja de estilo XSL para transformar el XML en una interfaz HTML interactiva al abrirlo en un navegador.

## 3. Validación y Visualización del Reporte

El archivo `reporte.xml` generado se abrió en el navegador web para verificar la renderización limpia de la tabla de puertos y servicios.

![](nmap-xml-browser.png)
*Interfaz visual del reporte interactivo mostrando los puertos abiertos (21, 22, 23, 25, 53, 80) y sus versiones.

## 4. Impacto y Mitigación

### Impacto

- **Identificación de Vectores Críticos:** La ejecución del script `--script vuln` reveló la presencia de `vsftpd 2.3.4`, una versión notoriamente vulnerable a ejecución remota de comandos (RCE) mediante un _backdoor_ (CVE-2011-2523).
    
- **Superficie Expuesta:** Servicios obsoletos e inseguros como Telnet (puerto 23) transmiten credenciales en texto plano por la red.
    

### Mitigación

1. **Actualización de Software:** Actualizar inmediatamente las versiones de los servicios expuestos a versiones estables y parcheadas.
    
2. **Cierre de Servicios Innecesarios:** Desactivar protocolos inseguros o en desuso (ej. cambiar Telnet por SSH).
    
3. **Reglas de Filtrado:** Implementar políticas de firewall para limitar los puertos visibles desde segmentos de red no autorizados.