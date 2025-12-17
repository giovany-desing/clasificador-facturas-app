import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Portfolio • Invoice Processing Pipeline",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS ESTILO APPLE PREMIUM CON TEXTO GRIS CLARO ---
st.markdown("""
    <style>
    /* Imports de SF Pro Display (Apple's font) o similar */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Reset y base */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Variables estilo Apple */
    :root {
        --apple-blue: #0071e3;
        --apple-dark: #a1a1a6;
        --apple-light: #f5f5f7;
        --apple-gray: #a1a1a6;
        --apple-text: #a1a1a6;
        --glass-bg: rgba(255, 255, 255, 0.72);
        --glass-border: rgba(255, 255, 255, 0.18);
    }
    
    /* Fondo con efecto gradient sutil estilo Apple */
    .main {
        background: linear-gradient(180deg, #ffffff 0%, #f5f5f7 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        color: var(--apple-text);
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    
    /* Header principal estilo Apple - minimalista y elegante */
    .main-header {
        font-size: 4rem;
        font-weight: 700;
        letter-spacing: -0.05em;
        background: linear-gradient(135deg, #a1a1a6 0%, #86868b 50%, #a1a1a6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin: 3rem 0 1rem 0;
        padding: 0;
        line-height: 1.1;
        animation: fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Subtítulo con blur de fondo (glassmorphism) */
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        color: #a1a1a6;
        text-align: center;
        margin-bottom: 3rem;
        letter-spacing: -0.01em;
        animation: fadeInUp 1.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Sub-headers minimalistas */
    .sub-header {
        font-size: 2.5rem;
        color: #a1a1a6;
        font-weight: 700;
        margin-top: 4rem;
        margin-bottom: 1.5rem;
        letter-spacing: -0.03em;
        position: relative;
        padding-bottom: 0;
        border: none;
    }
    
    /* Glassmorphism cards estilo iOS/macOS */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: saturate(180%) blur(20px);
        -webkit-backdrop-filter: saturate(180%) blur(20px);
        border-radius: 18px;
        border: 1px solid var(--glass-border);
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.12);
    }
    
    /* Tech badges estilo Apple - minimalistas */
    .tech-badge {
        background: rgba(0, 113, 227, 0.1);
        color: var(--apple-blue);
        padding: 6px 16px;
        border-radius: 980px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-right: 6px;
        margin-bottom: 6px;
        display: inline-block;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(0, 113, 227, 0.15);
        letter-spacing: 0.01em;
    }
    
    .tech-badge:hover {
        background: rgba(0, 113, 227, 0.15);
        transform: scale(1.05);
    }
    
    /* Highlight estilo Apple Pages */
    .highlight {
        background: linear-gradient(120deg, rgba(255, 204, 0, 0.3) 0%, rgba(255, 149, 0, 0.2) 100%);
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 600;
        color: #a1a1a6;
    }
    
    /* Sidebar con efecto glass */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.95) 0%, rgba(245, 245, 247, 0.95) 100%);
        backdrop-filter: blur(40px);
        -webkit-backdrop-filter: blur(40px);
        border-right: 1px solid rgba(0, 0, 0, 0.06);
    }
    
    [data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }
    
    /* Texto del sidebar */
    [data-testid="stSidebar"] * {
        color: #a1a1a6 !important;
    }
    
    /* Botones estilo Apple - minimalistas y elegantes */
    .stButton > button {
        background: var(--apple-blue);
        color: white;
        border: none;
        border-radius: 980px;
        padding: 12px 32px;
        font-weight: 500;
        font-size: 1rem;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        box-shadow: 0 4px 16px rgba(0, 113, 227, 0.3);
        letter-spacing: -0.01em;
    }
    
    .stButton > button:hover {
        background: #0077ed;
        transform: scale(1.02);
        box-shadow: 0 6px 24px rgba(0, 113, 227, 0.4);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Tabs estilo macOS - Más grandes y llamativos */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(0, 0, 0, 0.05);
        border-radius: 16px;
        padding: 8px;
        margin-bottom: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px;
        padding: 18px 32px;
        font-weight: 600;
        font-size: 1.1rem;
        color: #000000 !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        border: none;
        background: rgba(255, 255, 255, 0.5);
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.8);
        transform: translateY(-2px);
        color: #000000 !important;
    }
    
    .stTabs [data-baseweb="tab"] span {
        color: #000000 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0071e3 0%, #0051a3 100%);
        color: white !important;
        box-shadow: 0 4px 16px rgba(0, 113, 227, 0.3);
        font-weight: 700;
        font-size: 1.15rem;
    }
    
    .stTabs [aria-selected="true"]:hover {
        background: linear-gradient(135deg, #0077ed 0%, #005bb3 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 113, 227, 0.4);
    }
    
    /* Métricas estilo Apple Watch */
    .metric-card {
        background: linear-gradient(135deg, rgba(0, 113, 227, 0.05) 0%, rgba(0, 113, 227, 0.02) 100%);
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        border: 1px solid rgba(0, 0, 0, 0.06);
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 700;
        color: #a1a1a6;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: #a1a1a6;
        font-weight: 500;
        letter-spacing: 0.01em;
    }
    
    /* Info boxes estilo iOS */
    .stAlert {
        border-radius: 16px;
        border: none;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
    }
    
    /* Timeline minimalista */
    .timeline-item {
        border-left: 2px solid rgba(0, 113, 227, 0.3);
        padding-left: 2rem;
        margin-bottom: 2.5rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: var(--apple-blue);
        box-shadow: 0 0 0 4px rgba(0, 113, 227, 0.15);
    }
    
    .timeline-item h4 {
        font-weight: 600;
        color: #a1a1a6;
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
        letter-spacing: -0.01em;
    }
    
    .timeline-item p {
        color: #a1a1a6;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* Imagen con efecto Apple */
    .image-container {
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        background: white;
        padding: 20px;
    }
    
    .image-container:hover {
        transform: scale(1.01);
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.2);
    }
    
    /* Expanders estilo Apple */
    .streamlit-expanderHeader {
        font-weight: 500;
        color: #a1a1a6 !important;
        border-radius: 12px;
        background: rgba(0, 0, 0, 0.02);
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(0, 0, 0, 0.04);
    }
    
    /* Code blocks estilo Xcode */
    .stCodeBlock {
        border-radius: 12px;
        background: #1d1d1f !important;
    }
    
    code {
        font-family: 'SF Mono', Monaco, monospace;
        font-size: 0.9rem;
    }
    
    /* Spacing Apple-like */
    p {
        line-height: 1.6;
        color: #a1a1a6 !important;
        font-size: 1.05rem;
        margin-bottom: 1rem;
    }
    
    /* Strong text más visible */
    strong {
        color: #a1a1a6 !important;
        font-weight: 600;
    }
    
    /* Lists más legibles */
    ul, ol {
        color: #a1a1a6 !important;
    }
    
    li {
        color: #a1a1a6 !important;
        margin-bottom: 0.5rem;
    }
    
    /* Links estilo Apple */
    a {
        color: var(--apple-blue);
        text-decoration: none;
        transition: opacity 0.3s ease;
    }
    
    a:hover {
        opacity: 0.7;
    }
    
    /* Download button especial */
    .stDownloadButton > button {
        background: #86868b;
        color: white;
        border-radius: 980px;
        font-weight: 500;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .stDownloadButton > button:hover {
        background: #a1a1a6;
        transform: scale(1.02);
    }
    
    /* Métricas de Streamlit personalizadas */
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 700;
        color: #a1a1a6 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #a1a1a6 !important;
        font-weight: 500;
    }
    
    /* Tabs text más visible - Override para mayor tamaño */
    .stTabs [data-baseweb="tab"] {
        color: #000000 !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    .stTabs [data-baseweb="tab"] * {
        color: #000000 !important;
    }
    
    .stTabs [aria-selected="true"] {
        color: white !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
    }
    
    /* Divider sutil */
    hr {
        border: none;
        height: 1px;
        background: rgba(0, 0, 0, 0.06);
        margin: 3rem 0;
    }
    
    /* Success/Warning/Error boxes estilo iOS */
    .element-container div[data-testid="stAlert"] {
        border-radius: 14px;
        backdrop-filter: blur(20px);
    }
    
    .element-container div[data-testid="stAlert"] * {
        color: #a1a1a6 !important;
    }
    
    /* Caption refinado */
    .caption-text {
        font-size: 0.85rem;
        color: #a1a1a6 !important;
        font-weight: 400;
        letter-spacing: 0.01em;
    }
    
    /* Markdown headings más claros */
    h1, h2, h3, h4, h5, h6 {
        color: #a1a1a6 !important;
    }
    
    /* Info/Success/Warning boxes con mejor contraste */
    .stAlert p {
        color: #a1a1a6 !important;
    }
    
    /* Todos los elementos de texto */
    div[data-testid="stMarkdownContainer"] * {
        color: #a1a1a6 !important;
    }
    
    /* Labels y otros textos */
    label, span {
        color: #a1a1a6 !important;
    }
    
    /* Mejoras adicionales para textos y flujos */
    .flow-section {
        margin: 3rem 0;
        padding: 2rem;
        background: var(--glass-bg);
        backdrop-filter: saturate(180%) blur(20px);
        border-radius: 18px;
        border: 1px solid var(--glass-border);
    }
    
    .flow-step {
        padding: 1.5rem;
        margin: 1.5rem 0;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        border-left: 4px solid var(--apple-blue);
        transition: all 0.3s ease;
    }
    
    .flow-step:hover {
        transform: translateX(8px);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
    }
    
    .flow-step h4 {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1d1d1f;
        margin-bottom: 0.8rem;
    }
    
    .flow-step p {
        color: #1d1d1f;
        line-height: 1.7;
        font-size: 1.05rem;
    }
    
    /* Mejoras para listas */
    ul, ol {
        padding-left: 1.5rem;
    }
    
    li {
        margin-bottom: 0.8rem;
        line-height: 1.7;
    }
    
    /* Mejoras para código */
    .stCodeBlock {
        border-radius: 12px;
        padding: 1.5rem;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* Espaciado mejorado entre secciones */
    .section-divider {
        margin: 4rem 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(0,0,0,0.1), transparent);
        border: none;
    }
    
    /* Cards con mejor contraste */
    .glass-card h2,
    .glass-card h3 {
        color: #1d1d1f !important;
    }
    
    .glass-card h4 {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    .glass-card p,
    .glass-card li {
        color: #1d1d1f !important;
    }
    
    /* Mejoras para tabs - Tamaño aumentado */
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #000000 !important;
    }
    
    .stTabs [data-baseweb="tab"] p,
    .stTabs [data-baseweb="tab"] span,
    .stTabs [data-baseweb="tab"] div {
        color: #000000 !important;
    }
    
    .stTabs [aria-selected="true"] {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: white !important;
    }
    
    .stTabs [aria-selected="true"] p,
    .stTabs [aria-selected="true"] span,
    .stTabs [aria-selected="true"] div {
        color: white !important;
    }
    
    /* Mejoras para markdown headings */
    h1, h2, h3, h4, h5, h6 {
        color: #1d1d1f !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)


# =========================================
# SIDEBAR ESTILO APPLE
# =========================================
with st.sidebar:
    st.markdown("### 🛠️ STACK TECNOLÓGICO UTILIZADO")
    st.markdown("---")
    
    # Backend & API
    with st.expander("⚡ Backend & API", expanded=False):
        st.markdown("""
        - **FastAPI 0.104+** - Web framework
        - **Pydantic 2.x** - Validación y settings
        - **Uvicorn** - ASGI server
        - **SQLAlchemy 2.x** - ORM
        - **PyMySQL** - MySQL driver
        """)
    
    # Machine Learning
    with st.expander("🤖 Machine Learning", expanded=False):
        st.markdown("""
        - **TensorFlow 2.x** - Deep learning
        - **Keras** - API de alto nivel
        - **Scikit-learn** - Preprocesamiento
        - **NumPy** - Operaciones numéricas
        - **OpenCV (cv2)** - Procesamiento de imágenes
        """)
    
    # Computer Vision & OCR
    with st.expander("👁️ Computer Vision & OCR", expanded=False):
        st.markdown("""
        - **Tesseract OCR** - Extracción de texto
        - **pdf2image** - Conversión PDF → Imagen
        - **Pillow (PIL)** - Manipulación de imágenes
        - **Poppler** - Backend PDF
        """)
    
    # MLOps
    with st.expander("🔄 MLOps", expanded=False):
        st.markdown("""
        - **DVC 3.x** - Versionado de datos/modelos
        - **MLflow 2.x** - Experiment tracking
        - **Apache Airflow 2.8** - Orquestación de workflows
        """)
    
    # Data & Analytics
    with st.expander("📊 Data & Analytics", expanded=False):
        st.markdown("""
        - **Pandas** - Manipulación de datos
        - **SciPy** - Tests estadísticos (KS-test)
        - **Matplotlib** - Visualización
        """)
    
    # Storage & Cloud
    with st.expander("☁️ Storage & Cloud", expanded=False):
        st.markdown("""
        - **AWS S3** - Object storage
        - **AWS RDS MySQL 8.0** - Base de datos relacional
        - **Google Drive API** - Storage de archivos
        - **Google OAuth2** - Autenticación
        """)
    
    # Databases
    with st.expander("💾 Databases", expanded=False):
        st.markdown("""
        - **MySQL 8.0** - RDBMS (Local + RDS)
          - Local: Airflow/MLflow metadata
          - RDS: Datos de negocio
        """)
    
    # Containerization & Orchestration
    with st.expander("🐳 Containerization & Orchestration", expanded=False):
        st.markdown("""
        - **Docker 24.x** - Containerización
        - **Docker Compose 2.x** - Multi-container orchestration
        - **Alpine Linux** - Base images (producción)
        - **Debian Slim** - Base images (desarrollo)
        """)
    
    # CI/CD & Testing
    with st.expander("🚀 CI/CD & Testing", expanded=False):
        st.markdown("""
        - **GitHub Actions** - CI/CD pipeline
        - **Pytest 7.x** - Testing framework
        - **Coverage.py** - Code coverage
        """)
    
    # Utilities & Dev Tools
    with st.expander("🛠️ Utilities & Dev Tools", expanded=False):
        st.markdown("""
        - **Python 3.11** - Lenguaje principal
        - **Boto3** - AWS SDK
        - **Requests** - HTTP client
        - **python-dotenv** - Environment management
        - **subprocess** - Shell commands (DVC)
        """)
    
    # Monitoring & Logging
    with st.expander("📈 Monitoring & Logging", expanded=False):
        st.markdown("""
        - **Python logging** - Structured logging
        - **Airflow UI** - Workflow monitoring
        - **MLflow UI** - Experiment tracking UI
        - (Pendiente: Prometheus/Grafana)
        """)
    
    # Version Control
    with st.expander("📝 Version Control", expanded=False):
        st.markdown("""
        - **Git** - Source control
        - **DVC** - Data/model versioning
        - **GitHub** - Repository hosting
        """)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="margin-top: 1.5rem; font-size: 0.9rem;">
        <p style="font-weight: 600; color: #a1a1a6; margin-bottom: 0.5rem;">Conectemos</p>
        <p style="margin: 0.3rem 0;"><a href="#">→ Mi perfil de LinkedIn</a></p>
        <p style="margin: 0.3rem 0;"><a href="#">→ Mi perfil de GitHub</a></p>
        <p style="margin: 0.3rem 0;"><a href="#">→ Mi Portafolio</a></p>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# HERO SECTION ESTILO APPLE
# =========================================
st.markdown("""
<div style="text-align: center; margin: 4rem 0 3rem 0;">
    <h1 style="font-size: 3.5rem; font-weight: 700; color: #1d1d1f; letter-spacing: -0.02em; margin-bottom: 1.5rem; line-height: 1.1;">
        Sistema ETL de Facturas con Machine Learning
    </h1>
    </div>
""", unsafe_allow_html=True)

# Sección: ¿Qué es este proyecto?
st.markdown("""
<div style="max-width: 900px; margin: 0.3rem auto; text-align: left; line-height: 1.4;">
    <h2 style="font-size: 1.8rem; font-weight: 700; color: #0051a3; margin-top: 0; margin-bottom: 0.2rem;">
        ¿Qué es este proyecto?
    </h2>
    <p style="font-size: 1.1rem; color: #1d1d1f; font-weight: 400; margin-bottom: 0.4rem; line-height: 1.4;">
        Este proyecto es un sistema ETL empresarial que automatiza end-to-end el procesamiento y clasificación de facturas textiles mediante inteligencia artificial. El flujo comienza extrayendo facturas en PDF desde AWS S3, las procesa con un modelo CNN custom que clasifica cada factura como correctiva o preventiva con más del 90% de precisión, aplica OCR (Tesseract) para extraer información estructurada (números de orden, productos, cantidades, totales), y almacena los datos en MySQL (AWS RDS) según su clasificación. Las facturas procesadas se suben automáticamente a Google Drive mediante su API OAuth 2.0 en tres ubicaciones: carpeta "histórico" (todas), "correctivos" (clase 0), y "preventivos" (clase 1), finalizando con la limpieza automática de archivos temporales y eliminación de facturas ya procesadas del bucket S3.<br/><br/>Todo el pipeline está orquestado con Apache Airflow en Amazon MWAA ejecutándose cada hora, gestionando además pipelines de entrenamiento del modelo bajo demanda, detección semanal de data drift mediante tests estadísticos que disparan reentrenamiento automático, y tracking de experimentos con MLflow y versionado de modelos con DVC. La arquitectura completa está desplegada sobre servicios serverless de AWS (ECS Fargate, ALB, CloudWatch, Secrets Manager) con auto-scaling automático de 2 a 10 tasks según demanda, y toda la infraestructura de 75+ recursos está definida mediante Infrastructure as Code con Terraform (2,300+ líneas), permitiendo deployment reproducible, versionado en Git, y CI/CD completo con GitHub Actions que ejecuta tests, valida calidad del modelo (F1 > 0.85), construye imágenes Docker, las publica en ECR, y despliega actualizaciones sin downtime.
    </p>
</div>
""", unsafe_allow_html=True)

# Flujo de ETL resumido
st.markdown("""
<div style="max-width: 1200px; margin: 2rem auto;">
    <h3 style="font-size: 1.5rem; font-weight: 700; color: #0051a3; margin-bottom: 1.5rem; text-align: center;">
        Flujo de ETL resumido
    </h3>
</div>
""", unsafe_allow_html=True)

# Pipeline ETL de Facturas - Flujo horizontal compacto
st.markdown("""
<div style="max-width: 1400px; margin: 0 auto 2rem auto; padding: 1rem; background: #f8f9fa; border-radius: 12px; overflow-x: auto;">
    <div style="display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 0.4rem; flex-wrap: nowrap; min-width: 900px;">
        <div style="background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid #0051a3; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 130px; flex-shrink: 0;">
            <div style="font-size: 1.2rem; margin-bottom: 0.15rem;">☁️</div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #0051a3; margin-bottom: 0.15rem;">S3 Bucket</div>
            <div style="font-size: 0.7rem; color: #666666;">(mes en curso)</div>
        </div>
        <div style="font-size: 1.2rem; color: #0051a3; font-weight: bold; flex-shrink: 0;">→</div>
        <div style="background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid #5856d6; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 160px; flex-shrink: 0;">
            <div style="font-size: 1.2rem; margin-bottom: 0.15rem;">🎯</div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #5856d6; margin-bottom: 0.15rem;">Clasificación ML</div>
            <div style="font-size: 0.7rem; color: #666666;">(CNN: correctiva vs preventiva)</div>
        </div>
        <div style="font-size: 1.2rem; color: #5856d6; font-weight: bold; flex-shrink: 0;">→</div>
        <div style="background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid #34c759; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 160px; flex-shrink: 0;">
            <div style="font-size: 1.2rem; margin-bottom: 0.15rem;">🔍</div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #34c759; margin-bottom: 0.15rem;">Extracción OCR</div>
            <div style="font-size: 0.7rem; color: #666666;">(Tesseract: orden, fecha, productos, $)</div>
        </div>
        <div style="font-size: 1.2rem; color: #34c759; font-weight: bold; flex-shrink: 0;">→</div>
        <div style="background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid #ff9500; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 120px; flex-shrink: 0;">
            <div style="font-size: 1.2rem; margin-bottom: 0.15rem;">💾</div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #ff9500; margin-bottom: 0.15rem;">MySQL</div>
            <div style="font-size: 0.7rem; color: #666666;">(AWS RDS)</div>
        </div>
        <div style="font-size: 1.2rem; color: #ff9500; font-weight: bold; flex-shrink: 0;">→</div>
        <div style="background: white; padding: 0.6rem 0.8rem; border-radius: 6px; border: 2px solid #ff2d55; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 160px; flex-shrink: 0;">
            <div style="font-size: 1.2rem; margin-bottom: 0.15rem;">📤</div>
            <div style="font-size: 0.85rem; font-weight: 700; color: #ff2d55; margin-bottom: 0.15rem;">Google Drive</div>
            <div style="font-size: 0.7rem; color: #666666;">(histórico, correctivos, preventivos)</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 4rem 0 3rem 0;">
</div>
""", unsafe_allow_html=True)

st.markdown("---")

##################

    

# Card: Problema de Negocio
st.markdown("""
<div class="glass-card" style="margin-bottom: 2rem;">
    <h2 style="font-size: 1.8rem; font-weight: 600; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.01em;">
        🔴 Problema de Negocio
    </h2>
    <p style="font-size: 1.1rem; color: #1d1d1f; line-height: 1.8;">
        Las empresas textiles procesan cientos de facturas diarias que deben clasificarse manualmente en dos categorías críticas: correctivas (ajustes/correcciones de pedidos) y preventivas (operaciones estándar). Este proceso manual requiere que personal administrativo revise cada factura, identifique características específicas, clasifique según criterios complejos, y extraiga datos manualmente para ingresarlos en sistemas. El resultado es un proceso que toma 2-3 minutos por factura, con tasa de error del ~15%, que no escala cuando aumenta el volumen, genera cuellos de botella durante horas laborales, y produce inconsistencias por diferentes interpretaciones del personal. Además, la información queda dispersa entre sistemas y la extracción de insights de negocio es lenta y costosa.
    </p>
</div>
""", unsafe_allow_html=True)

# Card: Solución Implementada
st.markdown("""
<div class="glass-card" style="margin-bottom: 2rem;">
    <h2 style="font-size: 1.8rem; font-weight: 600; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.01em;">
        ✅ Solución Implementada
    </h2>
    <p style="font-size: 1.1rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 1.5rem;">
        Sistema ETL automatizado con inteligencia artificial que procesa el ciclo completo: descarga automática de facturas desde S3, clasificación mediante modelo CNN con >90% de precisión (superando el ~85% humano), extracción de datos estructurados con OCR (orden de compra, productos, cantidades, totales), almacenamiento en base de datos relacional, y distribución automática a Google Drive en carpetas organizadas por tipo. El sistema opera 24/7 orquestado por Airflow, ejecutándose cada hora sin intervención humana, con capacidad de escalar automáticamente de 10 a 10,000 facturas mediante arquitectura serverless en AWS, y se auto-optimiza mediante detección semanal de drift que dispara reentrenamiento del modelo cuando los patrones de datos cambian.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card" style="margin-bottom: 2rem;">
    <hr style="border: none; height: 1px; background: rgba(0, 0, 0, 0.1); margin: 2rem 0;" />
    <h3 style="font-size: 1.5rem; font-weight: 600; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.01em;">
        💎 Valor para la Empresa
    </h3>
    <div style="margin-bottom: 2rem;">
        <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            Eficiencia Operacional:
        </h4>
        <p style="font-size: 1.05rem; color: #000000 !important; font-weight: 400; line-height: 1.8; margin: 0.5rem 0;">
            * 95% reducción en tiempo de procesamiento (de horas a segundos por factura)<br/>
            * Eliminación de cuellos de botella con procesamiento continuo 24/7/365<br/>
            * Capacidad ilimitada de escalar sin contratar personal adicional<br/>
            * Reducción de errores del 15% (humano) a &lt;10% (automatizado)
        </p>
    </div>
    <div style="margin-bottom: 2rem;">
        <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            Impacto Financiero:
        </h4>
        <p style="font-size: 1.05rem; color: #000000 !important; font-weight: 400; line-height: 1.8; margin: 0.5rem 0;">
            * Reducción de costos operacionales al eliminar horas-hombre de trabajo manual repetitivo<br/>
            * Liberación de talento humano para tareas de mayor valor (análisis, estrategia)<br/>
            * Faster time-to-insight con datos estructurados disponibles en tiempo real<br/>
            * Modelo pay-per-use que solo cobra por facturas procesadas (no costos fijos)
        </p>
    </div>
    <div style="margin-bottom: 0;">
        <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            Ventajas Competitivas:
        </h4>
        <p style="font-size: 1.05rem; color: #000000 !important; font-weight: 400; line-height: 1.8; margin: 0.5rem 0;">
            * Datos estructurados para análisis de negocio y toma de decisiones<br/>
            * Mejora continua automática del modelo sin intervención manual<br/>
            * Trazabilidad completa de cada factura procesada con logs y métricas<br/>
            * Escalabilidad probada para manejar crecimiento del negocio sin re-arquitectura
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# Tres columnas para las disciplinas

tab1, tab2, tab3, tab4 = st.tabs([
    "🏗️ Arquitectura & Stack Tecnológico",
    "</> Ver Software",
    "🧠 Pipeline de entrenamiento",
    "🦾 Orquestación con Apache Airflow",  
])

with tab1:
    # Mostrar imagen de arquitectura
    st.image("image_arquitecture.png", use_container_width=True)
    
    # Título Stack Tecnológico
    st.markdown("""
    <div style="margin: 2rem 0; text-align: center;">
        <h2 style="font-size: 2.5rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1rem; letter-spacing: -0.02em;">
            Stack Tecnológico
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Contenido Stack Tecnológico
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Python 3.11
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Lenguaje líder en Data Science, ML, y backend moderno. Ecosistema masivo de librerías (TensorFlow, pandas, scikit-learn, FastAPI) sin equivalente en otros lenguajes. Python 3.11 ofrece 10-60% mejora de performance vs 3.10 gracias a optimizaciones del bytecode compiler y faster startup. Type hints nativos mejoran maintainability en proyectos grandes.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Lenguaje base para TODO el proyecto: API FastAPI, scripts ETL, training pipelines, DAGs de Airflow, utilidades de procesamiento. Permite prototipado rápido y transition seamless entre data science (notebooks) y production code (módulos). Uso de virtual environments (venv) para aislamiento de dependencias.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # FastAPI 0.104
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            FastAPI 0.104
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Framework web async moderno construido sobre Starlette y Pydantic. Performance comparable a Node.js y Go gracias a async/await nativo. Auto-generación de documentación OpenAPI/Swagger sin código adicional. Validación automática de requests via Pydantic schemas reduce bugs. Comparado con Flask (sync) o Django (monolítico), FastAPI es ideal para microservicios de alta concurrencia.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Backbone de la API REST que expone endpoints: POST /predict (clasificación de facturas), GET /metrics (estadísticas), POST /upload (carga manual), /health y /ready (health checks ALB). Maneja autenticación JWT, rate limiting (100 req/min), CORS para frontend, y serialización JSON automática. Uvicorn ASGI server con 4 workers procesa ~500 requests/sec.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cloud & Infraestructura AWS
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Cloud & Infraestructura AWS
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Terraform 1.6+
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Terraform 1.6+
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Herramienta IaC (Infrastructure as Code) líder que permite definir infraestructura como código declarativo. Multi-cloud por diseño (vs CloudFormation solo AWS). State management permite detectar drift entre código y realidad. Plan/apply workflow previene cambios destructivos accidentales. Módulos reutilizables y outputs facilitan composición.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Define y aprovisiona 75+ recursos AWS en 2,317 líneas de código HCL: VPC, subnets, security groups, ECS cluster, task definitions, ALB + target groups, RDS instance, S3 buckets con policies, MWAA environment, IAM roles/policies, CloudWatch alarms. Organizado en módulos: networking/, compute/, storage/, security/. Comandos: terraform plan, apply, destroy.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    # Título y botón de GitHub
    col_title, col_btn = st.columns([3, 1])
    
    with col_title:
        st.markdown("""
        <div style="margin: 2rem 0 1rem 0;">
            <h2 style="font-size: 2.5rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem; letter-spacing: -0.02em;">
                📁 Estructura del Proyecto
            </h2>
            <p style="font-size: 1.1rem; color: #333333 !important; margin: 0;">
                Organización completa del repositorio y arquitectura del código
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_btn:
        st.markdown("""
        <div style="margin: 2rem 0 1rem 0; text-align: right;">
            <a href="https://github.com/giovany-desing/etl_facturas_textil" target="_blank" style="text-decoration: none;">
                <button style="background: linear-gradient(135deg, #24292e 0%, #1a1e22 100%); color: white; border: none; padding: 0.8rem 2rem; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: inline-flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.2rem;">🐙</span>
                    <span>Ver Codigo en GitHub</span>
                    <span style="font-size: 0.9rem;">↗</span>
                </button>
            </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Estructura del proyecto usando st.code para mejor renderizado
    st.markdown("""
    <div style="margin: 2rem 0;">
        <h3 style="font-size: 1.5rem; font-weight: 600; color: #000000 !important; margin-bottom: 1rem;">
            📦 Estructura de Directorios
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
etl_facturas_textil/
  │
  ├── 📄 .env                                    # Configuración: Variables de entorno (AWS, MySQL, credenciales)
  ├── 📄 .env.example                            # Template: Ejemplo de variables para configuración inicial
  ├── 📄 .gitignore                              # Git: Archivos/carpetas excluidos del versionado
  ├── 📄 .dockerignore                           # Docker: Archivos excluidos al construir imágenes
  ├── 📄 requirements.txt                        # Dependencias: Lista de paquetes Python del proyecto
  ├── 📄 credentials.json                        # OAuth: Credenciales de Google Drive API
  ├── 📄 token.json                              # OAuth: Token de acceso Google Drive (auto-renovado)
  │
  ├── 📁 .git/                                   # Git: Historial de versiones del código fuente
  │
  ├── 📁 .github/                                # CI/CD: Workflows de automatización
  │   ├── workflows/
  │   │   ├── 📄 tests.yml                      # CI/CD: Ejecuta pytest en cada push/PR
  │   │   └── 📄 ci-validation.yml              # CI/CD: Valida métricas de modelos (gate de calidad)
  │   └── 📄 README.md                           # Docs: Documentación de workflows CI/CD
  │
  ├── 📁 .dvc/                                   # DVC: Sistema de versionado de datos/modelos
  │   ├── 📄 config                             # DVC: Configuración de remote S3 storage
  │   ├── 📄 .gitignore                         # DVC: Ignora cache y archivos temporales
  │   ├── 📄 last_push_hash.txt                 # DVC: Tracking del último push exitoso
  │   ├── 📁 cache/                             # DVC: Cache local de archivos grandes (modelos, datos)
  │   │   └── files/md5/                        # DVC: Content-addressable storage por hash MD5
  │   │       ├── 3d/6e089549...                # DVC: Modelo modelo_facturas_final.h5 (255 MB)
  │   │       ├── 85/8d3c8a2d...dir             # DVC: Metadata de invoices_train/ (319 PDFs)
  │   │       └── 41/cb2a0062...dir             # DVC: Metadata de invoices_test/ (40 PDFs)
  │   └── 📁 tmp/                               # DVC: Archivos temporales de operaciones
  │
  ├── 📁 app/                                    # Core: Código fuente principal de la aplicación
  │   │
  │   ├── 📄 __init__.py                        # Python: Marca carpeta como paquete Python
  │   ├── 📄 main.py                            # API: FastAPI - Endpoints REST (procesar_facturas, train_model)
  │   ├── 📄 config.py                          # Config: Pydantic Settings - Configuración centralizada
  │   ├── 📄 utils.py                           # Utils: Logger configurado y funciones auxiliares
  │   │
  │   ├── 📄 model.py                           # ML: Entrenamiento CNN - Arquitectura, callbacks, métricas
  │   ├── 📄 predict.py                         # ML: Inferencia - Clasificación de facturas con modelo cargado
  │   ├── 📄 preprocessing.py                   # ML: Preprocesamiento - Load imágenes, resize, normalización
  │   ├── 📄 drift_analyzer.py                  # MLOps: Detección de drift - KS-test estadístico
  │   │
  │   ├── 📄 ocr.py                             # ETL: Extracción OCR - Tesseract + Regex parsing
  │   ├── 📄 database.py                        # ETL: Capa de BD - SQLAlchemy ORM, modelos, funciones CRUD
  │   ├── 📄 drive.py                           # ETL: Google Drive - OAuth2, upload/download de facturas
  │   ├── 📄 s3_utils.py                        # ETL: AWS S3 - Boto3 para descarga/eliminación de archivos
  │   │
  │   └── 📁 tests/                             # Testing: (Si existiera subcarpeta en app/)
  │
  ├── 📁 airflow/                                # Orquestación: Apache Airflow workflows
  │   │
  │   ├── 📁 dags/                              # Airflow: Definición de DAGs (Directed Acyclic Graphs)
  │   │   ├── 📄 etl_dag.py                     # Airflow: ETL horario - Procesa facturas cada hora
  │   │   ├── 📄 train_dag.py                   # Airflow: Training pipeline - CI/CD de modelos ML
  │   │   └── 📄 drift_dag.py                   # Airflow: Drift detection semanal - Trigger reentrenamiento
  │   │
  │   ├── 📁 plugins/                           # Airflow: Plugins personalizados (si existieran)
  │   ├── 📁 logs/                              # Airflow: Logs de ejecución de DAGs
  │   └── 📄 airflow.cfg                        # Airflow: Configuración del servidor (si existe)
  │
  ├── 📁 docker/                                 # Infraestructura: Containerización
  │   │
  │   ├── 📄 Dockerfile                         # Docker: Imagen de la API FastAPI (Python 3.11 + deps)
  │   ├── 📄 docker-compose.airflow.yml         # Docker Compose: Orquestación 4 servicios (API, Airflow, MLflow, MySQL)
  │   ├── 📄 .dockerignore                      # Docker: Archivos excluidos de la imagen
  │   └── 📁 nginx/                             # Nginx: Reverse proxy y SSL (si existiera)
  │
  ├── 📁 data/                                   # Datos: Datasets de entrenamiento/test
  │   │
  │   ├── 📄 invoices_train.dvc                 # DVC: Puntero a 319 PDFs de entrenamiento en S3
  │   ├── 📄 invoices_test.dvc                  # DVC: Puntero a 40 PDFs de prueba en S3
  │   │
  │   ├── 📁 invoices_train/                    # Datos: 319 facturas para entrenamiento (versionado DVC)
  │   │   ├── 0/                                # Datos: Clase 0 (Preventivas)
  │   │   │   ├── factura001.pdf
  │   │   │   ├── factura002.pdf
  │   │   │   └── ...
  │   │   └── 1/                                # Datos: Clase 1 (Correctivas)
  │   │       ├── Invoicef0900.pdf
  │   │       └── ...
  │   │
  │   ├── 📁 invoices_test/                     # Datos: 40 facturas para testing (versionado DVC)
  │   │   ├── 0/
  │   │   └── 1/
  │   │
  │   ├── 📁 raw/                               # Datos: Datos crudos sin procesar (ignorado por Git)
  │   ├── 📁 processed/                         # Datos: Datos procesados intermedios (ignorado por Git)
  │   └── 📁 train_data/                        # Datos: Arrays NumPy preprocesados (ignorado por Git)
  │       ├── facturas_X_entrenamiento.npy      # Datos: Features de entrenamiento (generado por preprocessing.py)
  │       ├── facturas_y_entrenamiento.npy      # Datos: Labels de entrenamiento
  │       ├── facturas_X_prueba.npy             # Datos: Features de test
  │       ├── facturas_y_prueba.npy             # Datos: Labels de test
  │       └── facturas_mapeo_etiquetas.npy      # Datos: Mapeo de clases {'0': 0, '1': 1}
  │
  ├── 📁 modelos/                                # ML: Modelos entrenados y artefactos
  │   │
  │   ├── 📄 .gitignore                         # Git: Ignora archivos .h5 grandes (versionados con DVC)
  │   │
  │   ├── 📄 modelo_facturas_final.h5           # ML: Modelo CNN entrenado (255 MB, versionado DVC)
  │   ├── 📄 modelo_facturas_final.h5.dvc       # DVC: Puntero al modelo en S3 (versionado en Git)
  │   │
  │   ├── 📄 historial_entrenamiento.npy        # ML: Historial de métricas por época (versionado DVC)
  │   ├── 📄 historial_entrenamiento.npy.dvc    # DVC: Puntero al historial en S3
  │   │
  │   ├── 📄 mapeo_etiquetas.npy                # ML: Mapeo de clases (versionado DVC)
  │   ├── 📄 mapeo_etiquetas.npy.dvc            # DVC: Puntero al mapeo en S3
  │   │
  │   ├── 📄 baseline_caracteristicas.npy       # MLOps: Baseline para drift detection (features de referencia)
  │   │
  │   └── 📄 metricas_entrenamiento.png         # ML: Gráficas de accuracy, loss, precision, recall
  │
  ├── 📁 tests/                                  # Testing: Suite de pruebas automatizadas
  │   │
  │   ├── 📄 __init__.py                        # Python: Marca carpeta como paquete
  │   │
  │   ├── 📄 test_api.py                        # Testing: Pruebas de endpoints FastAPI
  │   ├── 📄 test_model.py                      # Testing: Pruebas del modelo ML (carga, inferencia)
  │   ├── 📄 test_preprocessing.py              # Testing: Pruebas de preprocesamiento de datos
  │   ├── 📄 test_ocr.py                        # Testing: Pruebas de extracción OCR
  │   ├── 📄 test_database.py                   # Testing: Pruebas de conexión y operaciones BD
  │   ├── 📄 test_mysql_connection.py           # Testing: Pruebas de conectividad MySQL RDS
  │   ├── 📄 test_ci_validation.py              # CI/CD: Validación de métricas del modelo (gate crítico)
  │   ├── 📄 test_api_stability.py              # Testing: Pruebas de estabilidad de la API
  │   │
  │   └── 📁 fixtures/                          # Testing: Datos de prueba (facturas dummy)
  │
  ├── 📁 logs/                                   # Logs: Archivos de logging del sistema (ignorado por Git)
  │   ├── app.log                               # Logs: Logs de la aplicación FastAPI
  │   ├── etl.log                               # Logs: Logs del pipeline ETL
  │   └── training.log                          # Logs: Logs del entrenamiento de modelos
  │
  ├── 📁 notebooks/                              # EDA: Jupyter notebooks para exploración (si existieran)
  │   ├── 01_exploratory_analysis.ipynb         # EDA: Análisis exploratorio de datos
  │   ├── 02_model_experiments.ipynb            # ML: Experimentos de arquitecturas de modelos
  │   └── 03_drift_analysis.ipynb               # MLOps: Análisis de drift detection
  │
  ├── 📁 scripts/                                # Scripts: Utilidades de línea de comandos (si existieran)
  │   ├── 📄 download_from_drive.py             # Script: Descarga masiva desde Google Drive
  │   ├── 📄 setup_database.py                  # Script: Inicialización de tablas MySQL
  │   └── 📄 generate_baseline.py               # Script: Genera baseline para drift detection
  │
  └── 📄 README.md                               # Docs: Documentación principal del proyecto
    """, language=None)
    
    st.markdown("---")

with tab3:
    # Título mejorado
    st.markdown("""
    <div style="margin: 2rem 0 3rem 0;">
        <h2 style="font-size: 2.5rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem; letter-spacing: -0.02em; text-align: center;">
            🧠 Pipeline de Entrenamiento Automatizado
        </h2>
        <p style="font-size: 1.2rem; color: #333333 !important; text-align: center; margin-top: 1rem;">
            Reentrenamiento inteligente con CI/CD y validación de calidad (F1 > 0.85)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Información del trigger
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.1) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #0071e3; margin-bottom: 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            ⚙️ TRIGGER - Inicio del Proceso
        </h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
            <div>
                <strong style="color: #0071e3 !important;">Manual:</strong>
                <span style="color: #000000 !important;">Admin ejecuta POST /train_model desde la API</span>
            </div>
            <div>
                <strong style="color: #0071e3 !important;">Automático:</strong>
                <span style="color: #000000 !important;">Drift Detection detecta degradación y activa reentrenamiento</span>
            </div>
        </div>
        <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.1);">
            <p style="margin: 0; color: #333333 !important; font-size: 0.95rem;">
                <strong>Stack:</strong> Apache Airflow (orquestación) • FastAPI (endpoint) • Python requests (comunicación)
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # FASE 0: Validación de requisitos previos
    with st.expander("📋 **FASE 0: Validación de Requisitos Previos** [10%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #34c759; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.1) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #34c759;">▰▰▰▱▱▱▱▱▱▱</span>
                    <span style="color: #000000 !important; font-weight: 600;">10%</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">✓ Verifica entrenamiento en curso</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">SQLAlchemy consulta estado en MySQL</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">✓ Valida Google Drive OAuth2</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">Google Drive API v3</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">✓ Confirma GPU/CPU disponible</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">psutil (recursos del sistema)</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">✓ Verifica espacio en disco</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">>5GB requerido</p>
                </div>
            </div>
            <div style="background: rgba(52, 199, 89, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Tiempo:</strong> 10 segundos | <strong>Output:</strong> Status check ✅
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 1: Descarga de datos desde Drive
    with st.expander("📥 **FASE 1: Descarga de Datos desde Google Drive** [20%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(255, 149, 0, 0.1) 0%, rgba(255, 149, 0, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #ff9500;">▰▰▰▰▰▱▱▱▱▱</span>
                    <span style="color: #000000 !important; font-weight: 600;">20%</span>
                </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem; background: rgba(255, 149, 0, 0.1); border-radius: 8px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📁</div>
                    <strong style="color: #000000 !important;">facturas/historico/preventivos/</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">200 PDFs</p>
                </div>
                <div style="font-size: 1.5rem; color: #ff9500;">+</div>
                <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem; background: rgba(255, 149, 0, 0.1); border-radius: 8px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📁</div>
                    <strong style="color: #000000 !important;">facturas/historico/correctivos/</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">119 PDFs</p>
                </div>
                <div style="font-size: 1.5rem; color: #ff9500;">→</div>
                <div style="flex: 1; min-width: 200px; text-align: center; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">💾</div>
                    <strong style="color: #000000 !important;">data/raw/invoices_train/</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">319 facturas</p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <p style="color: #000000 !important; margin: 0; font-size: 0.95rem;">
                    <strong>Stack:</strong> Google Drive API v3 • googleapiclient.discovery • OAuth2 • Boto3 (respaldo S3)
                </p>
            </div>
            <div style="background: rgba(255, 149, 0, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Tiempo:</strong> 2-3 minutos | <strong>Output:</strong> 319 facturas descargadas + validación MD5 checksum
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 2: Preprocesamiento de imágenes
    with st.expander("🔧 **FASE 2: Preprocesamiento de Imágenes** [40%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.1) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #5856d6;">▰▰▰▰▰▰▰▱▱▱</span>
                    <span style="color: #000000 !important; font-weight: 600;">40%</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">1. Conversión PDF → PNG</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">pdf2image (primera página)</p>
                </div>
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">2. Redimensionar a 224x224</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">Input CNN estándar</p>
                </div>
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">3. Normalización [0,255] → [0,1]</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">Valores de píxeles</p>
                </div>
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">4. Data Augmentation</strong>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">Rotación ±10°, Zoom 10%, Flip, Brightness</p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <p style="color: #000000 !important; margin: 0; font-size: 0.95rem;">
                    <strong>Stack:</strong> pdf2image • Pillow (PIL) • NumPy • TensorFlow ImageDataGenerator • OpenCV
                </p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.15) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 1rem; border-radius: 8px; border: 2px solid #34c759; text-align: center;">
                    <strong style="color: #000000 !important;">Train Set</strong>
                    <p style="font-size: 1.5rem; font-weight: 700; color: #34c759 !important; margin: 0.5rem 0 0 0;">255 imágenes</p>
                </div>
                <div style="background: linear-gradient(135deg, rgba(255, 45, 85, 0.15) 0%, rgba(255, 45, 85, 0.05) 100%); padding: 1rem; border-radius: 8px; border: 2px solid #ff2d55; text-align: center;">
                    <strong style="color: #000000 !important;">Validation Set</strong>
                    <p style="font-size: 1.5rem; font-weight: 700; color: #ff2d55 !important; margin: 0.5rem 0 0 0;">64 imágenes</p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center; margin-top: 1rem;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Tiempo:</strong> 5-7 minutos | <strong>Split:</strong> 80% train, 20% validation
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 3: Entrenamiento de CNN
    with st.expander("🤖 **FASE 3: Entrenamiento de CNN** [60%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #0071e3; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.1) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #0071e3;">▰▰▰▰▰▰▰▰▰▱</span>
                    <span style="color: #000000 !important; font-weight: 600;">60%</span>
                </div>
            </div>
            <div style="background: rgba(0, 113, 227, 0.05); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">Arquitectura CNN:</h4>
                <div style="font-family: monospace; background: white; padding: 1rem; border-radius: 6px; font-size: 0.9rem; line-height: 1.8; color: #000000 !important;">
                    Input (224x224x3)<br/>
                    ↓<br/>
                    Conv2D(32) + MaxPool → ReLU<br/>
                    Conv2D(64) + MaxPool → ReLU<br/>
                    Conv2D(128) + MaxPool → ReLU<br/>
                    ↓<br/>
                    Flatten<br/>
                    ↓<br/>
                    Dense(256) + Dropout(0.5)<br/>
                    Dense(128) + Dropout(0.3)<br/>
                    Dense(1) + Sigmoid [SALIDA]
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(0, 113, 227, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">Callbacks Inteligentes:</strong>
                    <ul style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>EarlyStopping (patience=10)</li>
                        <li>ReduceLROnPlateau</li>
                        <li>ModelCheckpoint (mejor modelo)</li>
                    </ul>
                </div>
                <div style="background: rgba(0, 113, 227, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">Hiperparámetros:</strong>
                    <ul style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>Optimizer: Adam (lr=0.001)</li>
                        <li>Loss: Binary Crossentropy</li>
                        <li>Batch size: 16</li>
                        <li>Max epochs: 50</li>
                    </ul>
                </div>
            </div>
            <div style="background: rgba(0, 113, 227, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Stack:</strong> TensorFlow 2.13 • Keras • CUDA (GPU) • NumPy | 
                    <strong>Tiempo:</strong> 15-25 minutos | 
                    <strong>Output:</strong> modelo_facturas_final.h5 (255MB) + historial_entrenamiento.npy
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 4: CI - Validación de calidad
    with st.expander("✅ **FASE 4: CI - Validación de Calidad** [75%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #34c759; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.1) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #34c759;">▰▰▰▰▰▰▰▰▰▰</span>
                    <span style="color: #000000 !important; font-weight: 600;">75%</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">1. Carga modelo entrenado</strong>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">2. Evalúa con test set (40 facturas)</strong>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">3. Calcula métricas:</strong>
                    <ul style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>Accuracy</li>
                        <li>Precision</li>
                        <li>Recall</li>
                        <li><strong>F1-Score ⭐ (principal)</strong></li>
                    </ul>
                </div>
                <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">4. Quality Gate:</strong>
                    <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-family: monospace; font-size: 0.85rem;">
                        if f1_score > 0.85:<br/>
                        &nbsp;&nbsp;&nbsp;&nbsp;APROBADO ✅<br/>
                        else:<br/>
                        &nbsp;&nbsp;&nbsp;&nbsp;RECHAZADO ❌
                    </div>
                </div>
            </div>
            <div style="background: rgba(52, 199, 89, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Stack:</strong> scikit-learn • TensorFlow • pytest | 
                    <strong>Tiempo:</strong> 2-3 minutos | 
                    <strong>Output:</strong> Reporte de métricas
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 5: CD - Despliegue con DVC
    with st.expander("🚢 **FASE 5: CD - Despliegue con DVC** [90%]", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(255, 149, 0, 0.1) 0%, rgba(255, 149, 0, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #ff9500;">▰▰▰▰▰▰▰▰▰▰</span>
                    <span style="color: #000000 !important; font-weight: 600;">90%</span>
                </div>
                <p style="color: #000000 !important; margin: 0; font-size: 0.9rem; font-weight: 600;">⚠️ Solo si pasó CI (F1 > 0.85)</p>
            </div>
            <div style="display: grid; grid-template-columns: 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">1. DVC Add:</strong>
                    <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-family: monospace; font-size: 0.85rem; color: #000000 !important;">
                        dvc add modelos/modelo_facturas_final.h5
                    </div>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">
                        • Genera modelo_facturas_final.h5.dvc (pointer)<br/>
                        • Calcula MD5 hash del modelo
                    </p>
                </div>
                <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">2. DVC Push:</strong>
                    <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-family: monospace; font-size: 0.85rem; color: #000000 !important;">
                        dvc push
                    </div>
                    <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0;">
                        • Sube modelo a S3 (versión inmutable)<br/>
                        • Usa content-addressable storage
                    </p>
                </div>
                <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">3. Git Commit:</strong>
                    <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-family: monospace; font-size: 0.85rem; color: #000000 !important;">
                        git add modelos/modelo_facturas_final.h5.dvc<br/>
                        git commit -m "model: v2.1.3 - f1=0.91 [PROMOTED]"
                    </div>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Stack:</strong> DVC • AWS S3 • Git • Boto3 | 
                    <strong>Tiempo:</strong> 3-5 minutos | 
                    <strong>Output:</strong> Modelo en producción
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # FASE 6: Tracking y notificaciones
    with st.expander("📊 **FASE 6: Tracking y Notificaciones** [100%] ✅", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.1) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; font-weight: 700; color: #5856d6;">▰▰▰▰▰▰▰▰▰▰</span>
                    <span style="color: #000000 !important; font-weight: 600;">100% ✅</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">1. Registro en MySQL</strong>
                    <ul style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>Timestamp de entrenamiento</li>
                        <li>Métricas (accuracy, F1, precision, recall)</li>
                        <li>Git commit hash</li>
                        <li>DVC MD5 hash</li>
                        <li>Estado: PROMOTED o REJECTED</li>
                    </ul>
                </div>
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">2. MLflow Tracking</strong>
                    <ul style="font-size: 0.85rem; color: #666666 !important; margin: 0.5rem 0 0 0; padding-left: 1.5rem;">
                        <li>Registra experimento</li>
                        <li>Logs de hiperparámetros</li>
                        <li>Artifacts (gráficas, confusion matrix)</li>
                    </ul>
                </div>
                <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                    <strong style="color: #000000 !important;">3. Slack Notification</strong>
                    <div style="background: rgba(52, 199, 89, 0.1); padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-size: 0.85rem;">
                        <strong>✅ PROMOTED:</strong><br/>
                        🎉 NUEVO MODELO EN PRODUCCIÓN<br/>
                        F1: 0.91 | Accuracy: 0.93<br/>
                        Versión: v2.1.3
                    </div>
                    <div style="background: rgba(255, 45, 85, 0.1); padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem; font-size: 0.85rem;">
                        <strong>❌ REJECTED:</strong><br/>
                        ⚠️ MODELO NO PROMOCIONADO<br/>
                        F1: 0.82 (< 0.85 requerido)
                    </div>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.1); padding: 0.8rem; border-radius: 6px; text-align: center;">
                <p style="margin: 0; color: #000000 !important; font-size: 0.9rem;">
                    <strong>Stack:</strong> SQLAlchemy • MySQL RDS • MLflow • Slack Webhooks • Requests | 
                    <strong>Tiempo:</strong> 30 segundos | 
                    <strong>Output:</strong> Auditoría completa registrada
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Resumen final
    st.markdown("---")
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.15) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 2rem; border-radius: 12px; border-left: 5px solid #34c759; margin-top: 2rem;">
        <h3 style="font-size: 1.5rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            🎯 Resumen del Pipeline
        </h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
            <div>
                <strong style="color: #000000 !important;">⏱️ Tiempo total:</strong>
                <span style="color: #333333 !important;">25-40 minutos</span>
            </div>
            <div>
                <strong style="color: #000000 !important;">👤 Intervención humana:</strong>
                <span style="color: #34c759 !important; font-weight: 600;">0% (completamente automatizado)</span>
            </div>
            <div>
                <strong style="color: #000000 !important;">📊 Modelo actual en producción:</strong>
                <span style="color: #333333 !important;">F1: 0.91 | Accuracy: 0.93 | Versión: v2.1.3</span>
            </div>
            <div>
                <strong style="color: #000000 !important;">🔄 Frecuencia:</strong>
                <span style="color: #333333 !important;">1 reentrenamiento cada 2-3 semanas</span>
            </div>
        </div>
        <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
            <p style="margin: 0; color: #000000 !important; font-size: 0.95rem;">
                <strong>🏆 Diferenciador competitivo:</strong> Este pipeline implementa MLOps nivel Senior con Continuous Training (CT), Continuous Validation (CV), Model Registry con DVC, Drift Detection automatizado, Quality Gates (F1 > 0.85), Reproducibilidad total, Observabilidad con MLflow y Alertas en tiempo real.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    # Título mejorado
    st.markdown("""
    <div style="margin: 2rem 0 3rem 0;">
        <h2 style="font-size: 2.5rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem; letter-spacing: -0.02em; text-align: center;">
            🎼 Orquestación Completa con Apache Airflow
        </h2>
        <p style="font-size: 1.2rem; color: #333333 !important; text-align: center; margin-top: 1rem;">
            Tres workflows coordinados que mantienen el sistema funcionando automáticamente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Explicación para reclutadores
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.1) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 2rem; border-radius: 12px; border-left: 5px solid #0071e3; margin: 2rem 0;">
        <h3 style="font-size: 1.4rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            🎯 ¿Qué es Apache Airflow?
        </h3>
        <p style="font-size: 1.1rem; color: #000000 !important; line-height: 1.8; margin-bottom: 1rem;">
            <strong>Apache Airflow</strong> es como un "director de orquesta" que coordina múltiples tareas automáticamente. 
            En este proyecto, gestiona <strong>3 workflows diferentes</strong> que trabajan juntos para mantener el sistema funcionando sin supervisión humana.
        </p>
        <div style="background: white; padding: 1.5rem; border-radius: 8px; margin-top: 1rem;">
            <p style="margin: 0; color: #333333 !important; font-size: 1rem;">
                <strong>💡 Analogía:</strong> Imagina que Airflow es un gerente que tiene 3 empleados (DAGs) trabajando en horarios diferentes, 
                cada uno con tareas específicas, pero todos coordinados para mantener el sistema funcionando perfectamente.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Vista general de los 3 DAGs
    st.markdown("""
    <div style="margin: 3rem 0 2rem 0;">
        <h3 style="font-size: 2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
            📊 Los 3 Workflows (DAGs)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Cards de los 3 DAGs
    col_dag1, col_dag2, col_dag3 = st.columns(3, gap="large")
    
    with col_dag1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.15) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 2rem; border-radius: 14px; border-top: 5px solid #0071e3; box-shadow: 0 4px 16px rgba(0,0,0,0.1); text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📥</div>
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                DAG 1: ETL Pipeline
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin-bottom: 1rem;">
                <strong>Horario:</strong> Cada hora<br/>
                <strong>Objetivo:</strong> Procesar facturas nuevas
            </p>
            <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 1rem;">
                <p style="margin: 0; font-size: 0.9rem; color: #000000 !important; font-weight: 600;">
                    ⏰ 0 * * * *
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_dag2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255, 149, 0, 0.15) 0%, rgba(255, 149, 0, 0.05) 100%); padding: 2rem; border-radius: 14px; border-top: 5px solid #ff9500; box-shadow: 0 4px 16px rgba(0,0,0,0.1); text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔍</div>
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                DAG 2: Drift Detection
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin-bottom: 1rem;">
                <strong>Horario:</strong> Domingos 3 AM<br/>
                <strong>Objetivo:</strong> Detectar cambios en datos
            </p>
            <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 1rem;">
                <p style="margin: 0; font-size: 0.9rem; color: #000000 !important; font-weight: 600;">
                    ⏰ 0 3 * * 0
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_dag3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.15) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 2rem; border-radius: 14px; border-top: 5px solid #5856d6; box-shadow: 0 4px 16px rgba(0,0,0,0.1); text-align: center; height: 100%;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🤖</div>
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                DAG 3: Training Pipeline
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin-bottom: 1rem;">
                <strong>Horario:</strong> On-Demand<br/>
                <strong>Objetivo:</strong> Reentrenar modelo
            </p>
            <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 1rem;">
                <p style="margin: 0; font-size: 0.9rem; color: #000000 !important; font-weight: 600;">
                    🖐️ Manual o Trigger
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # DAG 1: ETL Pipeline - Detalle completo
    with st.expander("📥 **DAG 1: ETL PIPELINE - Procesamiento de Facturas (Cada Hora)**", expanded=True):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.1) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #0071e3; margin-bottom: 1.5rem;">
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                📋 Información del DAG
            </h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div>
                    <strong style="color: #0071e3 !important;">Nombre:</strong>
                    <span style="color: #000000 !important;">process_invoices_etl</span>
                </div>
                <div>
                    <strong style="color: #0071e3 !important;">Horario:</strong>
                    <span style="color: #000000 !important;">0 * * * * (Cada hora)</span>
                </div>
                <div style="grid-column: 1 / -1;">
                    <strong style="color: #0071e3 !important;">Objetivo:</strong>
                    <span style="color: #000000 !important;">Procesar facturas nuevas automáticamente sin intervención humana</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Tarea 1 del DAG 1
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #0071e3; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🔍</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T1: Verificar Estado Inactivo
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: HttpSensor | Polling: Cada 30s | Timeout: 10 min
                    </p>
                </div>
            </div>
            <div style="background: rgba(0, 113, 227, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin: 0;">
                    Espera hasta que la API esté libre (estado = "inactivo"). Consulta <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">GET api:8000/procesar_facturas/status</code> cada 30 segundos.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Flecha
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #0071e3;">⬇️</div>
        """, unsafe_allow_html=True)
        
        # Tarea 2 del DAG 1
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #34c759; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🚀</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T2: Activar ETL
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: SimpleHttpOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(52, 199, 89, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin: 0;">
                    Dispara el procesamiento enviando <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">POST api:8000/procesar_facturas</code>. 
                    El sistema responde inmediatamente con <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">{"estado": "en_cola"}</code> y comienza a procesar en segundo plano.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Procesamiento en FastAPI
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.1) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #5856d6; margin: 1.5rem 0; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
            <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
                FastAPI ejecuta el procesamiento en segundo plano
            </h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin-top: 1rem;">
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    📥 Descarga S3
                </div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    🤖 Clasificación ML
                </div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    📝 Extracción OCR
                </div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    💾 Carga MySQL
                </div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    ☁️ Sube Drive
                </div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">
                    🗑️ Limpieza
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Flecha
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #5856d6;">⬇️</div>
        """, unsafe_allow_html=True)
        
        # Tarea 3 del DAG 1
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">📊</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T3: Monitorear ETL
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: HttpSensor | Polling: Cada 60s | Timeout: 1 hora
                    </p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin-bottom: 0.5rem;">
                    Monitorea el progreso consultando el estado cada minuto hasta que sea "completado" o "error".
                </p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.85rem;">
                    <div style="color: #333333 !important;">• descarga_s3 → 30%</div>
                    <div style="color: #333333 !important;">• clasificacion_ml → 60%</div>
                    <div style="color: #333333 !important;">• procesamiento_ocr → 80%</div>
                    <div style="color: #333333 !important;">• carga_base_datos → 90%</div>
                    <div style="color: #34c759 !important; font-weight: 600;">• completado → 100% ✅</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Resultado DAG 1
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.15) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #34c759; margin-top: 1.5rem; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">✅</div>
            <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                DAG 1 Completado
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin: 0;">
                Airflow resetea el estado y espera la próxima ejecución (en 1 hora)
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # DAG 2: Drift Detection
    with st.expander("🔍 **DAG 2: DRIFT DETECTION - Detección de Cambios en Datos (Semanal)**", expanded=False):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(255, 149, 0, 0.1) 0%, rgba(255, 149, 0, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #ff9500; margin-bottom: 1.5rem;">
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                📋 Información del DAG
            </h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div>
                    <strong style="color: #ff9500 !important;">Nombre:</strong>
                    <span style="color: #000000 !important;">detect_data_drift</span>
                </div>
                <div>
                    <strong style="color: #ff9500 !important;">Horario:</strong>
                    <span style="color: #000000 !important;">0 3 * * 0 (Domingos 3 AM)</span>
                </div>
                <div style="grid-column: 1 / -1;">
                    <strong style="color: #ff9500 !important;">Objetivo:</strong>
                    <span style="color: #000000 !important;">Detectar cambios en la distribución de datos y activar reentrenamiento si es necesario</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tareas del DAG 2
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">📊</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T1: Preparar Datos
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: PythonOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin: 0;">
                    Descarga facturas recientes de Google Drive (preventivos/ y correctivos/) y las guarda en <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">/opt/airflow/drift_data/</code>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #ff9500;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🔬</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T2: Detectar Drift
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: PythonOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin-bottom: 0.5rem;">
                    Realiza análisis estadístico usando <strong>Kolmogorov-Smirnov test</strong> para comparar las características actuales con el baseline.
                </p>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; margin-top: 0.5rem;">
                    <p style="margin: 0; font-size: 0.9rem; color: #333333 !important;">
                        Si <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">p_value < 0.05</code> Y <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">statistic > 0.3</code> → <strong style="color: #ff9500 !important;">Drift detectado ✅</strong>
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #ff9500;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🔀</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T3: Decisión Reentrenamiento
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: BranchPythonOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin-bottom: 0.5rem;">
                    Evalúa si se detectó drift y decide el siguiente paso:
                </p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.5rem;">
                    <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 6px; border-left: 3px solid #34c759;">
                        <strong style="color: #000000 !important;">Si hay drift:</strong>
                        <p style="color: #333333 !important; font-size: 0.9rem; margin: 0.3rem 0 0 0;">
                            → Activa DAG 3 (Training)
                        </p>
                    </div>
                    <div style="background: rgba(134, 134, 139, 0.1); padding: 1rem; border-radius: 6px; border-left: 3px solid #86868b;">
                        <strong style="color: #000000 !important;">Si NO hay drift:</strong>
                        <p style="color: #333333 !important; font-size: 0.9rem; margin: 0.3rem 0 0 0;">
                            → Finaliza (no se necesita reentrenar)
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # DAG 3: Training Pipeline
    with st.expander("🤖 **DAG 3: TRAINING PIPELINE - Reentrenamiento del Modelo (On-Demand)**", expanded=False):
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.1) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #5856d6; margin-bottom: 1.5rem;">
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">
                📋 Información del DAG
            </h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                <div>
                    <strong style="color: #5856d6 !important;">Nombre:</strong>
                    <span style="color: #000000 !important;">train_invoice_model</span>
                </div>
                <div>
                    <strong style="color: #5856d6 !important;">Horario:</strong>
                    <span style="color: #000000 !important;">None (Manual o Triggered)</span>
                </div>
                <div style="grid-column: 1 / -1;">
                    <strong style="color: #5856d6 !important;">Objetivo:</strong>
                    <span style="color: #000000 !important;">Reentrenar el modelo con CI/CD completo y versionado automático</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tareas del DAG 3
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🚀</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T1: Iniciar Entrenamiento
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: SimpleHttpOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin: 0;">
                    Dispara el pipeline de entrenamiento enviando <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">POST api:8000/train_model</code>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #5856d6;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(88, 86, 214, 0.1) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #5856d6; margin: 1rem 0; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚙️</div>
            <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
                FastAPI ejecuta el pipeline de entrenamiento
            </h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin-top: 1rem;">
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">📥 Download Drive</div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">🔄 Preprocesamiento</div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">🤖 Train CNN</div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">✅ CI: F1>0.85</div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">📦 DVC Push</div>
                <div style="background: white; padding: 0.8rem; border-radius: 6px; font-size: 0.85rem;">📊 Tracking MySQL</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #5856d6;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">📊</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T2: Monitorear CD
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: HttpSensor | Polling: Cada 120s | Timeout: 2 horas
                    </p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin-bottom: 0.5rem;">
                    Monitorea el progreso del entrenamiento consultando <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">GET api:8000/train_model/status</code> cada 2 minutos.
                </p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.85rem; margin-top: 0.5rem;">
                    <div style="color: #333333 !important;">• descarga_datos → 10%</div>
                    <div style="color: #333333 !important;">• preprocesamiento → 20%</div>
                    <div style="color: #333333 !important;">• entrenamiento → 50%</div>
                    <div style="color: #333333 !important;">• validacion_ci → 70%</div>
                    <div style="color: #333333 !important;">• dvc_push → 90%</div>
                    <div style="color: #34c759 !important; font-weight: 600;">• completado → 100% ✅</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #5856d6;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">✅</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T3: Verificar Promoción
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: PythonOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin-bottom: 0.5rem;">
                    Verifica si el modelo pasó las validaciones de CI (F1 > 0.85) y fue promovido a producción.
                </p>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.5rem;">
                    <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 6px; border-left: 3px solid #34c759;">
                        <strong style="color: #000000 !important;">Promovido ✅</strong>
                        <p style="color: #333333 !important; font-size: 0.9rem; margin: 0.3rem 0 0 0;">
                            Modelo versionado en DVC + S3
                        </p>
                    </div>
                    <div style="background: rgba(255, 59, 48, 0.1); padding: 1rem; border-radius: 6px; border-left: 3px solid #ff3b30;">
                        <strong style="color: #000000 !important;">Rechazado ⚠️</strong>
                        <p style="color: #333333 !important; font-size: 0.9rem; margin: 0.3rem 0 0 0;">
                            Alerta a Slack, modelo anterior se mantiene
                        </p>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0; font-size: 2rem; color: #5856d6;">⬇️</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">🔄</div>
                <div>
                    <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin: 0;">
                        T4: Reset Estado
                    </h4>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">
                        Tipo: SimpleHttpOperator
                    </p>
                </div>
            </div>
            <div style="background: rgba(88, 86, 214, 0.05); padding: 1rem; border-radius: 8px;">
                <p style="color: #000000 !important; font-size: 0.95rem; margin: 0;">
                    Resetea el estado del sistema a "inactivo" para permitir futuros entrenamientos. 
                    Envía <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">POST api:8000/train_model/reset</code>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")

    # Diagrama de Orquestación Creativo
    st.markdown("""
    <div style="margin: 3rem 0 2rem 0;">
        <h3 style="font-size: 2.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
            🎼 Diagrama de Orquestación Completa
        </h3>
        <p style="font-size: 1.2rem; color: #333333 !important; text-align: center; margin-bottom: 2rem;">
            Visualiza cómo los 3 DAGs trabajan juntos como una orquesta perfectamente sincronizada
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    
    
    # DAG 1
    st.markdown("""
        <div style="position: relative; margin-bottom: 4rem; z-index: 2;">
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="flex: 1; background: linear-gradient(135deg, rgba(0, 113, 227, 0.15) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 2rem; border-radius: 14px; border: 3px solid #0071e3; box-shadow: 0 4px 16px rgba(0, 113, 227, 0.2);">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <div style="font-size: 3rem;">📥</div>
                        <div>
                            <h4 style="font-size: 1.4rem; font-weight: 700; color: #000000 !important; margin: 0;">
                                DAG 1: ETL Pipeline
                            </h4>
                            <p style="font-size: 0.95rem; color: #0071e3 !important; margin: 0.3rem 0 0 0; font-weight: 600;">
                                ⏰ Cada hora (0 * * * *)
                            </p>
                        </div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <p style="color: #000000 !important; font-size: 0.95rem; margin: 0; line-height: 1.6;">
                            <strong>Función:</strong> Procesa facturas nuevas automáticamente<br>
                            <strong>Resultado:</strong> Datos en MySQL + Archivos en Google Drive<br>
                            <strong>Frecuencia:</strong> 24 veces al día
                        </p>
                    </div>
                </div>
                <div style="width: 60px; height: 60px; background: #0071e3; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: white; font-weight: bold; box-shadow: 0 4px 12px rgba(0, 113, 227, 0.4);">
                    1
                </div>
                <div style="flex: 0; width: 100px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Flecha y DAG 2
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0; font-size: 2.5rem; color: #ff9500; z-index: 2; position: relative;">
            ⬇️ <span style="font-size: 1rem; color: #000000 !important; margin-left: 1rem;">Genera datos que DAG 2 analiza</span>
        </div>
        
        <div style="position: relative; margin-bottom: 4rem; z-index: 2;">
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="flex: 0; width: 100px;"></div>
                <div style="width: 60px; height: 60px; background: #ff9500; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: white; font-weight: bold; box-shadow: 0 4px 12px rgba(255, 149, 0, 0.4);">
                    2
                </div>
                <div style="flex: 1; background: linear-gradient(135deg, rgba(255, 149, 0, 0.15) 0%, rgba(255, 149, 0, 0.05) 100%); padding: 2rem; border-radius: 14px; border: 3px solid #ff9500; box-shadow: 0 4px 16px rgba(255, 149, 0, 0.2);">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <div style="font-size: 3rem;">🔍</div>
                        <div>
                            <h4 style="font-size: 1.4rem; font-weight: 700; color: #000000 !important; margin: 0;">
                                DAG 2: Drift Detection
                            </h4>
                            <p style="font-size: 0.95rem; color: #ff9500 !important; margin: 0.3rem 0 0 0; font-weight: 600;">
                                ⏰ Domingos 3 AM (0 3 * * 0)
                            </p>
                        </div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <p style="color: #000000 !important; font-size: 0.95rem; margin: 0; line-height: 1.6;">
                            <strong>Función:</strong> Detecta cambios en la distribución de datos<br>
                            <strong>Método:</strong> Kolmogorov-Smirnov test estadístico<br>
                            <strong>Decisión:</strong> ¿Hay drift? → Activa DAG 3 automáticamente
                        </p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Flecha de decisión
    st.markdown("""
        <div style="text-align: center; margin: 2rem 0; z-index: 2; position: relative;">
            <div style="display: inline-block; background: rgba(255, 149, 0, 0.1); padding: 1rem 2rem; border-radius: 8px; border: 2px dashed #ff9500;">
                <p style="margin: 0; color: #000000 !important; font-size: 1rem; font-weight: 600;">
                    🔀 Si detecta drift → Dispara DAG 3
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # DAG 3
    st.markdown("""
        <div style="position: relative; z-index: 2;">
            <div style="display: flex; align-items: center; gap: 2rem;">
                <div style="flex: 1; background: linear-gradient(135deg, rgba(88, 86, 214, 0.15) 0%, rgba(88, 86, 214, 0.05) 100%); padding: 2rem; border-radius: 14px; border: 3px solid #5856d6; box-shadow: 0 4px 16px rgba(88, 86, 214, 0.2);">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <div style="font-size: 3rem;">🤖</div>
                        <div>
                            <h4 style="font-size: 1.4rem; font-weight: 700; color: #000000 !important; margin: 0;">
                                DAG 3: Training Pipeline
                            </h4>
                            <p style="font-size: 0.95rem; color: #5856d6 !important; margin: 0.3rem 0 0 0; font-weight: 600;">
                                🖐️ On-Demand (Triggered por DAG 2 o Manual)
                            </p>
                        </div>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                        <p style="color: #000000 !important; font-size: 0.95rem; margin: 0; line-height: 1.6;">
                            <strong>Función:</strong> Reentrena el modelo con nuevos datos<br>
                            <strong>CI/CD:</strong> Valida F1 > 0.85 antes de promover<br>
                            <strong>Versionado:</strong> DVC + S3 automático
                        </p>
                    </div>
                </div>
                <div style="width: 60px; height: 60px; background: #5856d6; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; color: white; font-weight: bold; box-shadow: 0 4px 12px rgba(88, 86, 214, 0.4);">
                    3
                </div>
                <div style="flex: 0; width: 100px;"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Resultado final
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.15) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 2rem; border-radius: 12px; border: 2px solid #34c759; margin-top: 3rem; text-align: center;">
            <h4 style="font-size: 1.3rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
                🎯 Resultado de la Orquestación
            </h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 1.5rem;">
                <div style="background: white; padding: 1.5rem; border-radius: 10px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔄</div>
                    <strong style="color: #000000 !important;">Automatización</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">
                        Sin intervención humana
                    </p>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                    <strong style="color: #000000 !important;">Monitoreo</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">
                        Detección automática de cambios
                    </p>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 10px;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🚀</div>
                    <strong style="color: #000000 !important;">Auto-mejora</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.5rem 0 0 0;">
                        Reentrenamiento inteligente
                    </p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Comunicación Airflow ↔ FastAPI
    st.markdown("""
    <div style="margin: 3rem 0 2rem 0;">
        <h3 style="font-size: 2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
            📡 Comunicación Airflow ↔ FastAPI
        </h3>
        <p style="font-size: 1.1rem; color: #333333 !important; text-align: center; margin-bottom: 2rem;">
            Cómo se comunican el orquestador y el ejecutor
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contenedor principal
    st.markdown("""
    <div style="background: #ffffff; padding: 2rem; border-radius: 14px; box-shadow: 0 4px 16px rgba(0,0,0,0.08); margin: 2rem 0;">
    """, unsafe_allow_html=True)
    
    # Grid con 3 columnas
    col_airflow, col_arrow, col_fastapi = st.columns([1, 0.3, 1])
    
    with col_airflow:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(0, 113, 227, 0.1) 0%, rgba(0, 113, 227, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #0071e3;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem; text-align: center;">🎼</div>
            <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
                Apache Airflow
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin-bottom: 1rem; text-align: center;">
                <strong>Rol:</strong> Orquestador
            </p>
            <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Programa tareas</li>
                <li>Monitorea progreso</li>
                <li>Gestiona errores</li>
                <li>Coordina workflows</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_arrow:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 2rem; color: #0071e3; margin-bottom: 0.5rem;">↔️</div>
            <div style="background: rgba(0, 113, 227, 0.1); padding: 0.5rem 1rem; border-radius: 6px; font-size: 0.85rem; color: #000000 !important;">
                HTTP REST API
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_fastapi:
        st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.1) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 1.5rem; border-radius: 12px; border: 2px solid #34c759;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem; text-align: center;">⚙️</div>
            <h4 style="font-size: 1.2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
                FastAPI
            </h4>
            <p style="font-size: 0.95rem; color: #333333 !important; margin-bottom: 1rem; text-align: center;">
                <strong>Rol:</strong> Ejecutor
            </p>
            <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0; padding-left: 1.2rem;">
                <li>Ejecuta ETL</li>
                <li>Entrena modelos</li>
                <li>Reporta estado</li>
                <li>Procesa datos</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)
    
    # Sección de Endpoints
    st.markdown("""
    <div style="background: rgba(0, 113, 227, 0.05); padding: 1.5rem; border-radius: 8px; margin-top: 2rem;">
        <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            🔄 Endpoints de Comunicación
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    col_end1, col_end2 = st.columns(2)
    
    with col_end1:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
            <strong style="color: #0071e3 !important;">Airflow → FastAPI:</strong>
            <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>POST /procesar_facturas</li>
                <li>POST /train_model</li>
                <li>POST /reset</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_end2:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 6px; margin-top: 1rem;">
            <strong style="color: #34c759 !important;">FastAPI → Airflow:</strong>
            <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>GET /status (respuestas)</li>
                <li>Estado: "inactivo", "en_cola", "ejecutando", "completado"</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detalles del Procesamiento - Secciones corregidas
    st.markdown("""
    <div style="margin: 3rem 0 2rem 0;">
        <h3 style="font-size: 2rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem; text-align: center;">
            🔧 Detalles del Procesamiento
        </h3>
        <p style="font-size: 1.1rem; color: #333333 !important; text-align: center; margin-bottom: 2rem;">
            Una vez activado, el sistema ejecuta estas 6 fases automáticamente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Fase 0: Verificación
    with st.expander("✅ **FASE 0: VERIFICACIÓN DE PRERREQUISITOS**", expanded=True):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #34c759;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">☁️</div>
                    <strong style="color: #000000 !important;">Google Drive</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">OAuth2 valida token.json</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #34c759;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💾</div>
                    <strong style="color: #000000 !important;">MySQL RDS</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">Test query a textil DB</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #34c759;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📦</div>
                    <strong style="color: #000000 !important;">AWS S3</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">Lista bucket mes-en-curso</p>
                </div>
                <div style="background: rgba(52, 199, 89, 0.1); padding: 1rem; border-radius: 8px; border-left: 3px solid #34c759;">
                    <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🤖</div>
                    <strong style="color: #000000 !important;">Modelo ML</strong>
                    <p style="font-size: 0.9rem; color: #666666 !important; margin: 0.3rem 0 0 0;">Verifica modelo_facturas_final.h5<br/>Si NO existe → dvc pull desde S3</p>
                </div>
            </div>
            <div style="background: rgba(255, 149, 0, 0.1); padding: 1rem; border-radius: 8px; text-align: center; border: 2px solid #ff9500;">
                <p style="margin: 0; color: #000000 !important; font-weight: 600;">
                    ⚠️ Si alguno falla → Estado: "error", termina proceso
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 1: Descarga S3
    with st.expander("📥 **FASE 1: DESCARGA DESDE S3**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #0071e3; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(0, 113, 227, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">📥 Boto3 conecta a AWS S3</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div>
                        <strong style="color: #0071e3 !important;">Bucket:</strong>
                        <span style="color: #000000 !important;">mes-en-curso</span>
                    </div>
                    <div>
                        <strong style="color: #0071e3 !important;">Archivos:</strong>
                        <span style="color: #000000 !important;">*.pdf</span>
                    </div>
                    <div>
                        <strong style="color: #0071e3 !important;">Destino:</strong>
                        <span style="color: #000000 !important;">/tmp/mes_en_curso/</span>
                    </div>
                </div>
            </div>
            <div style="background: rgba(0, 113, 227, 0.05); padding: 1rem; border-radius: 8px;">
                <h4 style="font-size: 1rem; font-weight: 700; color: #000000 !important; margin-bottom: 0.5rem;">Archivos descargados:</h4>
                <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0; padding-left: 1.5rem;">
                    <li>factura001.pdf (340 KB) ✅</li>
                    <li>factura002.pdf (450 KB) ✅</li>
                    <li>factura003.pdf (380 KB) ✅</li>
                </ul>
            </div>
            <div style="text-align: center; margin-top: 1rem; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                <strong style="color: #000000 !important;">Progreso: 30%</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 2: Clasificación ML
    with st.expander("🤖 **FASE 2: CLASIFICACIÓN CON INTELIGENCIA ARTIFICIAL**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #5856d6; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(88, 86, 214, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">🤖 Red Neuronal CNN analiza cada factura</h4>
                <div style="margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 6px; border-left: 3px solid #34c759;">
                    <strong style="color: #000000 !important;">factura001.pdf:</strong>
                    <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>PDF → Imagen RGB 224x224 (pdf2image)</li>
                        <li>Normaliza [0, 1] (NumPy)</li>
                        <li>Pasa por CNN (TensorFlow)</li>
                        <li>Score: 0.23 (< 0.5)</li>
                        <li><strong style="color: #34c759 !important;">Clasificación: PREVENTIVA ✅</strong></li>
                    </ul>
                </div>
                <div style="margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 6px; border-left: 3px solid #ff9500;">
                    <strong style="color: #000000 !important;">factura002.pdf:</strong>
                    <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Score: 0.87 (> 0.5)</li>
                        <li><strong style="color: #ff9500 !important;">Clasificación: CORRECTIVA ⚠️</strong></li>
                    </ul>
                </div>
                <div style="padding: 1rem; background: white; border-radius: 6px; border-left: 3px solid #34c759;">
                    <strong style="color: #000000 !important;">factura003.pdf:</strong>
                    <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>Score: 0.15</li>
                        <li><strong style="color: #34c759 !important;">Clasificación: PREVENTIVA ✅</strong></li>
                    </ul>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                <strong style="color: #000000 !important;">Progreso: 60%</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 3: OCR
    with st.expander("📝 **FASE 3: EXTRACCIÓN DE DATOS (OCR)**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff2d55; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(255, 45, 85, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">📝 Tesseract OCR lee cada factura</h4>
                <div style="margin-bottom: 1rem; padding: 1rem; background: white; border-radius: 6px;">
                    <strong style="color: #000000 !important;">factura001.pdf (Preventiva):</strong>
                    <div style="margin-top: 0.5rem; padding: 0.8rem; background: rgba(0,0,0,0.03); border-radius: 4px; font-family: monospace; font-size: 0.85rem; color: #333333 !important;">
                        "ORDEN DE COMPRA #12345<br/>
                        Fecha: 2024-01-15<br/>
                        Producto: Tela industrial<br/>
                        Cantidad: 100 metros<br/>
                        Total: $1,500.00"
                    </div>
                    <div style="margin-top: 0.8rem;">
                        <strong style="color: #ff2d55 !important;">Campos extraídos:</strong>
                        <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li>orden_compra: 12345</li>
                            <li>fecha: "2024-01-15"</li>
                            <li>productos: ["Tela industrial"]</li>
                            <li>cantidades: [100]</li>
                            <li>totales: [1500.00]</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                <strong style="color: #000000 !important;">Progreso: 80%</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 4: Carga MySQL
    with st.expander("💾 **FASE 4: CARGA EN MYSQL (AWS RDS)**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #34c759; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(52, 199, 89, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">💾 SQLAlchemy inserta en base de datos</h4>
                <p style="color: #333333 !important; margin-bottom: 1rem;">
                    <strong>Conexión:</strong> <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">textil.rds.amazonaws.com/textil</code>
                </p>
                <div style="background: white; padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                    <strong style="color: #000000 !important;">Transacciones ejecutadas:</strong>
                    <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>ventas_preventivas: 3 registros ✅</li>
                        <li>ventas_correctivas: 1 registro ✅</li>
                    </ul>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                <strong style="color: #000000 !important;">Progreso: 90% | 4 registros insertados</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 5: Google Drive
    with st.expander("☁️ **FASE 5: ARCHIVO EN GOOGLE DRIVE**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #ff9500; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(255, 149, 0, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">☁️ Google Drive API sube archivos</h4>
                <div style="background: white; padding: 1rem; border-radius: 6px; margin-bottom: 1rem;">
                    <strong style="color: #000000 !important;">Estructura:</strong>
                    <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                        <li>📁 facturas/historico/ → 3 facturas ✅</li>
                        <li>📁 facturas/preventivos/ → 2 facturas ✅</li>
                        <li>📁 facturas/correctivos/ → 1 factura ✅</li>
                    </ul>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(52, 199, 89, 0.1); border-radius: 8px;">
                <strong style="color: #000000 !important;">Progreso: 95% | Total subido: 6 archivos</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fase 6: Limpieza
    with st.expander("🗑️ **FASE 6: LIMPIEZA AUTOMÁTICA**", expanded=False):
        st.markdown("""
        <div style="background: #ffffff; padding: 1.5rem; border-radius: 12px; border-top: 4px solid #86868b; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <div style="background: rgba(134, 134, 139, 0.1); padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="font-size: 1.1rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">🗑️ Limpia recursos para evitar duplicados</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div style="background: white; padding: 1rem; border-radius: 6px;">
                        <strong style="color: #000000 !important;">1. Elimina de S3:</strong>
                        <ul style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0; padding-left: 1.5rem;">
                            <li>factura001.pdf ✅</li>
                            <li>factura002.pdf ✅</li>
                            <li>factura003.pdf ✅</li>
                        </ul>
                    </div>
                    <div style="background: white; padding: 1rem; border-radius: 6px;">
                        <strong style="color: #000000 !important;">2. Elimina locales:</strong>
                        <p style="color: #333333 !important; font-size: 0.9rem; margin: 0.5rem 0;">
                            <code style="background: rgba(0,0,0,0.05); padding: 0.2rem 0.5rem; border-radius: 4px;">rm -rf /tmp/mes_en_curso/</code> ✅
                        </p>
                    </div>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, rgba(52, 199, 89, 0.2) 0%, rgba(52, 199, 89, 0.1) 100%); border-radius: 8px; border: 2px solid #34c759;">
                <strong style="color: #000000 !important; font-size: 1.1rem;">Progreso: 100% ✅</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Resultado final
    st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(52, 199, 89, 0.15) 0%, rgba(52, 199, 89, 0.05) 100%); padding: 2rem; border-radius: 12px; border: 2px solid #34c759; margin: 3rem 0; text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">✅</div>
        <h3 style="font-size: 1.8rem; font-weight: 700; color: #000000 !important; margin-bottom: 1rem;">
            PROCESO COMPLETADO
        </h3>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1.5rem;">
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📊</div>
                <strong style="color: #000000 !important;">3 facturas</strong>
                <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.3rem 0 0 0;">clasificadas</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">💾</div>
                <strong style="color: #000000 !important;">4 registros</strong>
                <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.3rem 0 0 0;">en MySQL</p>
            </div>
            <div style="background: white; padding: 1rem; border-radius: 8px;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">☁️</div>
                <strong style="color: #000000 !important;">6 archivos</strong>
                <p style="font-size: 0.85rem; color: #666666 !important; margin: 0.3rem 0 0 0;">en Google Drive</p>
            </div>
        </div>
        <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 2px solid rgba(0,0,0,0.1);">
            <p style="font-size: 1.1rem; color: #000000 !important; margin: 0; font-weight: 600;">
                ⏱️ Duración total: ~5 minutos | 🎯 SIN INTERVENCIÓN HUMANA | ✅ CERO ERRORES
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")