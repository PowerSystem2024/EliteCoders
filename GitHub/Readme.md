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

# CLASE 08 MIÉRCOLES 2 DE OCTUBRE DEL 2024 - Portafolio 8  
## Manejo de ramas en GitHub  

Si no te funciona el comando `gitk`, es posible que no lo tengas instalado por defecto.  
Para instalar `gitk` debemos ejecutar los siguientes comandos:
```sh
sudo apt-get update
sudo apt-get install gitk
```

### Repasa: ¿Qué es Git?
Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (`main`). Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca usas en el repositorio local. Lo crucial es que aprendas a manejarlas para trabajar profesionalmente.  

Si, estando en otra rama, modificamos los archivos y hacemos commit, tanto el historial (`git log`) como los archivos serán afectados. La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. Si luego de “guardar” los archivos (usando commit) nos movemos a otra rama (`git checkout otraRama`), veremos cómo las modificaciones de la rama pasada no aparecen en la otra rama.  

### Comandos para manejo de ramas en GitHub  
**Crear una rama:**
```sh
git branch branchName # Crear una rama
git checkout branchName # Movernos a otra rama 
git checkout -b nombre-de-la-rama # Crear una rama en el repositorio local
git push origin nombre-de-la-rama # Publicar una rama local al repositorio remoto
```

Recuerda que podemos ver gráficamente nuestro entorno y flujo de trabajo local con Git utilizando el comando `gitk`. Gitk fue el primer visor gráfico que se desarrolló para ver de manera gráfica el historial de un repositorio de Git.  

---

## PORTAFOLIO  
Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:  
**Dante Nicolás Martinez**  
**Segundo Semestre Parte 7:**  
- **Video Capítulo 07**: [Ver Video](https://drive.google.com/file/d/13rdccGVNp1cyiximL7PBnzt0obCCID3H/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1mzSJke4-kr2CX3pBBuFbcgwkEeUqq5Wo/view) 

Revisar y ejecutar cada comando, hacerlo como práctica: **NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.**  
**Profesor Ariel Betancud**

---

# CLASE 09 MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9  
## Tarea para antes de las 23 horas:
Investigar cómo se puede clonar un repo con el HTTPS del mismo, es decir, siendo ustedes los dueños del repositorio y desde la nube quieren traer este repo a su ordenador. Nos pedirá **Username** y **password**: ¿qué se debe hacer para lograr cambios y así utilizar `pull`, `push`, y todo lo necesario para trabajar? Como referencia, solo usuario y contraseña no será suficiente, ya que esto cambió desde el año 2021.  

---

## Configurar múltiples colaboradores en un repositorio de GitHub  
Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits ni ramas. Esto quiere decir que pueden copiar tu proyecto pero no colaborar con él si es público. Si el repositorio es privado, es necesario que hagas una invitación, de lo contrario no podrán verlo.  

### Cómo agregar colaboradores en Github
Solo debemos entrar a la configuración de colaboradores de nuestro proyecto:
1. Repositorio > Settings > Collaborators  
2. Ahí, debemos añadir el email o username de los nuevos colaboradores.  

---

## Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar:
```sh
git commit --amend # Corregimos el mensaje
git pull origin main # Traer el repositorio remoto
git push --set-upstream origin main # Ejecutar el cambio, el error arreglado
```

---

## Comienzo del colaborador  
```sh
cd Documentos # Abre git bash
mkdir class-git # Crea la carpeta o directorio de trabajo
ls -al # Revisa los archivos o directorios existentes
```
1. No debe hacer un `git init`; debe buscar el repositorio en el cual está invitado a participar (en GitHub).  
2. Pasa a clonar desde HTTPS, copiando la URL, ya que no se arranca el proyecto desde cero.  
3. En git bash, ejecuta:
   ```sh
   git clone url-copiada-github
   ```
   Si el repositorio es público, no pedirá usuario ni contraseña.  

4. Abrir VSC con:
   ```sh
   code .
   ```
   O bien abrir con vim y modificar:
   ```sh
   vim historia.txt # Escribir: Aquí está un nuevo colaborador
   ```
   Luego:
   ```sh
   ctrl + x # Para salir
   s # Guardar
   enter # Confirmar
   ```

5. Hacer commit:
   ```sh
   git commit -am "Mi primer commit, estoy muy emocionado!!!"
   git pull origin main
   git fetch
   git branch # Ver las ramas disponibles
   git log # Ver toda la historia
   git log --graph # Ver el gráfico de ramas y commits
   git push origin main # Pedirá email y contraseña del colaborador
   ```

6. Si se recibe un **denegado**, significa que no tienes acceso. El dueño del repositorio no te agregó como colaborador.  
   Ve a **Settings > Collaborators** y agrega el correo o username del colaborador.  

7. El colaborador debe aceptar la invitación. Una vez aceptada, podrá hacer push al repositorio.

8. **El dueño no ve los cambios:**  
   ```sh
   git pull origin main
   git fetch
   git log --stat # Ver el primer commit del colaborador
   ```

9. A partir de aquí, el dueño y el colaborador deben repartir el trabajo en ramas. Por ejemplo:
   - El dueño trabaja en la rama `header`
   - El colaborador trabaja en la rama `footer`
   - Al final, se hace un merge para integrar el proyecto completo.

---

## PORTAFOLIO  
Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:  
**Dante Nicolás Martinez**  
**Segundo Semestre Parte 8:**  
- **Video Capítulo 08**: [Ver Video](https://drive.google.com/file/d/1e55H586Q_-znRiJHl7jSuJTud-UVf-ZX/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1Pa8KQK65csbgLEI_BAd2AOdonDarsLBU/view) 

Revisar y ejecutar cada comando, hacerlo como práctica: **NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.**  
**Profesor Ariel Betancud**

---

# CLASE 10 MIÉRCOLES 16 DE OCTUBRE DEL 2024 - Portafolio 10

## Flujo de trabajo profesional
### Haciendo merge de ramas de desarrollo a main

Para poder desarrollar software de manera óptima y ordenada, necesitamos tener un flujo de trabajo profesional que nos permita trabajar en conjunto sin interrumpir el trabajo de otros desarrolladores.

Una buena práctica de flujo de trabajo sería la siguiente:

1. Crear ramas
2. Asignar una rama a cada programador
3. El programador baja el repositorio con `git pull origin master`
4. El programador cambia de rama
5. El programador trabaja en esa rama y hace commits
6. El programador sube su trabajo con `git push origin #nombre_rama`
7. El encargado de organizar el proyecto baja, revisa y unifica todos los cambios

---

## PORTAFOLIO
Vamos a ver unos videos de cómo avanzar en lo que es un portafolio por el Tutor:
**Dante Nicolás Martinez**  
**Segundo Semestre Parte 8:**
- **Video Capítulo 08**: [Ver Video](https://drive.google.com/file/d/1Z80SxVKmkzhzVY5hIxTDtWjHfryHgt1J/view)
- **PDF**: [Ver PDF](https://drive.google.com/file/d/1SwPO2PrveW0DRGXyfzKD9yYWeKJUlCkm/view) 

Revisar y ejecutar cada comando, hacerlo como práctica: **NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.**  
**Profesor Ariel Betancud**
