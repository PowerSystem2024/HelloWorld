
# CLASE 1 MIÉRCOLES 27 DE MARZO DEL 2024

<sub>Lo que vimos en la clase anterior: </sub>
<sub>Abrimos la terminal de Git Bash en Window o la terminal de Ubuntu, tambien la terminal de Mac, y comenzamos con los siguientes comandos y creación de directorios</sub>

```sh
pwd  #Vemos la ruta de la carpeta en la que estamos
cd #Es para navegar a una carpeta: change directory -> cambiar de directorio
cd / #Nos llava al home, en la raíz del disco
cd ~ #La virgulilla significa que estamos en el lugar de los documentos o del usuario
ls #Esto es listar los archivos, nos muestra todos los archivos en la raíz
ls -al #El espacio -al significa que es un argumento especial para ver archivos ocultos
#Usar la flecha hacía arriba nos muestra el último comando utilizado
ls -l #Muestra casi todos los archivos sin los que están ocultos
ls -a #Muestra el grupo de archivos pero no en una lista
clear #Limpia la consola o ctrl + l
cd .. #Nos devuelve a la carpeta anterior
cd U + tab #Esto se usa para un autocompletado o para buscar una referencia
cd /D #Cambiamos de disco en window
df -h #Muestra todos los directorios en Ubuntu
cd /mnt/d #Cambia de directorio usando WSL Ubuntu en window
```

## AHORA COMENZAMOS CON LA CREACIÓN DE CARPETAS

```sh
cd ..
cd ..
cd /mnt/c
cd ~ #Vamos a la raíz
mkdir Tecnicatura #Recordar que en window las mayúsculas no tienen relevancia, pero si en Linux
cd tecnicatura
mkdir Python
mkdir Java
mkdir JavaScript
```
<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>
<sub>Profesor Ariel Betancudz</sub>


# CLASE 2 MIÉRCOLES 3 DE ABRIL DEL 2024

<sub>Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador</sub>

```sh
touch vacio.txt #Crea un archivo con su extención: ESCRIBIR DENTRO
ctrl + s #Guardamos lo que escribimos en el archivo
./ #Significa la carpeta actual
../ #Significa la carpeta anterior
cat vacio.txt #Vemos el contenido del archivo
history #Veremos la historia completa de los comandos que hemos utilizado
!72 + enter #Veremos el comando que utilizamos en ese número
rm vacio.txt #Borra el archivo seleccionado, ¡¡¡¡CUIDADO!!!!
rm --help #Muestra como funciona el comando
```

## CREAR UN REPOSITORIO DE GIT Y HAZ TU PRIMER COMMIT

```sh
cd tecnicatura
mkdir class-git
cd class-git #Entramos en la carpeta que necesitamos trabajar
git init #Creamos un repositorio en la carpeta central, se crea el archivo .git
code .  #Abrimos VSC, el punto hace que se abra el archivo en el que estamos situados
ctrl + n #Creamos un archivo nuevo y escribimos en el, como lo hicimos antes
ctrl + s #Guardamos poniendo el nombre: historia.txt
git status #Vemos el estado del proyecto en tiempo real, esta en el área de trabajo
git add historia.txt #Enviamos el archivo al área de preparación
git status #Para ver el estado de cambios
git rm --cached historia.txt #Quitamos el archivo del área de preparación, cached significa que esta en memoria ram
git config #Tedremos la lista de como funciona la configuración
git config --list #Configuraciones por defecto, faltan cosas importantes
git config --list --show-origin #Veremos donde están las configuraciones guardadas
git config --global user.name "Ariel Betancud"
git config --global user.email "betancudariel@gmail.com" #El correo debe ser el mismo que usaremos en GitHub
git config --list #Ahora veremos que ya están todos los datos completos
git add . #Ingresamos todos los archivos al área de preparación (ram)
git commit -m "Mensaje importante del commit" #El primer commit esta hecho
code . #Hacemos cambios en el archivo y guardamos
git status #Hay cambios para commitear
git add .
git commit -m "Mi segundo commit"
git log historia.txt #Vemos toda la historia de este archivo, el número largo es el hash del commit
```

<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 3 MIÉRCOLES 10 DE ABRIL DEL 2024

<sub>Analizar cambios en los archivos de tu proyecto Git parte 3</sub>

<sub>Ingresamos de la siguiente manera:</sub>

<sub>Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.</sub>

```sh
cd tecnicatura #Ingresamos al direcotorio donde están nuestras carpetas de trabajo
ls #Vemos los archivos y directorios que ya tenemos
cd git #No hay nada
cd .. #Salimos
rm historia.txt #Eliminamos el archivo que habíamos hecho, esto en git bash (window) esto es para practica
rm Git #rm: cannot remove 'Git': Is a directory
rm --recursive -R Git #By default, rm does not remove directories.  Use the --recursive (-r or -R) arguments
option to remove each listed directory, too, along with all of its contents. Esto es para practica
rm --help #Nos muestra lo que les puse arriba como documentación en Inglés.
mkdir class-git #Creamos la carpeta o directorio para trabajar en Git local por ahora.
cd class-git #Entramos para crear el README.md para este sector.
touch README.md #Vamos a crear un archivo nuevo, md significa markdown y se pueden trabajar con editores de texto, este es un lenguaje que transforma el texto a html.
```

<sub>Enlace a la documentación en GitHub de MARKDOWN</sub>

<sub>Leemos la documentación para ir creando en README.md como lo enseña GitHub.</sub>

```sh
code . #Abrimos VSC para editar el archivo.
```

<sub>Empezamos a cargar lo visto en las clases anteriores (Comandos) en el README y pasamos a commitear</sub>

```sh
git status
git add .
git status
git commit -m "Cargamos el README dentro del directorio class-git"
git status
git log #Para ver los dos commits hechos: Si tienes commiteada alguna clase anterior veras mas commits de los que yo tengo.
cd ..
cd ..
```

<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 4 MIÉRCOLES 17 DE ABRIL DEL 2024

<sub>Analizar cambios en los archivos de tu proyecto Git parte 4</sub>

<sub>Ingresamos de la siguiente manera:</sub>

<sub>Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.</sub>

<sub>TAREA -> AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUE PASA CON CADA UNO.</sub>

```sh
cd tecnicatura #Cambia la carpeta actual a la carpeta tecnicatura
cd class-git #Cambia la carpeta class-git
ls #Lista los archivos en la carpeta actual
touch historia.txt #Crea un archivo txt llamado historia
code . #Abre el editor de codigo

#Modificamos el archivo historia.txt colocando lo siguiente: Bienvenido     mi nombre es Ariel (coloca tu nombre)

ctrl + s #Guardar en el editor de codigo
git status #Muestra el estado de nuestros archivos en el repositorio
git add . #Agrega todos los archivos modificados al area de preparación
git status
git commit #Sin agregar -m veremos que pasa #Nos abre el editor de texto para agregar el mensaje

#Agregar mensaje y salir con

Esc #Presionamos Escape 
:wq! + enter #Y ya salimos si estamos en git bash con windows
Esc + shift + z + z #Salimos del mensaje para el commit, en linux, esto anda en algunas terminales

#Agregamos otra línea de mensaje en historia.txt desde VSC: estoy estudiando programación

ctrl + s
git add .
git commit

#Se abre un editor de código basado en línea de comandos, editor de texto como VSC llamado vim

Esc + i #Para comenzar a escribir mensaje del commit, no suele ser necesario
ctrl + x #Para salir en linux
s + enter #Para decir si al cambio y aceptar el nombre, ósea no cambiamos el nombre, la (s) es de si y la (y) es de yes, no olvidar enter en linux
git show #Vemos todos los cambios en el último commit
git log historia.txt #Vemos todos los commit
q #Para salir del registro de commits

#Copiamos un hash mas antoguo y otro reciente, ingresamos el siguiente comando

git diff hash_commit_numerico hash_commit_numerico #Comparamos diferentes commits y sus cambios, poner la versión mas vieja primero, luego la mas nueva
q #Para salir
cd ..
cd ..
```

<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 5 MIÉRCOLES 24 DE ABRIL DEL 2024

## ¿Qué es el staging?

<sub>Tienes una carpeta donde están los archivos de tu proyecto o un directorio y allí tenemos el archivo historia.txt, cuando entramos por consola a ese archivo y creamos el git init, se crea un área en memoria ram que se llama staging, y el otro es el repositorio esta es la carpeta .git donde estarán todos los cambios al final del proyecto.</sub>

<sub>Entonces tenemos el área de trabajo, cuando colocamos git add historia.txt pasamos al staging o área de preparación, que hay que recordar que esto es en la memoria ram y luego con git commit -m "Mensaje" pasa al repositorio en la rama master, allí se genera un nombre llenos de letras y números, es el hash, el nombre del commit.</sub>

## ¿Qué es Gitflow?

<sub>Gitflow es un modelo alternativo de creación de ramas en Git en el que se utilizan ramas de función y varias ramas principales. Fue Vincent Driessen en nvie quien lo publicó por primera vez y quien lo popularizó.</sub>

## ¿Qué es branch (rama) y cómo funciona un merge en git?

<sub>Tenemos una rama llamada master y es donde están los cambios de nuestros archivos, con cada commit creamos una nueva versión</sub>


<sub>Vamos a crear una rama experimental para otras versiones que suele llamarse development, al encontrar bug, se crea otra rama que suele llamarse hotfix para hacer reparaciones, siempre que ya tengamos resultados favorables, es donde decidimos hacer un merge, es unir los resultados de las ramas a la rama master.</sub>

<sub>La principal característica de las ramas principales es que solo existe una de cada tipo. El objetivo es que no se instancien y que no reciban código de forma directa a través de commit, siempre tienen que recibir código a través de ramas de tipo Feature, Release y Hotfix, siempre a través de ramas auxiliares.</sub>

<sub>Es un riesgo recibir código directamente en la rama Master, porque puede generar defectos en el repositorio en las subidas a producción, que no contemplemos o que no preveamos, por lo que siempre es mejor integrar código en otras ramas antes de integrar con las ramas Master y Develop.</sub>

<sub>Esta es una metodología estricta pero que da lugar a diferentes interpretaciones o diferentes formas de llevarla en cada equipo, por lo que en algunos casos, algún experto puede permitirse no seguir esa norma, pero son casos muy específicos y siempre de personas de confianza.</sub>

<sub>En las ramas auxiliares tenemos la rama Feature, la rama Release y la Rama Hotfix, que puede instanciarse todas las veces que se consideren necesarias:</sub>

<sub>
- La rama Feature, para nuevas características, nuevos requisitos o nuevas historias de usuario.
- La rama Release, para estandarizar o cortar una serie de código que ha estado desarrollándose en la rama Develop, se saca una rama de este tipo, se mergea y ahí se depura.
- La rama Hotfix, que habitualmente se utiliza para código para depurar el código que venga de producción, por haberse detectado un defecto crítico en producción que deba resolverse, al que se le va a hacer una Release puntual para corregirlo.
</sub>

<sub>Estas ramas tienen un principio y un fin, ya que son ramas que se mergean con las ramas Master y Develop y desaparecen.</sub>


<sub>Podemos tener tantas ramas como queramos, tantos repositorios como queramos, lo más importante es saber cuando hacemos un merge, porque es posible que hayan archivos que rompan otros archivos, a esto se lo llama conflicto o bug.</sub>


<sub>Hoy a sido un poco de teoría, repaso de todo lo que les dió la profe Naty.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 5 MIÉRCOLES 8 DE MAYO DEL 2024

<sub>Volver en el tiempo en nuestro repositorio utilizando reset y checkout parte 6</sub>

<sub>Ingresamos de la siguiente manera:</sub>

<sub>Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.</sub>

<sub>TAREA -> AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUE PASA CON CADA UNO.</sub>

```sh
cd tecnicatura #Cambia directorio actual al directorio tecnicatura
cd class-git #Cambia directorio actual al directorio class-git
ls #Muestra una lista de los contenidos del directorio actual
code . #Abre editor de texto o codigo por default en la carpeta actual 
git log #Vemos los commit hechos hasta ahora
Copiar el hash #El número largo que tiene el commit
git reset hash-nombre-commit #Este nos permite volver a una versión anterior, hay 2 tipos de reset: el duro y el suave
git status #Nos muestra los archivos modificados que están en el area de preparacion y los que no esten en el mismo.
git add . #Agrega los archivos modificados al area de preparacion
git commit -m "Agregamos datos de estudios en historia.txt" #Agrega el archivo en el area de preparacion al repositorio en la rama q se encuentre
git config --list #Veremos la configuración que ya hemos hecho con en nombre y email
git reset hash-nombre-commit --hard #Es el duro, todo vuelve a su estado anterior, es el más usado, desaparece todo
git reset hash-nombre-commit --soft #Este es el suave, lo que tengamos en staging segirá allí
```

<sub>crear un archivo portafolio.html e introducir el código basico</sub>

```sh
touch portafolio.html #crea un archivo html llamado portafolio
html : 5 #Con esto se carga el código básico de html y modificamos
ctrl + s #Guardamos
```

<sub>Clic derecho en VSC Open with Live Server para ver en el navegador</sub>

```sh
git status
ls
ls -al #Muestra una lista de los contenidos del directorio actual como una lista incluyendo archivos ocultos
git add .
git status
git commit -m "Agregamos el html para nuestro portafolio"
```

<sub>creamos CSS, este es un archivo de estilos, para esto creamos una nueva carpeta llamada css</sub>

```sh
mkdir css
ls
cd css
touch style.css #creamos un archivo dentro: estilos.css le cargamos el código.
ctrl + s #abrimos en el navegador y todo esta allí, pero todo esto supuestamente en git no existe.
git status #tenemos cosas en el área de trabajo, en staging distintas
git diff + enter #y nos muestra los cambios en memoria ram y en disco
git add . #Agregamos todo al staging
git status #Ya esta todo en memoria ram, a git solo le importan los archivos, guarda las carpetas como rutas y automaticamente las crea
git commit -m "Creamos el css para darle algo de estilo a nuestro portafolio"
git log #vemos lo nuevo que hemos hecho sin lo que borramos con el reset fuerte
hacer cambios en historia.txt #Cambiamos la última línea y
ctrl + s 
git diff
git commit -am "cambio en la última línea del historia.txt"
git log
q  #Esto para salir
git log --stat #veremos los cambios especificos que hicimos en cuales archivos por medio del commit y veremos los cambios en bits
q #salimos de la línea de commits, ahora queremos ver como era originalmente el archivo, osea la primera versión, copiamos el nombre del primer commit
git checkout hash-nombre-commit historia.txt #Veremos el archivo en su estado original
git status #Nos sugiere hacer un commit, si lo hacemos borramos todo lo que hicimos antes, debemos seguir con el siguiente commando
git checkout master historia.txt #Volvemos a la versión master del archivo historia.txt, esto es muy peligroso
git checkout hash-nombre-commit historia.txt #Volvemos a hacer esto y cambiamos cosas del archivo
git commit -am "Reemplazo de una versión por otra de la historia"
git log #Veremos los cambios sin tocar ningun otro archivo, esta es la forma de volver a una versión hacía atrás y llevarla a la cabeza de la master
cd ..
cd ..
```

<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 6 MIÉRCOLES 15 DE MAYO DEL 2024

<sub>Git reset vs. Git rm parte 7</sub>

<sub>Los comandos git reset y git rm tienen utilidades muy diferentes, pero pueden confundirse fácilmente.</sub>

## GIT RESET

<sub>El comando git reset es una herramienta poderosa que te permite deshacer o revertir cambios en tu repositorio de Git. Lo puedes ejecutar de tres maneras diferentes, con las líneas de commando --soft, --mixed y --hard.</sub>

<sub>Pero como git checkout que nos deja ir, mirar, pasear y volver. Con git reset volvemos al pasado sin la posibilidad de volver al futuro. Borramos la historia y la debemos sobreescribir. No hay vuelta atrás.</sub>


<sub>Tres árboles en Git Para entender lo anterior, recordemos que los “tres árboles” de Git son estructuras de datos basadas en nodos y punteros que Git utiliza para hacer seguimiento a un cronograma de ediciones, aunque no sean estructuras en forma de árbol en el sentido tradicional.</sub>

<sub>La mejor forma de entender estos mecanismos es creando un conjunto de cambios en un repositorio y siguiéndolos a través de los tres árboles. Averigüémoslo.</sub>

<sub>Ingresamos de la siguiente manera:</sub>

<sub>Abrir git bash en Window o la terminal de Linux o de Mac: al abrir Git Bash hacerlo como administrador, en terminal también o usar sudo para permisos especiales.</sub>

<sub>TAREA -> AGREGAR LOS COMENTARIOS EN LOS COMANDOS, PARA SABER QUE PASA CON CADA UNO.</sub>

```sh
mkdir git_reset_test #Vamos a hacer pruebas, es por esto que creamos una carpeta nueva
cd git_reset_test #Entramos en la carpeta
git init #Inicializamos el repositorio
touch reset_file.txt
git add reset_file.txt
git commit -m"Iniciando el primer commit"
```

<sub>¿Cómo funciona Git Reset en tu flujo de trabajo?</sub>

<sub>Git reset permite moverte entre diferentes commits para deshacer o rehacer cambios. Git guarda todo lo nuevo del repositorio como commits, que son instantáneas del estado del código en un momento dado y existen variaciones de este comando.</sub>

### Variaciones de Git Reset 

```sh
git reset --soft: #Borra el historial y los registros de Git de commits anteriores, pero guarda los cambios en Staging para aplicar las últimas actualizaciones a un nuevo commit. 
git reset --hard: #Deshace todo, absolutamente todo. Toda la información de los commits y del área de staging se elimina del historial. 
git reset --mixed: #Borra todo, exactamente todo. Toda la información de los commits y del área de staging se elimina del historial. 
git reset HEAD: #El comando git reset saca archivos del área de staging sin borrarlos ni realizar otras acciones. Esto impide que los últimos cambios en estos archivos se envíen al último commit. Podemos incluirlos de nuevo en staging con git add si cambiamos de opinión. Ten en cuenta que, si deshaces commits en un repositorio compartido en GitHub, estarás cambiando su historia y esto puede causar problemas de sincronización con otros colaboradores.
```

### ¿Qué es git reset HEAD? 

<sub>git reset HEAD es un comando que te permite revertir los cambios que ya habías preparado para subir, y moverlos de vuelta a tu proyecto. Con este comando puedes cancelar los cambios que ya habías agregado, para que puedas revisarlos, modificarlos o deshacerlos antes de confirmarlos con un commit.</sub>

<sub>git rm Por otro lado, es un comando que nos ayuda a eliminar archivos de Git sin eliminar su historial del sistema de versiones. Para recuperar el archivo eliminado, necesitamos retroceder en la historia del proyecto, recuperar el último commit y obtener la última confirmación antes de la eliminación del archivo.</sub>

<sub>Es importante tener en cuenta que git rm no puede usarse sin evaluarlo antes. Debemos usar uno de los flags siguientes para indicarle a Git cómo eliminar los archivos que ya no necesitamos en la última versión del proyecto.</sub>

### Variaciones de Git rm

```sh
git rm --cached: #Elimina archivos del repositorio local y del área de staging, pero los mantiene en el disco duro. Deja de trackear el historial de cambios de estos archivos, por lo que quedan en estado untracked, que significa: que un archivo no está siendo rastreado por Git
git rm --force: #Elimina los archivos de Git y del disco duro. Git guarda todo, por lo que podemos recuperar archivos eliminados si es necesario (empleando comandos avanzados). ¡Al usar git rm lo que haremos será eliminar este archivo completamente de git!
```

### ¿Cuál es la diferencia entre git rm y git reset Head? 


<sub>La diferencia principal entre git rm y git reset HEAD radica en que git rm elimina archivos del repositorio y de la historia del proyecto, mientras que git reset saca los cambios del área de preparación y los mueve del espacio de trabajo, sin afectar la historia del repositorio.</sub>

<sub>Es importante tener en cuenta el efecto que cada comando tiene en el proyecto y usarlos según tus necesidades y objetivos específicos.</sub>

### ¿Cuándo utilizar git reset en lugar de git revert? 

<sub>Para reescribir la historia del repositorio y eliminar confirmaciones anteriores, se utiliza git reset. Para deshacer cambios de confirmaciones anteriores de forma segura sin modificar la historia del repositorio, se emplea git revert.</sub>


<sub>Resumen Para evitar problemas en el trabajo, es valioso entender las implicaciones y riesgos de cada comando y elegir el enfoque adecuado según las necesidades y el flujo de trabajo del proyecto.</sub>

<sub>Con git rm eliminamos un archivo de Git, pero mantenemos su historial de cambios. Si no queremos borrar un archivo, sino dejarlo como está y actualizarlo después, no debemos usar este comando en este commit.</sub>

<sub>Empleando git reset HEAD, movemos los cambios de Staging a Unstaged, pero mantenemos el archivo en el repositorio con los últimos cambios en los que hicimos commit. Así, no perdemos nada relevante.</sub>

<sub>Siguientes pasos Bueno, todos los cambios están en el área de Staging, incluido el archivo con los cambios que no están listos. Esto significa que debemos sacar ese archivo de Staging para poder hacer commit de todos los demás.</sub>
<sub>Crear cambios en el archivo creado, donde vamos a hacer varios commits, para ir probando los nuevos comandos, al finalizar las pruebas, eliminar el directorio con todo su contenido.</sub>


<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 7 MIÉRCOLES 22 DE MAYO DEL 2024

<sub>Flujo de trabajo básico con un repositorio remoto parte 8</sub>

<sub>Cuando empiezas a trabajar en un entorno local, el proyecto vive únicamente en tu computadora. Esto significa que no hay forma de que otros miembros del equipo trabajen en él.</sub>

<sub>Para solucionar esto, utilizamos los servidores remotos: un nuevo estado que deben seguir nuestros archivos para conectarse y trabajar con equipos de cualquier parte del mundo.</sub>

<sub>Estos servidores remotos pueden estar alojados en GitHub, GitLab, BitBucket, entre otros. Lo que van a hacer es guardar el mismo repositorio que tienes en tu computadora y darnos una URL con la que todos podremos acceder a los archivos del proyecto. Así, el equipo podrá descargarlos, hacer cambios y volverlos a enviar al servidor remoto para que otras personas vean los cambios, comparen sus versiones y creen nuevas propuestas para el proyecto.</sub>

<sub>Esto significa que debes aprender algunos nuevos comandos</sub>

## Comandos para trabajo remoto con GIT

```sh
git clone url_del_servidor_remoto #Nos permite descargar los archivos de la última versión de la rama principal y todo el historial de cambios en la carpeta .git
git push #Luego de hacer git add y git commit debemos ejecutar este comando para mandar los cambios al servidor remoto.
git fetch #Lo usamos para traer actualizaciones del servidor remoto y guardarlas en nuestro repositorio local (en caso de que hayan, por supuesto).
git merge #También usamos el comando git merge con servidores remotos. Lo necesitamos para combinar los últimos cambios del servidor remoto y nuestro directorio de trabajo.
git pull #Básicamente, git fetch y git merge al mismo tiempo.
```

<sub>Adicionalmente, tenemos otros comandos que nos sirven para trabajar en proyectos muy grandes:</sub>

```sh
git log --oneline #Te muestra el id commit y el título del commit.
git log --decorate #Te muestra donde se encuentra el head point en el log.
git log --stat #Explica el número de líneas que se cambiaron brevemente.
git log -p #Explica el número de líneas que se cambiaron y te muestra que se cambió en el contenido.
git shortlog #Indica que commits ha realizado un usuario, mostrando el usuario y el título de sus commits.
git log --graph --oneline --decorate --all
git log --pretty=format #"%cn hizo un commit %h el dia %cd": Muestra mensajes personalizados de los commits.
git log -3 #Limitamos el número de commits.
git log --after=“2018-1-2”
git log --after=“today” 
git log --after=“2018-1-2” --before=“today” #Commits para localizar por fechas.
git log --author=“Name Author” #Commits hechos por autor que cumplan exactamente con el nombre.
git log --grep=“INVIE” #Busca los commits que cumplan tal cual está escrito entre las comillas.
git log --grep=“INVIE” –i #Busca los commits que cumplan sin importar mayúsculas o minúsculas.
git log – index.html #Busca los commits en un archivo en específico.
git log -S “Por contenido” #Buscar los commits con el contenido dentro del archivo.
git log > log.txt #guardar los logs en un archivo txt
```

<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Parte 2:</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
</sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 8 MIÉRCOLES 29 DE MAYO DEL 2024

## Introducción a las ramas o branches de Git parte 9

<sub>Cuando entramos en el proyecto veremos que nos encontramos con la rama master, y es a partir de allí que debe saber que esta es la rama madre o principal rama, y las otras ramas se crean para no afectar a la master</sub>

<sub>Las ramas (branches) son la forma de hacer cambios en nuestro proyecto sin afectar el flujo de trabajo de la rama principal. Esto porque queremos trabajar una parte muy específica de la aplicación o simplemente experimentar.</sub>

<sub>La cabecera o HEAD representan la rama y el commit de esa rama donde estamos trabajando. Por defecto, esta cabecera aparecerá en el último commit de nuestra rama principal. Pero podemos cambiarlo al crear una rama (git branch rama, git checkout -b rama) o movernos en el tiempo a cualquier otro commit de cualquier otra rama con los comandos (git reset id-commit, git checkout rama-o-id-commit).</sub>

<sub>Repasa: ¿Qué es Git?</sub>

## Cómo funcionan las ramas en GIT
<sub>Las ramas son la manera de hacer cambios en nuestro proyecto sin afectar el flujo de trabajo de la rama principal. Esto porque queremos trabajar una parte muy específica de la aplicación o simplemente experimentar.</sub>

```sh
git branch nombre de la rama #Con este comando se genera una nueva rama.
git checkout nombre de la rama #Con este comando puedes saltar de una rama a otra.
git checkout -b rama #Genera una rama y nos mueve a ella automáticamente, Es decir, es la combinación de git branch y git checkout al mismo tiempo.
git reset id-commit #Nos lleva a cualquier commit no importa la rama, ya que identificamos el id del tag., eliminando el historial de los commit posteriores al tag seleccionado.
git checkout rama-o-id-commit #Nos lleva a cualquier commit sin borrar los commit posteriores al tag seleccionado.
```

<sub>Vamos a hacer una practica: mientras la rama master esta cambiando normalmente, vamos a crear una rama paralela que va a crear nuevas secciones: osea una sección y a esta rama la vamos a llamar segunda y con esto, la vamos a fusionar para ver como queda en la rama master y así entender el flujo de ramas entre git. Al crear otra rama estamos creando una copia de todos los commit que ya tiene la rama master en la nueva rama y todos los cambios que hagamos en esta nueva rama, no los va a ver la rama master hasta que no la volvamos a fusionar con un proceso que se llama merge.</sub>

```sh
Abrir terminal #En ubuntu
Abrir como adminstrados git bash #En window
cd Tecnicatura
cd class-git
code . #En ubuntu
code . #En window, abrir como administrador
ctrl + s #Guardamos
clic mouse derecho #Abrimos en el navegador con Live Server vemos los cambios
git status
git commit -am "mensaje del commit" #Este solo funciona con archivos creado previamente
git commit -a -m "Mensaje del commit" #Esto es lo mismo que el anterior
git commit -a + enter #Se abrira el entorno para editar el vim con el mensaje
Escribir el mensaje
ctrl + x
s + enter #No cambiar el nombre ni ruta de ubicación
git log #Veremos los cambios guardados
q #Para salir
git log --stat #Veremos los cambios nombrando cada archivo
q #Para salir
git branch #Muestra en la rama que estamos, desde aquí crearemos una nueva
git show #Muestra el último cambio que hicimos, esto significa que desde el HEAD -> master es que haremos cambios
q #Para salir
ctrl + l #Limpiamos consola
git branch segunda #creamos una nueva rama
git show #Nos muestra ahora que esta en el HEAD -> master, cabecera aquí es donde esta apuntando, es decir el último commit esta pegado a dos ramas distintas, aunque todavía estemos en master
q #Para salir
git status #No hay nada para hacer commit
git chekout segunda #Nos movemos hacía otras ramas, en este caso a segunda, esto no se ve en mac ni en ubuntu, para ver donde estamos hay que ingresar...
git branch #veremos en que rama estamos ubicados o ingresando...
git status #Veremos en que HEAD estamos apuntando
VSC #hacemos cambios que veremos con Nico
```

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Parte 2:</sub>

<sub>Introducción</sub>
<sub>Practica</sub>
<sub>PDF</sub>

```sh
ctrl + s 
F5 #Actualizamos en el navegador para ver los cambios
git status #Veremos el archivo que modificamos
git add .
git commit
vim escribimos el mensaje del commit
ctrl + x
s #Para un si 
enter #Terminado el mensaje del commit
git status #No hay mas nada para commitear y estamos en la rama segunda
git show #Vemos todo lo que cambiamos
q #Para salir
git log #Nos muestra donde estabamos con la rama master y el HEAD paso a la rama cabecera
q #Para salir
git checkout master #Volvemos a la rama master, desaparese lo que habíamos hecho
git log #No muestra lo que hicimos en el portafolio
q #Para salir
git checkout segunda #Volvemos a ver todos los cambios que hicimos de nuevo
```

<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>


<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>



# CLASE 9 MIÉRCOLES 5 DE JUNIO DEL 2024

## Fusión de ramas con Git merge parte 10

<sub>La fusión en Git es la forma en que este sistema une un historial bifurcado. El comando git merge permite integrar líneas de desarrollo independientes generadas por git branch en una sola rama. Con este comando, podemos crear un nuevo commit que combina dos ramas o branches: la rama actual y la rama que se indica después del comando.</sub>

<sub>Estos comandos de fusión del merge afectan solo a la rama actual y no a la rama de destino. Por lo tanto, te recomendamos utilizar git checkout para seleccionar la rama actual y git branch -d para eliminar la rama de destino obsoleta.</sub>


## Funcionamiento de Git merge

<sub>Git merge fusiona secuencias de confirmaciones en un solo historial, generalmente para combinar dos ramas. Busca una confirmación de base común y genera una confirmación de fusión que representa la combinación de las dos ramas hasta el resultado final.</sub>


## ¿Cómo unir dos ramas en git?

<sub>Ahora bien, para combinar ramas en tu repositorio local, usa git checkout para cambiar a la rama donde deseas fusionar. Por lo general, esta es la rama principal. Luego, emplea git merge y especifica el nombre de la otra rama que deseas traer a esta rama. Ten en cuenta que esto es una combinación de avance rápido.</sub>

## ¿Cómo realizar un merge en git?

<sub>Para hacer un merge en Git, primero asegúrate de estar en la rama correcta. Después, usa el comando git merge seguido del nombre de la rama que quieres combinar. Por ejemplo, si quieres crear un nuevo commit en la rama master con los cambios de la rama segunda, usa este comando:

```sh
git checkout master
git merge segunda
```

<sub>Es importante tener en cuenta que en caso de haber conflictos, debes guardar tus cambios antes de hacer git checkout para evitar perder tu trabajo. También es recomendable emplear los comandos básicos de GitHub, como git fetch, git push y git pull, para mantener actualizado tu repositorio.</sub>

<sub>En este ejemplo, vamos a crear un nuevo commit en la rama master combinando los cambios de una rama llamada segunda: Otra opción es crear un nuevo commit en la rama segunda combinando los cambios de cualquier otra rama:</sub>

<sub>Git es asombroso porque puede saber cuáles cambios deben conservarse en una rama y cuáles no. En casos de conflictos, asegúrate de guardar tus cambios antes de hacer git checkout para evitar perder tu trabajo.</sub>

## Comandos básicos de GitHub:

```sh
git init # crear un repositorio, si ya esta en la nube traerlo sin hacer git init
git add . #agregar un archivo a staging.
git commit -m “mensaje” #guardar el archivo en git con un mensaje.
git branch nombre_rama #crear una nueva rama.
git checkout nombre_rama #moverse entre ramas.
git push origin rama #mandar cambios a un servidor remoto.
git fetch #traer actualizaciones del servidor remoto y guardarlas en nuestro repositorio local.
git merge rama #tiene dos usos. Uno es la fusión de ramas, funcionando como un commit en la rama actual, trayendo la rama indicada. Su otro uso es guardar los cambios de un servidor remoto en nuestro directorio.
git pull origin rama #fetch y merge al mismo tiempo.
git checkout “codigo de version” “nombre del archivo” #volver a la última versión de la que se ha hecho commit.
git reset #vuelve al pasado sin posibilidad de volver al futuro, se debe usar con especificaciones.
git reset --soft #vuelve a la versión en el repositorio, pero guarda los cambios en staging. Así, podemos aplicar actualizaciones a un nuevo commit.
git reset --hard #todo vuelve a su versión anterior
git reset HEAD #saca los cambios de staging, pero no los borra. Es lo opuesto a git add.
git rm #elimina los archivos, pero no su historial. Si queremos recuperar algo, solo hay que regresar. se utiliza así:
git rm --cached #elimina los archivos en staging pero los mantiene en el disco duro.
git rm --force #elimina los archivos de git y del disco duro.
git status #estado de archivos en el repositorio.
git log #historia entera del archivo.
git log --stat #cambios específicos en el archivo a partir de un commit.
git show #cambios históricos y específicos hechos en un archivo.
git diff “codigo de version 1” “codigo de version 2” #comparar cambios entre versiones.
git diff #comparar directorio con staging.
```

<sub>Comando en producción: TUVE QUE SOLUCIONAR UN CONFLICTO</sub>

```sh
git status #En rama segunda: hacemos cambios en el archivo y guardamos
git commit -am "Finalizado el cambio en rama segunda" #enter
git status
git checkout master #perdemos todo lo que ya habíamos hecho, hacemos cambios en el archivo agregando un nuevo parrafo y guardamos
git commit -am "Agregado el contenido adicional del archivo y un mejor aporte"
git checkout segunda #vemos como desaparecen los cambios
git checkout master #Aquí es que vamos a hacer el merge
git merge segunda #En mi caso tuve algunos conflictos que solucione a través de VSC, aclaro que nunca debemos utilizar Fusionar los dos cambios
git commit -am "Arreglando conflicto" #Una vez solucionado debemos commitear
git status #Debemos revisar en el navegador y en el código si algo quedo mal y cambiarlo
git commit -am "Solucionado el conflicto 2"
git merge segunda #ahora todo va bien
git commit -am "Volvi a comentar en este caso de mi area laboral" #Añado información al archivo
git log
q #Para salir
git commit -am "Para guardar estos cambios en el README.md"
git checkout segunda
git merge master #Traemos todos los cambios
git commit -am "Cargamos esto ahora" #vamos a master y mergeamos
git checkout master
git merge segunda #y terminamos con esto
```

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>
<sub>Parte 4:</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
<sub>PDF</sub>


<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 10 MIÉRCOLES 12 DE JUNIO DEL 2024

## Resolución de conflictos al hacer merge parte 11

### Sección lectura

<sub>Git nunca borra nada, a menos que nosotros se lo indiquemos. Cuando usamos los comandos git merge o git checkout estamos cambiando de rama o creando un nuevo commit, no borrando ramas ni commits (recuerda que puedes borrar commits con git reset y ramas con git branch -d).</sub>

<sub>Git es muy inteligente y puede resolver algunos conflictos automáticamente: cambios, nuevas líneas, entre otros. Pero algunas veces no sabe cómo resolver estas diferencias, por ejemplo, cuando dos ramas diferentes hacen cambios distintos a una misma línea.</sub>

<sub>Esto lo conocemos como conflicto y lo podemos resolver manualmente. Solo debemos hacer el merge, ir a nuestro editor de código y elegir si queremos quedarnos con alguna de estas dos versiones o algo diferente. Algunos editores de código como Visual Studio Code nos ayudan a resolver estos conflictos sin necesidad de borrar o escribir líneas de texto, basta con hacer clic en un botón y guardar el archivo.</sub>

<sub>Recuerda que siempre debemos crear un nuevo commit para aplicar los cambios del merge. Si Git puede resolver el conflicto, hará commit automáticamente. Pero, en caso de no pueda resolverlo, debemos solucionarlo y hacer el commit.</sub>

<sub>Los archivos con conflictos por el comando git merge entran en un nuevo estado que conocemos como Unmerged. Funcionan muy parecido a los archivos en estado Unstaged, algo así como un estado intermedio entre Untracked y Unstaged. Solo debemos ejecutar git add para pasarlos al área de staging y git commit para aplicar los cambios en el repositorio.</sub>

<sub>Cómo revertir un merge Si nos hemos equivocado y queremos cancelar el merge, debemos usar el siguiente comando:</sub>

```sh
git merge --abort
```

<sub>Conflictos en repositorios remotos Al trabajar con otras personas, es necesario utilizar un repositorio remoto.</sub>

<sub>­
-Para copiar el repositorio remoto al directorio de trabajo local, se utiliza el comando git clone , y para enviar cambios al repositorio remoto se utiliza git push.</sub>

<sub>-Para actualizar el repositorio local se hace uso del comando git fetch, luego se debe fusionar los datos traídos con los locales usando git merge.</sub>

<sub>Para traer los datos y fusionarlos a la vez, en un solo comando, se usa git pull.</sub>

<sub>­- Para crear commits rápidamente, fusionando git add y git commit -m "", usamos git commit -am "".</sub>

<sub>­- Para generar nuevas ramas, hay que posicionarse sobre la rama que se desea copiar y utilizar el comando git branch .</sub>

<sub>Para saltar entre ramas, se usa el comando git checkout</sub>

<sub>­- Una vez realizado los cambios en la rama, estas deben fusionarse con git merge.</sub>

<sub>El merge ocurre en la rama en la que se está posicionado. Por lo tanto, la rama a fusionar se transforma en la principal.</sub>

<sub>Los merges también son commits.</sub>

<sub>Los merges pueden generar conflictos, esto aborta la acción y pide que soluciones el problema manualmente, aceptando o rechazando los cambios que vienen.</sub>

<sub>Repasa qué es un branch</sub>


### Sección Práctica

```sh
git checkout segunda #falta lo que cargamos en master
git merge master #traemos los cambios desde la master y tenemos las dos ramas actualizadas
```

<sub>Ahora vamos a crear un conflicto para ver como salimos de el, vamos a cargar datos nuevos creando archivos html y css estando en la rama segunda, y también vamos a hacer lo mismo estando en la master y veremos como lo solucionamos.</sub>


<sub>Abrimos el html y modificamos estando en la rama segunda</sub>

<sub>Luego commiteamos en la rama segunda y pasamos a la rama master, guardar y commitear, hacer un merge estando en master: pongo en orden los comandos abajo.</sub>

```sh
ctrl + s #Guardamos los cambios en la rama segunda, ponemos cambios en css
git commit -am "Modifique el css y el color del texto" es un ejemplo
git checkout master #Modificamos el html, ponemos código y css ponemos texto blue
ctrl + s #Guardamos los cambios
git commit -am "Agregue suscripción, cambie el código y puse todo azul en css"
git merge segunda #Hacemos un merge estando en master y veremos el conflicto
```

<sub>Para solucionar el conflicto podemos abrir el archivo con el editor de texto y modificar lo que nos este señalando y guardamos, esto en el css y en el html, lo podemos hacer desde VSC seleccionando: el cambio entrante.</sub>


<sub>Debemos ahora commitear estos cambios, abajo pongo los comandos.</sub>

```sh
git status
git commit -am "Solución de conflictos al mergear las ramas"
git checkout segunda #Seguiremos con la versión anterior, porque el merge fue en master
git merge master #Ahora pasamos los cambios a la rama segunda.
```

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Parte 4:</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
<sub>PDF</sub>


<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 12 MIÉRCOLES 19 DE JUNIO DEL 2024 - Portafolio 6

## Cómo funcionan las llaves públicas y privadas parte 12

### Sección lectura

<sub>Las llaves públicas y privadas, conocidas también como cifrado asimétrico de un solo camino, sirven para mandar mensajes privados entre varios nodos con la lógica de que firmas tu mensaje con una llave pública vinculada con una llave privada que puede leer el mensaje.</sub>

<sub>Las llaves públicas y privadas nos ayudan a cifrar y descifrar nuestros archivos de forma que los podamos compartir sin correr el riesgo de que sean interceptados por personas con malas intenciones.</sub>

<sub>Cómo funciona un mensaje cifrado con llaves públicas y privadas Ambas personas deben crear su llave pública y privada.</sub>

<sub>Ambas personas pueden compartir su llave pública a las otras partes (recuerda que esta llave es pública, no hay problema si la “interceptan”).</sub>

<sub>La persona que quiere compartir un mensaje puede usar la llave pública de la otra persona para cifrar los archivos y asegurarse que solo puedan ser descifrados con la llave privada de la persona con la que queremos compartir el mensaje.</sub>

<sub>El mensaje está cifrado y puede ser enviado a la otra persona sin problemas en caso de que los archivos sean interceptados.</sub>

<sub>La persona a la que enviamos el mensaje cifrado puede emplear su llave privada para descifrar el mensaje y ver los archivos.</sub>

<sub>Nota: puedes compartir tu llave pública, pero nunca tu llave privada.</sub>


## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Parte 4:</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
<sub>PDF</sub>


<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 13 MIÉRCOLES 26 DE JUNIO DEL 2024 - Portafolio 7

## Configura tus llaves SSH en local parte 13

<sub>Si usamos GitHub solo con usuario y contraseña, si un día perdemos nuestra PC, perdemos todo, nuestras contraseñas y los proyectos de nuestros clientes están todos en riesgo. Esta es la forma en que muchos sitios web son jackeados, para evitar esto tenemos que agregar una capa de seguridad mucho más fuerte. Es aquí donde podemos comenzar a crear el entorno con llaves publicas y privadas. Esto tiene una ventaja, no solo es que nuestra seguridad será más fuerte, si no que ya no tendrás que poner nunca más tu usuario y contraseña.</sub>


<sub>En nuestra maquina, debemos crear una llave privada y otra pública, una vez creada la llave pública se la enviamos a GitHub en nuestro repositorio, y le decimos: para este repositorio quiero que uses esta llave pública, de mi llave privada en mi PC, todo esto lo conectamos por un protocolo nuevo, en vez de conectarnos al repositorio por HTTPS, vamos a conectarnos por un protocolo que se llama SSH.</sub>


<sub>En la primera conección GitHub se va a dar cuenta que le mandaste una llave publica que esta relacionada con tu llave privada y nos va a enviar cifrada con nuestra llave pública su propia llave pública de GitHub, porque GitHub también tiene una llave privada, todo esto sucederá automaticamente, a la llave privada que nosotros tenemos, se le puede hacer una contraseña encima, para añadir más seguridad para hacerla mas fuerte y más poderosa.</sub>


<sub>Las llaves SSH no son por repositorio o por proyecto, si no que es por persona, ahora vamos a crear unas llaves exclusivamente para nosotros.</sub>

<sub>En este ejemplo, aprenderemos cómo configurar nuestras llaves SSH en local.</sub>

#### Comandos:

```sh
abrir git bash #Esto en window
abrir terminal #En ubuntu, y nos quedamos sin entrar a ningun proyecto o carpeta.
git config -l #Recordamos nuestra configuración en Git, podemos hacer esto estando en la ruta de cualquier sitio en nuestro PC
git config --global user.email "alumnos@mail.com" #Actualizamos el correo que usamos en GitHub.
ssh-keygen -t rsa -b 4096 -C "alumnos@mail.com" #Dira que esta generando la llave pública y privada, también nos pregunta donde vamos a guardar la llave, presionamos enter, nos va a pedir otra contraseña
eval $(ssh-agent -s) #Encendemos el servidor de llaves SSH, ya esta corriendo
~ #Se utiliza virgulilla para poner la ruta, es una variable que tiene el nombre de nuestra carpeta home, esto para el siguiente comando
ssh-add ~/.ssh/id_ga35745 #Añadimos la llave, no la .pub ponemos la llave privada, recordar que es una ruta, se debe poner el nombre de la carpeta que contiene la clave privada.
```

#### Cómo generar tus llaves SSH:

<sub>a. Generar tus llaves SSH**</sub>

<sub>Recuerda que es muy buena idea proteger tu llave privada con una contraseña.</sub>

```sh
ssh-keygen -t rsa -b 4096 -C "tu@email.com"
```

<sub>b. Terminar de configurar nuestro sistema.</sub>

<sub>En Windows y Linux:</sub>

<sub>Encender el “servidor” de llaves SSH de tu computadora:</sub>

```sh
eval $(ssh-agent -s)
```

<sub>Añadir tu llave SSH a este “servidor”:</sub>

```sh
ssh-add ruta-donde-guardaste-tu-llave-privada
```

<sub>En Mac:</sub>

<sub>Encender el “servidor” de llaves SSH de tu computadora:</sub>

```sh
eval "$(ssh-agent -s)"
```

<sub>Si usas una versión de OSX superior a Mac Sierra (v10.12), debes crear o modificar un archivo “config” en la carpeta de tu usuario con el siguiente contenido (ten cuidado con las mayúsculas): vim config</sub>

```sh
Host *
AddKeysToAgent yes
UseKeychain yes
IdentityFile ruta-donde-guardaste-tu-llave-privada
```

<sub>Añadir tu llave SSH al “servidor” de llaves SSH de tu computadora (en caso de error puedes ejecutar este mismo comando pero sin el argumento -K):</sub>

```sh
ssh-add -K ruta-donde-guardaste-tu-llave-privada
```

<sub>Por último les quiero hablar del 2FA: Segundo Factor de Autenticación. Este se puede hacer con varios dispositivos, y deberías hacerlo, ante el robo o perdida de un celular o ordenador, deberías tener un respaldo ante esto, este 2FA se puede hacer con diferentes generadores de códigos  de seguridad.</sub>

<sub>Para añadir un 2FA:</sub>

1. Clic en nuestro perfil, arriba y a la derecha, seleccionamos...
2. Settings
3. Password and Authentication
4. GitHub Mobile: GitHub Mobile can be used for two-factor authentication by installing the GitHub Mobile app and signing in to your account. -> GitHub Mobile se puede utilizar para la autenticación de 2FA instalando la aplicación GitHub Mobile e iniciando sesión en su cuenta.

<sub>Esto quiere decir que también se utiliza la app de GitHub donde al iniciar sesión desde cualquier dispositivo nos muestra un número que debemos ingresar en la app de nuestro dispositivo celular.</sub>

5. Authenticator app: Edit

<sub>Esto para agregar a través de un QR una app que genere cada 1 segundo nuevos códigos numéricos para la autenticación, yo recomiendo la aplicación: Twilio Authy Authenticator</sub>

<sub>Es recomendable iniciar sesión, osea registrarnos y guardar estos datos para que al cambiar un dispositivo sigamos teniendo acceso.</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Parte 4:</sub>

<sub>Introducción</sub>
<sub>Práctica</sub>
<sub>PDF</sub>


<sub>La tarea de hoy, agregar esta clase al README.md con el lenguaje de markdown, como lo hicimos en la clase pasada, luego deben hacer el commit correspondiente al cambio agregado.</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 01 MIÉRCOLES 14 DE AGOSTO DEL 2024 - Portafolio 1

## USO DE GITHUB Parte 1

<sub>GitHub es una plataforma que nos permite guardar repositorios de Git que podemos usar como servidores remotos y ejecutar algunos comandos de forma visual e interactiva (sin necesidad de la consola de comandos).</sub>

<sub>Luego de crear nuestra cuenta, podemos crear o importar repositorios, crear organizaciones y proyectos de trabajo, descubrir repositorios de otras personas, contribuir a esos proyectos, dar estrellas y muchas otras cosas.</sub>

### COMANDOS

```sh
Import repository
New organization # significa que es como tu empresa
New project # significa es como un grupo de repositorios que puedes tener dentro de una empresa
New gist # es un pedasito de código que puedes compartir
New repository #Ponemos el nombre: class-git, descripción: Haremos un blog increible, hay muchas licencias para publicar el código: NO lo hacemos ahora.
Create repository #Lo ponemos en privado o en Publico.
```

<sub>El README.md es el archivo que veremos por defecto al entrar a un repositorio. Es una muy buena práctica configurarlo para describir el proyecto, los requerimientos y las instrucciones que debemos seguir para contribuir correctamente.</sub>

<sub>Para clonar un repositorio desde GitHub (o cualquier otro servidor remoto) debemos copiar la URL (por ahora, usando HTTPS) y ejecutar el comando git clone + la URL que acabamos de copiar. Esto descargará la versión de nuestro proyecto que se encuentra en GitHub.</sub>

<sub>ATENCIÓN: ¿Por qué? Porque a través de https nos pedirá usuario(nombre perfil) y contraseña.</sub>

<sub>Sin embargo, esto solo funciona para las personas que quieren empezar a contribuir en el proyecto.</sub>

<sub>Cómo conectar un repositorio de GitHub a nuestro documento local Si queremos conectar el repositorio de GitHub con nuestro repositorio local, que creamos aconsejo que al trabajar desde GitHub no utilizemos localmente el comando git init, si debemos ejecutar las siguientes instrucciones:</sub>

<sub>Guardar la URL del repositorio de GitHub con el nombre de origin</sub>

```sh
git remote add origin URL
```

<sub>Verificar que la URL se haya guardado correctamente:</sub>

```sh
git remote
git remote -v
```

<sub>Traer la versión del repositorio remoto y hacer merge para crear un commit con los archivos de ambas partes. Podemos usar git fetch y git merge o solo git pull con el flag --allow-unrelated-histories:</sub>

```sh
git pull origin master --allow-unrelated-histories
```

<sub>Por último, ahora sí podemos hacer git push para guardar los cambios de nuestro repositorio local en GitHub:</sub>

```sh
git push origin master
```

### Cómo autenticarte en GitHub 2022

<sub>Antes de empezar debemos renombrar la rama ‘máster’ a ‘main’, este es el nuevo estándar en GitHub, para esto:</sub>

<sub>Primero nos posicionamos en la rama a la que queremos cambiarle el nombre.</sub>

<sub>Ejecutamos el siguiente comando:</sub>

```sh
git branch -M main
```

### Pasos para crear un token de acceso personal.

<sub>Desde el 2022 GitHub ya no deja hacer el push con la contraseña del propio GitHub, para esto tenemos que crear un token, y este token es la contraseña que vamos a colocar cuando nos pida clave.</sub>


### Descubre el uso de tags en Github

<sub>
Seguir la secuencia:
Ingresamos a nuestra cuenta de GitHub.
Buscamos Settings
Click en Developer settings
Click en Personal access tokens
Click en Generate new token aquí se puede colocar un nombre, la fecha de expiración.
Tildar en repo y luego click en el botón verde Generate token
</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>
<sub>Segundo Semestre Parte 1:</sub>
<sub>IntroYpractica</sub>
<sub>PDF</sub>


<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 02 MIÉRCOLES 21 DE AGOSTO DEL 2024 - Portafolio 2

<sub>Vamos a cargar la llave SSH publica en GitHub</sub>

<sub>Para copiar la llave publica debes ir al archivo .ssh y allí encontrarás el archivo .pub lo podes abrir con el txt, luego copiar el contenido que esta dentro.</sub>

<sub>copiar la llave publica #Ir a GitHub, vamos a setting, vamos a SSH and GPG keys</sub>

<sub>crear una nueva #New SSH key poner nombre y pegar la ssh publica, con esto esta listo.</sub>

<sub>Aconsejo que la ssh tenga el nombre del ordenador en el que estas trabajando. Esto se debe hacer con cada pc nueva o dispositivo nuevo que tengamos para acceder a nuestra cuenta de GitHub.</sub>

```sh
git branch #Vemos en que rama estamos
git checkout master #Ponernos en la rama master
git branch -M main #Cambiamos el nombre a la rama master
git remote add origin git@github.com:nombreUsuario/class-git.git #Agregamos el repositorio remoto, este es un ejemplo
git remote -v #Vemos si ya esta conectado
git merge segunda #Mergeamos lo que tenemos en la rama segunda en main
git commit -am "Uso de GitHub parte 20" #Hacemos el commit de hoy
git push origin main #Pasamos todo lo hecho a GitHub, revisar en el repositorio en GitHub.
```

<sub>
Frente al cambio de nombre de rama master a main, suele suceder que en el repo de GitHub se hayan creado dos ramas, la rama master y la rama main, se debe ir al repo, settings y ahí se puede cambiar la rama principal, en vez de que siga siendo master, que sea la rama main, luego de eso ya podemos borrar la rama master.
</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Segundo Semestre Parte 2:</sub>

<sub>Video Capitulo 01</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 03 MIÉRCOLES 28 DE AGOSTO DEL 2024 - Portafolio 3

## Cambios en GitHub: de master a main

<sub>El escritor Argentino Julio Cortázar afirma que las palabras tienen color y peso. Por otro lado, los sinónimos existen por definición, pero no expresan lo mismo. Feo no es lo mismo que desagradable, ni aromático es lo mismo que oloroso.</sub>

<sub>Por lo anterior, podemos afirmar que los sinónimos no expresan lo mismo, no tienen el mismo “color” ni el mismo “peso”.</sub>

<sub>Sí, esta lectura es parte de la enseñanza profesional de Git & GitHub.</sub>

<sub>Desde el 1 de octubre de 2020 GitHub cambió el nombre de la rama principal: ya no es “master” -como aprenderás aquí- sino main.</sub>

<sub>Este derivado de una profunda reflexión ocasionada por el movimiento #BlackLivesMatter.</sub>

<sub>La industria de la tecnología lleva muchos años usando términos como master, slave, blacklist o whitelist y esperamos pronto puedan ir desapareciendo.</sub>

<sub>Y sí, las palabras importan.</sub>

<sub>Por lo que de aquí en adelante cada vez que me escuches mencionar “master” debes saber que hago referencia a “main”.</sub>

## ¿Cuando es que sigue siendo master y cuando sigue siendo main?
<sub>Cuando se crea un repositorio desde git bash en nuestro ordenador a través de git init, sigue siendo el estandar como master. ¿Qué hacer con esto? Debes cambiar el nombre de la rama master a main con el comando git branch -M main.</sub>
<sub>Ahora cuando creamos un repositorio desde la nube, osea desde GitHub, ya verás que la rama principal tiene por default el nombre de main y al clonar a nuestro ordenador seguira teniendo este nombre y no será necesario ningun cambio.</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Segundo Semestre Parte 3:</sub>
<sub>Video Capitulo 02</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 04 MIÉRCOLES 4 DE SEPTIEMBRE DEL 2024 - Portafolio 4

## Tu primer push

<sub>La creación de las SSH es necesario solo una vez por cada computadora. Aquí conocerás cómo conectar a GitHub usando SSH.</sub>

<sub>Luego de crear nuestras llaves SSH podemos entregarle la llave pública a GitHub para comunicarnos de forma segura y sin necesidad de escribir nuestro usuario y contraseña todo el tiempo.</sub>

<sub>Para esto debes entrar a la Configuración de Llaves SSH en GitHub, crear una nueva llave con el nombre que le quieras dar y el contenido de la llave pública de tu computadora.</sub>

<sub>Ahora podemos actualizar la URL que guardamos en nuestro repositorio remoto, solo que, en vez de guardar la URL con HTTPS, vamos a usar la URL con SSH:</sub>

```sh
ssh
git remote set-url origin url-ssh-del-repositorio-en-github
```

<sub>Comandos para copiar la llave SSH:</sub>

<sub>ESTAS SON LAS RUTAS DEL SSH PUBLICO</sub>

<sub>-Mac:</sub>

```sh
pbcopy < ~/.ssh/id_rsa.pub
```

<sub>Windows (Git Bash):</sub>

```sh
clip < ~/.ssh/id_rsa.pub
```

<sub>Linux (Ubuntu):</sub>

```sh
cat ~/.ssh/id_rsa.pub
```

## Importante

<sub>Las buenas costumbres nos enseñan que antes de hacer un push, siempre debemos hacer un pull, un fetch, esto para que si alguien ya hizo algún cambio, no se genere un conflicto.</sub>

## Invitar a un colaborador

<sub>Para invitar a un colaborador debemos ir a GitHub y seleccionar: setting -> colaborators -> ingresar contraseña o un F2A de verificación y enviar la invitación escribiendo el nombre de usuario.</sub>


<sub>Del otro lado el usuario invitado solo debe aceptar y listo, ya puede participar del proyecto haciendo commit.</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>

<sub>Segundo Semestre Parte 4:</sub>

<sub>Video Capitulo 03</sub>

<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 05 MIÉRCOLES 11 DE SEPTIEMBRE DEL 2024 - Portafolio 5

## Git tag y versiones en GitHub

<sub>En Git, las etiquetas o Git tags tienen un papel importante al asignar versiones a los commits más significativos de un proyecto. Aprender a utilizar el comando git tag, entender los diferentes tipos de etiquetas, cómo crearlas, eliminarlas y compartirlas, es esencial para un flujo de trabajo eficiente.</sub>


### Creación de etiquetas en Git

```sh
git tag
```

<sub>Sustituye con un identificador semántico que refleje el estado del repositorio en el momento de la creación. Git admite etiquetas anotadas y ligeras.</sub>

### Listado de etiquetas

<sub>Para obtener una lista de etiquetas en el repositorio, ejecuta el siguiente comando:</sub>

```sh
git tag -a v1.0 -m "Product release"
git tag -a rondurgundy -m "Brick killed a guy with a trident."
```

<sub>Para crear una etiqueta, ejecuta el siguiente comando:</sub>


<sub>Las etiquetas anotadas almacenan información adicional como la fecha, etiquetador y correo electrónico, y son ideales para publicaciones públicas. Las etiquetas ligeras son más simples y se emplean como “marcadores” de una confirmación específica.</sub>

```sh
git tag
```

<sub>Esto mostrará una lista de las etiquetas existentes, como:</sub>

<sub>
v1.0
v1.1
v1.2
</sub>

<sub>Para perfeccionar la lista, puedes utilizar opciones adicionales, como -l con una expresión comodín.</sub>


### Uso compartido de etiquetas

<sub>Compartir etiquetas requiere un enfoque explícito al usar el comando git push. Por defecto, las etiquetas no se envían automáticamente. Para enviar etiquetas específicas, utiliza:</sub>

```sh
git push origin
```

<sub>Para enviar varias etiquetas a la vez, usa:</sub>

```sh
git push origin --tags
```

### Eliminación de etiquetas

<sub>Para eliminar una etiqueta, usa el siguiente comando:</sub>

```sh
git tag -d
```

<sub>Esto eliminará la etiqueta identificada por en el repositorio local.</sub>

<sub>En resumen, las etiquetas en Git son esenciales para asignar versiones y capturar instantáneas importantes en el historial de un proyecto. Aprender a crear, listar, compartir y eliminar etiquetas mejorará tu flujo de trabajo con Git.</sub>


## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>
<sub>Segundo Semestre Parte 5:</sub>
<sub>Video Capitulo 04</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 06 MIÉRCOLES 18 DE SEPTIEMBRE DEL 2024 - Portafolio 6

## Error con los tags
<sub>Investigación: ¿Qué pasa si por error cargamos un tag dos veces?</sub>

<sub>¿Cómo solucionarías este problema o error?</sub>

<sub>La respuesta debe ser enviada antes de las 23 horas por cada grupo, deben enviar comandos y todo los pasos que harían frente a este conflicto.</0sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>
<sub>Segundo Semestre Parte 6:</sub>
<sub>Video Capitulo 05</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 07 MIÉRCOLES 25 DE SEPTIEMBRE DEL 2024 - Portafolio 7

## Error con los tags
<sub>Investigación: Si un tag es imposible generarlo dos veces ¿Cómo es que existe el error de dos tags con el mismo nombre?</sub>

<sub>¿Cómo se origina este problema o error?</sub>

<sub>La respuesta debe ser enviada antes de las 23 horas por cada grupo, deben enviar comandos y todo los pasos que harían frente a este conflicto.</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez</sub>
<sub>Segundo Semestre Parte 6:</sub>
<sub>Video Capitulo 06</sub>
<sub>PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 08 MIÉRCOLES 2 DE OCTUBRE DEL 2024 - Portafolio 8

## Manejo de ramas en GitHub

<sub>Si no te funciona el comando gitk es posible no lo tengas instalado por defecto.
Para instalar gitk debemos ejecutar los siguientes comandos:</sub>


```sh

  sudo apt-get update

  sudo apt-get install gitk

```

## Repasa: ¿Qué es Git?

<sub>Las ramas nos permiten hacer cambios a nuestros archivos sin modificar la versión principal (main). 
Puedes trabajar con ramas que nunca envías a GitHub, así como pueden haber ramas importantes en GitHub que nunca usas en el repositorio local. 
Lo crucial es que aprendas a manejarlas para trabajar profesionalmente.</sub>

<sub>Si, estando en otra rama, modificamos los archivos y hacemos commit, tanto el historial(git log) como los archivos serán afectados. 
La ventaja que tiene usar ramas es que las modificaciones solo afectarán a esa rama en particular. 
Si luego de “guardar” los archivos(usando commit) nos movemos a otra rama (git checkout otraRama) veremos como las modificaciones de la rama pasada no 
aparecen en la otraRama.</sub>

## Comandos para manejo de ramas en GitHub

<sub>Crear una rama:</sub>

```sh
git branch branchName #Crear una rama
git checkout branchName #Movernos a otra rama 
git checkout -b nombre-de-la-rama #Crear una rama en el repositorio local
git push origin nombre-de-la-rama #Publicar una rama local al repositorio remoto
```

<sub>Recuerda que podemos ver gráficamente nuestro entorno y flujo de trabajo local con Git utilizando el comando gitk. 
Gitk fue el primer visor gráfico que se desarrolló para ver de manera gráfica el historial de un repositorio de Git.</sub>

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez
Segundo Semestre Parte 7:
Video capitulo 07
PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>

# CLASE 09 MIÉRCOLES 9 DE OCTUBRE DEL 2024 - Portafolio 9

<sub>Tarea para antes de las 23 horas: Investigar como se puede clonar un repo con el https del mismo, ósea siendo ustedes los dueños del repositorio, y desde la nube quieren traer este repo a nuestro ordenador, nos pedira Username y password: ¿qué se debe hacer para lograr hacer cambios y así utilizar pull, push, y todo lo necesario para trabajar?. Como referencia les digo que solo usuario y contraseña no será suficiente, esto cambio desde el año 2021 y ahora hay algo más para poder hacer esto y tener así acceso total.</sub>

## Configurar múltiples colaboradores en un repositorio de GitHub

<sub>Por defecto, cualquier persona puede clonar o descargar tu proyecto desde GitHub, pero no pueden crear commits, ni ramas. 
Esto quiere decir que pueden copiar tu proyecto pero no colaborar con él, si este es publico, de otra manera, osea, si es privado 
es necesario que realmente estes haciendo una invitación, sino no lo van a poder ver. Existen varias formas de solucionar esto 
para poder aceptar contribuciones. Una de ellas es añadir a cada persona de nuestro equipo como colaborador de nuestro repositorio.</sub>


## Cómo agregar colaboradores en Github
<sub>Solo debemos entrar a la configuración de colaboradores de nuestro proyecto. Se encuentra en:</sub>

<sub>Repositorio > Settings > Collaborators
Ahí, debemos añadir el email o username de los nuevos colaboradores.</sub>



<sub>Si, como colaborador, agregaste erróneamente el mensaje del commit, lo puedes cambiar de la siguiente manera:</sub>

<sub>Hacer un commit con el nuevo mensaje que queremos, esto nos abre el editor de texto de la terminal:</sub>

```sh
git commit —amend #Corregimos el mensaje
git pull origin main #Traer el repositorio remoto
git push --set-upstream origin main #Ejecutar el cambio, el error arreglado
```

## Comienzo del colaborador

```sh
cd Documentos #Abre git bash
mkdir class-git #Crea la carpeta o directorio de trabajo
ls -al #Revisa lo que va haciendo, los archivos o directorios que tiene
# 1. No debe hacer un git init, debe buscar el repositorio en el cual esta invitado a participar, por supuesto en GitHub.
# 2. Pasa a clonar desde HTTPS, copiar la url, esto es porque no se arranca el proyecto desde cero, se esta uniendo otro colaborador.
# 3. En git bash ponemos el siguiente comando.
git clone url-copiada-github #Esto hace que clonemos el repositorio
# 4. No pide ni usuario ni contraseña si el repositorio es publico.
code . #Abre VSC y comienza con cambios, o abre el siguiente comando para hacer modificaciones
vim historia.txt #Vamos a escribir: Aquí esta un nuevo colaborador
vim escribimos el mensaje del commit #Esto en Ubuntu
ctrl + x
s #Para un si 
enter #Terminado el mensaje del commit
vim escribimos el mensaje del commit #Esto en git bash window
esc #Presionamos escaner luego de terminar de escribir
:wq! #Para salir del editor vim en window
git status
git commit -am "Mi primer commit, estoy muy emocionado!!!"
git pull origin main
git fetch
gti branch #Para ver las ramas que se trajo, no se trae sino solo main, si hay mas debes crearlas local
git log #Para ver toda las historia
git log --graph #Vemos el grafico de las diferentes ramas y del commit que acabamos de hacer que esta en el main, Git es una base de datos de toda las historia de todo lo que se ha hecho
git push origin main #Va a pedir un email que será el del colaborador, su contraseña.
# 5. Nos trae un denegado, ¿Por qué? Porque en el proceso de abordaje el jefe no le dio acceso: el dueño del repositorio no le agregó dandole acceso.
# 6. Ir a settings del repositorio, veremos la opsión Collaborators, agregamos el correo o nombre de usuario: el colaborador debe tener un email publico y visible o de otra manera debera ser con el nombre de usuario publico: ingresar el username y debe ir como colaborador.
# 7. Se puede enviar un email con la url, pero ya GitHub envia una notificación al usuario de invitado, es una cosa que debemos empezar a consultar y revisar.
# 8. El colaborador debe aceptar la invitación, una vez hecho eso ya tendrá total acceso para hacer push al repositorio.
git pull origin main
git push origin main #Colocar nombre de usuario y contraseña, listo
# 9. El dueño del repositorio no ve los cambios, ¿Qué hacer?
git pull origin main
git fetch
git log --stat #Se verá claro que el colaborador ingreso su primer commit
# 10. A partir de ahora el dueño del repositorio y el colaborador deberán repartir el trabajo, esto se hace con distintas ramas de trabajo: el dueño trabajará desde la rama header y el colaborador desde la rama footer, al final cuando se termine, se hara un merge para terminar el proyecto.
```

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>
Dante Nicolás Martinez
Segundo Semestre Parte 8:
Video Capitulo 08
PDF
</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 10 MIÉRCOLES 16 DE OCTUBRE DEL 2024 - Portafolio 10

## Flujo de trabajo profesional

<sub>Haciendo merge de ramas de desarrollo a main</sub>

<sub>Para poder desarrollar software de manera óptima y ordenada, 
necesitamos tener un flujo de trabajo profesional, que nos permita 
trabajar en conjunto sin interrumpir el trabajo de otros desarrolladores.</sub>

<sub>Una buena práctica de flujo de trabajo sería la siguiente:</sub>

1. Crear ramas
2. Asignar una rama a cada programador
3. El programador baja el repositorio con git pull origin master
4. El programador cambia de rama
5. El programador trabaja en esa rama y hace commits
6. El programador sube su trabajo con git push origin #nombre_rama
7. El encargado de organizar el proyecto baja, revisa y unifica todos los cambios

## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>
Dante Nicolás Martinez
Segundo Semestre Parte 8:
Video Capitulo 9
PDF
</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>


# CLASE 11 MIÉRCOLES 23 DE OCTUBRE DEL 2024 - Portafolio 11

## Flujo de trabajo profesional -> Archivos binarios

<sub>Las imagenes cargandolas en el repositorio, representan un problema: porque las imagenes son pesadas, y si la subimos al repositorio, siempre que hagamos 
cambios, vamos a estar trayendo la imagen siempre, estas imagenes son binarios para GitHub, mientras mas binarios carguemos, más pesado va a ser el repositorio,
 algo que no es parte de las buenas practicas.</sub>


<sub>Otra cosa muy importante a tener en cuenta, es que en cada commit que hagamos hay un tamaño predefinido para la carga, este no lo podemos superar
 o no podremos subir los commits, el tamaño es 100 mb, si acoplamos un archivo binario en un commit que pese mas de esto, será un problema, 
 no nos dejará seguir commiteando, porque siempre seguirá arrastrando el archivo binario.</sub>


## PORTAFOLIO

<sub>Vamos a ver unos videos de como avanzar en lo que es un portafolio por el Tutor:</sub>

<sub>Dante Nicolás Martinez
Segundo Semestre Parte 9:
Video Capitulo 10
PDF</sub>

<sub>Revisar y ejecutar cada comando, hacerlo como practica: NO olvidar hacer lo requerido por el Tutor Nico, lo que sea tarea o investigación.</sub>

<sub>Profesor Ariel Betancud</sub>