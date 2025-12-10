import re

# Leer el archivo HTML
with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Nuevo contenido para el Caso de Uso 2
case2_content = '''                    <!-- Caso de Uso 2 -->
                    <div class="use-case-card">
                        <div class="use-case-header">
                            <div class="use-case-number">2</div>
                            <h3 class="use-case-title">Clasificación No Supervisada de Facies Sísmicas con LMVAE</h3>
                        </div>
                        
                        <div class="use-case-section">
                            <h4 class="use-case-section-title">📋 Contexto</h4>
                            <div class="use-case-content">
                                <p>La caracterización de facies sísmicas es un proceso esencial para comprender la arquitectura interna de los reservorios. A diferencia de la detección de fallas, la clasificación de facies depende de patrones más sutiles del volumen sísmico: litologías, texturas, geometrías deposicionales y variaciones de estratigrafía fina.</p>
                                <p>Históricamente, este trabajo se realizaba mediante métodos supervisados que requieren etiquetas geológicas o clasificación manual previa, lo cual es costoso, lento y difícil de escalar. La exploración moderna requiere enfoques no supervisados que permitan identificar grupos y patrones directamente desde los volúmenes sísmicos, sin necesidad de datos etiquetados.</p>
                            </div>
                        </div>
                        
                        <div class="use-case-section">
                            <h4 class="use-case-section-title">⚠️ Problemática</h4>
                            <div class="use-case-content">
                                <p>La clasificación de facies presenta varios desafíos:</p>
                                <ul>
                                    <li><strong>No existen etiquetas "verdaderas"</strong> para entrenar modelos supervisados en la mayoría de los proyectos</li>
                                    <li>Los <strong>patrones de facies son más complejos y sutiles</strong> que las fallas, lo que dificulta el uso de CNNs simples</li>
                                    <li>La separación espacial de facies requiere <strong>capturar relaciones de alta dimensión</strong>, no detectables con atributos tradicionales</li>
                                    <li>Los modelos de clustering clásicos (PCA, k-means, GMM) <strong>no logran capturar la estructura real</strong> de los volúmenes</li>
                                    <li>Los métodos avanzados (VAEs, modelos de mezcla) <strong>demandan mucho poder de cómputo</strong>, especialmente con volúmenes 3D completos</li>
                                </ul>
                                <p>Esto genera la necesidad de un método no supervisado que pueda aprender representaciones útiles, separables y físicamente coherentes.</p>
                            </div>
                        </div>
                        
                        <div class="use-case-section">
                            <h4 class="use-case-section-title">✅ Solución Propuesta</h4>
                            <div class="use-case-content">
                                <p><strong>La solución combina:</strong></p>
                                <ul>
                                    <li>El enfoque del <span class="paper-reference">📄 Paper: Lognormal Mixture-based Variational Autoencoder (LMVAE)</span> para clustering no supervisado</li>
                                    <li>Un pipeline propio basado en volúmenes sísmicos sintéticos, los mismos del Caso de Uso 1</li>
                                    <li>Un diseño centrado en atributos linealmente independientes, clave para separar las facies en el espacio latente</li>
                                </ul>
                                
                                <p><strong>Fundamento técnico:</strong></p>
                                <p>El LMVAE utiliza un autoencoder variacional con una mezcla lognormal que:</p>
                                <ul>
                                    <li>Aprende una representación latente compacta del volumen sísmico</li>
                                    <li>Captura distribuciones complejas sin asumir gaussianidad</li>
                                    <li>Facilita la clusterización directa del espacio latente, sin necesidad de etiquetas</li>
                                </ul>
                                
                                <p><strong>Uso de cubos sintéticos:</strong></p>
                                <p>Tal como en el Caso 1, se emplearon cubos sísmicos sintéticos porque:</p>
                                <ul>
                                    <li>Permiten controlar variaciones litológicas y estratigráficas</li>
                                    <li>Son ideales para experimentación con diferentes geometrías deposicionales</li>
                                    <li>Generalizan muy bien a datos reales onshore y offshore</li>
                                    <li>Evitan costos y restricciones de confidencialidad</li>
                                </ul>
                                
                                <p><strong>1. Atributos linealmente independientes:</strong></p>
                                <p>Para mejorar la calidad del embedding latente y la separación de clusters, se priorizó un conjunto de atributos:</p>
                                <ul>
                                    <li>Estadísticos</li>
                                    <li>Geométricos</li>
                                    <li>Texturales</li>
                                    <li>Derivados locales del cubo</li>
                                </ul>
                                <p>La condición de <strong>independencia lineal</strong> permite:</p>
                                <ul>
                                    <li>✅ Reducir redundancia</li>
                                    <li>✅ Evitar colinealidad</li>
                                    <li>✅ Maximizar la información útil para el modelo</li>
                                    <li>✅ Mejorar la separabilidad de clusters en el espacio latente</li>
                                </ul>
                                <p>Esto fue fundamental para lograr que el LMVAE identifique facies geológicamente coherentes.</p>
                                
                                <p><strong>2. Manejo del poder de cómputo requerido:</strong></p>
                                <p>A diferencia del Caso 1, este enfoque exige una infraestructura más robusta:</p>
                                <ul>
                                    <li>GPUs con memoria extendida</li>
                                    <li>Procesamiento por bloques 3D</li>
                                    <li>Técnicas de optimización de entrenamiento</li>
                                    <li>Batch sizes adaptativos</li>
                                </ul>
                                <p>Se diseñó un pipeline que permite entrenar el LMVAE de manera eficiente, incluso combinando procesamiento distribuido cuando es necesario.</p>
                                
                                <p><strong>Valor para el negocio:</strong></p>
                                <ul>
                                    <li>✅ Identificación automática de facies, sin necesidad de etiquetas</li>
                                    <li>✅ Mejor entendimiento de heterogeneidades internas del reservorio</li>
                                    <li>✅ Reducción de tiempos, al evitar clasificaciones manuales o semisupervisadas</li>
                                    <li>✅ Mayor coherencia geológica gracias a atributos independientes y embebidos de alta calidad</li>
                                    <li>✅ Capacidad de escalar a múltiples cuencas y entornos (onshore y offshore)</li>
                                    <li>✅ Código libre, eliminando dependencias de software propietario</li>
                                </ul>
                            </div>
                        </div>
                    </div>'''

# Patrón para encontrar y reemplazar el Caso de Uso 2 completo
pattern = r'<!-- Caso de Uso 2 -->.*?</div>\s*</div>\s*</div>\s*</div>'

# Reemplazar todo el Caso de Uso 2
modified_content = re.sub(pattern, case2_content + '\n                </div>\n            </div>\n        </div>', content, count=1, flags=re.DOTALL)

# Guardar el archivo modificado
with open(r'c:\Users\Felipe\Desktop\IA_papers\index.html', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print("Caso de Uso 2 actualizado exitosamente!")
