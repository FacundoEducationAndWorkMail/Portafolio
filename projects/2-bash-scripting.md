# Scripting básico en Bash y Control de Integridad (Hashes)

Como parte de la preparación operativa en entornos Linux, se automatizaron tareas básicas de gestión de archivos y verificación de integridad mediante funciones hash (**SHA-256**).

## 1. Posición en la ruta y creación de directorio de trabajo mediante concatenación lógica (`&&`)
```bash
cd Desktop && mkdir Hashear
```

## 2. Creación del archivo, inserción de texto plano y verificación

```bash
cd Hashear && touch Ingresar-Texto && echo "Facundo Toledo" >> Ingresar-Texto
cat Ingresar-Texto
```

## 3. Generación de hash SHA-256 sin salto de línea (`-n`) y redirección - Lectura con Cat

```bash
echo -n "Facundo Toledo" | sha256sum > Ingresar-Texto
cat Ingresar-Texto
```


La idea principal al realizar esta línea de códigos es: Entender bash, principios y sintaxis así como operadores lógicos y de concatenación, mezclando los mismos con comandos esenciales de Linux como cd - cat - echo - mkdir con el fin de mantener la práctica constante. Por otro lado, pero no menos importante, la verificación de integridad mediante funciones hash, en este caso (SHA-256).