# Git: Clonar un Repositorio, Gestionar Ramas y Subir Código

Este tutorial te guiará a través de los siguientes pasos:

1. **Clonar un repositorio Git**
2. **Actualizar el repositorio local**
3. **Crear una nueva rama**
4. **Realizar cambios en los archivos**
5. **Hacer push de la nueva rama**
6. **Solicitar revisión y hacer merge a `main`**
7. **Cerrar la rama**
8. **Actualizar la rama `main` antes de comenzar nuevos trabajos**

## Prerrequisitos

- **Git Instalado**: Asegúrate de tener Git instalado en tu máquina. Puedes descargarlo desde [la página oficial de Git](https://git-scm.com/downloads).
- **Acceso al Repositorio**: Debes tener los permisos necesarios para clonar y subir al repositorio.
- **Cuenta de GitHub**: Este tutorial asume que utilizas GitHub, pero los pasos son similares para otros servicios de hosting de Git.

---

## Paso 1: Clonar el Repositorio

Clonar un repositorio crea una copia local del repositorio remoto en tu máquina.

### Comando:

```bash
git clone https://github.com/Wolfsteno/data-science-projects.git
```

### Después de Clonar:

Se creará un nuevo directorio llamado `data-science-projects` en tu directorio actual, conteniendo todos los archivos del repositorio.

---

## Paso 2: Actualizar el Repositorio Local

Si ya has clonado el repositorio anteriormente, es importante actualizar tu copia local con los últimos cambios del repositorio remoto.

### Comando:

```bash
git pull origin main
```

---

## Paso 3: Crear una Nueva Rama Basada en tu Nombre y Primer Apellido

Crear una nueva rama te permite trabajar en cambios específicos sin afectar la rama principal. En mi caso, sería "acarrasco" porque mi nombre es Álvaro Carrasco.

### Comando:

```bash
git checkout -b acarrasco/Eliminacion-de-nulos-hecha
```

---

## Paso 4: Realizar Cambios en los Archivos

Realiza los cambios necesarios en tu proyecto. Por ejemplo, eliminar valores nulos de un conjunto de datos. Cuando tengas los avances listos, continúa al siguiente paso.

---

## Paso 5: Preparar y Confirmar los Cambios

### Verificar y Preparar Todos los Cambios:

Para ver qué archivos han cambiado:

```bash
git status
```

Para preparar todos los archivos para su subida:

```bash
git add .
```

### Confirmar con un Mensaje Corto y Descriptivo:

```bash
git commit -m "Eliminación de valores nulos"
```

---

## Paso 6: Hacer Push de la Nueva Rama

Sube la nueva rama al repositorio remoto.

### Comando:

```bash
git push -u origin acarrasco/Eliminacion-de-nulos-hecha
```

---

## Paso 7: Crear una Pull Request (PR), Solicitar Revisión y Hacer Merge a `main`

1. **Crear una Pull Request (PR)**: Ve a tu repositorio en GitHub y crea una PR desde `acarrasco/Eliminacion-de-nulos-hecha` hacia `main`.
2. **Revisión de Código**: Espera a que otro colaborador revise tus cambios. Avisa a tus compañeros por el canal de comunicación que utilices para agilizar el proceso.
3. **Hacer Merge**: Una vez aprobada la PR, realiza el merge a la rama `main`.

---

## Paso 8: Cerrar la Rama

### Eliminar la Rama Local (Opcional):

```bash
git branch -d acarrasco/Eliminacion-de-nulos-hecha
```

### Eliminar la Rama Remota (Opcional):

```bash
git push origin --delete acarrasco/Eliminacion-de-nulos-hecha
```

---

## Paso 9: Actualizar la Rama `main` Antes de Comenzar Nuevos Trabajos

### Comandos:

```bash
git checkout main
git pull origin main
```

---

## Resumen de Comandos

```bash
# Clonar el repositorio
git clone https://github.com/Wolfsteno/data-science-projects.git

# Navegar al directorio del repositorio
cd data-science-projects

# Actualizar el repositorio local
git pull origin main

# Crear y cambiar a una nueva rama
git checkout -b acarrasco/Eliminacion-de-nulos-hecha

# Realizar cambios...

# Preparar todos los cambios
git add .

# Confirmar los cambios con un mensaje
git commit -m "Eliminación de valores nulos"

# Subir la nueva rama al remoto
git push -u origin acarrasco/Eliminacion-de-nulos-hecha

# Crear Pull Request y hacer merge a main

# Eliminar la rama localmente
git branch -d acarrasco/Eliminacion-de-nulos-hecha

# Eliminar la rama remotamente
git push origin --delete acarrasco/Eliminacion-de-nulos-hecha

# Cambiar a main y actualizar antes de nuevos trabajos
git checkout main
git pull origin main
```

---

## Consejos Adicionales

### 1. Listar Todas las Ramas

```bash
git branch          # Lista ramas locales
git branch -r       # Lista ramas remotas
```

### 2. Cambiar Entre Ramas

```bash
git checkout nombre-de-la-rama
```
