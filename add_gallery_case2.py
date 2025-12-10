import re

# Leer el archivo HTML
with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sección de galería de imágenes para el Caso de Uso 2
gallery_html = '''
                        
                        <!-- Gallery Section Case 2 -->
                        <div style="margin-top: 30px; padding-top: 30px; border-top: 2px solid #e2e8f0;">
                            <h4 style="font-size: 1.3em; font-weight: 600; color: #1e293b; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                                <span>🖼️</span> Resultados y Visualizaciones
                            </h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/case2/image1.png" alt="Pipeline LMVAE para clasificación de facies" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Pipeline completo del LMVAE para clasificación no supervisada de facies
                                    </div>
                                </div>
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/case2/image2.png" alt="Resultados de clustering en espacio latente" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Resultados del clustering en el espacio latente y visualización de facies identificadas
                                    </div>
                                </div>
                            </div>
                        </div>'''

# Buscar el final del Caso de Uso 2 (justo antes del cierre de divs)
# Patron para encontrar el final de la sección "Valor para el negocio" del Caso 2
pattern = r'(Código libre, eliminando dependencias de software propietario</li>\s*</ul>\s*</div>\s*</div>)\s*(</div>)'

# Verificar si encontramos el patrón
if re.search(pattern, content):
    # Reemplazar para insertar la galería
    replacement = r'\1' + gallery_html + r'\n                    \2'
    modified_content = re.sub(pattern, replacement, content, count=1)
    
    # Guardar el archivo modificado
    with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print("✅ Galería de imágenes agregada exitosamente al Caso de Uso 2!")
else:
    print("❌ No se encontró el patrón esperado. Verificando alternativas...")
    # Buscar una alternativa más simple
    pattern2 = r'(software propietario</li>\s*</ul>\s*</div>\s*</div>)\s*(</div>\s*</div>\s*</div>\s*</div>)'
    if re.search(pattern2, content):
        replacement = r'\1' + gallery_html + r'\n                    \2'
        modified_content = re.sub(pattern2, replacement, content, count=1)
        
        with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        print("✅ Galería de imágenes agregada exitosamente al Caso de Uso 2 (patrón alternativo)!")
    else:
        print("❌ Error: No se pudo encontrar el patrón para insertar la galería")
