"""
Generador de Informe HTML Profesional para Papers de IA en Interpretación Sísmica
"""

import json
from datetime import datetime


def generate_html_report(json_file: str, output_file: str):
    """
    Genera un informe HTML profesional a partir de la base de datos de papers
    """
    
    # Leer datos
    with open(json_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    # Filtrar papers más relevantes (score > 3.0)
    relevant_papers = [p for p in papers if p.get('relevance_score', 0) > 3.0]
    relevant_papers.sort(key=lambda x: (x['relevance_score'], x['year']), reverse=True)
    
    # Estadísticas
    total_papers = len(papers)
    high_relevance = len([p for p in papers if p.get('relevance_score', 0) > 5.0])
    medium_relevance = len([p for p in papers if 3.0 < p.get('relevance_score', 0) <= 5.0])
    
    # Agrupar por año
    papers_by_year = {}
    for paper in relevant_papers:
        year = paper['year']
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)
    
    # HTML
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe: IA en Interpretación Sísmica</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 700;
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .header .date {{
            margin-top: 20px;
            font-size: 0.95em;
            opacity: 0.8;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            border-left: 4px solid #667eea;
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-card .number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .stat-card .label {{
            color: #666;
            font-size: 0.95em;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 50px;
        }}
        
        .section h2 {{
            font-size: 2em;
            color: #1e3c72;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }}
        
        .section h3 {{
            font-size: 1.5em;
            color: #2a5298;
            margin: 30px 0 20px 0;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .year-badge {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        
        .paper-card {{
            background: #f8f9fa;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
            transition: all 0.3s ease;
        }}
        
        .paper-card:hover {{
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transform: translateX(5px);
        }}
        
        .paper-card .paper-title {{
            font-size: 1.3em;
            color: #1e3c72;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .paper-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 15px;
            font-size: 0.9em;
            color: #666;
        }}
        
        .paper-meta span {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        .badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.85em;
            font-weight: 500;
        }}
        
        .badge-source {{
            background: #e3f2fd;
            color: #1976d2;
        }}
        
        .badge-year {{
            background: #f3e5f5;
            color: #7b1fa2;
        }}
        
        .relevance {{
            color: #ff9800;
            font-weight: bold;
        }}
        
        .paper-abstract {{
            color: #555;
            line-height: 1.7;
            margin-top: 15px;
            padding: 15px;
            background: white;
            border-radius: 8px;
        }}
        
        .paper-url {{
            margin-top: 15px;
        }}
        
        .paper-url a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }}
        
        .paper-url a:hover {{
            text-decoration: underline;
        }}
        
        .recommendations {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-top: 40px;
        }}
        
        .recommendations h2 {{
            color: white;
            border-bottom-color: rgba(255,255,255,0.3);
        }}
        
        .recommendation-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        
        .recommendation-card {{
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 25px;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.2);
        }}
        
        .recommendation-card h4 {{
            font-size: 1.2em;
            margin-bottom: 15px;
            color: white;
        }}
        
        .recommendation-card p {{
            font-size: 0.95em;
            line-height: 1.6;
            opacity: 0.95;
            margin-bottom: 10px;
        }}
        
        .recommendation-card .tag {{
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 5px 10px;
            border-radius: 15px;
            font-size: 0.85em;
            margin-top: 10px;
            margin-right: 5px;
        }}
        
        .footer {{
            background: #1e3c72;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .areas-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .area-item {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .area-item h4 {{
            color: #1e3c72;
            margin-bottom: 10px;
        }}
        
        .area-item p {{
            color: #666;
            font-size: 0.95em;
        }}
        
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Aplicaciones de IA en Interpretación Sísmica</h1>
            <div class="subtitle">Informe de Investigación Tecnológica</div>
            <div class="date">Generado el {datetime.now().strftime("%d de %B de %Y")}</div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">{total_papers}</div>
                <div class="label">Papers Encontrados</div>
            </div>
            <div class="stat-card">
                <div class="number">{high_relevance}</div>
                <div class="label">Alta Relevancia</div>
            </div>
            <div class="stat-card">
                <div class="number">{medium_relevance}</div>
                <div class="label">Relevancia Media</div>
            </div>
            <div class="stat-card">
                <div class="number">{len(papers_by_year)}</div>
                <div class="label">Años Cubiertos</div>
            </div>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📋 Resumen Ejecutivo</h2>
                <p>Este informe presenta una recopilación exhaustiva de investigaciones sobre la aplicación de <strong>Inteligencia Artificial y Machine Learning</strong> en interpretación sísmica geofísica. Se han analizado {total_papers} publicaciones de fuentes académicas reconocidas, identificando {len(relevant_papers)} papers de alta relevancia para posibles proyectos de exploración.</p>
                
                <div class="areas-list">
                    <div class="area-item">
                        <h4>🔍 Detección de Fallas</h4>
                        <p>Uso de CNNs y redes neuronales profundas para identificación automática de fallas sísmicas</p>
                    </div>
                    <div class="area-item">
                        <h4>🎯 Clasificación de Facies</h4>
                        <p>Algoritmos de clustering y clasificación para análisis de facies sísmicas</p>
                    </div>
                    <div class="area-item">
                        <h4>📊 Horizon Picking</h4>
                        <p>Selección automática de horizontes sísmicos con deep learning</p>
                    </div>
                    <div class="area-item">
                        <h4>🔄 Inversión Sísmica</h4>
                        <p>Técnicas de ML para mejorar procesos de inversión sísmica</p>
                    </div>
                    <div class="area-item">
                        <h4>🧠 Physics-Informed AI</h4>
                        <p>Integración de principios físicos en modelos de IA</p>
                    </div>
                    <div class="area-item">
                        <h4>🎲 Datos Sintéticos</h4>
                        <p>Generación de datos de entrenamiento con GANs</p>
                    </div>
                </div>
            </div>
"""

    # Papers por año
    html += """
            <div class="section">
                <h2>📚 Papers Relevantes</h2>
"""
    
    for year in sorted(papers_by_year.keys(), reverse=True):
        html += f"""
                <h3><span class="year-badge">{year}</span> {len(papers_by_year[year])} publicaciones</h3>
"""
        
        for i, paper in enumerate(papers_by_year[year][:15], 1):  # Limitar a 15 por año
            authors_str = ", ".join(paper['authors'][:3])
            if len(paper['authors']) > 3:
                authors_str += " et al."
            
            relevance_stars = "⭐" * min(5, int(paper.get('relevance_score', 0) / 2))
            
            html += f"""
                <div class="paper-card">
                    <div class="paper-title">{i}. {paper['title']}</div>
                    <div class="paper-meta">
                        <span>👤 {authors_str}</span>
                        <span class="badge badge-source">{paper['source']}</span>
                        <span class="badge badge-year">{paper['year']}</span>
                        <span class="relevance">{relevance_stars}</span>
                    </div>
                    <div class="paper-abstract">
                        {paper['abstract'][:400]}{"..." if len(paper['abstract']) > 400 else ""}
                    </div>
                    <div class="paper-url">
                        <a href="{paper['url']}" target="_blank">🔗 Ver paper completo →</a>
                    </div>
                </div>
"""
    
    # Recomendaciones
    html += """
            </div>
            
            <div class="section recommendations">
                <h2>💡 Proyectos Recomendados</h2>
                <p>Con base en el análisis de la literatura actual, se identifican las siguientes oportunidades de alto impacto:</p>
                
                <div class="recommendation-grid">
                    <div class="recommendation-card">
                        <h4>🎯 Detección Automática de Fallas</h4>
                        <p><strong>Objetivo:</strong> Sistema de ML para identificación automática de fallas en datos sísmicos 3D</p>
                        <p><strong>Tecnologías:</strong> CNN, U-Net, Transfer Learning</p>
                        <p><strong>ROI:</strong> Reducción de tiempo en 60-80%</p>
                        <span class="tag">Alta Prioridad</span>
                        <span class="tag">Complejidad Media</span>
                    </div>
                    
                    <div class="recommendation-card">
                        <h4>📊 Clasificación de Facies</h4>
                        <p><strong>Objetivo:</strong> Implementar clustering y clasificación para análisis de facies</p>
                        <p><strong>Tecnologías:</strong> SOM, Random Forest, Deep Learning</p>
                        <p><strong>ROI:</strong> Mejora en predicción litológica</p>
                        <span class="tag">Prioridad Media</span>
                        <span class="tag">Complejidad Media</span>
                    </div>
                    
                    <div class="recommendation-card">
                        <h4>🔄 Horizon Picking Inteligente</h4>
                        <p><strong>Objetivo:</strong> Automatizar selección de horizontes sísmicos</p>
                        <p><strong>Tecnologías:</strong> U-Net, Segmentación semántica</p>
                        <p><strong>ROI:</strong> Automatización de tarea manual</p>
                        <span class="tag">Alta Prioridad</span>
                        <span class="tag">Complejidad Alta</span>
                    </div>
                    
                    <div class="recommendation-card">
                        <h4>🧠 Inversión con Physics-Informed AI</h4>
                        <p><strong>Objetivo:</strong> Mejorar inversión sísmica con PINN</p>
                        <p><strong>Tecnologías:</strong> Physics-Informed Neural Networks</p>
                        <p><strong>ROI:</strong> Mejora resolución del subsuelo</p>
                        <span class="tag">ROI Muy Alto</span>
                        <span class="tag">Complejidad Muy Alta</span>
                    </div>
                    
                    <div class="recommendation-card">
                        <h4>🎲 Generación de Datos Sintéticos</h4>
                        <p><strong>Objetivo:</strong> Crear datos sísmicos sintéticos para entrenar modelos</p>
                        <p><strong>Tecnologías:</strong> GANs, Simulación física</p>
                        <p><strong>ROI:</strong> Facilita desarrollo de otros proyectos</p>
                        <span class="tag">Estratégico</span>
                        <span class="tag">Complejidad Alta</span>
                    </div>
                    
                    <div class="recommendation-card">
                        <h4>📈 Procesamiento Multi-task</h4>
                        <p><strong>Objetivo:</strong> Sistema integrado para múltiples tareas de interpretación</p>
                        <p><strong>Tecnologías:</strong> Multi-task Learning, Transformers</p>
                        <p><strong>ROI:</strong> Solución integral end-to-end</p>
                        <span class="tag">Visión a Futuro</span>
                        <span class="tag">Complejidad Muy Alta</span>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p><strong>Informe generado automáticamente por el Agente de Investigación de IA en Geofísica</strong></p>
            <p style="margin-top: 10px; opacity: 0.8;">Para consultas técnicas sobre papers específicos, por favor acceder a las URLs proporcionadas</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Guardar HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Informe HTML generado: {output_file}")


if __name__ == "__main__":
    generate_html_report(
        json_file="c:/Users/Felipe/Desktop/IA_papers/papers_database.json",
        output_file="c:/Users/Felipe/Desktop/IA_papers/informe_ia_sismica.html"
    )
