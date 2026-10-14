productos = []
opcion = ""


while opcion != "5":

    print("---MENU---")    
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Elige una opcion (1 - 5): ").strip()
    
    
    
    if opcion == "1":
        print("Agregar producto")
        
        nombre = input("Ingresa el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacio")
            nombre = input("Ingresa el nombre del producto: ").strip()
            
        
        categoria = input("Ingresa la categoria de tu producto: ").strip()
        while categoria == "":
            print("La categoria no puede estar vacio")
            categoria = input("Ingresa la categoria de tu producto: ").strip()
             
             
        precio = input("Ingresa el precio de tu procto, sin centavos ").strip()
        
        while not precio.isdigit() or int(precio) == 0:
            print("El precio debe ser un numero entero mayor a 0")
            precio = input("Ingresa el precio de tu procto, sin centavos ").strip()
        
        # precio = int(precio)
        # productos = productos + [[nombre, categoria, precio]]
        
        productos.append([nombre, categoria, int(precio)])  
    
    
    elif opcion == "2":
        print("Listar productos")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            numero = 1
            for producto in productos:
                print(f"ID:{numero} \n Nombre: {producto[0]} \n Categoria: {producto[1]} \n Precio: ${producto[2]}")
                numero = numero + 1
    
    elif opcion == "3":
        print('Buscar producto')
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            busqueda = input("Ingresa el nombre del producto ").strip()
            while busqueda == "":
                print("El campo de busqueda no debe estar vacio")
                busqueda = input("Ingresa el nombre del producto").strip()
            encontrado = 0
            numero = 1
            for producto in productos:
                if busqueda.lower() in producto[0].lower():
                    print(f"ID:{numero} \n Nombre: {producto[0]} \n Categoria: {producto[1]} \n Precio: ${producto[2]}")
                    encontrado = encontrado + 1
                    numero += 1
            
            if encontrado == 0:
                print("No se encontraron productos con ese nombre:", busqueda)
                
                
    elif opcion == "4":
        print()
        print("Elimanar producto")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            numero = 1
            for producto in productos:
                print(f"ID:{numero} \n Nombre: {producto[0]} \n Categoria: {producto[1]} \n Precio: ${producto[2]}")
                numero = numero + 1
            
            posicion = input("Numero del producto a eliminar").strip()
            while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(productos):
                print(f"Ingresa un numero valido entre 1 y {len(productos)}")
                posicion = input("Numero del producto a eliminar").strip()
                                                                                          #1 - 1 = 0
            eliminado = productos.pop(int(posicion) - 1) # [nombre, categoria, precio] #posicion - 1
            print(f"Producto '{eliminado[0]}' eliminado correctamente")
        
    elif opcion == "5":
        print("Gracias por usar el sistema! Hasta luego!")
    else:
        print("Opcion invalida: Elegi un numero del 1 al 5.")
    