# Git: Clonar un Repositorio, Editar el README y Subir Cambios

Este tutorial te muestra cómo clonar un repositorio, editar el archivo `README.md`, y subir los cambios mediante una Pull Request (PR).

---

## Prerrequisitos

- **Git Instalado**: [Descargar](https://git-scm.com/downloads)
- **Acceso a Repositorio GitHub**
- **GitHub CLI**: [Descargar](https://cli.github.com/)

---

## Iniciar Sesión en GitHub

Autentícate con GitHub CLI:

```bash
gh auth login
```

---

## 1. Clonar el Repositorio

```bash
git clone https://github.com/Wolfsteno/data-science-projects.git
cd data-science-projects
```

---

## 2. Actualizar el Repositorio Local

Asegúrate de tener la última versión de `main`:

```bash
git pull origin main
```

---

## 3. Crear una Nueva Rama para Editar el README

```bash
git checkout -b acarrasco/editar-readme
```

---

## 4. Realizar Cambios en el README

Edita el archivo `README.md` y añade o modifica contenido según sea necesario.

---

## 5. Preparar y Confirmar los Cambios

### Verificar los Cambios

```bash
git status
```

### Preparar los Cambios

```bash
git add README.md
```

### Confirmar los Cambios con un Mensaje Descriptivo

```bash
git commit -m "Actualización del README: descripción mejorada y ejemplos añadidos"
```

---

## 6. Subir la Nueva Rama al Repositorio Remoto

```bash
git push -u origin acarrasco/editar-readme
```

> **Nota**: Si aparece un error, verifica que el nombre de la rama sea correcto y que hayas creado la rama.

---

## 7. Crear una Pull Request (PR)

Crea una Pull Request para que tus cambios puedan ser revisados y mergeados a `main`.

```bash
gh pr create --base main --head acarrasco/editar-readme --title "Actualización del README" --body "He mejorado la descripción del proyecto y añadido ejemplos claros para facilitar su comprensión."
```

---

### Verificar PR Abierta

Para listar las Pull Requests abiertas:

```bash
gh pr list --state open
```

### Abrir la Pull Request en el Navegador

```bash
gh pr view 1 --web
```

---

## 8. Cerrar la Rama una Vez Mergeada

Una vez que la PR ha sido aprobada y mergeada, puedes eliminar la rama local y remota:

### Eliminar la Rama Local

```bash
git branch -d acarrasco/editar-readme
```

### Eliminar la Rama Remota

```bash
git push origin --delete acarrasco/editar-readme
```

---

## 9. Actualizar la Rama `main`

Para asegurarte de tener la última versión de `main`:

```bash
git checkout main
git pull origin main
```

---

## Resumen de Comandos

```bash
# Clonar el repositorio y navegar al directorio
git clone https://github.com/Wolfsteno/data-science-projects.git
cd data-science-projects

# Crear y cambiar a una nueva rama
git checkout -b acarrasco/editar-readme

# Editar README.md...

# Preparar y confirmar cambios
git add README.md
git commit -m "Actualización del README: descripción mejorada y ejemplos añadidos"

# Subir la nueva rama al remoto
git push -u origin acarrasco/editar-readme

# Crear una Pull Request con GitHub CLI
gh pr create --base main --head acarrasco/editar-readme --title "Actualización del README" --body "He mejorado la descripción del proyecto y añadido ejemplos claros para facilitar su comprensión."

# Listar PRs abiertas
gh pr list --state open

# Ver la PR específica en el navegador
gh pr view 1 --web

# Eliminar la rama local y remota después del merge
git branch -d acarrasco/editar-readme
git push origin --delete acarrasco/editar-readme

# Cambiar a main y actualizar
git checkout main
git pull origin main
```