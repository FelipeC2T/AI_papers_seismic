"""
Script de búsqueda mejorada - Búsqueda más específica en temas de interpretación sísmica con IA
"""

import requests
import json
from datetime import datetime
import xml.etree.ElementTree as ET
import time


def search_focused_arxiv():
    """
    Búsqueda focalizada en arXiv con términos altamente específicos
    """
    
    print("🔍 Búsqueda focalizada en papers de IA para interpretación sísmica...\n")
    
    base_url = "http://export.arxiv.org/api/query?"
    
    # Términos muy específicos para interpretación sísmica
    specific_queries = [
        "seismic data interpretation deep learning",
        "seismic fault detection neural network",
        "seismic horizon picking machine learning",
        "seismic facies classification CNN",
        "seismic inversion artificial intelligence",
        "seismic attribute analysis machine learning",
        "geophysical data processing deep learning",
        "subsurface imaging machine learning",
        "seismic image segmentation deep learning",
        "petroleum geophysics artificial intelligence",
        "reservoir characterization machine learning",
        "well log analysis neural network",
    ]
    
    all_papers = []
    
    for query_term in specific_queries:
        print(f"   📡 Buscando: '{query_term}'")
        
        # Construir query con filtros específicos
        query = f"search_query=all:{query_term}&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending"
        
        try:
            response = requests.get(base_url + query, timeout=30)
            
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                
                ns = {
                    'atom': 'http://www.w3.org/2005/Atom',
                    'arxiv': 'http://arxiv.org/schemas/atom'
                }
                
                entries = root.findall('atom:entry', ns)
                count = 0
                
                for entry in entries:
                    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                    summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                    published = entry.find('atom:published', ns).text[:10]
                    authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
                    link = entry.find('atom:id', ns).text
                    
                    # Filtrar por año
                    pub_year = int(published[:4])
                    if pub_year >= 2020:  # Últimos 5 años
                        
                        # Calcular relevancia
                        relevance = calculate_relevance(title, summary)
                        
                        # Solo guardar si es altamente relevante
                        if relevance >= 4.0:
                            paper = {
                                'title': title,
                                'authors': authors,
                                'abstract': summary,
                                'year': pub_year,
                                'source': 'arXiv',
                                'url': link,
                                'published_date': published,
                                'relevance_score': relevance,
                                'search_term': query_term
                            }
                            
                            # Evitar duplicados
                            if not any(p['title'] == title for p in all_papers):
                                all_papers.append(paper)
                                count += 1
                
                print(f"      ✓ {count} papers relevantes encontrados")
                time.sleep(3)  # Rate limiting
                
        except Exception as e:
            print(f"      ✗ Error: {str(e)}")
            continue
    
    return all_papers


def calculate_relevance(title: str, abstract: str) -> float:
    """
    Calcula score de relevancia mejorado
    """
    text = (title + ' ' + abstract).lower()
    score = 0.0
    
    # Palabras clave de MUY alta relevancia (peso 5.0)
    ultra_high = [
        'seismic interpretation',
        'seismic data interpretation',
        'seismic fault detection',
        'seismic horizon',
        'seismic facies',
        'seismic inversion',
        'seismic attribute'
    ]
    
    # Palabras clave de alta relevancia (peso 3.0)
    high_keywords = [
        'geophysical',
        'subsurface',
        'reservoir characterization',
        'well log',
        'petroleum exploration',
        'seismic survey',
        'seismic processing',
        'seismic image',
        'reflection seismology'
    ]
    
    # Técnicas de ML/DL (peso 2.0)
    ml_keywords = [
        'convolutional neural network',
        'deep learning',
        'machine learning',
        'u-net',
        'semantic segmentation',
        'encoder-decoder',
        'transfer learning',
        'supervised learning',
        'unsupervised learning',
        'self-organizing map'
    ]
    
    # Términos complementarios (peso 1.0)
    complementary = [
        'neural network',
        'artificial intelligence',
        'classification',
        'regression',
        'prediction',
        'automation'
    ]
    
    for kw in ultra_high:
        if kw in text:
            score += 5.0
    
    for kw in high_keywords:
        if kw in text:
            score += 3.0
    
    for kw in ml_keywords:
        if kw in text:
            score += 2.0
    
    for kw in complementary:
        if kw in text:
            score += 1.0
    
    return score


def main():
    print("=" * 80)
    print("  BÚSQUEDA FOCALIZADA: Papers de IA en Interpretación Sísmica")
    print("=" * 80)
    print()
    
    papers = search_focused_arxiv()
    
    # Ordenar por relevancia
    papers.sort(key=lambda x: (x['relevance_score'], x['year']), reverse=True)
    
    print(f"\n{'=' * 80}")
    print(f"✅ Búsqueda completada!")
    print(f"   Total de papers altamente relevantes: {len(papers)}")
    print(f"{'=' * 80}\n")
    
    # Guardar resultados
    output_file = "c:/Users/Felipe/Desktop/IA_papers/papers_focused_search.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent=2, ensure_ascii=False)
    
    print(f"📁 Resultados guardados en: {output_file}")
    
    # Mostrar top 10
    print(f"\n🏆 Top 10 papers más relevantes:\n")
    for i, paper in enumerate(papers[:10], 1):
        print(f"{i}. {paper['title']}")
        print(f"   Año: {paper['year']} | Relevancia: {paper['relevance_score']:.1f} ⭐")
        print(f"   {paper['url']}\n")
    
    # Generar estadísticas
    print(f"\n📊 Estadísticas:")
    papers_by_year = {}
    for p in papers:
        year = p['year']
        papers_by_year[year] = papers_by_year.get(year, 0) + 1
    
    for year in sorted(papers_by_year.keys(), reverse=True):
        print(f"   {year}: {papers_by_year[year]} papers")


if __name__ == "__main__":
    main()
