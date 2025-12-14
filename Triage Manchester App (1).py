import streamlit as st

st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS - TELEPATIA DESIGN SYSTEM + DARK MODE FIXES
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
    
    :root {
        --brand-primary: #006B3F;
        --olive-500: #4C9E6B;
        --olive-600: #3C7F56;
        --olive-700: #306544;
    }
    
    * { font-family: 'IBM Plex Sans', -apple-system, sans-serif !important; }
    
    #MainMenu, footer, .stDeployButton { display: none !important; }
    
    /* ===== HEADER ===== */
    .telepatia-header {
        background: #FFFFFF;
        padding: 16px 24px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .telepatia-logo-icon {
        width: 40px;
        height: 40px;
        background: linear-gradient(135deg, #006B3F 0%, #4C9E6B 100%);
        border-radius: 8px;
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
        color: #006B3F;
    }
    
    .telepatia-subtitle {
        color: #666;
        font-size: 14px;
        margin-left: 16px;
        padding-left: 16px;
        border-left: 1px solid #E5E5E5;
    }
    
    /* ===== RESULT BANNER - HIGH CONTRAST ===== */
    .result-banner {
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-left: 5px solid;
    }
    
    .result-content { display: flex; flex-direction: column; gap: 8px; }
    .result-title { font-size: 26px; font-weight: 700; }
    .result-subtitle { font-size: 14px; font-weight: 500; }
    .result-time { font-size: 32px; font-weight: 700; }
    .result-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }
    
    /* High contrast banners */
    .banner-immediate { 
        background: #FEE2E2; 
        border-color: #DC2626;
    }
    .banner-immediate .result-title,
    .banner-immediate .result-time { color: #991B1B; }
    .banner-immediate .result-subtitle { color: #B91C1C; }
    
    .banner-very_urgent { 
        background: #FFEDD5; 
        border-color: #EA580C;
    }
    .banner-very_urgent .result-title,
    .banner-very_urgent .result-time { color: #9A3412; }
    .banner-very_urgent .result-subtitle { color: #C2410C; }
    
    .banner-urgent { 
        background: #FEF9C3; 
        border-color: #EAB308;
    }
    .banner-urgent .result-title,
    .banner-urgent .result-time { color: #713F12; }
    .banner-urgent .result-subtitle { color: #854D0E; }
    
    .banner-standard { 
        background: #DCFCE7; 
        border-color: #22C55E;
    }
    .banner-standard .result-title,
    .banner-standard .result-time { color: #166534; }
    .banner-standard .result-subtitle { color: #15803D; }
    
    .banner-non_urgent { 
        background: #DBEAFE; 
        border-color: #3B82F6;
    }
    .banner-non_urgent .result-title,
    .banner-non_urgent .result-time { color: #1E40AF; }
    .banner-non_urgent .result-subtitle { color: #1D4ED8; }
    
    /* ===== BADGES - HIGH CONTRAST ===== */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .badge::before {
        content: '';
        width: 6px;
        height: 6px;
        border-radius: 50%;
    }
    
    .badge-immediate { background: #DC2626; color: #FFFFFF; }
    .badge-immediate::before { background: #FEE2E2; }
    
    .badge-very_urgent { background: #EA580C; color: #FFFFFF; }
    .badge-very_urgent::before { background: #FFEDD5; }
    
    .badge-urgent { background: #CA8A04; color: #FFFFFF; }
    .badge-urgent::before { background: #FEF9C3; }
    
    .badge-standard { background: #16A34A; color: #FFFFFF; }
    .badge-standard::before { background: #DCFCE7; }
    
    .badge-non_urgent { background: #2563EB; color: #FFFFFF; }
    .badge-non_urgent::before { background: #DBEAFE; }
    
    /* ===== SECTION CARDS ===== */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .section-header {
        font-size: 13px;
        font-weight: 600;
        color: #374151;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid #E5E5E5;
    }
    
    /* ===== FLOWCHART SECTION ===== */
    .flowchart-section {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 24px;
        margin-top: 24px;
    }
    
    .flowchart-title {
        font-size: 20px;
        font-weight: 600;
        color: #111827;
        margin-bottom: 8px;
    }
    
    .flowchart-subtitle {
        font-size: 14px;
        color: #6B7280;
        margin-bottom: 20px;
    }
    
    .priority-group {
        margin-bottom: 20px;
        padding: 16px;
        border-radius: 8px;
        border: 1px solid #E5E5E5;
    }
    
    .priority-group-immediate { background: #FEF2F2; border-color: #FECACA; }
    .priority-group-very_urgent { background: #FFF7ED; border-color: #FED7AA; }
    .priority-group-urgent { background: #FEFCE8; border-color: #FEF08A; }
    .priority-group-standard { background: #F0FDF4; border-color: #BBF7D0; }
    .priority-group-non_urgent { background: #EFF6FF; border-color: #BFDBFE; }
    
    .priority-group-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid rgba(0,0,0,0.1);
    }
    
    .priority-group-title {
        font-weight: 600;
        font-size: 14px;
    }
    
    .priority-group-time {
        font-size: 12px;
        color: #6B7280;
    }
    
    .disc-item {
        padding: 12px 0;
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }
    
    .disc-item:last-child { border-bottom: none; }
    
    .disc-question {
        font-weight: 500;
        color: #111827;
        margin-bottom: 4px;
    }
    
    .disc-desc {
        font-size: 13px;
        color: #6B7280;
    }
    
    .disc-disabled {
        opacity: 0.5;
        pointer-events: none;
    }
    
    /* ===== SAFETY BANNER ===== */
    .safety-banner {
        background: #1F2937;
        color: #FFFFFF;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 20px 0;
    }
    
    .safety-icon {
        width: 40px;
        height: 40px;
        background: #374151;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    
    .safety-title { font-weight: 600; font-size: 15px; }
    .safety-desc { font-size: 13px; opacity: 0.8; margin-top: 2px; }
    
    /* ===== PRIORITY LEGEND ===== */
    .legend-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        padding: 16px;
        background: #F9FAFB;
        border-radius: 8px;
        margin-top: 20px;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        background: #FFFFFF;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    }
    
    .legend-bar {
        width: 4px;
        height: 28px;
        border-radius: 2px;
    }
    
    .legend-label { font-size: 12px; font-weight: 600; }
    .legend-time { font-size: 11px; color: #6B7280; }
    
    /* ===== FOOTER ===== */
    .telepatia-footer {
        background: #F9FAFB;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        font-size: 13px;
        color: #4B5563;
    }
    
    .telepatia-footer strong { color: #006B3F; }
    
    /* ===== STREAMLIT OVERRIDES ===== */
    .stSelectbox > div > div {
        border-radius: 8px !important;
    }
    
    .stRadio > div { gap: 8px !important; flex-wrap: wrap; }
    
    .stRadio label {
        padding: 8px 16px !important;
        border-radius: 8px !important;
        border: 1.5px solid #D1D5DB !important;
        background: #FFFFFF !important;
        color: #374151 !important;
        font-size: 13px !important;
    }
    
    .stRadio label:has(input:checked) {
        border-color: #006B3F !important;
        background: #ECFDF5 !important;
        color: #065F46 !important;
    }
    
    .stButton > button {
        border-radius: 8px !important;
        font-weight: 500 !important;
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #006B3F 0%, #4C9E6B 100%) !important;
        border: none !important;
    }
    
    .stExpander {
        border: 1px solid #E5E5E5 !important;
        border-radius: 12px !important;
        background: #FFFFFF !important;
    }
    
    /* Force light backgrounds on inputs for dark mode compatibility */
    .stSelectbox > div > div,
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background: #FFFFFF !important;
        color: #111827 !important;
    }
    
    div[data-testid="stExpander"] > details {
        background: #FFFFFF !important;
        border-radius: 12px !important;
    }
    
    div[data-testid="stExpander"] summary {
        color: #111827 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA
# ============================================================================
PRIORITIES = {
    'immediate': {'color': '#DC2626', 'label': 'IMEDIATO', 'label_en': 'IMMEDIATE', 'time': '0 min', 'text': '#991B1B'},
    'very_urgent': {'color': '#EA580C', 'label': 'MUITO URGENTE', 'label_en': 'VERY URGENT', 'time': '10 min', 'text': '#9A3412'},
    'urgent': {'color': '#CA8A04', 'label': 'URGENTE', 'label_en': 'URGENT', 'time': '60 min', 'text': '#713F12'},
    'standard': {'color': '#16A34A', 'label': 'PADRÃO', 'label_en': 'STANDARD', 'time': '120 min', 'text': '#166534'},
    'non_urgent': {'color': '#2563EB', 'label': 'NÃO URGENTE', 'label_en': 'NON-URGENT', 'time': '240 min', 'text': '#1E40AF'}
}

PRIORITY_ORDER = ['immediate', 'very_urgent', 'urgent', 'standard', 'non_urgent']

FLOWCHARTS = {
    'headache': {
        'name': 'Cefaleia', 'name_en': 'Headache', 'icon': '🤕',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, incapacidade de manter VA'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, cianose'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco, hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U'},
            {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Movimentos tônico-clônicos'},
            {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'GCS <15, confusão, letargia'},
            {'id': 'focal_deficit', 'priority': 'very_urgent', 'question': 'Déficit neurológico focal?', 'desc': 'Hemiparesia, afasia, alt. visual súbita'},
            {'id': 'meningism', 'priority': 'very_urgent', 'question': 'Sinais de meningismo?', 'desc': 'Rigidez nuca, fotofobia'},
            {'id': 'thunderclap', 'priority': 'very_urgent', 'question': 'Cefaleia súbita intensa (thunderclap)?', 'desc': '"Pior dor da vida"'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável'},
            {'id': 'purpura', 'priority': 'very_urgent', 'question': 'Púrpura/petéquias?', 'desc': 'Manchas não somem à pressão'},
            {'id': 'very_hot', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Interfere nas atividades'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'vomiting', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Múltiplos episódios'},
            {'id': 'syncope', 'priority': 'urgent', 'question': 'História de síncope?', 'desc': 'Perda consciência prévia'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula'},
            {'id': 'recent', 'priority': 'standard', 'question': 'Problema recente (<7 dias)?', 'desc': 'Última semana'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Cefaleia usual'},
        ]
    },
    'chest_pain': {
        'name': 'Dor Torácica', 'name_en': 'Chest Pain', 'icon': '💔',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria'},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U'},
            {'id': 'cardiac_pain', 'priority': 'very_urgent', 'question': 'Dor cardíaca típica?', 'desc': 'Precordial, opressão, irradiação'},
            {'id': 'acute_sob', 'priority': 'very_urgent', 'question': 'Dispneia aguda?', 'desc': 'Início súbito'},
            {'id': 'abnormal_pulse', 'priority': 'very_urgent', 'question': 'Pulso anormal?', 'desc': 'Muito rápido/lento/irregular'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável'},
            {'id': 'low_spo2', 'priority': 'very_urgent', 'question': 'SpO₂ <95% com O₂?', 'desc': 'Baixa saturação'},
            {'id': 'pleuritic', 'priority': 'urgent', 'question': 'Dor pleurítica?', 'desc': 'Piora com respiração'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Significativa'},
            {'id': 'hx_cardiac', 'priority': 'urgent', 'question': 'História cardíaca?', 'desc': 'IAM, angina, stent'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dor habitual'},
        ]
    },
    'abdominal_pain': {
        'name': 'Dor Abdominal', 'name_en': 'Abdominal Pain', 'icon': '🤢',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão'},
            {'id': 'haemorrhage', 'priority': 'immediate', 'question': 'Hemorragia grave?', 'desc': 'Hematêmese volumosa'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Insuportável'},
            {'id': 'peritonism', 'priority': 'very_urgent', 'question': 'Sinais de peritonismo?', 'desc': 'Rigidez, descompressão +'},
            {'id': 'black_stool', 'priority': 'very_urgent', 'question': 'Fezes escuras/sangue?', 'desc': 'Melena/hematoquezia'},
            {'id': 'persistent_vomit', 'priority': 'very_urgent', 'question': 'Vômitos persistentes?', 'desc': 'Não tolera líquidos'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Significativa'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'pregnancy', 'priority': 'urgent', 'question': 'Possível gravidez?', 'desc': 'Idade fértil, amenorreia'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Dor habitual'},
        ]
    },
    'shortness_of_breath': {
        'name': 'Dispneia', 'name_en': 'Shortness of Breath', 'icon': '😮‍💨',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, estridor'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, cianose'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão'},
            {'id': 'low_spo2', 'priority': 'very_urgent', 'question': 'SpO₂ <95%?', 'desc': 'Saturação baixa'},
            {'id': 'unable_speak', 'priority': 'very_urgent', 'question': 'Incapaz de falar frases?', 'desc': 'Fala entrecortada'},
            {'id': 'stridor', 'priority': 'very_urgent', 'question': 'Estridor?', 'desc': 'Som inspiratório agudo'},
            {'id': 'severe_wheeze', 'priority': 'very_urgent', 'question': 'Sibilância grave?', 'desc': 'Audível à distância'},
            {'id': 'moderate_wheeze', 'priority': 'urgent', 'question': 'Sibilância moderada?', 'desc': 'Broncoespasmo'},
            {'id': 'pleuritic', 'priority': 'urgent', 'question': 'Dor pleurítica?', 'desc': 'Dor ao respirar'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'cough', 'priority': 'urgent', 'question': 'Tosse produtiva?', 'desc': 'Expectoração'},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Dispneia crônica?', 'desc': 'Habitual'},
        ]
    },
    'unwell_adult': {
        'name': 'Indisposição Adulto', 'name_en': 'Unwell Adult', 'icon': '🤒',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U'},
            {'id': 'altered', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, letargia'},
            {'id': 'very_hot', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia grave'},
            {'id': 'very_cold', 'priority': 'very_urgent', 'question': 'Temp ≤35°C?', 'desc': 'Hipotermia'},
            {'id': 'purpura', 'priority': 'very_urgent', 'question': 'Púrpura/petéquias?', 'desc': 'Não somem à pressão'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Insuportável'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Significativa'},
            {'id': 'warm', 'priority': 'standard', 'question': 'Temp 37.5-38.4°C?', 'desc': 'Febrícula'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Sintomas habituais'},
        ]
    },
    'limb_problems': {
        'name': 'Problemas Membros', 'name_en': 'Limb Problems', 'icon': '🦵',
        'discriminators': [
            {'id': 'shock', 'priority': 'immediate', 'question': 'Hemorragia grave/choque?', 'desc': 'Sangramento arterial'},
            {'id': 'no_pulse', 'priority': 'very_urgent', 'question': 'Ausência de pulso distal?', 'desc': 'Membro frio'},
            {'id': 'open_fracture', 'priority': 'very_urgent', 'question': 'Fratura exposta?', 'desc': 'Osso visível'},
            {'id': 'deformity', 'priority': 'very_urgent', 'question': 'Deformidade grosseira?', 'desc': 'Angulação anormal'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Insuportável'},
            {'id': 'compartment', 'priority': 'very_urgent', 'question': 'Síndrome compartimental?', 'desc': 'Dor desproporcional'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Significativa'},
            {'id': 'unable_weight', 'priority': 'urgent', 'question': 'Incapaz de apoiar peso?', 'desc': 'Não consegue andar'},
            {'id': 'swelling', 'priority': 'urgent', 'question': 'Edema significativo?', 'desc': 'Inchaço importante'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Dor habitual'},
        ]
    },
    'wounds': {
        'name': 'Feridas', 'name_en': 'Wounds', 'icon': '🩹',
        'discriminators': [
            {'id': 'shock', 'priority': 'immediate', 'question': 'Hemorragia grave/choque?', 'desc': 'Sangramento arterial'},
            {'id': 'active_bleeding', 'priority': 'very_urgent', 'question': 'Sangramento não controlado?', 'desc': 'Não cede com pressão'},
            {'id': 'amputation', 'priority': 'very_urgent', 'question': 'Amputação?', 'desc': 'Perda de parte'},
            {'id': 'tendon_nerve', 'priority': 'very_urgent', 'question': 'Lesão tendão/nervo?', 'desc': 'Déficit motor/sensitivo'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Insuportável'},
            {'id': 'deep', 'priority': 'urgent', 'question': 'Ferida profunda?', 'desc': 'Exposição estruturas'},
            {'id': 'contaminated', 'priority': 'urgent', 'question': 'Ferida contaminada?', 'desc': 'Sujeira, mordida'},
            {'id': 'needs_suture', 'priority': 'urgent', 'question': 'Necessita sutura?', 'desc': 'Bordas separadas'},
            {'id': 'superficial', 'priority': 'standard', 'question': 'Ferida superficial?', 'desc': 'Abrasão, corte'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Ferida crônica?', 'desc': 'Úlcera, ferida antiga'},
        ]
    },
    'falls': {
        'name': 'Quedas', 'name_en': 'Falls', 'icon': '⬇️',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U'},
            {'id': 'altered', 'priority': 'very_urgent', 'question': 'Alteração consciência?', 'desc': 'Confusão pós-queda'},
            {'id': 'spine_pain', 'priority': 'very_urgent', 'question': 'Dor na coluna?', 'desc': 'Cervical/lombar'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Insuportável'},
            {'id': 'deformity', 'priority': 'very_urgent', 'question': 'Deformidade?', 'desc': 'Angulação'},
            {'id': 'anticoag', 'priority': 'very_urgent', 'question': 'Anticoagulante + TCE?', 'desc': 'Warfarina, DOACs'},
            {'id': 'hip_pain', 'priority': 'urgent', 'question': 'Dor no quadril?', 'desc': 'Incapaz movimentar'},
            {'id': 'head_injury', 'priority': 'urgent', 'question': 'Trauma craniano?', 'desc': 'Bateu a cabeça'},
            {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável'},
            {'id': 'walking', 'priority': 'standard', 'question': 'Deambulando bem?', 'desc': 'Sem dificuldade'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Quedas recorrentes?', 'desc': 'Investigação'},
        ]
    },
    'vomiting': {
        'name': 'Vômitos', 'name_en': 'Vomiting', 'icon': '🤮',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento via aérea?', 'desc': 'Obstrução por vômito'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Desidratação grave'},
            {'id': 'haematemesis', 'priority': 'very_urgent', 'question': 'Hematêmese?', 'desc': 'Sangue vivo'},
            {'id': 'coffee_ground', 'priority': 'very_urgent', 'question': 'Vômito borra de café?', 'desc': 'Sangue digerido'},
            {'id': 'severe_dehydration', 'priority': 'very_urgent', 'question': 'Desidratação grave?', 'desc': 'Olhos fundos, letargia'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor abdominal intensa?', 'desc': 'Insuportável'},
            {'id': 'moderate_dehydration', 'priority': 'urgent', 'question': 'Desidratação moderada?', 'desc': 'Sede, oligúria'},
            {'id': 'persistent', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Não tolera líquidos'},
            {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre'},
            {'id': 'mild', 'priority': 'standard', 'question': 'Vômitos ocasionais?', 'desc': 'Tolera líquidos'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Náuseas recorrentes'},
        ]
    },
    'head_injury': {
        'name': 'TCE', 'name_en': 'Head Injury', 'icon': '🤕',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento via aérea?', 'desc': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'question': 'GCS ≤8?', 'desc': 'Não responsivo'},
            {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão pós-trauma?', 'desc': 'Crise convulsiva'},
            {'id': 'altered', 'priority': 'very_urgent', 'question': 'Alteração consciência?', 'desc': 'GCS 9-14, confusão'},
            {'id': 'focal_deficit', 'priority': 'very_urgent', 'question': 'Déficit neurológico?', 'desc': 'Hemiparesia, anisocoria'},
            {'id': 'skull_fracture', 'priority': 'very_urgent', 'question': 'Sinais fratura crânio?', 'desc': 'Olhos guaxinim, Battle'},
            {'id': 'anticoag', 'priority': 'very_urgent', 'question': 'Anticoagulante?', 'desc': 'Warfarina, DOACs'},
            {'id': 'high_mechanism', 'priority': 'very_urgent', 'question': 'Alta energia?', 'desc': 'Queda >1m, ejeção'},
            {'id': 'repeated_vomit', 'priority': 'very_urgent', 'question': 'Vômitos repetidos?', 'desc': '≥2 episódios'},
            {'id': 'amnesia', 'priority': 'urgent', 'question': 'Amnésia do evento?', 'desc': 'Não lembra'},
            {'id': 'loc', 'priority': 'urgent', 'question': 'Perda de consciência?', 'desc': 'Mesmo breve'},
            {'id': 'headache', 'priority': 'urgent', 'question': 'Cefaleia intensa?', 'desc': 'Pós-trauma'},
            {'id': 'age_risk', 'priority': 'urgent', 'question': 'Idade ≥65 anos?', 'desc': 'Maior risco'},
            {'id': 'scalp_wound', 'priority': 'standard', 'question': 'Ferida couro cabeludo?', 'desc': 'Sutura'},
            {'id': 'mild_headache', 'priority': 'standard', 'question': 'Cefaleia leve?', 'desc': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Avaliação tardia (>24h)?', 'desc': 'Sem alarme'},
        ]
    }
}

# ============================================================================
# FUNCTIONS
# ============================================================================
def get_highest_priority(discs):
    if not discs:
        return 'non_urgent', []
    priority_values = {p: i for i, p in enumerate(PRIORITY_ORDER)}
    highest = 'non_urgent'
    highest_discs = []
    for d in discs:
        if priority_values.get(d['priority'], 99) < priority_values.get(highest, 99):
            highest = d['priority']
            highest_discs = [d]
        elif d['priority'] == highest:
            highest_discs.append(d)
    return highest, highest_discs

def evaluate_gcs(e, v, m):
    gcs = e + v + m
    if gcs <= 8: return 'immediate', f"GCS {gcs}"
    elif gcs <= 12: return 'very_urgent', f"GCS {gcs}"
    elif gcs <= 14: return 'urgent', f"GCS {gcs}"
    return None, f"GCS {gcs}"

def evaluate_vitals(hr, rr, sbp, spo2, temp, o2):
    r = []
    if hr < 40 or hr > 150: r.append({'priority': 'immediate', 'question': f'FC {hr}'})
    elif hr < 50 or hr > 130: r.append({'priority': 'very_urgent', 'question': f'FC {hr}'})
    if rr < 10 or rr > 30: r.append({'priority': 'immediate', 'question': f'FR {rr}'})
    elif rr < 12 or rr > 25: r.append({'priority': 'very_urgent', 'question': f'FR {rr}'})
    if sbp < 80: r.append({'priority': 'immediate', 'question': f'PAS {sbp}'})
    elif sbp < 90: r.append({'priority': 'very_urgent', 'question': f'PAS {sbp}'})
    elif sbp > 200: r.append({'priority': 'very_urgent', 'question': f'PAS {sbp}'})
    if spo2 < 90: r.append({'priority': 'immediate', 'question': f'SpO₂ {spo2}%'})
    elif spo2 < 94: r.append({'priority': 'very_urgent', 'question': f'SpO₂ {spo2}%'})
    if temp >= 41 or temp <= 32: r.append({'priority': 'immediate', 'question': f'Temp {temp}°C'})
    elif temp >= 40 or temp <= 35: r.append({'priority': 'very_urgent', 'question': f'Temp {temp}°C'})
    elif temp >= 38.5: r.append({'priority': 'urgent', 'question': f'Temp {temp}°C'})
    elif temp >= 37.5: r.append({'priority': 'standard', 'question': f'Temp {temp}°C'})
    return r

def evaluate_pain(p):
    if p >= 8: return 'very_urgent', f'Dor {p}/10'
    elif p >= 5: return 'urgent', f'Dor {p}/10'
    elif p >= 1: return 'standard', f'Dor {p}/10'
    return None, 'Sem dor'

def badge(text, pri):
    return f'<span class="badge badge-{pri}">{text}</span>'

def result_banner(pri, discs):
    p = PRIORITIES[pri]
    badges = "".join([badge(d['question'][:30], d['priority']) for d in discs[:4]])
    return f"""
    <div class="result-banner banner-{pri}">
        <div class="result-content">
            <div><span class="result-title">{p['label']}</span><span class="result-subtitle"> · {p['label_en']}</span></div>
            <div class="result-badges">{badges}</div>
        </div>
        <div class="result-time">{p['time']}</div>
    </div>
    """

# ============================================================================
# SESSION STATE
# ============================================================================
if 'selected_fc' not in st.session_state:
    st.session_state.selected_fc = 'headache'

# ============================================================================
# HEADER
# ============================================================================
st.markdown("""
<div class="telepatia-header">
    <div class="telepatia-logo-icon">✚</div>
    <span class="telepatia-logo-text">telepatia</span>
    <span class="telepatia-subtitle">Sistema de Triagem de Manchester</span>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# RESULT PLACEHOLDER
# ============================================================================
result_placeholder = st.empty()

# ============================================================================
# MAIN ASSESSMENT
# ============================================================================
all_discs = []

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section-header">🧠 Nível de Consciência</div>', unsafe_allow_html=True)
    eye = st.selectbox("Abertura Ocular", [4,3,2,1], format_func=lambda x: {4:"4-Espontânea",3:"3-Comando",2:"2-Dor",1:"1-Nenhuma"}[x], key="eye")
    verbal = st.selectbox("Resposta Verbal", [5,4,3,2,1], format_func=lambda x: {5:"5-Orientada",4:"4-Confusa",3:"3-Inapropriada",2:"2-Incompreensível",1:"1-Nenhuma"}[x], key="verbal")
    motor = st.selectbox("Resposta Motora", [6,5,4,3,2,1], format_func=lambda x: {6:"6-Obedece",5:"5-Localiza",4:"4-Retirada",3:"3-Flexão",2:"2-Extensão",1:"1-Nenhuma"}[x], key="motor")
    gcs_pri, gcs_txt = evaluate_gcs(eye, verbal, motor)
    if gcs_pri: all_discs.append({'priority': gcs_pri, 'question': gcs_txt})
    st.markdown(f"**GCS: {eye+verbal+motor}/15**")
    
    st.markdown('<div class="section-header" style="margin-top:20px;">📊 AVPU</div>', unsafe_allow_html=True)
    avpu = st.radio("", ["A","V","P","U"], horizontal=True, key="avpu")
    avpu_map = {"A": None, "V": 'urgent', "P": 'very_urgent', "U": 'immediate'}
    if avpu_map[avpu]: all_discs.append({'priority': avpu_map[avpu], 'question': f'AVPU={avpu}'})
    
    st.markdown('<div class="section-header" style="margin-top:20px;">😣 Dor (0-10)</div>', unsafe_allow_html=True)
    pain = st.slider("", 0, 10, 0, key="pain", label_visibility="collapsed")
    pain_pri, pain_txt = evaluate_pain(pain)
    if pain_pri: all_discs.append({'priority': pain_pri, 'question': pain_txt})

with col2:
    st.markdown('<div class="section-header">💓 Sinais Vitais</div>', unsafe_allow_html=True)
    hr = st.number_input("FC (bpm)", 30, 250, 80, key="hr")
    rr = st.number_input("FR (rpm)", 4, 60, 16, key="rr")
    sbp = st.number_input("PAS (mmHg)", 40, 280, 120, key="sbp")
    spo2 = st.number_input("SpO₂ (%)", 50, 100, 98, key="spo2")
    temp = st.number_input("Temp (°C)", 30.0, 44.0, 36.5, 0.1, key="temp")
    o2 = st.checkbox("Em uso de O₂", key="o2")
    all_discs.extend(evaluate_vitals(hr, rr, sbp, spo2, temp, o2))

with col3:
    st.markdown('<div class="section-header">🔍 Fluxograma</div>', unsafe_allow_html=True)
    opts = {k: f"{v['icon']} {v['name']}" for k, v in FLOWCHARTS.items()}
    selected = st.selectbox("Selecione a queixa principal", list(opts.keys()), format_func=lambda x: opts[x], key="fc_select")
    
    if selected != st.session_state.selected_fc:
        st.session_state.selected_fc = selected
        # Clear previous answers
        for key in list(st.session_state.keys()):
            if key.startswith('disc_'):
                del st.session_state[key]
        st.rerun()

# ============================================================================
# SAFETY BANNER
# ============================================================================
st.markdown("""
<div class="safety-banner">
    <div class="safety-icon">⚠️</div>
    <div>
        <div class="safety-title">Avalie de CIMA para BAIXO</div>
        <div class="safety-desc">O primeiro SIM determina a prioridade. Em dúvida, escolha a mais grave.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FLOWCHART SECTION (INLINE)
# ============================================================================
fc = FLOWCHARTS[st.session_state.selected_fc]

st.markdown(f"""
<div class="flowchart-section">
    <div class="flowchart-title">{fc['icon']} {fc['name']}</div>
    <div class="flowchart-subtitle">{fc['name_en']} · Responda os discriminadores abaixo</div>
</div>
""", unsafe_allow_html=True)

# Group by priority
by_pri = {}
for d in fc['discriminators']:
    by_pri.setdefault(d['priority'], []).append(d)

fc_discs = []
determined = None

for pri in PRIORITY_ORDER:
    if pri not in by_pri:
        continue
    
    p = PRIORITIES[pri]
    
    with st.expander(f"● {p['label']} ({p['time']})", expanded=(pri in ['immediate', 'very_urgent'])):
        for d in by_pri[pri]:
            key = f"disc_{st.session_state.selected_fc}_{d['id']}"
            disabled = determined is not None
            
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{d['question']}**")
                st.caption(d['desc'])
            with c2:
                if disabled:
                    st.markdown("*—*")
                else:
                    ans = st.radio("", ["—", "SIM", "NÃO"], key=key, horizontal=True, label_visibility="collapsed")
                    if ans == "SIM":
                        determined = pri
                        fc_discs.append(d)
                        all_discs.append({'priority': pri, 'question': d['question']})

# Clear button
if st.button("🔄 Limpar Respostas do Fluxograma", type="secondary"):
    for key in list(st.session_state.keys()):
        if key.startswith('disc_'):
            del st.session_state[key]
    st.rerun()

# ============================================================================
# CALCULATE & SHOW RESULT
# ============================================================================
final_pri, active = get_highest_priority(all_discs)

with result_placeholder.container():
    st.markdown(result_banner(final_pri, all_discs), unsafe_allow_html=True)

# ============================================================================
# PRIORITY LEGEND
# ============================================================================
st.markdown('<div class="legend-container">', unsafe_allow_html=True)
cols = st.columns(5)
for i, (k, p) in enumerate(PRIORITIES.items()):
    with cols[i]:
        st.markdown(f"""
        <div class="legend-item">
            <div class="legend-bar" style="background:{p['color']};"></div>
            <div>
                <div class="legend-label" style="color:{p['text']};">{p['label']}</div>
                <div class="legend-time">{p['time']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
<div class="telepatia-footer">
    <strong>telepatia</strong> · Sistema de Escalas Médicas · Manchester Triage System<br>
    <small>Ferramenta de apoio à decisão. Não substitui o julgamento clínico.</small>
</div>
""", unsafe_allow_html=True)
