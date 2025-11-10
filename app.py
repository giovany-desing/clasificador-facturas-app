import streamlit as st
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
    
    /* Tabs estilo macOS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: rgba(0, 0, 0, 0.03);
        border-radius: 12px;
        padding: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 500;
        color: #a1a1a6;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        border: none;
        background: transparent;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        color: #86868b;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
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
    
    /* Tabs text más visible */
    .stTabs [data-baseweb="tab"] {
        color: #a1a1a6 !important;
    }
    
    .stTabs [aria-selected="true"] {
        color: #86868b !important;
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
</style>
""", unsafe_allow_html=True)

# --- FUNCIÓN PARA CARGAR IMÁGENES ---
def load_image(image_path):
    """Carga una imagen de forma segura con múltiples intentos de ruta"""
    possible_paths = [
        image_path,
        Path(image_path),
        Path(__file__).parent / image_path,
        Path.cwd() / image_path,
    ]
    
    for path in possible_paths:
        try:
            if Path(path).exists():
                return Image.open(path)
        except Exception as e:
            continue
    
    st.error(f"""
    ⚠️ **Image not found:** `{image_path}`
    
    **Paths tried:**
    - `{Path.cwd() / image_path}`
    - `{Path(__file__).parent / image_path}`
    
    **Please ensure:**
    - File exists in the same folder as `app.py`
    - Filename matches exactly (case-sensitive)
    - File is a valid image (.png, .jpg, etc.)
    """)
    return None

# =========================================
# SIDEBAR ESTILO APPLE
# =========================================
with st.sidebar:
    # Avatar con efecto
    st.markdown("#### 🛠️ Stack Tecnologico")
    
    technologies = {
        "🐍 Python": ["google apis" , "Git", "pdf2image","matplotlib"],
        "🤖 Red Neuronal": ["TensorFlow", "Keras", "OpenCV", "Tesseract"],
        "⚡ Backend": ["FastAPI", "Uvicorn"],
        "💾 Data": ["SQLserver", "pyodbc", "Pandas", "NumPy"],
        "☁️ Cloud": ["GCP", "Docker", "Cloud Scheduler", "Cloud Run"],
        "📊 BI": ["Power BI"]
    }
    
    for category, techs in technologies.items():
        with st.expander(category, expanded=False):
            for tech in techs:
                st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)

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
st.markdown('<h1 class="hero-subtitle">Sistema de Clasificación de facturas y extracción de información mediante reconocimiento optico de caracteres</h1>', unsafe_allow_html=True)

# Métricas estilo Apple Watch
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">98%</div>
            <div class="metric-label">Model Acuraccy</div>
        </div>
    """, unsafe_allow_html=True)
with col_m2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">95%</div>
            <div class="metric-label">OCR Accuracy</div>
        </div>
    """, unsafe_allow_html=True)
with col_m3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">100%</div>
            <div class="metric-label">Pipeline Automatizado de procesamiento de facturas</div>
        </div>
    """, unsafe_allow_html=True)
with col_m4:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-value">100%</div>
            <div class="metric-label">Pipeline Automatizado entrenamiento del modelo</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Content en glass cards
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    ### Desafío de Negocio: Automatización Crítica en la Gestión Documental
    
    Una empresa en expansión del sector textil enfrenta un cuello de botella operativo significativo en el procesamiento de sus facturas en formato PDF. El método actual, basado en la clasificación y almacenamiento manual en Google Drive por parte del equipo administrativo, se ha vuelto insostenible debido al creciente volumen de transacciones.
    
    **Necesidad Específica:**
    - **Facturas de Materia Prima (Preventivas):** Esenciales para la cadena de suministro y producción.
    - **Facturas de Productos Terminados (Correctivas):** Destinadas a almacenes y puntos de venta.
    
    Esta automatización no solo liberará horas de operacion valiosas, sino que también reducirá errores humanos, agilizará el flujo de caja y mejorará la visibilidad financiera de la compañía.**.
    """)

with col2:
    st.info("""
    **🎯 ¡Importante!**
    
    **Este proyecto se desarrolló mediante reglas de negocio e historias de usuario establecidas por el cliente, lo que lo hace totalmente personalizado y funcional a largo plazo teniendo en cuenta el crecimiento de la facturación.**

    """)

# =========================================
# FLOW
# =========================================
st.markdown('<h2 class="sub-header">Implementación del Flow</h2>', unsafe_allow_html=True)

st.markdown("""
En la siguiente imagen se evidencia del como se realiza el pipeline o flow de procesamiento totalmente atomatizado:
""")

# Cargar imagen con efecto premium
pipeline_img = load_image("image_2c0120.png")
if pipeline_img:
    st.image(pipeline_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)



# =========================================
# FLOW TRAIN
# =========================================
st.markdown('<h2 class="sub-header">Flow de entrenamiento</h2>', unsafe_allow_html=True)

st.markdown("""
El Flow o pipeline de entrenamiento esta diseñado para que se haga de manera automatica sin intervención humana
""")

# Cargar imagen con efecto premium
pipeline_img = load_image("train_image.png")
if pipeline_img:
    st.image(pipeline_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


# =========================================
# DISTRIBUCION DE ARCHIVOS
# =========================================
st.markdown('<h2 class="sub-header">Distribución De Software</h2>', unsafe_allow_html=True)
st.markdown("""
La distribución de archivos Python queda de la siguiente manera:
""")

pipeline_img = load_image("software.png")
if pipeline_img:
    st.image(pipeline_img, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('''
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://github.com/giovany-desing/clasificador-facturas" target="_blank" class="github-button">
        🔗 Ver Código en GitHub
    </a>
</div>
''', unsafe_allow_html=True)
# =========================================
# MANUAL DE DESPLIEGUE
# =========================================
st.markdown('<h2 class="sub-header">Manual de despliegue</h2>', unsafe_allow_html=True)
st.markdown("""
    ### En la terminal de bash en local se deben ejecutar los siguientes comandos:
    
    
    **Prerrequisitos:**
    - **1. Google Cloud SDK instalado y configurado:** Se debe instalar y configurar segun el proyecto en la nube   
    - **2. Docker instalado:** Para desplegar el contenedor y hacer testeos en local
    - **3. Cuenta de Google Cloud :** Para interactuar con los servicios de google
    - **4. Permisos a GCP de usuario y cuenta de serivcio activa**
             
    **Paso 1 Ejecutar en bash:**
    - 1. gcloud auth login -- Iniciar sesión en GCP
    - 2. gcloud config set project TU_PROYECTO_ID -- Configurar proyecto
    - 3. gcloud services enable containerregistry.googleapis.com -- Habilitar Api necesaria
    
    **Paso 2Construir y subir la imagen Docker**
    - 1. docker build -t gcr.io/TU_PROYECTO_ID/clasificador-facturas:latest . -- Construir la imagen de docker
    - 2. docker push gcr.io/TU_PROYECTO_ID/clasificador-facturas:latest -- Subir a Container Registry
    
    **Paso 3 Desplegar en Cloud Run**
    
    gcloud run deploy clasificador-facturas \
  --image gcr.io/TU_PROYECTO_ID/clasificador-facturas:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi \
  --cpu 2
    
    """)


# =========================================
# KEY COMPETENCIES
# =========================================
st.markdown('<h2 class="sub-header">En este proyecto quiero mostrar mis habilidades en:</h2>', unsafe_allow_html=True)

col_comp1, col_comp2, col_comp3, col_comp4 = st.columns(4)

with col_comp1:
    st.markdown("""
    **🤖 Machine Learning & AI**
    - TensorFlow/Keras: Modelos de deep learning
    - Procesamiento de documentos (PDF)
    - Expresiones regulares para extracción de datos
    - Preprocesamiento de datos para ML
    """)

with col_comp2:
    st.markdown("""
    ⚙️ Desarrollo de APIs 
    - REST API (FastAPI)
    - Procesamiento asíncrono en lotes (batch processing)
    - Manejo de pipelines de datos
    - Arquitectura modular y mantenible
    """)

with col_comp3:
    st.markdown("""
    **☁️ Contenerización & DevOps**
    - Docker: Empaquetado de aplicaciones
    - Docker Compose: Orquestación de contenedores locales
    - CI/CD implícito con despliegues automatizados
    - MLOps workflows
    - Gestión de dependencias y entornos
    """)
with col_comp4:
    st.markdown("""
    Bases de Datos & Almacenamiento
    - SQL Server (bases de datos relacionales)
    - Google Drive API como sistema de archivos
    - Expresiones regulares para extracción de datos
    - Integración con múltiples fuentes de datos
    """)


# =========================================
# FOOTER
# =========================================
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.markdown('<p class="caption-text">© 2023 - Edgar Yovany Samaca Acuña</p>', unsafe_allow_html=True)
with col_footer2:
    st.markdown('<p class="caption-text" style="text-align: center;"></p>', unsafe_allow_html=True)
with col_footer3:
    st.markdown('<p class="caption-text" style="text-align: right;">Last update: Nov 2025</p>', unsafe_allow_html=True)