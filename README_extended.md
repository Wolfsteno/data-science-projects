# Git: Clonar un Repositorio, Gestionar Ramas y Subir Código

Este tutorial te guiará a través de los siguientes pasos:

1. **Clonar un repositorio Git**
2. **Actualizar el repositorio local**
3. **Crear una nueva rama**
4. **Realizar cambios en los archivos**
5. **Preparar y confirmar los cambios**
6. **Subir la nueva rama**
7. **Crear una Pull Request (PR) y realizar el merge a `main`**
8. **Cerrar la rama**
9. **Actualizar la rama `main` antes de comenzar nuevos trabajos**

---

## Prerrequisitos

- **Git Instalado**: Asegúrate de tener Git instalado en tu máquina. Puedes descargarlo desde [la página oficial de Git](https://git-scm.com/downloads).
- **Acceso al Repositorio**: Debes tener los permisos necesarios para clonar y subir al repositorio.
- **Cuenta de GitHub**: Este tutorial asume que utilizas GitHub.
- **CLI de GitHub**: Instala el CLI de GitHub para facilitar la gestión de tu cuenta y el acceso al repositorio. Puedes descargarlo desde [GitHub CLI](https://cli.github.com/).

---

## Logea a tu cuenta de GitHub

Antes de comenzar, es recomendable autenticarte en GitHub utilizando la CLI de GitHub.

```bash
gh auth login
```

Este comando te guiará a través del proceso de autenticación en tu navegador.

---

## Paso 1: Clonar el Repositorio

Clonar un repositorio crea una copia local del repositorio remoto en tu máquina.

### Comando:

```bash
git clone https://github.com/Wolfsteno/data-science-projects.git
```

Accede al directorio del proyecto:

```bash
cd data-science-projects
```

---

## Paso 2: Actualizar el Repositorio Local

Si ya has clonado el repositorio anteriormente, asegúrate de actualizar tu copia local con los últimos cambios.

### Comando:

```bash
git pull origin main
```

---

## Paso 3: Crear una Nueva Rama

Crear una nueva rama te permite trabajar en cambios sin afectar `main`. Usa un nombre de rama basado en tu nombre y el propósito de la tarea. Por ejemplo, si tu nombre es Álvaro Carrasco, usarías "acarrasco" como prefijo.

### Ejemplo de Comando:

```bash
git checkout -b acarrasco/edicion-archivo-README
```

---

## Paso 4: Realizar Cambios en los Archivos

Edita los archivos necesarios, como el `README.md` o cualquier otro archivo del proyecto.

---

## Paso 5: Preparar y Confirmar los Cambios

### Verificar los Cambios:

```bash
git status
```

**Salida:**

```
On branch acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

### Preparar Todos los Archivos:

```bash
git add .
```

### Confirmar con un Mensaje Descriptivo:

```bash
git commit -m "Commit inicial"
```

**Salida:**

```
[acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio 1aaad78] Commit inicial
 1 file changed, 13 insertions(+), 2 deletions(-)
```

---

## Paso 6: Subir la Nueva Rama

Intenta subir tu nueva rama al repositorio remoto.

### Comando:

```bash
git push -u origin acarrasco/Edicion-del-archivo-README.md
```

**Salida:**

```
error: src refspec acarrasco/Edicion-del-archivo-README.md does not match any
error: failed to push some refs to 'https://github.com/Wolfsteno/data-science-projects.git'
```

### Solución al Error:

El error `src refspec ... does not match any` indica que la rama que intentas subir no existe o tiene un nombre incorrecto. Asegúrate de que la rama existe y está correctamente nombrada.

1. **Verificar Ramas Locales:**

   ```bash
   git branch
   ```

2. **Crear la Rama Correctamente:**

   Si hubo un error al crear la rama anteriormente, créala nuevamente con el nombre correcto:

   ```bash
   git checkout -b acarrasco/Edicion-del-archivo-README
   ```

3. **Subir la Rama:**

   ```bash
   git push -u origin acarrasco/Edicion-del-archivo-README
   ```

---

## Paso 7: Crear una Pull Request (PR) y Realizar el Merge a `main`

### Crear una Pull Request desde la CLI

Una vez que tu rama está en el repositorio remoto, puedes crear una Pull Request utilizando la CLI de GitHub.

#### Comando Inicial con Error:

```bash
gh pr create --base main --head acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio --title "Commit_inicial_con_helpers_e_inicio_del_ejercicio" --body 'Descripcion opcional...'
```

**Salida:**

```
flag needs an argument: --body

Usage:  gh pr create [flags]

... (lista de flags y ayuda)
```

**Corrección:** Debes proporcionar un argumento para `--body`. Si no deseas incluir un cuerpo, puedes dejarlo vacío o usar comillas.

#### Comando Corregido:

```bash
gh pr create --base main --head acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio --title "Commit inicial con helpers e inicio del ejercicio" --body ""
```

**Salida:**

```
Warning: 1 uncommitted change

Creating pull request for acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio into main in Wolfsteno/data-science-projects

https://github.com/Wolfsteno/data-science-projects/pull/1
```

### Verificar las Pull Requests Abiertas

```bash
gh pr list --state open
```

**Salida:**

```
Showing 1 of 1 open pull request in Wolfsteno/data-science-projects

ID  TITLE                                              BRANCH                                                       CREATED AT        
#1  Commit inicial con helpers e inicio del ejercicio  acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio  about 1 minute ago
```

### Ver la Pull Request en el Navegador

Para abrir la Pull Request en tu navegador, utiliza el siguiente comando reemplazando `<número-de-PR>` con el número de la PR:

```bash
gh pr view <número-de-PR> --web
```

**Ejemplo:**

```bash
gh pr view 1 --web
```

**Salida:**

```
Opening https://github.com/Wolfsteno/data-science-projects/pull/1 in your browser.
```

---

## Paso 8: Cerrar la Rama

### Eliminar la Rama Local:

Después de que la Pull Request ha sido mergeada, puedes eliminar la rama localmente.

```bash
git branch -d acarrasco/Edicion-del-archivo-README
```

### Eliminar la Rama Remota:

También es recomendable eliminar la rama del repositorio remoto.

```bash
git push origin --delete acarrasco/Edicion-del-archivo-README
```

---

## Paso 9: Actualizar la Rama `main`

Antes de comenzar nuevos trabajos, asegúrate de tener la última versión de `main`.

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

# Navegar al directorio
cd data-science-projects

# Actualizar el repositorio local
git pull origin main

# Crear y cambiar a una nueva rama
git checkout -b acarrasco/edicion-archivo-README

# Realizar cambios...

# Verificar los cambios
git status

# Preparar todos los cambios
git add .

# Confirmar los cambios
git commit -m "Commit inicial"

# Subir la nueva rama al remoto
git push -u origin acarrasco/Edicion-del-archivo-README

# Abrir una Pull Request desde la CLI
gh pr create --base main --head acarrasco/Edicion-del-archivo-README --title "Título de la PR" --body "Descripción de los cambios realizados"

# Listar Pull Requests abiertas
gh pr list --state open

# Ver una Pull Request específica en el navegador
gh pr view 1 --web

# Eliminar la rama local
git branch -d acarrasco/Edicion-del-archivo-README

# Eliminar la rama remota
git push origin --delete acarrasco/Edicion-del-archivo-README

# Cambiar a main y actualizar
git checkout main
git pull origin main
```

---

## Consejos Adicionales

1. **Listar Todas las Ramas:**

   ```bash
   git branch       # Ramas locales
   git branch -r    # Ramas remotas
   ```

2. **Cambiar Entre Ramas:**

   ```bash
   git checkout nombre-de-la-rama
   ```

3. **Autenticación con GitHub CLI:**

   Si encuentras errores relacionados con la autenticación al usar `gh`, asegúrate de haber instalado correctamente la CLI de GitHub y estar autenticado.

   - **Instalar GitHub CLI en Windows:**
     - Descarga el instalador desde [GitHub CLI Releases](https://github.com/cli/cli/releases/latest).
     - Ejecuta el archivo `.msi` y sigue las instrucciones de instalación.

   - **Verificar la Instalación:**

     ```bash
     gh --version
     ```

   - **Autenticar con GitHub CLI:**

     ```bash
     gh auth login
     ```

     Sigue las instrucciones en pantalla para completar la autenticación en tu navegador.

4. **Manejo de Errores Comunes:**

   - **Error 403 al Push:**

     ```
     remote: Permission to Wolfsteno/data-science-projects.git denied to tecnocracia-espanola.
     fatal: unable to access 'https://github.com/Wolfsteno/data-science-projects.git/': The requested URL returned error: 403
     ```

     **Solución:**
     - Verifica que estás autenticado con la cuenta correcta que tiene permisos para el repositorio.
     - Revisa la configuración remota:

       ```bash
       git remote -v
       ```

     - Actualiza las credenciales si es necesario o cambia a autenticación SSH.

   - **Refspec No Coincide:**

     ```
     error: src refspec acarrasco/Edicion-del-archivo-README.md does not match any
     ```

     **Solución:**
     - Asegúrate de que la rama existe y está correctamente nombrada.
     - Verifica el nombre de la rama actual con `git branch`.

5. **Uso de SSH en Lugar de HTTPS:**

   Configurar SSH puede simplificar la autenticación y evitar problemas con tokens personales.

   - **Generar una Clave SSH:**

     ```bash
     ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
     ```

   - **Agregar la Clave SSH a GitHub:**
     - Copia el contenido de `~/.ssh/id_rsa.pub`.
     - Ve a [GitHub SSH Keys Settings](https://github.com/settings/keys) y añade una nueva clave SSH.

   - **Actualizar la URL Remota a SSH:**

     ```bash
     git remote set-url origin git@github.com:Wolfsteno/data-science-projects.git
     ```

   - **Probar la Conexión SSH:**

     ```bash
     ssh -T git@github.com
     ```

---

## Ejemplo Práctico: Flujo Completo de Trabajo

A continuación, se presenta un ejemplo práctico que integra los comandos y soluciones a errores comunes durante el flujo de trabajo.

### 1. Crear y Cambiar a una Nueva Rama

```bash
git checkout -b acarrasco/Edicion-del-archivo-README
```

### 2. Verificar el Estado de Git

```bash
git status
```

**Salida:**

```
On branch acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
```

### 3. Preparar los Cambios

```bash
git add .
```

### 4. Confirmar los Cambios

```bash
git commit -m "Commit inicial"
```

**Salida:**

```
[acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio 1aaad78] Commit inicial
 1 file changed, 13 insertions(+), 2 deletions(-)
```

### 5. Subir la Rama al Remoto

```bash
git push -u origin acarrasco/Edicion-del-archivo-README.md
```

**Salida:**

```
error: src refspec acarrasco/Edicion-del-archivo-README.md does not match any
error: failed to push some refs to 'https://github.com/Wolfsteno/data-science-projects.git'
```

**Solución:** Asegúrate de que la rama existe y está correctamente nombrada.

```bash
git checkout -b acarrasco/Edicion-del-archivo-README
git push -u origin acarrasco/Edicion-del-archivo-README
```

### 6. Crear una Pull Request

#### Intento Inicial con Error:

```bash
gh pr create --base main --head acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio --title "Commit_inicial_con_helpers_e_inicio_del_ejercicio" --body
```

**Salida:**

```
flag needs an argument: --body

Usage:  gh pr create [flags]

... (lista de flags y ayuda)
```

#### Comando Corregido:

```bash
gh pr create --base main --head acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio --title "Commit inicial con helpers e inicio del ejercicio" --body ""
```

**Salida:**

```
Warning: 1 uncommitted change

Creating pull request for acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio into main in Wolfsteno/data-science-projects

https://github.com/Wolfsteno/data-science-projects/pull/1
```

### 7. Listar Pull Requests Abiertas

```bash
gh pr list --state open
```

**Salida:**

```
Showing 1 of 1 open pull request in Wolfsteno/data-science-projects

ID  TITLE                                              BRANCH                                                       CREATED AT        
#1  Commit inicial con helpers e inicio del ejercicio  acarrasco/Commit_inicial_con_helpers_e_inicio_del_ejercicio  about 1 minute ago
```

### 8. Ver la Pull Request en el Navegador

```bash
gh pr view 1 --web
```

**Salida:**

```
Opening https://github.com/Wolfsteno/data-science-projects/pull/1 in your browser.
```

---

## Manejo de la CLI de GitHub en WSL

Si utilizas el Subsistema de Windows para Linux (WSL) y encuentras que `gh` no está instalado, puedes instalarlo utilizando `snap` o `apt`.

### Instalar GitHub CLI en Ubuntu (WSL)

#### Usando `snap`:

```bash
sudo snap install gh
```

#### Usando `apt`:

```bash
sudo apt update
sudo apt install gh
```

**Nota:** Después de la instalación, verifica que `gh` esté correctamente instalado.

```bash
gh --version
```
