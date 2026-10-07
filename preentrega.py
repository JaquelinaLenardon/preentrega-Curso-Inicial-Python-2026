import time 
productos = [{"nombre": "🐣 Poción juventud eterna", "categoria": "Pociones", "precio": 2500,"descripcion": "Ya te empezo a doler la cadera?\nNo te preocupes, con esta poción puedes volver a tener 20 otra vez!"},
             {"nombre": "🧴 Shampoo Cabello Instantaneo", "categoria": "Cuidado del cabello","precio": 1500,"descripcion":"Se te cae el pelo? Te llaman chupetin?🍭🫣\nPrueba este shampoo y veras como tu cabello vuelve a crecer en 24hs!\nEfectos adversos: Puede provocar que tu cabello crezca en lugares no deseados."},
             {"nombre": "💄 Labial Cambia Rostro", "categoria": "Maquillaje", "precio": 900,"descripcion": "Este labial tiene la capacidad de cambiar tu rostro a tu antojo.\nPero cuidado! No es recomendable usarlo en exceso, ya que puede provocar que tu rostro se quede con la forma que elegiste."},
             {"nombre": "😶‍🌫️ Rubor de Invisibilidad", "categoria": "Maquillaje", "precio": 1400,"descripcion": "Ideal para quienes busquen escapar de la ley o de situaciones incomodas 🙂.\nEste rubor tiene la capacidad de hacerte invisible por 30 minutos.\nSe desaconseja su uso frecuente, podría causar invisibilidad permanente."},
             {"nombre": "🪥 Cepillo de dientes Feliz de Verte", "categoria": "Cuidado bucal", "precio": 600,"descripcion": "Le cae mal a su compañero de oficina? 🤔 Su suegra no para de decir que es un inutil?\nEste cepillo de dientes hará que la gente se siente feliz de verlo.\nCon su tecnología avanzada, no solo limpia de manera eficaz los dientes sino que hará que cualquiera se alegre de verlo por 24hs.\nNo recomendado para personas con sensibilidad dental.\nAdvertencia: al pasar su efecto la gente puede sentir desagrado por usted más de lo habitual 😦."},
             {"nombre": "💧 Secador de cabello Seca mis lagrimas", "categoria": "Electrobeauty", "precio": 7300,"descripcion": " Diseñado para resolver situaciones que le causen tristeza.\nAunque también podría poner su vida de cabeza🙃."},
             {"nombre": "🥶 Perfume Asustalos a todos", "categoria": "Fragancia","precio": 12450,"descripcion": "Con este perfume, verte será como ver a un fantasma 👻.\nIdeal para quienes buscan destacar en cualquier ocasión."},
             {"nombre": "🤴🏻🏅🏆 Perfume Boss", "categoria": "Fragancia", "precio": 13470,"descripcion": "Un perfume para gente ambiciosa.\nSi ha soñado con volverse implacable en el trabajo, tener la valentía para declarar su amor o conquistar Polonia, este perfume es para usted.\nComo nota al pie, es de mencionar que varios usuarios han reportado que, de usarse en exceso, genera una ligera sensación de superioridad y arrogancia 🤭.\nTambién se ha reportado gente que ha terminado en la carcel por su uso prolongado 🤫."},
             {"nombre": "🤓 Acondicionador Olvidadiza", "categoria": "Cuidado del cabello", "precio": 789,"descripcion": "Olvide sus preocupaciones amorosas: amor no correspondido, una dolorosa separación o una infidelidad. Este acondicionador le ayudará a olvidar todo lo que le hace daño.\nNota de uso: mencione el nombre de la persona que desea olvidar mientras aplica el producto y digale adios de una vez por todas ☺️."},
             {"nombre": "🫦 Crema facial LLamame Bonita", "categoria": "Cuidado de la piel", "precio": 6206,"descripcion": "Quiere que todos los hombres o mujeres caigan rendidos a sus pies?😉 Esta es la solución.\nCon esta crema facial, su presencia se volverá irresistible 😘 por 24hs.\nNota de uso: no unte demasiado, no quiere terminar en la panza de nadie.😦"},
             {"nombre": "🫚 Maquina de escribir Pimienta", "categoria": "Articulo de libreria", "precio": 3270,"descripcion": "😒Cansado de la rutina?\n😲 Haga correr acontecimientos divertidos con la nueva maquina de escribir pimienta.\nEscriba el guion de su vida y mire como los acontecimientos repercuten en la vida real. caigan rendidos a sus pies? Esta es la solución. Nota de uso: no lo olvide, toda causa tiene una consecuencia. Los acontecimientos no tienen marcha atras, no incluye garantias. Puede que la maquina quede inutilizable despues de unas 20 paginas"},
             {"nombre": "🥛 Vaso Encuentra Cosas Perdidas", "categoria": "Articulo de la vida diaria", "precio": 4540,"descripcion": "El poder de este vaso dado vuelta es tan grande que puede hacer aparecer hasta padres que han desaparecido 🤭.\nBasta con nombrar el nombre del objeto o persona que desea encontrar al dar vuelta el vaso.\nEso si! solo funciona con cosas o personas que esten perdidas. No le ayudara a encontrar el amor de su vida."},
             {"nombre": " 🗒️🖋️ Diario personal Necesito un consejo", "categoria": "Articulo de libreria", "precio": 1280,"descripcion": "Escribale al diario un problema y preparese para escuchar un consejo.\nEso si, no se garantiza que sea un buen consejo.😅"},
             {"nombre": "🕶️ Anteojos de sol Claridad total", "categoria": "Articulo de la vidad diaria", "precio": 8900,"descripcion": "Con estos lentes de sol, usted podra ver cosas que los demas no pueden🫣.\nIdeal para quienes buscan descubrir secretos o cosas ocultas.\nNota de uso: No funciona en días nublados y/o lluviosos.\n Cuidado con los espiritus: a los muertos no les gusta ser molestados ni vistos."},
             {"nombre": "🍫 Chispitas de Chocolate Sabrina", "categoria": "Alimentos", "precio": 1500,"descripcion": "🤔Desea saber si alguien miente o dice la verdad? Esparcir estas chispitas de chocolate en cualquier alimento dulce hara que las personas le digan la verdad. Advertencia: la verdad puede ser amarga."},
             {"nombre": "🎰🍀 Perfume Trebol Verde", "categoria": "Fragancia", "precio": 2500,"descripcion": "Una fragancia simple, sin ningun tipo de aroma. Puede usarlo para cualquier ocasion, y en todas ellas, acabara con la mejor oportunidad y el mejor resultado posible.🤩"},
             {"nombre": "🍐🍐 Peras del Olmo", "categoria": "Alimentos", "precio": 3450,"descripcion": "Con estas peras, hasta el limonero da naranjas, si asi usted lo desea. Uso: Admisistre una pera completa a cualquier persona y despues de que se la coma, diga lo que usted espera de ella.\nAdvertencia: la persona que consuma Peras del Olmo, puede quedar en estado catatonico hasta que usted no le vuelva a sumistrar una orden.🧟\nDocilidad y servicio garantizado."},
             {"nombre": "🐸 Poción Quiero ser un Sapo", "categoria": "Pociones", "precio": 500,"descripcion": "🤔No nos pregunte por qué desarrollamos esta poción, se le ocurrió a uno de nuestros ingeniros y solo funciona para convertirlo en sapo.🤓\nAparentemente es más sencillo que convertirse en cualquier otro animal.\nGarantia por un año, si en ese transcurso vuelve a ser humano, le devolvemos su dinero y le damos un tipo de anfibio a elección de regalo."},
             {"nombre": "🌪️ Rizador de pestañas Vientos Huracanados", "categoria": "Electrobeauty", "precio": 9500,"descripcion": "Uselo y provoque vientos uracanados en un parpadeo.\nPor obvios motivos, su efecto sólo dura 1 minuto."},
             {"nombre": "🗣️ Enjuague Bucal Acidez Estovamal", "categoria": "Cuidado Bucal", "precio": 2500,"descripcion": "Lance escupitajos tan acidos que derriten hasta hierros y concreto😂. Su duración es de 24hs.\nEfectos adversos: acidez estomacal por 72hs."},]

clientes = []
contrasenias = []


#Cartel de bienvenida
print ("*"*60)
print ("           ⭐ B I E N V E N I D O 💫   ")
print ("                      A L             ")
print (" 🪄 B A Z A R   D E   C U R I O S I D A D E S 🔮📿🐈‍⬛  ")
print ("              de la tia Jackie ⭐")                                     
print ("-"*60)
print("\n"*2)
print("✨ Preparando el bazar... Por favor, Aguarde un momento...")
time.sleep(5)
print (f"¡Saludos desde la luna, nuevo usuario!\n En este Bazar encontrarás una gran variedad de productos mágicos.\n No garantizamos que resuelvan tus problemas ni mejoren tu vida, pero puedes intentarlo.\n La compra y el uso de los articulos magicos queda bajo responsabilidad exclusiva del usuario.\n Pero antes, no olvides crear tu cuenta con nombre y contraseña para ingresar.\n ¡Comencemos!")
time.sleep(6)
nombre = input("Ingrese su nombre: ").strip().title()
contrasenia = input("Ingrese su contraseña: ")
while True:
    if nombre == "" or contrasenia == "":
        print("Error: Por favor, complete todos los campos.")
        nombre = input("Ingrese su nombre: ").strip().title()
        contrasenia = input("Ingrese su contraseña: ")
    else:
        clientes.append(nombre)
        contrasenias.append(contrasenia)
        print(f"¡Bienvenido {nombre}! Su cuenta ha sido creada exitosamente.")
        break 

print ("-"*35)
print("\n"*2)
time.sleep(3)

print(f"Presta atención, {nombre}! Acontinuación, se desplagara un Menu de opciones para que puedas navegar y gestionar te experiencia en nuestro bazar.\n Por favor, elija una opción del 1 al 5.")

time.sleep(3)

while True:
    print("-" * 35)
    print("\n" * 2)
    print("=" * 35)
    print(f"||" + " " * 5 + "🪄M E N U   D E   O P C I O N E S🪬" + " " * 5 + "||")
    print("=" * 35)
    print("\n" * 2)
    print("*" * 35)
    print("🎃  1. Agregar Articulo mágico")
    print("🪄  2. Ver catálogo de Articulos mágicos")
    print("👻  3. Buscar Articulo mágico")
    print("💀  4. Eliminar Articulo mágico")
    print("🪬  5. Salir")
    print("*" * 35)

    opcion = input("Ingrese el número de la opción deseada: ").strip()
    time.sleep(3)
    print("✨   ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨   ")
    print("No te asustes, el caldero se esta cocinando...")
    print("✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨  ✨   ")
    print("\n" * 2)

    if opcion == "1":
        print("\nElegiste la opción 1: Agregar Articulo mágico.")
        nuevo_producto = input("\n Ingrese el nombre del Articulo mágico: ").strip()
        categoria = input("\n Ingrese la categoría del Articulo mágico: ").strip()
        precio = float(input("\n Ingrese el precio del Articulo mágico: "))
        descripcion = input("\n Ingrese la descripción del Articulo mágico: ").strip()
        time.sleep(3)
        print("🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  🐈‍⬛  ")
        productos.append({"nombre": nuevo_producto, "categoria": categoria, "precio": precio, "descripcion": descripcion})
        print(f"Articulo agregado exitosamente: {nuevo_producto}")

    elif opcion == "2":
        print("\nElegiste la opción 2: Ver catálogo de articulos magicos.")
        print("🪬  🪬 🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  🪬  ")
        print("Catalogo de articulos magicos:")
        for producto in productos:
            print("-" * 65)
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Descripción: {producto['descripcion']}")
            print("-" * 65)
            time.sleep(1)

    elif opcion == "3":
        print("\nElegiste la opción 3: Buscar articulo mágico.")
        busqueda = input("Ingrese el nombre del articulo que desea buscar: ").strip().lower()
        encontrado = False
        for producto in productos:
            if busqueda in producto['nombre'].lower():
                time.sleep(3)
                print("🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  ")
                print(f"Nombre: {producto['nombre']}")
                print(f"Categoría: {producto['categoria']}")
                print(f"Precio: ${producto['precio']}")
                print(f"Descripción: {producto['descripcion']}")
                print("🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  🪄  ")
                encontrado = True
        if not encontrado:
            time.sleep(3)
            print("El articulo mágico que buscas no se encuentra en el catalogo. \n Por favor, inténtelo de nuevo.")

    elif opcion == "4":
        print("\nElegiste la opción 4: Eliminar articulo mágico.")
        eliminar = input("Ingrese el nombre del articulo que desea eliminar: ").strip().lower()
        eliminado = False
        for producto in productos:
            if eliminar in producto['nombre'].lower():
                productos.remove(producto)
                time.sleep(3)
                print("👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  👻  ")
                print(f"Articulo eliminado exitosamente: {producto['nombre']}")
                eliminado = True
                break
        if not eliminado:
            print("🤔  El articulo mágico que deseas eliminar no se encuentra en el catalogo.\n Por favor, inténtelo de nuevo.")

    elif opcion == "5":
        print("\nElegiste la opción 5: Salir.")
        time.sleep(3)
        print("🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃 ")
        print("Gracias por visitar nuestro bazar de curiosidades. \nSe que vas a regresar pronto😉 \n¡Hasta luego!")
        print("🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃  🎃")
        break

    else:
        print("⛔  Opción inválida. Por favor, ingrese un número del 1 al 5.")
    