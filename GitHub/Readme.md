# CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1

## USO DE GITHUB Parte 1

GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).

Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.

## COMANDOS

- **Import repository**, **New repository**, **New organization**: significa que es como tu empresa, 
- **New project**: significa que es como un grupo de repositorios que puedes tener dentro de una empresa, 
- **New gist**: es un pedacito de código que puedes compartir.

### New repository

- Ponemos el nombre: `class-git`, 
- Descripción: Haremos un blog increíble, 
- Hay muchas licencias para publicar el código: **NO** lo hacemos ahora.

### Create repository

- Lo ponemos en privado o en público.

El `README.md` es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.

### Clonar un repositorio

Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando `git clone + la URL` que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.

**ATENCIÓN**: ¿Por qué? Porque a través de https nos pedirá usuario (nombre perfil) y contraseña.

Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.

### Cómo conectar un repositorio de GitHub a nuestro documento local

Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos, aconsejo que al trabajar desde GitHub no utilicemos localmente el comando `git init`, si debemos ejecutar las siguientes instrucciones:

1. Guardar la URL del repositorio de GitHub con el nombre de `origin`:
    ```bash
    git remote add origin URL
    ```

2. Verificar que la URL se haya guardado correctamente:
    ```bash
    git remote
    git remote -v
    ```

3. Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar `git fetch` y `git merge` o solo `git pull` con el flag `--allow-unrelated-histories`:
    ```bash
    git pull origin master --allow-unrelated-histories
    ```

4. Por último, ahora sí podemos hacer `git push` para guardar los cambios de nuestro repositorio local en GitHub:
    ```bash
    git push origin master
    ```

### Cómo autenticarte en GitHub 2022

Antes de empezar, debemos renombrar la rama ‘master’ a ‘main’, este es el nuevo estándar en GitHub. Para esto:

1. Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.
2. Ejecutamos el siguiente comando: 
    ```bash
    git branch -M main
    ```

### Pasos para crear un token de acceso personal

Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.

1. Seguir la secuencia:
   - Ingresamos a nuestra cuenta de GitHub.
   - Buscamos **Settings**.
   - Click en **Developer settings**.
   - Click en **Personal access tokens**.
   - Click en **Generate new token** aquí se puede colocar un nombre, la fecha de expiración.
   - Tildar en **repo** y luego click en el botón verde **Generate token**.

## PORTAFOLIO

Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:
- **Dante Nicolás Martinez**
- **Segundo Semestre Parte 1**:
  - **INTRO**: [Ver Video](https://drive.google.com/file/d/1yFihiQVMKXJvOXSwMdczrCesocRS9heY/view)
  - **PDF**: [Ver PDF](https://docs.google.com/presentation/d/10QC9Ii6zvYgTa5fbzUJGNC8z9LukEN5r/edit#slide=id.p1)

Revisar y ejecutar cada comando, hacerlo como práctica: **NO** olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.

**Profesor Ariel Betancud**


---

## CLASE 02 - Miércoles 21 de Agosto del 2024
### Portafolio 2: Cargar la Llave SSH Pública en GitHub

#### Copiar la llave pública
- Encontrar la llave en `.ssh/`, abrir el archivo `.pub` y copiar el contenido.

#### Añadir llave SSH en GitHub
1. Navegar a `Settings` -> `SSH and GPG keys`.
2. Crear una nueva llave SSH y pegar la llave pública.

#### Comandos Git para trabajar con SSH:
- Cambiar el nombre de la rama `master` a `main`:
```sh
git branch -M main
```
- Agregar el repositorio remoto:
```sh
git remote add origin git@github.com:nombreUsuario/class-git.git
```
- Enviar los cambios:
```sh
git push origin main
```

#### Portafolio
- **Video Capítulo 01**: [Ver Video](https://drive.google.com/file/d/1op_N1lCHQey2jIJKLHt0JyDi5tqlSYcQ/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1irin9hTI2Jqf-0Zg2mOsB1nzARkL4Gs3/view)

---

## CLASE 03 - Miércoles 28 de Agosto del 2024
### Portafolio 3: Cambios en GitHub: de Master a Main

Desde el 1 de octubre de 2020, GitHub cambió el nombre de la rama principal de `master` a `main` como parte de un esfuerzo por eliminar términos problemáticos en la industria de la tecnología.

#### Cambio de rama `master` a `main`:
```sh
git branch -M main
```

#### Portafolio
- **Video Capítulo 02**: [Ver Video](https://drive.google.com/file/d/1sNtWVHF-L4pIiEVTr4qEQUVhT4W964tD/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1snYyd_MldpZ1iGRLTmADzG4uUC21nda5/view)

---

## CLASE 04 - Miércoles 4 de Septiembre del 2024
### Portafolio 4: Tu Primer Push

#### Comandos para copiar la llave SSH pública:
- **Mac**:
```sh
pbcopy < ~/.ssh/id_rsa.pub
```
- **Windows (Git Bash)**:
```sh
clip < ~/.ssh/id_rsa.pub
```
- **Linux (Ubuntu)**:
```sh
cat ~/.ssh/id_rsa.pub
```

#### Actualización de la URL del repositorio remoto:
```sh
git remote set-url origin [url-ssh]
```

#### Portafolio
- **Video Capítulo 03**: [Ver Video](https://drive.google.com/file/d/1LgOq1_qtjeZcIq1f1PR4GMV8AWANN6Ju/view)
- **PDF**: [Ver PDF](https://docs.google.com/presentation/d/14odWSx7zoJ78nEj83V5sKkVaRIxqk0j_/edit#slide=id.p1)

---

## CLASE 05 - Miércoles 11 de Septiembre del 2024
### Portafolio 5: Git Tags y Versiones en GitHub

#### Creación de etiquetas:
```sh
git tag [etiqueta]
```

#### Listado de etiquetas:
```sh
git tag
```

#### Enviar etiquetas a GitHub:
```sh
git push origin --tags
```

#### Portafolio
- **Video Capítulo 04**: [Ver Video](https://drive.google.com/file/d/1F_kpPnOEJRQDvdymclsKNyqr4h09NWfz/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/12MArnwaV5RfzzedZ0AtDlRk_a12kL-9W/view)

---

## CLASE 06 - Miércoles 18 de Septiembre del 2024
### Portafolio 6: Error con los Tags

#### Investigación
¿Qué sucede si se carga un tag dos veces? La solución a este problema debe ser enviada antes de las 23 horas.

#### Respuesta a la pregunta: ¿Qué pasa si cargas un tag dos veces?
Cuando cargas un tag dos veces en Git, Git te dará un error porque los tags son inmutables. Esto significa que no puedes sobrescribir un tag existente a menos que fuerces la actualización. 

Si intentas crear o “pushear” un tag que ya existe, Git te mostrará un error diciendo algo como:
   *“fatal: tag 'v1.0' already exists”*
Esto se debe a que un tag es una referencia a un commit específico, y una vez creado, no debería cambiarse.

#### Solución al problema de haber cargado un tag dos veces:

**1. Verificar el tag existente:**
Primero, verifica si el tag que intentas crear ya existe y si está apuntando al commit correcto con el siguiente comando:
```sh
git show <nombre-del-tag>
```

**2. Eliminar el tag localmente (si el commit al que apunta el tag no es correcto):**
Si el tag está apuntando a un commit incorrecto o necesitas corregirlo, puedes eliminar el tag localmente con el siguiente comando:
```sh
git tag -d <nombre-del-tag>
```

**3. Recrear el tag:**
Luego de eliminar el tag, puedes crear uno nuevo apuntando al commit correcto con el siguiente comando:
```sh
git tag <nombre-del-tag> <commit-id>
```

**4. Eliminar el tag en el repositorio remoto (si también necesitas corregirlo en el repositorio remoto):**
Si el tag ya fue empujado al repositorio remoto y necesitas actualizarlo, primero elimínalo del remoto con el siguiente comando:
```sh
git push origin --delete <nombre-del-tag>
```

**5. Empujar el tag actualizado:**
Luego de corregir el tag localmente, empújalo nuevamente al repositorio remoto con el siguiente comando:
```sh
git push origin <nombre-del-tag>
```

Al eliminar y recrear un tag en Git, ten en cuenta que si otros desarrolladores ya han descargado el tag, podrían enfrentar conflictos o inconsistencias. Por lo tanto, forzar la actualización de tags debe hacerse con cuidado, comunicando los cambios al equipo si es necesario.

#### Portafolio
- **Video Capítulo 05**: [Ver Video](https://drive.google.com/file/d/1SV4-SAizEU84_T9B6-iBHJm5c72Gt-Z5/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1HoelHkism3xk_2BzmpN_rMhWokEDADaf/view)

---

## CLASE 07 - Viernes 20 de Septiembre del 2024
### Portafolio 7: Conflicto con los Tags Duplicados

#### Investigación
¿Qué ocurre cuando hay tags duplicados en Git? La solución a este problema debe ser enviada antes de las 23 horas.

#### Respuesta a la pregunta: ¿Cómo abordar el conflicto de tener dos tags con el mismo nombre?
El error de tener dos tags con el mismo nombre puede surgir por varias razones en sistemas de control de versiones como Git. Aquí hay un desglose de cómo puede ocurrir este problema, cómo se origina, y cómo solucionarlo.

### ¿Cómo se origina el problema?
1. **Creación de Tags Locales**: Si creas un tag en tu repositorio local y luego haces un `git push` sin especificar el tag, es posible que no se suba automáticamente a tu repositorio remoto. Si otro colaborador crea un tag con el mismo nombre en el repositorio remoto, puede surgir un conflicto.

2. **Fusiones de Repositorios**: Si dos ramas diferentes tienen tags con el mismo nombre y se fusionan, esto puede causar confusión, ya que Git no permite tener dos tags con el mismo nombre.

3. **Problemas de Sincronización**: Si trabajas en diferentes clones de un mismo repositorio y no estás sincronizando correctamente los tags, puedes crear un tag local que ya existe en el repositorio remoto.

### Pasos para abordar el conflicto

1. **Verificar los Tags Existentes**:
- Comando:
```bash
git tag
```
- Esto te mostrará todos los tags existentes en tu repositorio local.

2. **Verificar Tags Remotos**:
- Comando:
```bash
git ls-remote --tags origin
```
- Esto mostrará los tags que existen en el repositorio remoto.

3. **Identificar el Conflicto**:
- Si al intentar crear un nuevo tag, Git te da un error de que el tag ya existe, necesitas identificar si el tag está en tu repositorio local o remoto.

4. **Eliminar el Tag Duplicado**:
- Si decides que necesitas eliminar uno de los tags, puedes hacerlo de la siguiente manera:

- **Eliminar un Tag Local**:
```bash
git tag -d nombre_del_tag
```

- **Eliminar un Tag Remoto**:
```bash
git push --delete origin nombre_del_tag
```

5. **Crear el Tag de Nuevo**:
- Después de eliminar el tag conflictivo, puedes volver a crear el tag que necesitas:
```bash
git tag nombre_del_tag
```

6. **Pushear el Tag a Remoto**:
- Finalmente, asegúrate de enviar el nuevo tag al repositorio remoto:
```bash
git push origin nombre_del_tag
```

### Comandos Resumidos:
- Verificar tags locales:
```bash
git tag
```

- Verificar tags remotos:
```bash
git ls-remote --tags origin
```

- Eliminar un tag local:
```bash
git tag -d nombre_del_tag
```

- Eliminar un tag remoto:
```bash
git push --delete origin nombre_del_tag
```

- Crear un nuevo tag:
```bash
git tag nombre_del_tag
```

- Pushear el tag al remoto:
```bash
git push origin nombre_del_tag
```

#### Portafolio
- **Video Capítulo 06**: [Ver Video](https://drive.google.com/file/d/1wrqZlPWWZGseWpop94J0jZSgFj_XTqER/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/14p1D22y8L8DJNdQ6BMmkR22So2b3lWkk/view)

---