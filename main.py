from json import load
from antlr4 import *
from grammarTraductorLexer import grammarTraductorLexer
from grammarTraductorParser import grammarTraductorParser
from grammarTraductorListener import grammarTraductorListener

# Crear una clase que extienda grammarTraductorListener
class TraductorCodeListener(grammarTraductorListener):
    
    # Constructor de la clase
    def __init__(self):
        # Para almacenar datos en la clase 
        # (Funciones, variables y codigo del main)
        self.functions = {}
        self.main_function = []
        self.declared_variables = {"main": set()}
        self.java_code = ""
    
    def enterFunction_declaration(self, ctx: grammarTraductorParser.Function_declarationContext):
        # Guardar la declaración de la función en el diccionario
        # Obtenemos el nombre de la funcion y el valor de retorno predeterminado void
        function_name = ctx.ID().getText()
        return_content = "void"
        
        # Obtener los parámetros de la función
        params = []
        param_list = ctx.param_list()
        if param_list is not None:
            for param in param_list.param():
                params.append(param.ID().getText())

        # Crear una entrada en el diccionario para la función
        self.functions[function_name] = {
            'return_content': return_content,
            'params': params,
            'body': []  
        }
    
    def exitProgram(self, ctx: grammarTraductorParser.ProgramContext):
        
        # Generamos el codigo en java
        self.java_code = self.generateCode()
        
        # Especificamos el nombre del archivo y abrimos en modo de escritura
        file_name = "Main.java"
        with open(file_name, "w") as file:
            file.write(self.java_code)

        print(f"El código Java ha sido guardado en el archivo '{file_name}'.")
        print(self.java_code)

    def enterCode_block(self, ctx: grammarTraductorParser.Code_blockContext):
        pass

    def exitCode_block(self, ctx: grammarTraductorParser.Code_blockContext):
        pass
    
    def enterStatement(self, ctx: grammarTraductorParser.StatementContext):
        # Bandera para controlar si se esta en un bloque de codigo o no
        isInCode_Block = False
        
        # Nombre de la funcion en la que se esta
        function_name = "main"
        
        # Revisamos si el 'statement' esta dentro de un 'code_bloc'
        if isinstance(ctx.parentCtx, grammarTraductorParser.Code_blockContext):
            # Actualizamos la bandera
            isInCode_Block = True
            # Obtenemos el nombre de la funcion padre
            function_name = ctx.parentCtx.parentCtx.function_declaration().ID().getText()
            
            # Comprobamos si la funcion ya se habia encontrado en 
            if function_name not in self.declared_variables:
                self.declared_variables[function_name] = set()
            
        # Verificamos si el statement es un return_statement
        if ctx.return_statement():
            
            # Obtenemos el nombre de la funcion padre
            function_name = ctx.parentCtx.parentCtx.function_declaration().ID().getText()
            
            # Obtenemos la expresion de retorno
            return_expr = ctx.return_statement().expr().getText()
            
            # Si obtuvimos una el nombre de la funcion, ponemos la expresion de retorno en el diccionario de funciones
            if function_name:
                self.functions[function_name]['return_content'] = return_expr


        # Verificamos si el statement es una llamada a función
        elif ctx.function_call():
            # Obtenemos el contenido de la funcion
            function_call = ctx.function_call()
            
            # Obtenemos el nombre de la funcion llamada
            function_called = function_call.ID().getText()
            
            # Cadena para generar la expresion
            statement = ""
            
            # Si la función llamada es `print`, traducimos a formato Java
            if function_called == "print":
                
                # Traducir el print de Python a un equivalente en Java
                statement = "System.out.println("
                
                # Obtenemos el argumento de la función print (suponiendo un solo argumento por simplicidad)
                if function_call.arg_list():
                    statement += function_call.arg_list().getText()
                
                statement += ")"                 
            else:
                # Si es cualquier otra función, imprimir la llamada tal como está
                statement += function_call.getText()+";\n"
                True
            
            if isInCode_Block:
                # Nombre de la funcion padre
                father_fuction_name = ctx.parentCtx.function_declaration().ID().getText()
                self.functions[father_fuction_name]['body'].append(statement)
                
            else:
                self.main_function.append(statement)
        # Otros tipos de statements
        else:
            # Extraer el nombre de la variable del statement
            variable_name = ctx.assignment().ID().getText()
            statement = ""
            # Verificar si la variable ya fue declarada en la función actual
            if variable_name not in self.declared_variables[function_name]:
                
                # Declaración inicial con `int` si no está en el conjunto
                statement = f"int {ctx.getText()}"
                
                # Registrar la variable como declarada en esta función
                self.declared_variables[function_name].add(variable_name)
            else:
                # Solo la asignación sin `int` si ya está declarada
                statement = f"{ctx.getText()}"
                
                
            if isInCode_Block:
                function_name = ctx.parentCtx.parentCtx.function_declaration().ID().getText()
                self.functions[function_name]['body'].append(statement)
            else:
                self.main_function.append(statement)

    def generateCode(self):
        # Iniciamos la clase
        code = "public class Main {\n"
        
        # Iniciamos la funcion principal
        code += "\n\tpublic static void main(String[] args) {\n"
        
        # Recorremos todas las instrucciones guardadas en la clase principal
        for statement in self.main_function:
            code += "\t\t" + statement +";\n"
            
        # Cerramos la funcion principal
        code += "\t}\n\n"
        
        # Recorremos todas las funciones que se hayan generado
        for functionName in self.functions:
            function = self.functions[functionName]
            code += (f"\t public static int {functionName}(")
            code += ", ".join([f"int {param}" for param in function['params']])
            code += ") {\n"
            
            # Recorremos todas las instrucciones guardadas en el cuerpo de la funciiion
            for statement in function['body'] :
                code += "\t\t" + statement +";\n"
            
            # Imprimimos el retorno
            code += "\t\treturn " + function['return_content'] + ";\n"
            
            # Cerramos la funcion
            code += "\t}\n"
        # Cerramos la clase
        code += "\n}"
        return code
    
def loadFile(link):
    content = open(link, "r").read()
    #print(repr(content))
    return content

def main():
    fileName = input("Ingrese el nombre del archivo (Se considerara que es .txt, por lo que no ponga la extencion)")
    link = fileName + ".txt"
    code = loadFile(link)
    #print(f'Codigo en python \n{code}')
    lexer = grammarTraductorLexer(InputStream(code))
    stream = CommonTokenStream(lexer)
    parser = grammarTraductorParser(stream)
    tree = parser.program()
    
    #print(tree.toStringTree(recog=parser))
    
    # Crear una instancia de ParseTreeWalker y TraductorCodeListener
    walker = ParseTreeWalker()
    listener = TraductorCodeListener()
    
    # Recorrer el árbol y activar la traducción de Traductor a texto
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
