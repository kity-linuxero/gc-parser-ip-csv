# Parser GC Labeler
Un Script para procesar y convertir archivos "Malicious IP" `top_ips.csv` a un formato CSV compatible con GC-Labeler.

## Uso
Se debe ejecutar como `./parser_labeler.exe`. Los siguientes parámetros están disponibles:

- `-h`, `--help`: Imprime listado de comandos
- `-o ORIGEN`, `--origen ORIGEN`: Archivo CSV origen con IPs.
- `-d DESTINO`, `--destino DESTION`: (Opcional) Archivo CSV destino para guardar el resultado (Por defecto `exported.csv`).
- `-t TAG`, `--tag TAG`: Indica el tag donde se asignarán las IPs maliciosas. (Por defecto `IP_Maliciosas`).
- `--version`: Muestra la versión del programa y sale.

## Ejemplo:

```powershell
./parse_labeler.exe -o top_ips.csv -o archivo_exportado.csv -t "BAD_IPS"

Se terminó el proceso sin errores:
Se han procesado 49 IPs

```



