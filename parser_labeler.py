import csv
import argparse
import os

# Versión del programa
VERSION = "1.0"

def process_ips(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)
            
            # Escribir los encabezados del archivo de salida
            writer.writerow(['Target', 'Enforcement'])

            process_rows=0
            
            # Procesar cada fila del archivo de entrada
            for row in reader:
                ip_address = row['IP Name']
                writer.writerow([ip_address, 'IP_Maliciosas'])
                process_rows+=1


    except FileNotFoundError:
        print("No se encontró el archivo")
    except KeyError:
        print("Formato incorrecto en el archivo origen")
        # Para borrar el archivo destino
        os.remove(output_file)
    except:
        print("Ha ocurrido un error inesperado.")

    return process_rows

def main():
    # Configurar los argumentos del script
    parser = argparse.ArgumentParser(
        description='Procesa un archivo CSV de IPs maliciosas.',
        epilog='Desarrollado por [kity-linuxero] - cgiambruni@gmail.com'
    )
    
    parser.add_argument('-o', '--origen', required=True, help='Archivo CSV de origen con las IPs maliciosas')
    parser.add_argument('-d', '--destino', default='exported.csv', help='Archivo CSV de destino para guardar el resultado (por defecto: exported.csv)')
    parser.add_argument('-t', '--tag', default='IP_Maliciosas', help='Tag donde se asignarán el listado de IP (por defecto: IP_Maliciosas)')
    
    # Agregar el argumento --version para mostrar la versión del programa
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    
    args = parser.parse_args()
    
    # Ejecutar el procesamiento del archivo
    count = process_ips(args.origen, args.destino)

    # Finalizado sin error
    print("Se terminó el proceso sin errores:")
    if count > 0:
        print(f"Se han procesado {count} IPs")
    else:
        print("No se han procesado direcciones IPs")

if __name__ == "__main__":
    main()
