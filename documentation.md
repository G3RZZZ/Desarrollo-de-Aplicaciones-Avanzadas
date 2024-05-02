# Evidencia Final Compiladores
## Desarrollo de aplicaciones avanzadas de ciencias computacionales 

- Gerardo Gutierrez Paniagua - A01029422
- Mateo Herrera Lavalle - A01751912
- Jacobo Soffer Levy - A01028653


## Indice

- [Reglas de la Gramática Implementada](#reglas-de-la-gramática-implementada)
- [Funciones](#funciones)
- [Demostración](#demostración)
    - [Operaciones numéricas básicas](#operaciones-numéricas-básicas)
    - [Manejo de imágenes con OpenCV](#manejo-de-imágenes-con-opencv)
    - [Aceptación de archivos y ejecución de su contenido](#aceptación-de-archivos-y-ejecución-de-su-contenido)
    - [Implementación de funciones](#implementación-de-funciones)
- [Conclusiones Individuales](#conclusiones-individuales)



## Reglas de la Gramática Implementada

    assignment      : VARIABLE SETTO expression 
                    | VARIABLE CONNECT flow 
                    | expression



    top_level       : top_level_expr 
                    | top_level top_level_expr

    top_level_expr  : assignment newline 
                    | function_definition newline 
                    | expression newline

    flow            : VARIABLE CONNECT flow_functions

    flow_functions  : flow_function_call CONNECT flow_functions 
                    | flow_function_call

    flow_function_call : VARIABLE DOT LPAREN params RPAREN

    expression      : expression PLUS term 
                    | expression MINUS term
                    | term 
                    | string

    string             : STRING

    term            : term TIMES exponent 
                    | term DIVIDE exponent
                    | exponent
                    
    exponent        : factor EXP factor 
                    | factor
                    | LPAREN expression RPAREN

    factor          : NUMBER 
                    | VARIABLE 
                    | function_call

    function_call   : VARIABLE DOT LPAREN params RPAREN

    params          : params COMMA expression 
                    | expression 
                    | empty

    function_definition : VARIABLE LPAREN args RPAREN LBRACE newline statements newline RBRACE

    statements      : statement 
                    | statements newline statement

    statement       : assignment

    args            : VARIABLE COMMA args 
                    | VARIABLE 
                    | empty

    empty           :


## Funciones
Como herramientas adicionales o accesorios de la gramática, se utilizaron varias funciones adicionales que ayudan al manejo de imágenes por parte de OpenCV en el lexer, las cuáles se encuentran en el archivo library.py.

**load_image** carga una imagen utilizando la librería de OpenCV.

**save_image** guarda una imagen, tomando los parámetros en orden del nombre como se quiere guardar y la imagen a ser almacenada.

**show_image** muestra la imagen que se da como parámetro

**search_cv2** busca y devuelve alguna función existente en la librería de OpenCV.

**gen_matrix** genera una matriz utilizando los primeros dos parámetros como los datos para las dimensiones y posterior los elementos que irían dentro de la matriz.

**gen_vector** genera un vector usando la librería NumPy con los parámetros que se le proveen.

## Demostración
Demostraciones de la implementación de procesamientos de imágenes de OpenCV junto con flujos de transformaciones en esas imágenes. Al igual que la adición de funcionalidades como la aceptación de archivos y la ejecución de su contenido junto con la implementación de funciones. 

### Funcionalidades básicas 

#### Operaciones numéricas básicas

    >5 + 5 - 3 * 2 / 1
    TREE_RESULT:  4.0

![basic_operations](/basicOps.png)

    
#### Asignación de variables

    >a = 5
    TREE_RESULT:  5.0
    >a
    TREE_RESULT:  5.0
![variable_assignment](/varAssign.png)

    >a + 5
    TREE_RESULT:  10.0


### Manejo de imágenes con OpenCV

#### Cargar y mostrar una imagen

    >img = load_image("test.jpg")
    >show_image(img)

![test.jpg](/test.jpg)

#### Buscar y ejecutar una función de OpenCV

    >img2 = blur(img, gen_vector(5, 5))
    >show_image(img2)
    >save_image("blurred.jpg", img2)

![blurred.jpg](/blurred.jpg)


### Aceptación de archivos y ejecución de su contenido



### Implementación de funciones



## Conclusiones Individuales
Enlaces a los videos individuales:

Video: [![Gerardo Gutierrez Paniagua]()](https://www.youtube.com/watch?v=1mLkspkZ5UevL_AIoTtATdBphluvQkwk6)

- Mateo Herrera Lavalle - 
- Jacobo Soffer Levy - 

## Referencias

La implementación de la gramática fue implementada parcialmente con base en sugerencias hechas por la herramienta de Inteligencia Artificial Copilot de GitHub.
