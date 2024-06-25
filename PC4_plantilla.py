# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>˚ʚ♡ɞ˚¡Hello Kitty!˚ʚ♡ɞ˚¡Hello Kris!˚ʚ♡ɞ˚</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("profile_pic.png", caption='Esa soy yo en mi estado mas natural, con gorrito y todo ꒰ᐢ. .ᐢ꒱₊˚⊹', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
Holaaa, me llamo Kristell, pero todos mis amigos me dicen Kris.
Tengo 20 años y actualmente curso el quinto ciclo de la carrera de Publicidad en la
Pontificia Universidad Catolica del Perú. Este trabajo lo estoy realizando para mi 
curso de Pensamiento Computacional para Comunicaciones :D.
Tengo 2 gatos llamados Chizi y Harryson y un perro chihuahua llamado Bruce.
Me gusta muchisimo dibujar, actualmente estoy participando en una ravista como ilustradora de viñetas!, tambien
me gusta mucho escuchar musica, especialmente a bandas del genero nu metal y black metal.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
⊹₊｡ꕤ˚₊⊹Al empezar con las clases de programación tenia un sesgo, pues pensaba que se trataba de un curso dificil
y que me tardaria mucho en aprender. Poco a poco me di cuenta de que, si bien si debes prestar mucha atención al detalle
cuando vas a programar, esto no resulta tan dificil, al menos hasta que te acostumbras. Claro, es frustrante cuando una 
vez que tienes el codigo listo salta un error y no sabes como resolverlo, pero no es nada que no se pueda aprender y solucionar.
Personalmente creo que mi experiencia fue bastante buena, pues entendi muchas de las cosas base en las primeras clases 
y no tarde en ponerlas en practica, debo admitir que era hasta algo emocionante cuando escribia sola los codigos y estos funcionaban.
Pero como todo, las clases empezaron a avanzar en complejidad, al inicio fue chocante, pues pensaba "pero esto no me lo han enseñado" (especialmente cuando llegamos a bucles), pero
pronto me di cuenta que si me lo habian enseñado, que solo necesitaba pensar un poco mas fuera de la caja para hacerlo funcionar.
Tambien estoy muy agaradecida por la Jefa de Practica que me toco, fue muy paciente con todas mis preguntas y una de las persons que 
mas me ayudo a aprender completamente los temas, asi como mi amiga con la que me met al curso, Avi con quien el proceso de aprendzaje se me facilito,
pues yo tenia que aprender bien para poder ayudarla, y asi ella me ayudaba a mi. ⊹₊｡ꕤ˚₊⊹
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣴⠶⠶⠶⠶⠦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠟⣿⣿⠾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠉⠀⠀⠸⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣀⠈⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⢀⡿⠁⠀⠀⣰⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠙⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠐⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠉⠁⠉⠈⠉⠀⠀⠀⠀⠀⠀⣠⢤⣀⠀⠀⠀⠀⠀⠉⠿⠿⠁⡀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⠀⠀⠀
⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣄⠤⠠⠐⢀⡀⠀⠀⠀⠀⠀⠋⠁⠉⠁⠀⠀⠀⠀⠀⠄⠀⠀⠀⢁⠀⠀⣼⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀
⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠻⢶⣤⣴⡾⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣤⠀⠜⣀⣴⠟⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀
⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⣿⠃⠀⠀⢸⡟⠳⠶⠶⠶⢦⣶⣴⣶⣴⣶⣶⣿⠉⠀⠹⣷⣿⣿⣥⣄⡀⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢿⣆⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠀⢀⣿⠟⠉⠉⠉⠛⣷⡄⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇
⠘⢷⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠃⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠿⣷⡀⠀⠀⣀⠀⠈⣿⡄⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⣀⣼⠏⠀
⠀⠀⠉⠛⠷⠶⠶⠶⠶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣴⠏⠀⠀⣽⡇⠀⠀⠀⠈⠛⠿⠶⠶⠶⠶⠿⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡾⠋⠀⠁⠀⠀⠀⠀⠀⢀⣾⠛⠉⠙⠓⠀⠀⢀⣴⠟⠛⠿⠾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠐⢶⣶⣶⣶⣶⣾⣿⡀⠀⠀⢶⡶⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣀⣠⡿⠁⠀⠀⠀⠀⢹⣇⡀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>｡𖦹°‧ Estos son algunos gráficos que hice durante mis practicas!!( ˶ˆᗜˆ˵ )</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de goles', '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de Pastel comparativo de goles', '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Grafico de promedio de tarjetas amarillas']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de goles':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>₊˚⊹♡Este grafico lo hice con una base de datos de partios de equipos italianos. Especificamente la comparativa de goles en partidos como local y como visitante del equipo Napoli.₊˚⊹♡</div>", unsafe_allow_html=True)
    sidebar.image("goles_y_mas_goles_Napoli.png", caption='˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de goles', width=500)
    pass
elif grafico_seleccionado == '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de Pastel comparativo de goles':
    sidebar.markdown("<div style='text-align: justify'>₊˚⊹♡De igual forma, este grafico de pastel fue crado para ver la comparativa porcentual de los goles como visitante y local pero esta vez del equipo Bologna.₊˚⊹♡</div>", unsafe_allow_html=True)
    sidebar.image("pastel_bologna.png", caption='˚₊‧꒰ა ☆ ໒꒱ ‧₊˚Gráfico de Pastel comparativo de goles', width=500)
    pass
elif grafico_seleccionado == '˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Grafico de promedio de tarjetas amarillas':
    sidebar.markdown("<div style='text-align: justify'>₊˚⊹♡Este ultimo grafico, nos muestra el promedio de tarjetas amarillas recibidas de todos los equipos de la selección italiana.₊˚⊹♡</div>", unsafe_allow_html=True)
    sidebar.image("Promedio_tarjetas_amarillas_local.png", caption='˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Grafico de promedio de tarjetas amarillas', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas':: Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
