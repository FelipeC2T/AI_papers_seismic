import re

# Leer el archivo HTML
with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sección de galería de imágenes
gallery_html = '''
                        
                        <!-- Gallery Section -->
                        <div style="margin-top: 30px; padding-top: 30px; border-top: 2px solid #e2e8f0;">
                            <h4 style="font-size: 1.3em; font-weight: 600; color: #1e293b; margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
                                <span>🖼️</span> Resultados y Visualizaciones
                            </h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/image1.png" alt="Cubos sísmicos sintéticos - Entrenamiento" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Cubos sísmicos sintéticos utilizados para entrenamiento
                                    </div>
                                </div>
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/image2.png" alt="Cubos sísmicos sintéticos - Testeo" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Cubos sísmicos de testeo
                                    </div>
                                </div>
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/image3.png" alt="Arquitectura del modelo" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Arquitectura del modelo CNN 3D
                                    </div>
                                </div>
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/image4.png" alt="Resultados en datos reales" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Resultados en datos reales
                                    </div>
                                </div>
                                <div style="background: #f8fafc; border-radius: 12px; overflow: hidden; border: 2px solid #e2e8f0;">
                                    <img src="images/image5.png" alt="Caso real offshore" style="width: 100%; height: auto; display: block;">
                                    <div style="padding: 15px; font-size: 0.9em; color: #64748b; text-align: center; font-weight: 500;">
                                        Aplicación en caso real offshore
                                    </div>
                                </div>
                            </div>
                        </div>'''

# Buscar el lugar donde termina el último <li> de la sección "Valor para el negocio" del Caso de Uso 1
# y donde comienza el cierre de divs
pattern = r'(Mayor velocidad para analizar múltiples cubos en paralelo</li>\s*</ul>\s*</div>\s*</div>)\s*(</div>\s*<!-- Caso de Uso 2 -->)'

# Reemplazar para insertar la galería
replacement = r'\1' + gallery_html + r'\n                    \2'
modified_content = re.sub(pattern, replacement, content, count=1)

# Guardar el archivo modificado
with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Galería de imágenes agregada exitosamente!")
