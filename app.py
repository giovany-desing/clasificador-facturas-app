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
    # Mostrar imagen de datos
    st.image("image_data.png", use_container_width=True)
    
    # Sección de enfoque serverless
    st.markdown("""
    <div style="max-width: 1000px; margin: 2rem auto; padding: 0 2rem;">
        <h3 style="font-size: 1.8rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Construir sobre AWS con enfoque serverless (ECS Fargate, MWAA) en lugar de servidores tradicionales (EC2)
        </h3>
        
        <h4 style="font-size: 1.4rem; font-weight: 700; color: #1d1d1f; margin-top: 2rem; margin-bottom: 1rem;">
            Por qué:
        </h4>
        
        <div style="margin-bottom: 2rem;">
            <h5 style="font-size: 1.2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 0.8rem;">
                Razones Técnicas:
            </h5>
            <ul style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-left: 1.5rem; margin-bottom: 1.5rem;">
                <li>Zero gestión de infraestructura: No aprovisionar, parchear ni mantener servidores</li>
                <li>Alta disponibilidad automática: Multi-AZ sin configuración manual</li>
                <li>Elasticidad nativa: Auto-scaling basado en demanda (2-10 tasks según carga)</li>
                <li>Pay-per-use: Pago por segundo de uso real, no por capacidad aprovisionada</li>
                <li>Tiempo de deploy: Segundos vs minutos (EC2)</li>
                <li>Patching automático: AWS gestiona actualizaciones de seguridad</li>
            </ul>
        </div>
        
        <div style="margin-bottom: 2rem;">
            <h5 style="font-size: 1.2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 0.8rem;">
                Razones de Negocio:
            </h5>
            <ul style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-left: 1.5rem; margin-bottom: 1.5rem;">
                <li>Reducción de costos operacionales: ~60% menos vs EC2 gestionado manualmente</li>
                <li>Time-to-market: Deploy en minutos vs días de configuración</li>
                <li>Enfoque en valor: Equipo se enfoca en ML/ETL, no en infraestructura</li>
                <li>Predictibilidad de costos: Sin sobre-aprovisionamiento, pago por uso real</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Amazon ECR
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Amazon ECR (Elastic Container Registry)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Registry privado de Docker images totalmente gestionado con integración nativa a ECS/Fargate. Escaneo automático de vulnerabilidades (CVEs) en imágenes vía Amazon Inspector. Replicación cross-region y lifecycle policies para eliminar tags antiguos. Comparado con Docker Hub público, ECR ofrece seguridad enterprise-grade y pull ilimitado sin rate limits.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Almacena 3 imágenes Docker privadas: (1) fastapi-app:latest (API backend), (2) training:v2.x (jobs de entrenamiento CNN), (3) mlflow:latest (servidor tracking). ECS Fargate pull images desde ECR usando IAM roles (no credenciales hardcoded). CI/CD pipeline (GitHub Actions) construye imágenes, las tagea con commit SHA, y las pushea a ECR automáticamente.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # AWS VPC & Networking
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            AWS VPC & Networking
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Virtual Private Cloud permite aislamiento de red completo con control granular sobre subnets, routing, NAT gateways, e Internet Gateways. Subnets públicas/privadas implementan arquitectura de defensa en profundidad: recursos internos (RDS, ECS tasks) en subnets privadas sin acceso directo desde internet. Security Groups actúan como firewalls stateful a nivel de instancia.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> VPC dedicada con CIDR 10.0.0.0/16 contiene: (1) 2 subnets públicas (AZs us-east-1a/1b) para ALB e NAT Gateway, (2) 2 subnets privadas para ECS Fargate tasks y RDS (Multi-AZ). Route tables dirigen tráfico: subnet privada → NAT Gateway → Internet para actualizaciones. Security Groups: ALB permite 80/443 desde 0.0.0.0/0, ECS permite 8000 solo desde ALB, RDS permite 3306 solo desde ECS.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Orquestación & Workflow
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Orquestación & Workflow
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Apache Airflow 2.8
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Apache Airflow 2.8
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Plataforma de orquestación de workflows líder con 10+ años de madurez. DAG (Directed Acyclic Graph) paradigm permite definir dependencias complejas entre tareas como código Python. Scheduler robusto con retry logic, SLA monitoring, backfill capabilities. Comparado con Prefect o Dagster (más nuevos), Airflow tiene ecosistema de operators más amplio (400+) y comunidad más grande.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Orquesta 3 DAGs críticos en producción: (1) etl_production.py cron 0 * * * * (cada hora) ejecuta 5 tasks: check_drive → download_files → ocr_processing → db_insert → cleanup, (2) train_production.py trigger manual ejecuta: fetch_data → preprocess → train_model → evaluate → register_mlflow → deploy_to_s3, (3) drift_production.py cron semanal ejecuta KS tests, calcula PSI (Population Stability Index), genera alertas si drift >0.15.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # MWAA Executors & Workers
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            MWAA Executors & Workers
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> MWAA usa CeleryExecutor que distribuye task execution entre múltiples workers escalables. Comparado con LocalExecutor (single-machine) o KubernetesExecutor (complejo), Celery ofrece balance ideal entre performance y simplicidad. Workers escalan automáticamente entre 1-10 basado en queue depth.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> CeleryExecutor con Redis como message broker coordina ejecución paralela de tasks. Configuración: 2 workers mínimo (alta disponibilidad), cada worker con 4 vCPU + 8GB RAM. Tasks de larga duración (OCR batch processing) ejecutan en workers dedicados, tasks livianas (DB queries) en pool shared. Logs de cada task se almacenan en CloudWatch con retention 30 días.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Machine Learning & Data Science
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Machine Learning & Data Science
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # TensorFlow 2.15 + Keras
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            TensorFlow 2.15 + Keras
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Framework de deep learning más adoptado en producción (usado por Google, Uber, Airbnb). TensorFlow 2.x con eager execution simplifica debugging vs TensorFlow 1.x. Keras high-level API permite prototipado rápido de arquitecturas complejas en <100 líneas. SavedModel format es estándar para deployment (TF Serving, ONNX compatible). GPU support nativo con CUDA.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Define arquitectura CNN de clasificación binaria: Input(224x224x3) → Conv2D(32, relu) → MaxPool → Conv2D(64, relu) → MaxPool → Conv2D(128, relu) → Flatten → Dense(256, relu) → Dropout(0.5) → Dense(1, sigmoid). Compilado con Adam optimizer (lr=0.001), binary_crossentropy loss. Entrenamiento: 50 epochs, batch_size=32, validation_split=0.2, early_stopping callback (patience=5). Output: probabilidad [0-1] de factura válida.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # NumPy 1.24 + Pandas 2.1
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            NumPy 1.24 + Pandas 2.1
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> NumPy es la librería fundamental para computación numérica en Python, base de todo el ecosistema científico. Arrays N-dimensionales optimizados en C ofrecen 10-100x speedup vs listas Python puras. Pandas construido sobre NumPy proporciona DataFrames (estructuras tabulares) con operaciones SQL-like. Sin equivalentes en otros lenguajes con esta madurez.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> NumPy maneja operaciones vectorizadas en preprocessing: normalización de imágenes (pixel values [0-255] → [0-1]), reshaping de tensores, cálculos de métricas (confusion matrix, accuracy). Pandas procesa datos tabulares: CSVs de facturas → DataFrames con columnas (nit, fecha, monto, label). Operaciones: filtering (df[df['monto'] > 1000000]), groupby agregaciones, merge entre datasets, exportación a MySQL.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Scikit-learn 1.3
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Scikit-learn 1.3
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Librería de ML clásico más completa con implementaciones optimizadas de 100+ algoritmos. Train/test split utilities, metrics (accuracy, precision, recall, ROC-AUC), preprocessing (StandardScaler, LabelEncoder), y model selection (GridSearchCV). Comparado con implementaciones custom, sklearn ofrece código battle-tested y API consistente.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Provee utilidades críticas para pipeline ML: (1) train_test_split() divide dataset en 70% train, 15% val, 15% test manteniendo stratification de clases, (2) classification_report() genera precision/recall/f1 por clase, (3) KolmogorovSmirnovTest detecta data drift comparando distribuciones de features entre training set y production data, (4) StandardScaler normaliza features numéricos (montos, confidences OCR) antes de alimentar CNN.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Matplotlib 3.8 + Seaborn 0.13
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Matplotlib 3.8 + Seaborn 0.13
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Matplotlib es el estándar de facto para visualización en Python, altamente customizable. Seaborn construido sobre matplotlib añade aesthetic defaults y plots estadísticos high-level. Generación programática de gráficos permite integración en pipelines automatizados (vs herramientas interactivas como Tableau).
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Genera visualizaciones para análisis ML y reportes: (1) Training curves accuracy/loss vs epochs con plt.plot(), (2) Confusion matrix heatmap con sns.heatmap() mostrando TP/FP/TN/FN, (3) ROC curves con AUC score, (4) Feature distributions histogramas comparando train vs production data para drift detection, (5) Drift reports line plots de PSI scores semanales. Gráficos guardados como PNG en S3 y registrados en MLflow artifacts.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # MLOps & Versionado
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            MLOps & Versionado
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # MLflow 2.9
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            MLflow 2.9
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Suite MLOps completa con 4 componentes: Tracking (experimentos), Projects (reproducibilidad), Models (deployment), Registry (gestión de versiones). Open-source y cloud-agnostic permite evitar vendor lock-in vs SageMaker. REST API y Python SDK facilitan integración en cualquier workflow. UI web intuitiva para stakeholders no-técnicos.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Tracking Server (puerto 5000) registra cada run con: mlflow.log_params({'epochs': 50, 'batch_size': 32}), mlflow.log_metrics({'accuracy': 0.92, 'val_loss': 0.18}), mlflow.log_artifacts('plots/'). Model Registry almacena modelos con stages: Development → Staging → Production. Metadata incluye: training timestamp, dataset version (DVC hash), hyperparameters, performance metrics. API permite fetch programático: model = mlflow.pyfunc.load_model('models:/invoice-classifier/Production').
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # DVC 3.30
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            DVC 3.30
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Solución Git-based para versionar datasets (GBs-TBs) que no caben en repositorios Git normales. .dvc files (lightweight pointers) se commiten a Git mientras datos reales viven en S3. Permite branching de datos similar a Git branches. DVC pipelines definen DAGs de data processing garantizando reproducibilidad end-to-end.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Versiona 3 componentes: (1) data/train.csv (5.2GB, 50k facturas etiquetadas), (2) models/cnn_model.h5 (240MB), (3) data/validation.csv (1.1GB). Workflow: dvc add data/train.csv crea train.csv.dvc con MD5 hash, dvc push sube archivo a S3 remote storage. Checkout específico: git checkout v2.3.1 && dvc checkout restaura exactamente dataset usado en experimento v2.3.1. Pipeline dvc.yaml define stages: preprocess → train → evaluate con dependencies automáticas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Git & GitHub
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Git & GitHub
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Git es el sistema de control de versiones distribuido estándar en la industria. Branching/merging model permite desarrollo paralelo. GitHub añade colaboración (PRs, code review), issue tracking, y GitHub Actions para CI/CD. Comparado con GitLab (self-hosted) o Bitbucket, GitHub tiene ecosistema más amplio de integraciones.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Repositorio central con branching strategy: main (production-ready), develop (integration), feature branches feature/*. Commits siguen Conventional Commits: feat:, fix:, docs:. .gitignore excluye: datos crudos (.csv >10MB), secrets (.env), artefactos ML (*.h5), Terraform state (terraform.tfstate). GitHub Projects trackea tareas, milestones, sprints.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Base de Datos & Almacenamiento
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Base de Datos & Almacenamiento
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # MySQL 8.0
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            MySQL 8.0
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> RDBMS open-source maduro con 25+ años de producción. MySQL 8.0 introduce features enterprise: window functions, CTEs (Common Table Expressions), JSON datatype nativo, role-based access control. Performance mejorada ~2x vs 5.7 gracias a nuevo storage engine InnoDB. ACID compliance garantiza integridad transaccional.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Schema facturas_db con 5 tablas relacionadas: (1) invoices (id PK, nit, fecha, monto, ciudad, ocr_text TEXT, classification_score FLOAT, created_at), (2) clients (nit PK, nombre, ciudad), (3) predictions (id, invoice_id FK, model_version, probability, predicted_class, timestamp), (4) model_metadata (version, training_date, accuracy, f1_score), (5) audit_log (event_type, user, timestamp, details JSON). Índices: B-tree en nit, fecha; Full-text index en ocr_text para búsquedas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # SQLAlchemy 2.0 ORM
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            SQLAlchemy 2.0 ORM
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> ORM (Object-Relational Mapping) más popular de Python que abstrae SQL en objetos Python. Previene SQL injection via parameterized queries. Connection pooling automático mejora performance. Migrations con Alembic permiten evolucionar schema sin downtime. Comparado con raw SQL, SQLAlchemy ofrece portabilidad entre databases (MySQL, PostgreSQL).
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Define modelos declarativos: class Invoice(Base): __tablename__ = 'invoices'; id = Column(Integer, primary_key=True); nit = Column(String(20), index=True). Queries: session.query(Invoice).filter(Invoice.monto > 1000000).all(). Relaciones: Invoice.client = relationship('Client', backref='invoices') permite invoice.client.nombre automáticamente. Connection pool: 5-20 conexiones reutilizables reduce overhead de crear conexiones por request.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Amazon S3 (detalles adicionales)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Amazon S3 (detalles adicionales)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Lifecycle Policies:</strong> Transición automática raw/ → S3 Glacier Deep Archive después 90 días reduce costos 95%. Versioning habilitado en models/ permite rollback a modelos anteriores. Server-side encryption (SSE-S3) encrypta datos at rest automáticamente.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Organización:</strong> Buckets estructurados por ambiente: etl-facturas-dev, etl-facturas-prod. Prefixes simulan directorios: s3://etl-facturas-prod/raw/2025/01/15/invoice_001.pdf. Uso de presigned URLs (expiran en 1 hora) permite descarga temporal sin credenciales AWS.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # API & Backend
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            API & Backend
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Pydantic 2.5
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Pydantic 2.5
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Librería de validación de datos usando Python type hints. Parsing automático y validación de requests/responses previene bugs de tipos en runtime. Performance optimizada con Rust core (10-50x faster vs v1). Generación automática de JSON schemas para OpenAPI. FastAPI construido sobre Pydantic aprovechando validación sin código boilerplate.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Define schemas de API: class PredictionRequest(BaseModel): nit: str = Field(pattern=r'^\d{9}$'); fecha: date; monto: float = Field(gt=0). Validación automática: request con nit='abc' retorna 422 Unprocessable Entity con error detallado. Response models garantizan consistencia: class PredictionResponse(BaseModel): invoice_id: int; is_valid: bool; confidence: float; processing_time_ms: int.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Uvicorn 0.24 ASGI Server
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Uvicorn 0.24 ASGI Server
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Servidor ASGI (Asynchronous Server Gateway Interface) ultra-rápido construido con uvloop (event loop optimizado en Cython). Soporta async/await nativo de FastAPI permitiendo concurrencia masiva con bajo overhead. Comparado con Gunicorn WSGI (sync), Uvicorn maneja 3-5x más requests/sec. Hot reload en desarrollo acelera iteración.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Ejecuta aplicación FastAPI en ECS containers con configuración: uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4 --loop uvloop --log-level info. 4 workers aprovechan CPU multi-core. Access logs formato JSON enviados a CloudWatch. Graceful shutdown maneja SIGTERM de ECS draining correctamente finalizando requests in-flight.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # JWT (JSON Web Tokens)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            JWT (JSON Web Tokens)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Estándar de autenticación stateless (RFC 7519) ideal para APIs distribuidas. Tokens auto-contenidos (payload + signature) eliminan necesidad de session store centralizado. Comparado con session cookies, JWT escala horizontalmente sin sticky sessions. HS256 signing con secret key previene tampering.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Endpoint POST /auth/login valida credenciales contra DB, retorna JWT: {"access_token": "eyJ...", "token_type": "bearer", "expires_in": 3600}. Requests subsecuentes incluyen header Authorization: Bearer eyJ.... Middleware FastAPI (@Depends(get_current_user)) valida token, extrae user_id del payload, inyecta user object en endpoint. Tokens expiran en 1 hora, refresh tokens permiten renovación sin re-login.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Containerización & Orquestación
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Containerización & Orquestación
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Docker 24+
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Docker 24+
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Plataforma de containerización líder que garantiza "runs anywhere": dev laptop, CI, production. Aislamiento de procesos via Linux namespaces y cgroups. Imágenes inmutables versionadas garantizan reproducibilidad exacta. Comparado con VMs, containers comparten kernel resultando en startup <1 segundo y overhead mínimo (~5% vs ~20% VMs).
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> 3 Dockerfiles multi-stage optimizados: (1) Dockerfile.fastapi base Python 3.11-slim (130MB) → instala deps → COPY código → EXPOSE 8000 → CMD uvicorn, imagen final ~450MB. (2) Dockerfile.training incluye TensorFlow GPU support, imagen ~2.1GB. (3) Dockerfile.mlflow imagen ~380MB. Multi-stage builds reducen tamaño 60% separando build dependencies de runtime. .dockerignore excluye tests/, .git/, pycache/.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Docker Compose
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Docker Compose
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Herramienta para definir y ejecutar aplicaciones multi-container. docker-compose.yml declarativo define servicios, networks, volumes en single file. Ideal para desarrollo local replicando producción. Comparado con orchestrar containers manualmente, Compose simplifica networking (service discovery automático) y dependency management (depends_on).
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> docker-compose.yml define stack local: services api (FastAPI), db (MySQL 8.0), mlflow (tracking server), redis (Celery broker). Networking: shared network etl-network permite api conectar a db via hostname mysql://db:3306. Volumes: mysql-data:/var/lib/mysql persiste datos entre restarts. Comando: docker-compose up -d levanta stack completo en <30 segundos.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CI/CD & DevOps
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            CI/CD & DevOps
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # GitHub Actions
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            GitHub Actions
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> CI/CD nativo de GitHub con integración seamless en repositorio. YAML-based workflows versionados como código. Matrix builds permiten testear múltiples Python versions en paralelo. 2,000 minutos/mes gratis para repos públicos. Comparado con Jenkins (self-hosted, complejo) o CircleCI (pago), GitHub Actions ofrece mejor DX (developer experience) para proyectos en GitHub.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> 3 workflows: (1) ci.yml trigger en PRs ejecuta: checkout code → setup Python 3.11 → install deps → run pytest + coverage → lint con ruff → type check con mypy. (2) cd.yml trigger en push a main ejecuta: build Docker images → tag con commit SHA → push a ECR → update ECS service con nueva task definition → wait for deployment. (3) drift-alert.yml trigger semanal ejecuta drift detection, envía Slack notification si PSI >0.15.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pytest 7.4
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Pytest 7.4
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Framework de testing moderno con fixtures poderosas, parametrization, y plugins extensos. Sintaxis Pythonic (assert x == y) vs unittest verboso (self.assertEqual(x, y)). Pytest-cov integra coverage.py mostrando líneas no testeadas. Parallel execution con pytest-xdist acelera suites grandes.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Test suite con 120+ tests: (1) Unit tests tests/unit/ cubren funciones puras (OCR parsing, preprocessing, metrics calculation) con mocks de DB/S3. (2) Integration tests tests/integration/ prueban API endpoints con TestClient de FastAPI y DB test fixture. (3) Model tests tests/model/ validan accuracy >85% en test set, inference time <200ms. Coverage target: >80%. Fixtures: @pytest.fixture setup DB test, seed data, teardown.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Ruff & MyPy
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Ruff & MyPy
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Ruff es linter/formatter ultra-rápido (escrito en Rust) que reemplaza 10+ herramientas (Flake8, Black, isort, pyupgrade). 10-100x faster permite linting en <1 segundo. MyPy es type checker estático que detecta type errors antes de runtime. Type hints mejoran IDE autocomplete y detectan bugs early.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Ruff configurado en pyproject.toml: line-length=100, rules=E,F,W,I (errors, warnings, imports). Auto-fix on save en VSCode. MyPy en modo strict verifica: function signatures match, no implicit Any types, dict key types correctos. Pre-commit hook bloquea commits con lint errors o type mismatches. CI fails si ruff/mypy reportan issues.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Procesamiento de Documentos
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Procesamiento de Documentos
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Tesseract OCR 5.3
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Tesseract OCR 5.3
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Engine OCR open-source más preciso desarrollado por Google con soporte 100+ idiomas. Tesseract 5.x usa LSTM neural networks logrando 10-15% mejor accuracy vs Tesseract 4. Configurable vía flags (--psm, --oem) para diferentes layouts de documentos. Comparado con cloud APIs (AWS Textract $1.50/1000 pages), Tesseract es gratis e ilimitado.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Procesa PDFs convertidos a imágenes PNG (300 DPI via pdf2image). Configuración: --psm 6 (assume single uniform block of text), --oem 1 (LSTM only), -l spa (Spanish). Output: TSV con columnas (level, page_num, block_num, text, conf). Post-processing: filtra palabras con confidence <60%, aplica regex patterns para extraer NIT (\d{9}), fechas (\d{2}/\d{2}/\d{4}), montos ($[\d,]+). Procesa ~200 páginas/hora en CPU 4-core, accuracy ~85% en facturas con calidad media.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # pdf2image + Pillow
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            pdf2image + Pillow
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> pdf2image wrapper de Poppler convierte PDFs multi-página a imágenes PIL. Pillow (Python Imaging Library) librería estándar para manipulación de imágenes con operaciones: resize, rotate, crop, format conversion. Comparado con ImageMagick CLI, Pillow ofrece API Python nativa más fácil de integrar.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Pipeline: PDF → pdf2image convierte a list de PIL Images (300 DPI para preservar calidad OCR) → Pillow preprocessing: convert to grayscale, apply threshold (binarization), deskew si rotación detectada, resize to 224x224 para CNN input. Optimizaciones: JPEG compression quality=85 reduce tamaño 70% con minimal quality loss, max_width=2000px evita imágenes gigantes (>10MB).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Regex (re module)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Regex (re module)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Regular expressions son herramienta fundamental para pattern matching en strings. Python re module compila patterns a bytecode optimizado. Regex permite extraer structured data de texto semi-estructurado (facturas OCR) sin ML complejo. Más rápido y determinístico que NER (Named Entity Recognition) models para casos bien definidos.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Patterns críticos: NIT_PATTERN = r'\b\d{9}\b' (9 dígitos exactos), DATE_PATTERN = r'\b\d{2}/\d{2}/\d{4}\b', AMOUNT_PATTERN = r'\$[\d,]+(?:\.\d{2})?', CITY_PATTERN = r'\b(Bogotá|Medellín|Cali|Barranquilla)\b'. Uso: nit_match = re.search(NIT_PATTERN, ocr_text); nit = nit_match.group() if nit_match else None. Validación: fechas parseadas con datetime, montos convertidos a float después de strip $ y ,.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Monitoreo & Observabilidad
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Monitoreo & Observabilidad
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # CloudWatch Logs Insights
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            CloudWatch Logs Insights
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Query engine SQL-like sobre logs de CloudWatch. Permite análisis ad-hoc sin exportar a herramienta externa (Splunk, ELK). Queries rápidas sobre TBs de logs con auto-complete y visualizaciones. Comparado con grep manual en archivos, Insights escala a millones de log entries y múltiples streams.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Queries comunes: (1) fields @timestamp, @message | filter @message like /ERROR/ | sort @timestamp desc | limit 100 encuentra últimos 100 errores, (2) stats count(*) by bin(5m) muestra requests/5min para detectar spikes, (3) parse @message /latency: (?<latency>\d+)ms/ | stats avg(latency), max(latency), p99(latency) calcula latency percentiles. Dashboards guardan queries frecuentes para monitoreo continuo.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # CloudWatch Alarms
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            CloudWatch Alarms
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Sistema de alertas basado en métricas con acciones automáticas (SNS notifications, auto-scaling, Lambda triggers). Comparado con polling manual, alarms detectan issues inmediatamente. Stateful (OK → ALARM → OK transitions) evita alert fatigue por flapping.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> 8 alarmas configuradas: (1) ecs-cpu-high trigger si CPU >80% por 5 minutos consecutivos → SNS email, (2) alb-5xx-errors trigger si rate >50 errors/min → PagerDuty, (3) rds-connections trigger si connections >90% del max → escala instance size, (4) api-latency-p99 trigger si P99 >2 segundos, (5) drift-detected trigger por custom metric desde DAG. Configuración: evaluation periods, datapoints to alarm, treat missing data as "notBreaching".
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Prometheus + Grafana (opcional local)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            Prometheus + Grafana (opcional local)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Stack de monitoreo open-source estándar en Kubernetes/Docker. Prometheus scrape metrics vía HTTP endpoints, time-series database optimizada para queries rápidas. Grafana dashboards customizables con 100+ datasources. Comparado con CloudWatch (AWS-only), Prometheus es portable y gratis.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Deployment local opcional para development: Prometheus scrapes /metrics endpoint de FastAPI (vía prometheus-fastapi-instrumentator) cada 15s. Métricas expuestas: http_requests_total (counter), http_request_duration_seconds (histogram), active_connections (gauge). Grafana dashboards muestran: request rate, latency percentiles P50/P95/P99, error rate, CPU/memory por container. PromQL queries: rate(http_requests_total[5m]), histogram_quantile(0.95, http_request_duration_seconds).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seguridad
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 2rem 2rem 1rem 2rem;">
        <h2 style="font-size: 2rem; font-weight: 700; color: #1d1d1f; margin-bottom: 1.5rem; letter-spacing: -0.02em;">
            Seguridad
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # AWS IAM (Identity and Access Management)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            AWS IAM (Identity and Access Management)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> Sistema de permisos granulares que sigue principio de least privilege. IAM roles para servicios (vs access keys hardcoded) permiten rotación automática. Policies JSON declarativas versionadas como código en Terraform. IAM Access Analyzer detecta permisos demasiado permisivos.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> 5 roles definidos: (1) ecs-task-role permite ECS tasks leer de S3 (GetObject), escribir logs CloudWatch (PutLogEvents), leer Secrets Manager (GetSecretValue), (2) mwaa-execution-role permite MWAA ejecutar DAGs con acceso a S3/RDS, (3) lambda-drift-role (futuro) para Lambda triggers, (4) rds-monitoring-role para Enhanced Monitoring, (5) ecr-push-role para GitHub Actions push images. Policies: deny s3:DeleteBucket, require MFA para acciones destructivas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # AWS Secrets Manager (detalles adicionales)
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            AWS Secrets Manager (detalles adicionales)
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rotation Lambdas:</strong> Lambda functions automáticas rotan DB passwords cada 30 días sin downtime. RDS connections transparentemente usan nuevo password después de rotación. Secrets versionados con staging labels: AWSCURRENT, AWSPENDING, AWSPREVIOUS.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Encriptación:</strong> Secrets encriptados at rest con AWS KMS (Key Management Service) usando customer managed key. KMS key policy restringe decrypt solo a ECS task role. CloudTrail audita cada GetSecretValue call: quién, cuándo, desde dónde.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # SSL/TLS Certificates
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 0 2rem;">
        <h3 style="font-size: 1.3rem; font-weight: 700; color: #ffffff; background: #1d1d1f; padding: 0.8rem; border-radius: 8px; margin-bottom: 1.5rem; display: inline-block;">
            SSL/TLS Certificates
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="max-width: 1000px; margin: 0 auto; padding: 0 2rem 2rem 2rem;">
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0.8rem;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Justificación:</strong> AWS Certificate Manager (ACM) provee certificados SSL/TLS gratis con renovación automática. Validación DNS vía Route 53 automatizada completamente. Comparado con Let's Encrypt self-managed, ACM elimina operational burden de renovaciones manuales cada 90 días.
        </p>
        <p style="font-size: 1.05rem; color: #1d1d1f; line-height: 1.8; margin-bottom: 0;">
            <strong style="font-weight: 800; color: #ffffff; background: #000000; padding: 0.3rem 0.6rem; border-radius: 4px; text-shadow: 1px 1px 2px rgba(0,0,0,0.3); display: inline-block; margin-right: 0.5rem;">Rol en el proyecto:</strong> Certificado wildcard *.etl-facturas.com attached a ALB listener HTTPS (puerto 443). Redirect automático HTTP (80) → HTTPS. TLS 1.2+ enforced, cipher suites modernos (ECDHE-RSA-AES128-GCM-SHA256). Certificate transparency logs públicos permiten auditoría.
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
    </div>
    """, unsafe_allow_html=True)
