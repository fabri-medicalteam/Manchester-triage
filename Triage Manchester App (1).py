import streamlit as st

# Page config
st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# TELEPATIA DESIGN SYSTEM CSS
# ============================================================================
st.markdown("""
<style>
    /* ===== TELEPATIA DESIGN TOKENS ===== */
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
    
    :root {
        /* Olive (Primary) */
        --olive-50: #F6F7F5;
        --olive-100: #E8EBE6;
        --olive-200: #D1D7CD;
        --olive-300: #B0BAA8;
        --olive-400: #8A9A7D;
        --olive-500: #6B7D5E;
        --olive-600: #556349;
        --olive-700: #4C6444;
        --olive-800: #3D4F37;
        --olive-900: #34422F;
        
        /* Gray */
        --gray-50: #FAFAFA;
        --gray-100: #F5F5F5;
        --gray-200: #E5E5E5;
        --gray-300: #D4D4D4;
        --gray-400: #A3A3A3;
        --gray-500: #737373;
        --gray-600: #525252;
        --gray-700: #404040;
        --gray-800: #262626;
        --gray-900: #171717;
        --gray-1000: #0A0A0A;
        
        /* Semantic Colors */
        --success: #22C55E;
        --warning: #EAB308;
        --error: #DC2626;
        --info: #3B82F6;
        
        /* Brand Gradient */
        --brand-gradient: linear-gradient(135deg, #4C6444 0%, #006B3F 100%);
        
        /* Shadows */
        --elevation-1: 0 4px 4px rgba(0, 0, 0, 0.05);
        --elevation-2: 0 4px 12px rgba(0, 0, 0, 0.2);
        --divider: 0 4px 4px rgba(0, 0, 0, 0.04);
        
        /* Border Radius */
        --radius-100: 4px;
        --radius-200: 8px;
        --radius-300: 12px;
        --radius-400: 16px;
        --radius-600: 24px;
        --radius-800: 32px;
        --radius-pill: 999px;
    }
    
    * { 
        font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif !important; 
    }
    
    /* ===== HEADER ===== */
    .telepatia-header {
        background: white;
        padding: 16px 24px;
        border-radius: var(--radius-300);
        box-shadow: var(--elevation-1);
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .telepatia-logo {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .telepatia-logo-icon {
        width: 40px;
        height: 40px;
        background: var(--brand-gradient);
        border-radius: var(--radius-200);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 20px;
        font-weight: 700;
    }
    
    .telepatia-logo-text {
        font-size: 24px;
        font-weight: 600;
        background: var(--brand-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .telepatia-subtitle {
        color: var(--gray-500);
        font-size: 14px;
        font-weight: 400;
        margin-left: 16px;
        padding-left: 16px;
        border-left: 1px solid var(--gray-200);
    }
    
    /* ===== RESULT BANNER ===== */
    .result-banner {
        padding: 16px 20px;
        border-radius: var(--radius-300);
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: var(--elevation-1);
    }
    
    .result-banner-left {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    
    .result-title {
        font-size: 24px;
        font-weight: 700;
    }
    
    .result-subtitle {
        font-size: 14px;
        font-weight: 400;
        opacity: 0.7;
    }
    
    .result-time {
        font-size: 28px;
        font-weight: 700;
    }
    
    .result-discriminators {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 4px;
    }
    
    /* Priority-specific banner colors */
    .banner-immediate { 
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
        border-left: 4px solid #DC2626;
    }
    .banner-immediate .result-title, .banner-immediate .result-time { color: #991B1B; }
    .banner-immediate .result-subtitle { color: #B91C1C; }
    
    .banner-very_urgent { 
        background: linear-gradient(135deg, #FFEDD5 0%, #FED7AA 100%);
        border-left: 4px solid #EA580C;
    }
    .banner-very_urgent .result-title, .banner-very_urgent .result-time { color: #9A3412; }
    .banner-very_urgent .result-subtitle { color: #C2410C; }
    
    .banner-urgent { 
        background: linear-gradient(135deg, #FEF9C3 0%, #FEF08A 100%);
        border-left: 4px solid #EAB308;
    }
    .banner-urgent .result-title, .banner-urgent .result-time { color: #854D0E; }
    .banner-urgent .result-subtitle { color: #A16207; }
    
    .banner-standard { 
        background: linear-gradient(135deg, #DCFCE7 0%, #BBF7D0 100%);
        border-left: 4px solid #22C55E;
    }
    .banner-standard .result-title, .banner-standard .result-time { color: #166534; }
    .banner-standard .result-subtitle { color: #15803D; }
    
    .banner-non_urgent { 
        background: linear-gradient(135deg, #DBEAFE 0%, #BFDBFE 100%);
        border-left: 4px solid #3B82F6;
    }
    .banner-non_urgent .result-title, .banner-non_urgent .result-time { color: #1E40AF; }
    .banner-non_urgent .result-subtitle { color: #1D4ED8; }
    
    /* ===== BADGES (Telepatia Style) ===== */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 10px;
        border-radius: var(--radius-pill);
        font-size: 12px;
        font-weight: 500;
    }
    
    .badge-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
    }
    
    /* Filled badges */
    .badge-immediate { background: #DC2626; color: white; }
    .badge-immediate .badge-dot { background: #FEE2E2; }
    
    .badge-very_urgent { background: #EA580C; color: white; }
    .badge-very_urgent .badge-dot { background: #FFEDD5; }
    
    .badge-urgent { background: #EAB308; color: #422006; }
    .badge-urgent .badge-dot { background: #854D0E; }
    
    .badge-standard { background: #22C55E; color: white; }
    .badge-standard .badge-dot { background: #DCFCE7; }
    
    .badge-non_urgent { background: #3B82F6; color: white; }
    .badge-non_urgent .badge-dot { background: #DBEAFE; }
    
    /* Outline badges */
    .badge-outline-immediate { background: #FEE2E2; color: #991B1B; border: 1px solid #FECACA; }
    .badge-outline-immediate .badge-dot { background: #DC2626; }
    
    .badge-outline-very_urgent { background: #FFEDD5; color: #9A3412; border: 1px solid #FED7AA; }
    .badge-outline-very_urgent .badge-dot { background: #EA580C; }
    
    .badge-outline-urgent { background: #FEF9C3; color: #854D0E; border: 1px solid #FEF08A; }
    .badge-outline-urgent .badge-dot { background: #EAB308; }
    
    .badge-outline-standard { background: #DCFCE7; color: #166534; border: 1px solid #BBF7D0; }
    .badge-outline-standard .badge-dot { background: #22C55E; }
    
    .badge-outline-non_urgent { background: #DBEAFE; color: #1E40AF; border: 1px solid #BFDBFE; }
    .badge-outline-non_urgent .badge-dot { background: #3B82F6; }
    
    /* ===== CARDS ===== */
    .telepatia-card {
        background: white;
        border-radius: var(--radius-300);
        padding: 20px;
        box-shadow: var(--elevation-1);
        border: 1px solid var(--gray-100);
    }
    
    .card-title {
        font-size: 16px;
        font-weight: 600;
        color: var(--gray-900);
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* ===== SECTION HEADERS ===== */
    .section-header {
        font-size: 14px;
        font-weight: 600;
        color: var(--gray-700);
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* ===== PRIORITY LEGEND ===== */
    .priority-legend {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        padding: 16px;
        background: var(--gray-50);
        border-radius: var(--radius-200);
        margin-top: 20px;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        background: white;
        border-radius: var(--radius-200);
        box-shadow: var(--elevation-1);
    }
    
    .legend-color {
        width: 4px;
        height: 32px;
        border-radius: 2px;
    }
    
    .legend-text {
        display: flex;
        flex-direction: column;
    }
    
    .legend-label {
        font-size: 12px;
        font-weight: 600;
    }
    
    .legend-time {
        font-size: 11px;
        color: var(--gray-500);
    }
    
    /* ===== SAFETY WARNING (Telepatia Banner Style) ===== */
    .safety-banner {
        background: var(--gray-900);
        color: white;
        padding: 16px 20px;
        border-radius: var(--radius-300);
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 20px 0;
    }
    
    .safety-banner-icon {
        width: 32px;
        height: 32px;
        background: var(--olive-600);
        border-radius: var(--radius-200);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }
    
    .safety-banner-text {
        flex: 1;
    }
    
    .safety-banner-title {
        font-weight: 600;
        font-size: 14px;
    }
    
    .safety-banner-desc {
        font-size: 13px;
        opacity: 0.8;
        margin-top: 2px;
    }
    
    /* ===== FOOTER ===== */
    .telepatia-footer {
        background: var(--gray-50);
        border-radius: var(--radius-200);
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        color: var(--gray-600);
        font-size: 13px;
    }
    
    .telepatia-footer strong {
        color: var(--gray-800);
    }
    
    /* ===== DISCRIMINATOR LIST ===== */
    .discriminator-group {
        margin-bottom: 20px;
    }
    
    .discriminator-group-header {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid var(--gray-200);
    }
    
    .discriminator-item {
        padding: 12px 16px;
        border-radius: var(--radius-200);
        margin-bottom: 8px;
        background: var(--gray-50);
        border: 1px solid var(--gray-200);
        transition: all 0.2s ease;
    }
    
    .discriminator-item:hover {
        background: white;
        box-shadow: var(--elevation-1);
    }
    
    .discriminator-question {
        font-weight: 500;
        color: var(--gray-900);
        margin-bottom: 4px;
    }
    
    .discriminator-desc {
        font-size: 13px;
        color: var(--gray-500);
    }
    
    /* ===== FLOWCHART SELECTOR ===== */
    .flowchart-btn {
        padding: 12px 16px;
        border-radius: var(--radius-200);
        border: 1.5px solid var(--gray-200);
        background: white;
        cursor: pointer;
        transition: all 0.2s ease;
        text-align: left;
        width: 100%;
        margin-bottom: 8px;
    }
    
    .flowchart-btn:hover {
        border-color: var(--olive-500);
        background: var(--olive-50);
    }
    
    .flowchart-btn.active {
        border-color: var(--olive-700);
        background: var(--olive-50);
        box-shadow: 0 0 0 3px rgba(76, 100, 68, 0.1);
    }
    
    .flowchart-btn-icon {
        font-size: 20px;
        margin-right: 8px;
    }
    
    .flowchart-btn-text {
        font-weight: 500;
        color: var(--gray-800);
    }
    
    /* ===== HIDE STREAMLIT DEFAULTS ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* ===== CUSTOM TABS ===== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--gray-100);
        padding: 4px;
        border-radius: var(--radius-200);
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-100);
        padding: 8px 16px;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background: white !important;
        box-shadow: var(--elevation-1);
    }
    
    /* ===== STREAMLIT COMPONENTS OVERRIDE ===== */
    .stSelectbox > div > div {
        border-radius: var(--radius-200) !important;
        border-color: var(--gray-200) !important;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: var(--olive-500) !important;
        box-shadow: 0 0 0 3px rgba(76, 100, 68, 0.1) !important;
    }
    
    .stSlider > div > div > div {
        background: var(--olive-500) !important;
    }
    
    .stRadio > div {
        gap: 8px !important;
    }
    
    .stRadio label {
        padding: 8px 16px !important;
        border-radius: var(--radius-200) !important;
        border: 1.5px solid var(--gray-200) !important;
        background: white !important;
    }
    
    .stRadio label:has(input:checked) {
        border-color: var(--olive-600) !important;
        background: var(--olive-50) !important;
    }
    
    .stCheckbox label {
        font-size: 14px;
    }
    
    .stButton > button {
        border-radius: var(--radius-200) !important;
        font-weight: 500 !important;
        padding: 8px 20px !important;
    }
    
    .stButton > button[kind="primary"] {
        background: var(--brand-gradient) !important;
        border: none !important;
    }
    
    .stButton > button[kind="secondary"] {
        border: 1.5px solid var(--gray-200) !important;
        background: white !important;
        color: var(--gray-700) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# PRIORITY CONFIGURATION
# ============================================================================
PRIORITIES = {
    'immediate': {'color': '#DC2626', 'label': 'IMEDIATO', 'label_en': 'IMMEDIATE', 'time': '0 min', 'bg': '#FEE2E2', 'text': '#991B1B'},
    'very_urgent': {'color': '#EA580C', 'label': 'MUITO URGENTE', 'label_en': 'VERY URGENT', 'time': '10 min', 'bg': '#FFEDD5', 'text': '#9A3412'},
    'urgent': {'color': '#EAB308', 'label': 'URGENTE', 'label_en': 'URGENT', 'time': '60 min', 'bg': '#FEF9C3', 'text': '#854D0E'},
    'standard': {'color': '#22C55E', 'label': 'PADRÃO', 'label_en': 'STANDARD', 'time': '120 min', 'bg': '#DCFCE7', 'text': '#166534'},
    'non_urgent': {'color': '#3B82F6', 'label': 'NÃO URGENTE', 'label_en': 'NON-URGENT', 'time': '240 min', 'bg': '#DBEAFE', 'text': '#1E40AF'}
}

PRIORITY_ORDER = ['immediate', 'very_urgent', 'urgent', 'standard', 'non_urgent']

# ============================================================================
# TOP 10 FLOWCHARTS WITH SPECIFIC DISCRIMINATORS
# ============================================================================
FLOWCHARTS = {
    'headache': {
        'name': 'Cefaleia',
        'name_en': 'Headache',
        'icon': '🤕',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, incapacidade de manter VA pérvia', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, uso musculatura acessória, cianose', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco, hipotensão', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Movimentos tônico-clônicos', 'critical': True},
            {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'GCS <15, confusão, letargia', 'critical': True},
            {'id': 'focal_deficit', 'priority': 'very_urgent', 'question': 'Déficit neurológico focal?', 'desc': 'Hemiparesia, afasia, alt. visual súbita', 'critical': True},
            {'id': 'meningism', 'priority': 'very_urgent', 'question': 'Sinais de meningismo?', 'desc': 'Rigidez nuca, fotofobia, Kernig/Brudzinski', 'critical': True},
            {'id': 'thunderclap', 'priority': 'very_urgent', 'question': 'Cefaleia súbita intensa (thunderclap)?', 'desc': '"Pior dor da vida", início segundos/min', 'critical': True},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'purpura', 'priority': 'very_urgent', 'question': 'Púrpura/petéquias?', 'desc': 'Manchas não somem à pressão', 'critical': True},
            {'id': 'very_hot', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Interfere nas atividades', 'critical': False},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'vomiting', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Múltiplos episódios', 'critical': False},
            {'id': 'syncope', 'priority': 'urgent', 'question': 'História de síncope?', 'desc': 'Perda consciência prévia', 'critical': False},
            {'id': 'acute_onset', 'priority': 'urgent', 'question': 'Início agudo (<12h)?', 'desc': 'Nas últimas 12 horas', 'critical': False},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'recent', 'priority': 'standard', 'question': 'Problema recente (<7 dias)?', 'desc': 'Última semana', 'critical': False},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Cefaleia usual, sem mudança', 'critical': False},
        ]
    },
    'chest_pain': {
        'name': 'Dor Torácica',
        'name_en': 'Chest Pain',
        'icon': '💔',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução ou incapacidade de manter VA', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, esforço respiratório grave', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria, pulso fraco', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'cardiac_pain', 'priority': 'very_urgent', 'question': 'Dor cardíaca típica?', 'desc': 'Dor precordial, opressão, irradiação MSE/mandíbula', 'critical': True},
            {'id': 'acute_sob', 'priority': 'very_urgent', 'question': 'Dispneia aguda?', 'desc': 'Falta de ar de início súbito', 'critical': True},
            {'id': 'abnormal_pulse', 'priority': 'very_urgent', 'question': 'Pulso anormal?', 'desc': 'Muito rápido, muito lento ou irregular', 'critical': True},
            {'id': 'severe_pain_chest', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'very_hot_chest', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'acutely_sob', 'priority': 'very_urgent', 'question': 'Baixa saturação com O₂?', 'desc': 'SpO₂ <95% mesmo com oxigênio', 'critical': True},
            {'id': 'pleuritic', 'priority': 'urgent', 'question': 'Dor pleurítica?', 'desc': 'Dor que piora com respiração', 'critical': False},
            {'id': 'moderate_pain_chest', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'hx_cardiac', 'priority': 'urgent', 'question': 'História cardíaca?', 'desc': 'IAM prévio, angina, stent, cirurgia', 'critical': False},
            {'id': 'hot_chest', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'mild_pain_chest', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'warm_chest', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'chronic_chest', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dor torácica habitual', 'critical': False},
        ]
    },
    'abdominal_pain': {
        'name': 'Dor Abdominal',
        'name_en': 'Abdominal Pain',
        'icon': '🤢',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução ou incapacidade de manter VA', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria, pulso fraco', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'severe_haemorrhage', 'priority': 'immediate', 'question': 'Hemorragia grave?', 'desc': 'Hematêmese volumosa, melena', 'critical': True},
            {'id': 'severe_pain_abd', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'peritonism', 'priority': 'very_urgent', 'question': 'Sinais de peritonismo?', 'desc': 'Rigidez, descompressão +, abdome em tábua', 'critical': True},
            {'id': 'very_hot_abd', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'black_stool', 'priority': 'very_urgent', 'question': 'Fezes escuras/sangue vivo?', 'desc': 'Melena ou hematoquezia', 'critical': True},
            {'id': 'persistent_vomit', 'priority': 'very_urgent', 'question': 'Vômitos persistentes?', 'desc': 'Incapaz de tolerar líquidos', 'critical': False},
            {'id': 'moderate_pain_abd', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'hot_abd', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'vomiting_abd', 'priority': 'urgent', 'question': 'Vômitos?', 'desc': 'Episódios de vômito', 'critical': False},
            {'id': 'pregnancy', 'priority': 'urgent', 'question': 'Possível gravidez?', 'desc': 'Em idade fértil, amenorreia', 'critical': False},
            {'id': 'mild_pain_abd', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'warm_abd', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'chronic_abd', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dor abdominal habitual', 'critical': False},
        ]
    },
    'shortness_of_breath': {
        'name': 'Dispneia',
        'name_en': 'Shortness of Breath',
        'icon': '😮‍💨',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, estridor, incapacidade de falar', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, cianose central', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'low_spo2', 'priority': 'very_urgent', 'question': 'SpO₂ <95% em ar ambiente?', 'desc': 'Saturação baixa', 'critical': True},
            {'id': 'unable_speak', 'priority': 'very_urgent', 'question': 'Incapaz de completar frases?', 'desc': 'Fala entrecortada', 'critical': True},
            {'id': 'stridor', 'priority': 'very_urgent', 'question': 'Estridor?', 'desc': 'Som inspiratório agudo', 'critical': True},
            {'id': 'severe_wheeze', 'priority': 'very_urgent', 'question': 'Sibilância grave?', 'desc': 'Audível à distância', 'critical': True},
            {'id': 'very_hot_sob', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'moderate_wheeze', 'priority': 'urgent', 'question': 'Sibilância moderada?', 'desc': 'Broncoespasmo', 'critical': False},
            {'id': 'pleuritic_sob', 'priority': 'urgent', 'question': 'Dor pleurítica?', 'desc': 'Dor ao respirar', 'critical': False},
            {'id': 'hot_sob', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'productive_cough', 'priority': 'urgent', 'question': 'Tosse produtiva?', 'desc': 'Expectoração', 'critical': False},
            {'id': 'warm_sob', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'chronic_sob', 'priority': 'standard', 'question': 'Dispneia de esforço?', 'desc': 'Aos esforços moderados', 'critical': False},
            {'id': 'non_urgent_sob', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dispneia habitual', 'critical': False},
        ]
    },
    'unwell_adult': {
        'name': 'Indisposição no Adulto',
        'name_en': 'Unwell Adult',
        'icon': '🤒',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'altered_consciousness_uw', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, letargia', 'critical': True},
            {'id': 'very_hot_uw', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'very_cold_uw', 'priority': 'very_urgent', 'question': 'Temp ≤35°C?', 'desc': 'Hipotermia', 'critical': True},
            {'id': 'purpura_uw', 'priority': 'very_urgent', 'question': 'Púrpura/petéquias?', 'desc': 'Não somem à pressão', 'critical': True},
            {'id': 'severe_pain_uw', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'hot_uw', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'moderate_pain_uw', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'persistent_vomit_uw', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Múltiplos episódios', 'critical': False},
            {'id': 'warm_uw', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'mild_pain_uw', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'recent_uw', 'priority': 'standard', 'question': 'Problema recente (<7 dias)?', 'desc': 'Última semana', 'critical': False},
            {'id': 'chronic_uw', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Sintomas habituais', 'critical': False},
        ]
    },
    'limb_problems': {
        'name': 'Problemas em Membros',
        'name_en': 'Limb Problems',
        'icon': '🦵',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hemorragia grave, hipotensão', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'no_pulse', 'priority': 'very_urgent', 'question': 'Ausência de pulso distal?', 'desc': 'Membro frio, sem pulso', 'critical': True},
            {'id': 'open_fracture', 'priority': 'very_urgent', 'question': 'Fratura exposta?', 'desc': 'Osso visível', 'critical': True},
            {'id': 'deformity', 'priority': 'very_urgent', 'question': 'Deformidade grosseira?', 'desc': 'Angulação anormal', 'critical': True},
            {'id': 'severe_pain_limb', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'compartment', 'priority': 'very_urgent', 'question': 'Sinais de síndrome compartimental?', 'desc': 'Dor desproporcional, parestesia', 'critical': True},
            {'id': 'moderate_pain_limb', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'unable_weight', 'priority': 'urgent', 'question': 'Incapaz de apoiar peso?', 'desc': 'Não consegue andar', 'critical': False},
            {'id': 'swelling', 'priority': 'urgent', 'question': 'Edema significativo?', 'desc': 'Inchaço importante', 'critical': False},
            {'id': 'hot_limb', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'mild_pain_limb', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'warm_limb', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'recent_limb', 'priority': 'standard', 'question': 'Problema recente (<7 dias)?', 'desc': 'Última semana', 'critical': False},
            {'id': 'chronic_limb', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dor habitual', 'critical': False},
        ]
    },
    'wounds': {
        'name': 'Feridas',
        'name_en': 'Wounds',
        'icon': '🩹',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Ferida em pescoço com obstrução', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'Ferida torácica aspirativa', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Hemorragia grave/choque?', 'desc': 'Sangramento arterial, hipotensão', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'active_bleeding', 'priority': 'very_urgent', 'question': 'Sangramento ativo não controlado?', 'desc': 'Não cede com pressão', 'critical': True},
            {'id': 'amputation', 'priority': 'very_urgent', 'question': 'Amputação?', 'desc': 'Perda de parte do corpo', 'critical': True},
            {'id': 'tendon_nerve', 'priority': 'very_urgent', 'question': 'Lesão de tendão/nervo/vaso?', 'desc': 'Déficit motor/sensitivo, sangramento pulsátil', 'critical': True},
            {'id': 'severe_pain_wound', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'deep_wound', 'priority': 'urgent', 'question': 'Ferida profunda?', 'desc': 'Exposição de estruturas', 'critical': False},
            {'id': 'contaminated', 'priority': 'urgent', 'question': 'Ferida contaminada?', 'desc': 'Sujeira, mordida, material orgânico', 'critical': False},
            {'id': 'moderate_pain_wound', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'needs_suture', 'priority': 'urgent', 'question': 'Necessita sutura?', 'desc': 'Bordas separadas', 'critical': False},
            {'id': 'mild_pain_wound', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'superficial', 'priority': 'standard', 'question': 'Ferida superficial?', 'desc': 'Abrasão, corte superficial', 'critical': False},
            {'id': 'recent_wound', 'priority': 'standard', 'question': 'Ferida recente (<12h)?', 'desc': 'Nas últimas 12 horas', 'critical': False},
            {'id': 'chronic_wound', 'priority': 'non_urgent', 'question': 'Ferida crônica para avaliação?', 'desc': 'Úlcera, ferida antiga', 'critical': False},
        ]
    },
    'falls': {
        'name': 'Quedas',
        'name_en': 'Falls',
        'icon': '⬇️',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'altered_consciousness_fall', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, letargia pós-queda', 'critical': True},
            {'id': 'focal_deficit_fall', 'priority': 'very_urgent', 'question': 'Déficit neurológico?', 'desc': 'Fraqueza, formigamento', 'critical': True},
            {'id': 'spine_pain', 'priority': 'very_urgent', 'question': 'Dor na coluna?', 'desc': 'Dor cervical/lombar pós-trauma', 'critical': True},
            {'id': 'severe_pain_fall', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'deformity_fall', 'priority': 'very_urgent', 'question': 'Deformidade?', 'desc': 'Angulação, encurtamento', 'critical': True},
            {'id': 'anticoag', 'priority': 'very_urgent', 'question': 'Uso de anticoagulante + TCE?', 'desc': 'Warfarina, DOACs, + trauma crânio', 'critical': True},
            {'id': 'hip_pain', 'priority': 'urgent', 'question': 'Dor no quadril?', 'desc': 'Incapaz de movimentar', 'critical': False},
            {'id': 'moderate_pain_fall', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'unable_walk', 'priority': 'urgent', 'question': 'Incapaz de deambular?', 'desc': 'Não consegue andar', 'critical': False},
            {'id': 'head_injury', 'priority': 'urgent', 'question': 'Trauma craniano?', 'desc': 'Bateu a cabeça', 'critical': False},
            {'id': 'mild_pain_fall', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'abrasions', 'priority': 'standard', 'question': 'Apenas escoriações?', 'desc': 'Ferimentos superficiais', 'critical': False},
            {'id': 'walking', 'priority': 'standard', 'question': 'Deambulando normalmente?', 'desc': 'Sem dificuldade para andar', 'critical': False},
            {'id': 'chronic_fall', 'priority': 'non_urgent', 'question': 'Avaliação de quedas recorrentes?', 'desc': 'Investigação de causas', 'critical': False},
        ]
    },
    'vomiting': {
        'name': 'Vômitos',
        'name_en': 'Vomiting',
        'icon': '🤮',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução por vômito', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Desidratação grave, hipotensão', 'critical': True},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
            {'id': 'haematemesis', 'priority': 'very_urgent', 'question': 'Hematêmese?', 'desc': 'Vômito com sangue vivo', 'critical': True},
            {'id': 'coffee_ground', 'priority': 'very_urgent', 'question': 'Vômito em borra de café?', 'desc': 'Sangue digerido', 'critical': True},
            {'id': 'severe_dehydration', 'priority': 'very_urgent', 'question': 'Desidratação grave?', 'desc': 'Olhos fundos, pele seca, letargia', 'critical': True},
            {'id': 'very_hot_vom', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave', 'critical': True},
            {'id': 'severe_pain_vom', 'priority': 'very_urgent', 'question': 'Dor abdominal intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
            {'id': 'moderate_dehydration', 'priority': 'urgent', 'question': 'Desidratação moderada?', 'desc': 'Sede, oligúria, mucosas secas', 'critical': False},
            {'id': 'persistent_vom', 'priority': 'urgent', 'question': 'Vômitos persistentes (>24h)?', 'desc': 'Incapaz de tolerar líquidos', 'critical': False},
            {'id': 'hot_vom', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
            {'id': 'moderate_pain_vom', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
            {'id': 'warm_vom', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula', 'critical': False},
            {'id': 'mild_vom', 'priority': 'standard', 'question': 'Vômitos ocasionais?', 'desc': 'Tolerando líquidos', 'critical': False},
            {'id': 'mild_pain_vom', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Desconforto tolerável', 'critical': False},
            {'id': 'chronic_vom', 'priority': 'non_urgent', 'question': 'Problema crônico para avaliação?', 'desc': 'Náuseas recorrentes', 'critical': False},
        ]
    },
    'head_injury': {
        'name': 'TCE - Trauma Cranioencefálico',
        'name_en': 'Head Injury',
        'icon': '🤕',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30', 'critical': True},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria', 'critical': True},
            {'id': 'unresponsive_tce', 'priority': 'immediate', 'question': 'Não responsivo (GCS ≤8)?', 'desc': 'AVPU = U ou GCS ≤8', 'critical': True},
            {'id': 'seizure_tce', 'priority': 'immediate', 'question': 'Convulsão pós-trauma?', 'desc': 'Crise convulsiva', 'critical': True},
            {'id': 'altered_consciousness_tce', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'GCS 9-14, confusão', 'critical': True},
            {'id': 'focal_deficit_tce', 'priority': 'very_urgent', 'question': 'Déficit neurológico focal?', 'desc': 'Hemiparesia, anisocoria', 'critical': True},
            {'id': 'skull_fracture', 'priority': 'very_urgent', 'question': 'Sinais de fratura de crânio?', 'desc': 'Olhos de guaxinim, Battle, otorreia', 'critical': True},
            {'id': 'anticoag_tce', 'priority': 'very_urgent', 'question': 'Anticoagulante/antiplaquetário?', 'desc': 'Warfarina, DOACs, AAS', 'critical': True},
            {'id': 'high_mechanism', 'priority': 'very_urgent', 'question': 'Mecanismo de alta energia?', 'desc': 'Queda >1m, ejeção, atropelamento', 'critical': True},
            {'id': 'repeated_vomit', 'priority': 'very_urgent', 'question': 'Vômitos repetidos (≥2)?', 'desc': 'Sinal de hipertensão intracraniana', 'critical': True},
            {'id': 'amnesia', 'priority': 'urgent', 'question': 'Amnésia do evento?', 'desc': 'Não lembra do ocorrido', 'critical': False},
            {'id': 'loss_consciousness', 'priority': 'urgent', 'question': 'Perda de consciência?', 'desc': 'Mesmo que breve', 'critical': False},
            {'id': 'severe_headache', 'priority': 'urgent', 'question': 'Cefaleia intensa?', 'desc': 'Dor de cabeça pós-trauma', 'critical': False},
            {'id': 'moderate_pain_tce', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor no local do trauma', 'critical': False},
            {'id': 'age_risk', 'priority': 'urgent', 'question': 'Idade ≥65 anos?', 'desc': 'Maior risco de sangramento', 'critical': False},
            {'id': 'scalp_wound', 'priority': 'standard', 'question': 'Ferida em couro cabeludo?', 'desc': 'Necessita avaliação/sutura', 'critical': False},
            {'id': 'mild_headache', 'priority': 'standard', 'question': 'Cefaleia leve?', 'desc': 'Dor tolerável', 'critical': False},
            {'id': 'superficial_tce', 'priority': 'standard', 'question': 'Trauma superficial?', 'desc': 'Contusão leve, hematoma', 'critical': False},
            {'id': 'chronic_tce', 'priority': 'non_urgent', 'question': 'Avaliação tardia (>24h)?', 'desc': 'Sem sinais de alarme', 'critical': False},
        ]
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def get_highest_priority(discriminators_triggered: list) -> tuple:
    """Return the highest priority level from triggered discriminators"""
    if not discriminators_triggered:
        return 'non_urgent', []
    
    priority_values = {p: i for i, p in enumerate(PRIORITY_ORDER)}
    highest = 'non_urgent'
    highest_discs = []
    
    for disc in discriminators_triggered:
        if priority_values.get(disc['priority'], 99) < priority_values.get(highest, 99):
            highest = disc['priority']
            highest_discs = [disc]
        elif disc['priority'] == highest:
            highest_discs.append(disc)
    
    return highest, highest_discs

def evaluate_gcs(eye, verbal, motor):
    """Evaluate GCS and return priority"""
    gcs = eye + verbal + motor
    if gcs <= 8:
        return 'immediate', f"GCS {gcs} - Coma"
    elif gcs <= 12:
        return 'very_urgent', f"GCS {gcs} - Alterado"
    elif gcs <= 14:
        return 'urgent', f"GCS {gcs} - Leve alteração"
    return None, f"GCS {gcs}"

def evaluate_vitals(hr, rr, sbp, spo2, temp, on_o2):
    """Evaluate vital signs and return list of discriminators triggered"""
    results = []
    
    # Heart rate
    if hr < 40 or hr > 150:
        results.append({'priority': 'immediate', 'question': f'FC {hr} bpm - crítico'})
    elif hr < 50 or hr > 130:
        results.append({'priority': 'very_urgent', 'question': f'FC {hr} bpm - alterado'})
    elif hr < 60 or hr > 100:
        results.append({'priority': 'urgent', 'question': f'FC {hr} bpm - anormal'})
    
    # Respiratory rate
    if rr < 10 or rr > 30:
        results.append({'priority': 'immediate', 'question': f'FR {rr} rpm - crítico'})
    elif rr < 12 or rr > 25:
        results.append({'priority': 'very_urgent', 'question': f'FR {rr} rpm - alterado'})
    
    # Blood pressure
    if sbp < 80:
        results.append({'priority': 'immediate', 'question': f'PAS {sbp} mmHg - choque'})
    elif sbp < 90:
        results.append({'priority': 'very_urgent', 'question': f'PAS {sbp} mmHg - hipotensão'})
    elif sbp > 200:
        results.append({'priority': 'very_urgent', 'question': f'PAS {sbp} mmHg - crise hipertensiva'})
    
    # SpO2
    if spo2 < 90:
        results.append({'priority': 'immediate', 'question': f'SpO₂ {spo2}% - hipóxia grave'})
    elif spo2 < 94:
        results.append({'priority': 'very_urgent', 'question': f'SpO₂ {spo2}%{" c/O₂" if on_o2 else ""} - hipóxia'})
    elif spo2 < 95 and on_o2:
        results.append({'priority': 'very_urgent', 'question': f'SpO₂ {spo2}% c/O₂ - baixa saturação'})
    
    # Temperature
    if temp >= 41 or temp <= 32:
        results.append({'priority': 'immediate', 'question': f'Temp {temp}°C - crítico'})
    elif temp >= 40 or temp <= 35:
        results.append({'priority': 'very_urgent', 'question': f'Temp {temp}°C - grave'})
    elif temp >= 38.5:
        results.append({'priority': 'urgent', 'question': f'Temp {temp}°C - febre'})
    elif temp >= 37.5:
        results.append({'priority': 'standard', 'question': f'Temp {temp}°C - febrícula'})
    
    return results

def evaluate_pain(pain_level):
    """Evaluate pain level and return priority"""
    if pain_level >= 8:
        return 'very_urgent', f'Dor intensa ({pain_level}/10)'
    elif pain_level >= 5:
        return 'urgent', f'Dor moderada ({pain_level}/10)'
    elif pain_level >= 1:
        return 'standard', f'Dor leve ({pain_level}/10)'
    return None, 'Sem dor'

def create_badge(text, priority, outline=False):
    """Create a badge HTML element"""
    style_class = f"badge-outline-{priority}" if outline else f"badge-{priority}"
    return f'<span class="badge {style_class}"><span class="badge-dot"></span>{text}</span>'

def create_result_banner(priority, discriminators):
    """Create the result banner HTML"""
    p = PRIORITIES[priority]
    
    disc_badges = ""
    for d in discriminators[:5]:
        disc_badges += create_badge(d['question'][:40], d['priority'])
    
    return f"""
    <div class="result-banner banner-{priority}">
        <div class="result-banner-left">
            <div>
                <span class="result-title">{p['label']}</span>
                <span class="result-subtitle"> · {p['label_en']}</span>
            </div>
            <div class="result-discriminators">{disc_badges}</div>
        </div>
        <div class="result-time">{p['time']}</div>
    </div>
    """

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'flowchart_answers' not in st.session_state:
    st.session_state.flowchart_answers = {}
if 'selected_flowchart' not in st.session_state:
    st.session_state.selected_flowchart = 'headache'

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="telepatia-header">
    <div class="telepatia-logo">
        <div class="telepatia-logo-icon">✚</div>
        <span class="telepatia-logo-text">telepatia</span>
    </div>
    <span class="telepatia-subtitle">Sistema de Triagem de Manchester</span>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# MAIN TABS
# ============================================================================
tab1, tab2 = st.tabs(["📋 Avaliação Rápida", "🔄 Fluxogramas Específicos"])

# ============================================================================
# TAB 1: QUICK ASSESSMENT
# ============================================================================
with tab1:
    # Result placeholder at top
    result_placeholder = st.empty()
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    # Collect all triggered discriminators
    all_discriminators = []
    
    # ----- COLUMN 1: GCS / AVPU / PAIN -----
    with col1:
        st.markdown('<div class="section-header">🧠 Nível de Consciência</div>', unsafe_allow_html=True)
        
        # GCS
        eye = st.selectbox("Abertura Ocular (E)", 
            options=[4, 3, 2, 1],
            format_func=lambda x: {4: "4 - Espontânea", 3: "3 - Ao comando verbal", 2: "2 - À dor", 1: "1 - Nenhuma"}[x],
            key="gcs_eye"
        )
        verbal = st.selectbox("Resposta Verbal (V)",
            options=[5, 4, 3, 2, 1],
            format_func=lambda x: {5: "5 - Orientada", 4: "4 - Confusa", 3: "3 - Palavras inapropriadas", 2: "2 - Sons incompreensíveis", 1: "1 - Nenhuma"}[x],
            key="gcs_verbal"
        )
        motor = st.selectbox("Resposta Motora (M)",
            options=[6, 5, 4, 3, 2, 1],
            format_func=lambda x: {6: "6 - Obedece comandos", 5: "5 - Localiza dor", 4: "4 - Retirada à dor", 3: "3 - Flexão anormal", 2: "2 - Extensão anormal", 1: "1 - Nenhuma"}[x],
            key="gcs_motor"
        )
        
        gcs_priority, gcs_text = evaluate_gcs(eye, verbal, motor)
        gcs_total = eye + verbal + motor
        
        if gcs_priority:
            all_discriminators.append({'priority': gcs_priority, 'question': gcs_text})
        
        st.markdown(f"**GCS Total:** {gcs_total}/15")
        
        st.markdown("---")
        
        # AVPU
        st.markdown('<div class="section-header">📊 AVPU</div>', unsafe_allow_html=True)
        avpu = st.radio("Estado", ["A - Alerta", "V - Responde à voz", "P - Responde à dor", "U - Não responsivo"], horizontal=True, key="avpu")
        
        avpu_map = {
            "A - Alerta": None,
            "V - Responde à voz": 'urgent',
            "P - Responde à dor": 'very_urgent',
            "U - Não responsivo": 'immediate'
        }
        if avpu_map[avpu]:
            all_discriminators.append({'priority': avpu_map[avpu], 'question': f'AVPU: {avpu[0]}'})
        
        st.markdown("---")
        
        # Pain
        st.markdown('<div class="section-header">😣 Dor (NRS)</div>', unsafe_allow_html=True)
        pain = st.slider("Intensidade", 0, 10, 0, key="pain")
        
        pain_priority, pain_text = evaluate_pain(pain)
        if pain_priority:
            all_discriminators.append({'priority': pain_priority, 'question': pain_text})
    
    # ----- COLUMN 2: VITAL SIGNS -----
    with col2:
        st.markdown('<div class="section-header">💓 Sinais Vitais</div>', unsafe_allow_html=True)
        
        hr = st.number_input("FC (bpm)", 30, 250, 80, key="hr")
        rr = st.number_input("FR (rpm)", 4, 60, 16, key="rr")
        sbp = st.number_input("PAS (mmHg)", 40, 280, 120, key="sbp")
        spo2 = st.number_input("SpO₂ (%)", 50, 100, 98, key="spo2")
        temp = st.number_input("Temperatura (°C)", 30.0, 44.0, 36.5, 0.1, key="temp")
        on_o2 = st.checkbox("Em uso de O₂", key="on_o2")
        
        vital_discs = evaluate_vitals(hr, rr, sbp, spo2, temp, on_o2)
        all_discriminators.extend(vital_discs)
    
    # ----- COLUMN 3: FLOWCHART SELECTOR -----
    with col3:
        st.markdown('<div class="section-header">🔍 Fluxograma</div>', unsafe_allow_html=True)
        
        flowchart_options = {k: f"{v['icon']} {v['name']}" for k, v in FLOWCHARTS.items()}
        selected = st.selectbox(
            "Selecione o fluxograma",
            options=list(flowchart_options.keys()),
            format_func=lambda x: flowchart_options[x],
            key="flowchart_select"
        )
        
        if selected != st.session_state.selected_flowchart:
            st.session_state.selected_flowchart = selected
            st.session_state.flowchart_answers = {}
        
        # Show critical discriminators
        fc = FLOWCHARTS[selected]
        critical_discs = [d for d in fc['discriminators'] if d.get('critical', False)][:5]
        
        st.markdown("**Discriminadores Críticos:**")
        
        for disc in critical_discs:
            key = f"quick_{selected}_{disc['id']}"
            if st.checkbox(disc['question'], key=key, help=disc['desc']):
                all_discriminators.append({'priority': disc['priority'], 'question': disc['question']})
    
    # Calculate final priority
    final_priority, active_discs = get_highest_priority(all_discriminators)
    
    # Show result banner at top
    with result_placeholder.container():
        st.markdown(create_result_banner(final_priority, all_discriminators), unsafe_allow_html=True)
    
    # Safety Banner
    st.markdown("""
    <div class="safety-banner">
        <div class="safety-banner-icon">⚠️</div>
        <div class="safety-banner-text">
            <div class="safety-banner-title">Avalie de CIMA para BAIXO</div>
            <div class="safety-banner-desc">O primeiro SIM determina a prioridade. Em dúvida, escolha a categoria mais grave.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Priority Legend
    st.markdown('<div class="priority-legend">', unsafe_allow_html=True)
    legend_cols = st.columns(5)
    for i, (key, p) in enumerate(PRIORITIES.items()):
        with legend_cols[i]:
            st.markdown(f"""
            <div class="legend-item">
                <div class="legend-color" style="background: {p['color']};"></div>
                <div class="legend-text">
                    <span class="legend-label" style="color: {p['text']};">{p['label']}</span>
                    <span class="legend-time">{p['time']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# TAB 2: SPECIFIC FLOWCHARTS
# ============================================================================
with tab2:
    col_list, col_detail = st.columns([1, 3])
    
    with col_list:
        st.markdown('<div class="section-header">Fluxogramas</div>', unsafe_allow_html=True)
        
        for key, fc in FLOWCHARTS.items():
            is_active = st.session_state.selected_flowchart == key
            if st.button(f"{fc['icon']} {fc['name']}", key=f"btn_{key}", 
                        type="primary" if is_active else "secondary",
                        use_container_width=True):
                if key != st.session_state.selected_flowchart:
                    st.session_state.selected_flowchart = key
                    st.session_state.flowchart_answers = {}
                    st.rerun()
    
    with col_detail:
        fc = FLOWCHARTS[st.session_state.selected_flowchart]
        st.markdown(f"### {fc['icon']} {fc['name']}")
        st.markdown(f"*{fc['name_en']}*")
        
        st.markdown("---")
        
        # Group discriminators by priority
        by_priority = {}
        for disc in fc['discriminators']:
            p = disc['priority']
            if p not in by_priority:
                by_priority[p] = []
            by_priority[p].append(disc)
        
        flowchart_discs = []
        determined_priority = None
        
        for priority in PRIORITY_ORDER:
            if priority not in by_priority:
                continue
            
            p = PRIORITIES[priority]
            
            st.markdown(f"""
            <div class="discriminator-group-header">
                {create_badge(p['label'], priority)}
                <span style="color: var(--gray-500); font-size: 13px;">{p['time']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            for disc in by_priority[priority]:
                key = f"fc_{st.session_state.selected_flowchart}_{disc['id']}"
                
                disabled = determined_priority is not None
                
                col_q, col_a = st.columns([3, 1])
                with col_q:
                    st.markdown(f"**{disc['question']}**")
                    st.markdown(f"<small style='color: var(--gray-500);'>{disc['desc']}</small>", unsafe_allow_html=True)
                
                with col_a:
                    answer = st.radio(
                        "Resposta",
                        options=["—", "SIM", "NÃO"],
                        key=key,
                        horizontal=True,
                        disabled=disabled,
                        label_visibility="collapsed"
                    )
                    
                    if answer == "SIM" and determined_priority is None:
                        determined_priority = priority
                        flowchart_discs.append(disc)
                
                st.markdown("<hr style='margin: 8px 0; border-color: var(--gray-100);'>", unsafe_allow_html=True)
        
        # Show result for this flowchart
        if flowchart_discs:
            st.markdown("### Resultado da Avaliação")
            st.markdown(create_result_banner(determined_priority, flowchart_discs), unsafe_allow_html=True)
        
        if st.button("🔄 Limpar Respostas", key="clear_fc"):
            st.session_state.flowchart_answers = {}
            st.rerun()

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="telepatia-footer">
    <strong>telepatia</strong> · Sistema de Escalas Médicas · Manchester Triage System<br>
    <small>Ferramenta de apoio à decisão. Não substitui o julgamento clínico.</small>
</div>
""", unsafe_allow_html=True)
