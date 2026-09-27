# Extractor de PDF — Manual de usuario

Esta aplicación web te permite cargar un archivo PDF, ver su contenido de texto directamente en el navegador y descargarlo como un archivo `.txt`.

## Cómo iniciar la aplicación

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:
   ```
   uv run pdf-sso-prycto-mla-prctca-2026
   ```
3. Abre tu navegador en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Cómo usarla

### 1. Cargar un PDF
- En la página principal verás un botón **"Cargar PDF"** junto a un selector de archivo.
- Haz clic en el selector, elige el PDF desde tu computadora y luego presiona **"Cargar PDF"**.
- Solo se aceptan archivos con extensión `.pdf`. Si eliges otro tipo de archivo o no seleccionas ninguno, verás un mensaje de error pidiéndote un PDF válido.

### 2. Ver el contenido extraído
- Después de cargar el archivo, la página se actualiza automáticamente mostrando:
  - El nombre del archivo cargado.
  - El texto extraído del PDF, dentro de un recuadro con scroll si el texto es largo.

### 3. Exportar a TXT
- Debajo del texto extraído aparece el botón **"Exportar a TXT"**.
- Al hacer clic, tu navegador descargará un archivo `.txt` con el mismo contenido que se muestra en pantalla, usando el nombre del PDF original.

### 4. Cargar otro PDF
- Puedes repetir el proceso en cualquier momento: selecciona un nuevo archivo y presiona **"Cargar PDF"** de nuevo. El contenido mostrado se reemplaza por el del nuevo archivo.

## Limitaciones a tener en cuenta

- **Tamaño máximo por archivo:** 20 MB. Archivos más grandes serán rechazados.
- **PDFs escaneados o basados en imágenes:** si el PDF no contiene texto real (por ejemplo, es una foto o escaneo sin OCR), el resultado puede aparecer vacío o incompleto, ya que la extracción funciona sobre texto embebido, no sobre imágenes.
- **Un archivo a la vez:** cada carga reemplaza al PDF anterior; no se guarda un historial de archivos cargados.
