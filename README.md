# Agente de Recopilación de Papers: IA en Interpretación Sísmica

## 📋 Descripción

Este proyecto contiene un agente automatizado para recopilar papers geofísicos sobre aplicaciones de Inteligencia Artificial en interpretación sísmica. El agente busca en múltiples fuentes académicas confiables y genera informes profesionales para evaluación de proyectos de I+D.

## 🎯 Características

- **Búsqueda Multi-fuente**: Recopila papers de:
  - arXiv (API oficial)
  - SEG Library (Society of Exploration Geophysicists)
  - OnePetro (biblioteca técnica de petróleo y gas)
  
- **Filtrado Inteligente**: 
  - Sistema de scoring de relevancia basado en palabras clave
  - Filtro por años recientes (últimos 5 años)
  - Eliminación de duplicados

- **Informes Profesionales**:
  - Informe en Markdown (`.md`)
  - Informe HTML interactivo y visualmente atractivo
  - Base de datos JSON para procesamiento posterior

## 📂 Estructura de Archivos

```
IA_papers/
├── seismic_ai_research_agent.py   # Agente principal de búsqueda
├── generate_html_report.py        # Generador de informe HTML
├── requirements.txt                # Dependencias Python
├── informe_papers_ia_sismica.md   # Informe en Markdown
├── informe_ia_sismica.html        # Informe HTML interactivo
├── papers_database.json           # Base de datos de papers
└── README.md                      # Este archivo
```

## 🚀 Uso

### Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución

```bash
# Ejecutar el agente de búsqueda
python seismic_ai_research_agent.py

# Generar informe HTML
python generate_html_report.py
```

## 🔧 Configuración

### Modificar Parámetros de Búsqueda

Edita `seismic_ai_research_agent.py`:

```python
# Cambiar número máximo de resultados por búsqueda
agent.search_arxiv(
    keywords=['seismic', 'interpretation', 'machine learning'],
    max_results=30  # Modificar aquí
)

# Agregar más términos de búsqueda
search_terms = [
    "seismic interpretation machine learning",
    "tu nuevo término aquí",
    # ...
]
```

### Filtro de Relevancia

En `generate_html_report.py`, modifica el umbral de relevancia:

```python
# Filtrar papers más relevantes (score > 3.0)
relevant_papers = [p for p in papers if p.get('relevance_score', 0) > 3.0]
```

## 📊 Sistema de Scoring

El agente asigna scores de relevancia basados en palabras clave:

- **Alta relevancia (3.0 puntos c/u)**:
  - seismic interpretation
  - machine learning
  - deep learning
  - fault detection
  - horizon picking
  - facies classification

- **Media relevancia (1.5 puntos c/u)**:
  - artificial intelligence
  - CNN, RNN
  - supervised learning
  - geophysics

- **Baja relevancia (0.5 puntos c/u)**:
  - data, model, algorithm

## 📝 Formatos de Salida

### 1. Markdown (`informe_papers_ia_sismica.md`)
- Formato texto plano con formato Markdown
- Ideal para documentación técnica
- Fácil de versionar en Git

### 2. HTML (`informe_ia_sismica.html`)
- Informe interactivo y visualmente atractivo
- Diseño responsive (adaptable a móviles)
- Estadísticas visuales
- Tarjetas de papers con enlaces directos
- Recomendaciones de proyectos

### 3. JSON (`papers_database.json`)
- Base de datos estructurada
- Ideal para procesamiento programático
- Integración con otros sistemas

## 🎯 Proyectos Recomendados

El informe identifica oportunidades de alto impacto:

1. **Detección Automática de Fallas**
   - Tecnologías: CNN, U-Net, Transfer Learning
   - ROI: Reducción de tiempo en 60-80%

2. **Clasificación de Facies Sísmicas**
   - Tecnologías: SOM, Random Forest, Deep Learning
   - ROI: Mejora en predicción litológica

3. **Horizon Picking Inteligente**
   - Tecnologías: U-Net, Segmentación semántica
   - ROI: Automatización de tarea manual

4. **Inversión Sísmica con Physics-Informed AI**
   - Tecnologías: PINN, Neural Operators
   - ROI: Mejora resolución del subsuelo

5. **Generación de Datos Sintéticos**
   - Tecnologías: GANs, Simulación física
   - ROI: Facilita desarrollo de otros proyectos

## 🔍 Fuentes de Datos

### arXiv
- **Acceso**: API pública
- **Cobertura**: Papers de física, matemáticas, ciencias de la computación
- **Ventajas**: Acceso gratuito, abstracts completos, preprints más recientes

### SEG Library
- **Acceso**: Web scraping de páginas públicas
- **Cobertura**: Journal of Geophysics, The Leading Edge, conference papers
- **Ventajas**: Contenido altamente especializado en geofísica

### OnePetro
- **Acceso**: Web scraping de páginas públicas
- **Cobertura**: 1.3M+ documentos técnicos de la industria petrolera
- **Ventajas**: Aplicaciones industriales, casos de estudio

## 🛠️ Desarrollo Futuro

Posibles mejoras:

- [ ] Integración con Google Scholar API
- [ ] Acceso a APIs de IEEE Xplore
- [ ] Sistema de notificaciones para nuevos papers
- [ ] Análisis de citaciones
- [ ] Extracción automática de metodologías
- [ ] Clasificación por subcategorías
- [ ] Generación de gráficos de tendencias

## 📧 Mantenimiento

Para actualizar la base de datos de papers:

```bash
# Re-ejecutar el agente
python seismic_ai_research_agent.py

# Re-generar el informe HTML
python generate_html_report.py
```

## 📚 Referencias

- **SEG**: https://library.seg.org
- **OnePetro**: https://onepetro.org
- **arXiv**: https://arxiv.org

## 📄 Licencia

Este proyecto es para uso interno de evaluación de proyectos de I+D.

---

**Última actualización**: Diciembre 2025  
**Generado por**: Agente de Investigación de IA en Geofísica
