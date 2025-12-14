import streamlit as st
import base64

st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS - MINIMAL, RELY ON CONFIG.TOML FOR THEME
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
    
    * { font-family: 'IBM Plex Sans', -apple-system, sans-serif !important; }
    
    #MainMenu, footer, .stDeployButton { display: none !important; }
    
    /* ===== HEADER ===== */
    .header-container {
        background: #FFFFFF;
        padding: 16px 24px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    .header-logo {
        height: 40px;
    }
    
    .header-divider {
        width: 1px;
        height: 30px;
        background: #E5E5E5;
    }
    
    .header-title {
        font-size: 16px;
        font-weight: 500;
        color: #6B7280;
    }
    
    /* ===== RESULT BANNER ===== */
    .result-box {
        padding: 20px 24px;
        border-radius: 12px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-left: 5px solid;
    }
    
    .result-left { display: flex; flex-direction: column; gap: 6px; }
    .result-priority { font-size: 24px; font-weight: 700; }
    .result-priority-en { font-size: 14px; font-weight: 500; margin-left: 8px; }
    .result-time { font-size: 28px; font-weight: 700; }
    .result-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
    
    .result-immediate { background: #FEE2E2; border-color: #DC2626; }
    .result-immediate .result-priority, .result-immediate .result-time { color: #991B1B; }
    .result-immediate .result-priority-en { color: #B91C1C; }
    
    .result-very_urgent { background: #FFEDD5; border-color: #EA580C; }
    .result-very_urgent .result-priority, .result-very_urgent .result-time { color: #9A3412; }
    .result-very_urgent .result-priority-en { color: #C2410C; }
    
    .result-urgent { background: #FEF9C3; border-color: #EAB308; }
    .result-urgent .result-priority, .result-urgent .result-time { color: #713F12; }
    .result-urgent .result-priority-en { color: #854D0E; }
    
    .result-standard { background: #DCFCE7; border-color: #22C55E; }
    .result-standard .result-priority, .result-standard .result-time { color: #166534; }
    .result-standard .result-priority-en { color: #15803D; }
    
    .result-non_urgent { background: #DBEAFE; border-color: #3B82F6; }
    .result-non_urgent .result-priority, .result-non_urgent .result-time { color: #1E40AF; }
    .result-non_urgent .result-priority-en { color: #1D4ED8; }
    
    /* ===== TAGS ===== */
    .tag {
        display: inline-flex;
        align-items: center;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        color: #FFFFFF;
    }
    
    .tag-immediate { background: #DC2626; }
    .tag-very_urgent { background: #EA580C; }
    .tag-urgent { background: #CA8A04; }
    .tag-standard { background: #16A34A; }
    .tag-non_urgent { background: #2563EB; }
    
    /* ===== SECTION CARD ===== */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }
    
    .section-title {
        font-size: 14px;
        font-weight: 600;
        color: #374151;
        margin-bottom: 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid #E5E5E5;
    }
    
    /* ===== SAFETY ===== */
    .safety-box {
        background: #1F2937;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        gap: 16px;
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
    
    .safety-text-title { font-weight: 600; font-size: 15px; color: #FFFFFF; }
    .safety-text-desc { font-size: 13px; color: #9CA3AF; margin-top: 2px; }
    
    /* ===== FLOWCHART ===== */
    .flowchart-box {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 16px;
    }
    
    .flowchart-name {
        font-size: 20px;
        font-weight: 600;
        color: #111827;
    }
    
    .flowchart-name-en {
        font-size: 14px;
        color: #6B7280;
        margin-top: 4px;
    }
    
    /* ===== PRIORITY HEADERS ===== */
    .pri-header {
        padding: 10px 16px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 12px;
    }
    
    .pri-header-immediate { background: #FEE2E2; color: #991B1B; }
    .pri-header-very_urgent { background: #FFEDD5; color: #9A3412; }
    .pri-header-urgent { background: #FEF9C3; color: #713F12; }
    .pri-header-standard { background: #DCFCE7; color: #166534; }
    .pri-header-non_urgent { background: #DBEAFE; color: #1E40AF; }
    
    /* ===== LEGEND ===== */
    .legend-box {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 16px;
        margin-top: 20px;
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        background: #F9FAFB;
        border-radius: 8px;
    }
    
    .legend-bar { width: 4px; height: 24px; border-radius: 2px; }
    .legend-label { font-size: 12px; font-weight: 600; }
    .legend-time { font-size: 11px; color: #6B7280; }
    
    /* ===== FOOTER ===== */
    .footer-box {
        background: #FFFFFF;
        border: 1px solid #E5E5E5;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        margin-top: 24px;
        font-size: 13px;
        color: #6B7280;
    }
    
    .footer-box strong { color: #006B3F; }
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
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução, incapacidade de manter VA'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30, cianose'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Pele fria, pulso fraco, hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'q': 'Não responsivo?', 'd': 'AVPU = U'},
            {'id': 'seizure', 'priority': 'immediate', 'q': 'Convulsão ativa?', 'd': 'Movimentos tônico-clônicos'},
            {'id': 'altered', 'priority': 'very_urgent', 'q': 'Alteração da consciência?', 'd': 'GCS <15, confusão'},
            {'id': 'focal', 'priority': 'very_urgent', 'q': 'Déficit neurológico focal?', 'd': 'Hemiparesia, afasia'},
            {'id': 'meningism', 'priority': 'very_urgent', 'q': 'Sinais de meningismo?', 'd': 'Rigidez nuca, fotofobia'},
            {'id': 'thunderclap', 'priority': 'very_urgent', 'q': 'Cefaleia súbita intensa?', 'd': '"Pior dor da vida"'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Dor insuportável'},
            {'id': 'purpura', 'priority': 'very_urgent', 'q': 'Púrpura/petéquias?', 'd': 'Não somem à pressão'},
            {'id': 'very_hot', 'priority': 'very_urgent', 'q': 'Temp ≥41°C?', 'd': 'Hipertermia grave'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'q': 'Dor moderada (5-7)?', 'd': 'Interfere atividades'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'vomiting', 'priority': 'urgent', 'q': 'Vômitos persistentes?', 'd': 'Múltiplos episódios'},
            {'id': 'syncope', 'priority': 'urgent', 'q': 'História de síncope?', 'd': 'Perda consciência prévia'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'q': 'Temp 37.5-38.4°C?', 'd': 'Febrícula'},
            {'id': 'recent', 'priority': 'standard', 'q': 'Problema recente?', 'd': '<7 dias'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Cefaleia usual'},
        ]
    },
    'chest_pain': {
        'name': 'Dor Torácica', 'name_en': 'Chest Pain', 'icon': '💔',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão, pele fria'},
            {'id': 'unresponsive', 'priority': 'immediate', 'q': 'Não responsivo?', 'd': 'AVPU = U'},
            {'id': 'cardiac', 'priority': 'very_urgent', 'q': 'Dor cardíaca típica?', 'd': 'Precordial, opressão'},
            {'id': 'acute_sob', 'priority': 'very_urgent', 'q': 'Dispneia aguda?', 'd': 'Início súbito'},
            {'id': 'abnormal_pulse', 'priority': 'very_urgent', 'q': 'Pulso anormal?', 'd': 'Rápido/lento/irregular'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'low_spo2', 'priority': 'very_urgent', 'q': 'SpO₂ <95% com O₂?', 'd': 'Baixa saturação'},
            {'id': 'pleuritic', 'priority': 'urgent', 'q': 'Dor pleurítica?', 'd': 'Piora com respiração'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'q': 'Dor moderada (5-7)?', 'd': 'Significativa'},
            {'id': 'hx_cardiac', 'priority': 'urgent', 'q': 'História cardíaca?', 'd': 'IAM, angina, stent'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'q': 'Temp 37.5-38.4°C?', 'd': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Dor habitual'},
        ]
    },
    'abdominal_pain': {
        'name': 'Dor Abdominal', 'name_en': 'Abdominal Pain', 'icon': '🤢',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão'},
            {'id': 'haemorrhage', 'priority': 'immediate', 'q': 'Hemorragia grave?', 'd': 'Hematêmese volumosa'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'peritonism', 'priority': 'very_urgent', 'q': 'Sinais de peritonismo?', 'd': 'Rigidez, descompressão +'},
            {'id': 'black_stool', 'priority': 'very_urgent', 'q': 'Fezes escuras/sangue?', 'd': 'Melena/hematoquezia'},
            {'id': 'persistent_vomit', 'priority': 'very_urgent', 'q': 'Vômitos persistentes?', 'd': 'Não tolera líquidos'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'q': 'Dor moderada (5-7)?', 'd': 'Significativa'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'pregnancy', 'priority': 'urgent', 'q': 'Possível gravidez?', 'd': 'Idade fértil'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'warm', 'priority': 'standard', 'q': 'Temp 37.5-38.4°C?', 'd': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Dor habitual'},
        ]
    },
    'shortness_of_breath': {
        'name': 'Dispneia', 'name_en': 'Shortness of Breath', 'icon': '😮‍💨',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução, estridor'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30, cianose'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão'},
            {'id': 'low_spo2', 'priority': 'very_urgent', 'q': 'SpO₂ <95%?', 'd': 'Saturação baixa'},
            {'id': 'unable_speak', 'priority': 'very_urgent', 'q': 'Incapaz de falar frases?', 'd': 'Fala entrecortada'},
            {'id': 'stridor', 'priority': 'very_urgent', 'q': 'Estridor?', 'd': 'Som inspiratório agudo'},
            {'id': 'severe_wheeze', 'priority': 'very_urgent', 'q': 'Sibilância grave?', 'd': 'Audível à distância'},
            {'id': 'moderate_wheeze', 'priority': 'urgent', 'q': 'Sibilância moderada?', 'd': 'Broncoespasmo'},
            {'id': 'pleuritic', 'priority': 'urgent', 'q': 'Dor pleurítica?', 'd': 'Dor ao respirar'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'cough', 'priority': 'urgent', 'q': 'Tosse produtiva?', 'd': 'Expectoração'},
            {'id': 'warm', 'priority': 'standard', 'q': 'Temp 37.5-38.4°C?', 'd': 'Febrícula'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Dispneia crônica?', 'd': 'Habitual'},
        ]
    },
    'unwell_adult': {
        'name': 'Indisposição Adulto', 'name_en': 'Unwell Adult', 'icon': '🤒',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'q': 'Não responsivo?', 'd': 'AVPU = U'},
            {'id': 'altered', 'priority': 'very_urgent', 'q': 'Alteração da consciência?', 'd': 'Confusão, letargia'},
            {'id': 'very_hot', 'priority': 'very_urgent', 'q': 'Temp ≥41°C?', 'd': 'Hipertermia grave'},
            {'id': 'very_cold', 'priority': 'very_urgent', 'q': 'Temp ≤35°C?', 'd': 'Hipotermia'},
            {'id': 'purpura', 'priority': 'very_urgent', 'q': 'Púrpura/petéquias?', 'd': 'Não somem à pressão'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'q': 'Dor moderada (5-7)?', 'd': 'Significativa'},
            {'id': 'warm', 'priority': 'standard', 'q': 'Temp 37.5-38.4°C?', 'd': 'Febrícula'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Habitual'},
        ]
    },
    'limb_problems': {
        'name': 'Problemas Membros', 'name_en': 'Limb Problems', 'icon': '🦵',
        'discriminators': [
            {'id': 'shock', 'priority': 'immediate', 'q': 'Hemorragia grave/choque?', 'd': 'Sangramento arterial'},
            {'id': 'no_pulse', 'priority': 'very_urgent', 'q': 'Ausência de pulso distal?', 'd': 'Membro frio'},
            {'id': 'open_fracture', 'priority': 'very_urgent', 'q': 'Fratura exposta?', 'd': 'Osso visível'},
            {'id': 'deformity', 'priority': 'very_urgent', 'q': 'Deformidade grosseira?', 'd': 'Angulação anormal'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'compartment', 'priority': 'very_urgent', 'q': 'Síndrome compartimental?', 'd': 'Dor desproporcional'},
            {'id': 'moderate_pain', 'priority': 'urgent', 'q': 'Dor moderada (5-7)?', 'd': 'Significativa'},
            {'id': 'unable_weight', 'priority': 'urgent', 'q': 'Incapaz de apoiar peso?', 'd': 'Não consegue andar'},
            {'id': 'swelling', 'priority': 'urgent', 'q': 'Edema significativo?', 'd': 'Inchaço importante'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Dor habitual'},
        ]
    },
    'wounds': {
        'name': 'Feridas', 'name_en': 'Wounds', 'icon': '🩹',
        'discriminators': [
            {'id': 'shock', 'priority': 'immediate', 'q': 'Hemorragia grave/choque?', 'd': 'Sangramento arterial'},
            {'id': 'active_bleeding', 'priority': 'very_urgent', 'q': 'Sangramento não controlado?', 'd': 'Não cede com pressão'},
            {'id': 'amputation', 'priority': 'very_urgent', 'q': 'Amputação?', 'd': 'Perda de parte'},
            {'id': 'tendon_nerve', 'priority': 'very_urgent', 'q': 'Lesão tendão/nervo?', 'd': 'Déficit motor/sensitivo'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'deep', 'priority': 'urgent', 'q': 'Ferida profunda?', 'd': 'Exposição estruturas'},
            {'id': 'contaminated', 'priority': 'urgent', 'q': 'Ferida contaminada?', 'd': 'Sujeira, mordida'},
            {'id': 'needs_suture', 'priority': 'urgent', 'q': 'Necessita sutura?', 'd': 'Bordas separadas'},
            {'id': 'superficial', 'priority': 'standard', 'q': 'Ferida superficial?', 'd': 'Abrasão, corte'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Ferida crônica?', 'd': 'Úlcera, ferida antiga'},
        ]
    },
    'falls': {
        'name': 'Quedas', 'name_en': 'Falls', 'icon': '⬇️',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento de via aérea?', 'd': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'q': 'Não responsivo?', 'd': 'AVPU = U'},
            {'id': 'altered', 'priority': 'very_urgent', 'q': 'Alteração consciência?', 'd': 'Confusão pós-queda'},
            {'id': 'spine_pain', 'priority': 'very_urgent', 'q': 'Dor na coluna?', 'd': 'Cervical/lombar'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor intensa (8-10)?', 'd': 'Insuportável'},
            {'id': 'deformity', 'priority': 'very_urgent', 'q': 'Deformidade?', 'd': 'Angulação'},
            {'id': 'anticoag', 'priority': 'very_urgent', 'q': 'Anticoagulante + TCE?', 'd': 'Warfarina, DOACs'},
            {'id': 'hip_pain', 'priority': 'urgent', 'q': 'Dor no quadril?', 'd': 'Incapaz movimentar'},
            {'id': 'head_injury', 'priority': 'urgent', 'q': 'Trauma craniano?', 'd': 'Bateu a cabeça'},
            {'id': 'mild_pain', 'priority': 'standard', 'q': 'Dor leve (1-4)?', 'd': 'Tolerável'},
            {'id': 'walking', 'priority': 'standard', 'q': 'Deambulando bem?', 'd': 'Sem dificuldade'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Quedas recorrentes?', 'd': 'Investigação'},
        ]
    },
    'vomiting': {
        'name': 'Vômitos', 'name_en': 'Vomiting', 'icon': '🤮',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento via aérea?', 'd': 'Obstrução por vômito'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Desidratação grave'},
            {'id': 'haematemesis', 'priority': 'very_urgent', 'q': 'Hematêmese?', 'd': 'Sangue vivo'},
            {'id': 'coffee_ground', 'priority': 'very_urgent', 'q': 'Vômito borra de café?', 'd': 'Sangue digerido'},
            {'id': 'severe_dehydration', 'priority': 'very_urgent', 'q': 'Desidratação grave?', 'd': 'Olhos fundos, letargia'},
            {'id': 'severe_pain', 'priority': 'very_urgent', 'q': 'Dor abdominal intensa?', 'd': 'Insuportável'},
            {'id': 'moderate_dehydration', 'priority': 'urgent', 'q': 'Desidratação moderada?', 'd': 'Sede, oligúria'},
            {'id': 'persistent', 'priority': 'urgent', 'q': 'Vômitos persistentes?', 'd': 'Não tolera líquidos'},
            {'id': 'hot', 'priority': 'urgent', 'q': 'Temp 38.5-40.9°C?', 'd': 'Febre'},
            {'id': 'mild', 'priority': 'standard', 'q': 'Vômitos ocasionais?', 'd': 'Tolera líquidos'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Problema crônico?', 'd': 'Náuseas recorrentes'},
        ]
    },
    'head_injury': {
        'name': 'TCE', 'name_en': 'Head Injury', 'icon': '🤕',
        'discriminators': [
            {'id': 'airway', 'priority': 'immediate', 'q': 'Comprometimento via aérea?', 'd': 'Obstrução'},
            {'id': 'breathing', 'priority': 'immediate', 'q': 'Respiração inadequada?', 'd': 'FR <10 ou >30'},
            {'id': 'shock', 'priority': 'immediate', 'q': 'Sinais de choque?', 'd': 'Hipotensão'},
            {'id': 'unresponsive', 'priority': 'immediate', 'q': 'GCS ≤8?', 'd': 'Não responsivo'},
            {'id': 'seizure', 'priority': 'immediate', 'q': 'Convulsão pós-trauma?', 'd': 'Crise convulsiva'},
            {'id': 'altered', 'priority': 'very_urgent', 'q': 'Alteração consciência?', 'd': 'GCS 9-14, confusão'},
            {'id': 'focal', 'priority': 'very_urgent', 'q': 'Déficit neurológico?', 'd': 'Hemiparesia, anisocoria'},
            {'id': 'skull_fracture', 'priority': 'very_urgent', 'q': 'Sinais fratura crânio?', 'd': 'Olhos guaxinim, Battle'},
            {'id': 'anticoag', 'priority': 'very_urgent', 'q': 'Anticoagulante?', 'd': 'Warfarina, DOACs'},
            {'id': 'high_mechanism', 'priority': 'very_urgent', 'q': 'Alta energia?', 'd': 'Queda >1m, ejeção'},
            {'id': 'repeated_vomit', 'priority': 'very_urgent', 'q': 'Vômitos repetidos?', 'd': '≥2 episódios'},
            {'id': 'amnesia', 'priority': 'urgent', 'q': 'Amnésia do evento?', 'd': 'Não lembra'},
            {'id': 'loc', 'priority': 'urgent', 'q': 'Perda de consciência?', 'd': 'Mesmo breve'},
            {'id': 'headache', 'priority': 'urgent', 'q': 'Cefaleia intensa?', 'd': 'Pós-trauma'},
            {'id': 'age_risk', 'priority': 'urgent', 'q': 'Idade ≥65 anos?', 'd': 'Maior risco'},
            {'id': 'scalp_wound', 'priority': 'standard', 'q': 'Ferida couro cabeludo?', 'd': 'Sutura'},
            {'id': 'mild_headache', 'priority': 'standard', 'q': 'Cefaleia leve?', 'd': 'Tolerável'},
            {'id': 'chronic', 'priority': 'non_urgent', 'q': 'Avaliação tardia?', 'd': '>24h, sem alarme'},
        ]
    }
}

# ============================================================================
# FUNCTIONS
# ============================================================================
def get_highest_priority(discs):
    if not discs:
        return 'non_urgent', []
    pv = {p: i for i, p in enumerate(PRIORITY_ORDER)}
    highest = 'non_urgent'
    hd = []
    for d in discs:
        if pv.get(d['priority'], 99) < pv.get(highest, 99):
            highest = d['priority']
            hd = [d]
        elif d['priority'] == highest:
            hd.append(d)
    return highest, hd

def eval_gcs(e, v, m):
    gcs = e + v + m
    if gcs <= 8: return 'immediate', f"GCS {gcs}"
    elif gcs <= 12: return 'very_urgent', f"GCS {gcs}"
    elif gcs <= 14: return 'urgent', f"GCS {gcs}"
    return None, f"GCS {gcs}"

def eval_vitals(hr, rr, sbp, spo2, temp):
    r = []
    if hr < 40 or hr > 150: r.append({'priority': 'immediate', 'q': f'FC {hr}'})
    elif hr < 50 or hr > 130: r.append({'priority': 'very_urgent', 'q': f'FC {hr}'})
    if rr < 10 or rr > 30: r.append({'priority': 'immediate', 'q': f'FR {rr}'})
    elif rr < 12 or rr > 25: r.append({'priority': 'very_urgent', 'q': f'FR {rr}'})
    if sbp < 80: r.append({'priority': 'immediate', 'q': f'PAS {sbp}'})
    elif sbp < 90 or sbp > 200: r.append({'priority': 'very_urgent', 'q': f'PAS {sbp}'})
    if spo2 < 90: r.append({'priority': 'immediate', 'q': f'SpO₂ {spo2}%'})
    elif spo2 < 94: r.append({'priority': 'very_urgent', 'q': f'SpO₂ {spo2}%'})
    if temp >= 41 or temp <= 32: r.append({'priority': 'immediate', 'q': f'Temp {temp}°C'})
    elif temp >= 40 or temp <= 35: r.append({'priority': 'very_urgent', 'q': f'Temp {temp}°C'})
    elif temp >= 38.5: r.append({'priority': 'urgent', 'q': f'Temp {temp}°C'})
    elif temp >= 37.5: r.append({'priority': 'standard', 'q': f'Temp {temp}°C'})
    return r

def eval_pain(p):
    if p >= 8: return 'very_urgent', f'Dor {p}/10'
    elif p >= 5: return 'urgent', f'Dor {p}/10'
    elif p >= 1: return 'standard', f'Dor {p}/10'
    return None, None

def make_tag(text, pri):
    return f'<span class="tag tag-{pri}">{text}</span>'

def make_result(pri, discs):
    p = PRIORITIES[pri]
    tags = "".join([make_tag(d.get('q', d.get('question', ''))[:25], d['priority']) for d in discs[:4]])
    return f"""
    <div class="result-box result-{pri}">
        <div class="result-left">
            <div><span class="result-priority">{p['label']}</span><span class="result-priority-en">{p['label_en']}</span></div>
            <div class="result-tags">{tags}</div>
        </div>
        <div class="result-time">{p['time']}</div>
    </div>
    """

# ============================================================================
# SESSION STATE
# ============================================================================
if 'fc' not in st.session_state:
    st.session_state.fc = 'headache'

# ============================================================================
# HEADER WITH SVG LOGO
# ============================================================================
# Telepatia logo SVG (simplified version of the cross logo)
logo_svg = '''<svg width="120" height="32" viewBox="0 0 120 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 12C8 10.8954 8.89543 10 10 10H14C15.1046 10 16 10.8954 16 12V14H18C19.1046 14 20 14.8954 20 16V20C20 21.1046 19.1046 22 18 22H16V24C16 25.1046 15.1046 26 14 26H10C8.89543 26 8 25.1046 8 24V22H6C4.89543 22 4 21.1046 4 20V16C4 14.8954 4.89543 14 6 14H8V12Z" fill="url(#grad1)"/>
  <text x="28" y="23" font-family="IBM Plex Sans, sans-serif" font-size="18" font-weight="600" fill="#006B3F">telepatia</text>
  <defs>
    <linearGradient id="grad1" x1="4" y1="10" x2="20" y2="26" gradientUnits="userSpaceOnUse">
      <stop stop-color="#006B3F"/>
      <stop offset="1" stop-color="#4C9E6B"/>
    </linearGradient>
  </defs>
</svg>'''

st.markdown(f"""
<div class="header-container">
    {logo_svg}
    <div class="header-divider"></div>
    <span class="header-title">Sistema de Triagem de Manchester</span>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# RESULT PLACEHOLDER
# ============================================================================
result_ph = st.empty()

# ============================================================================
# ASSESSMENT
# ============================================================================
all_discs = []

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 🧠 Consciência")
    eye = st.selectbox("Abertura Ocular", [4,3,2,1], format_func=lambda x: f"{x} - "+{4:"Espontânea",3:"Comando",2:"Dor",1:"Nenhuma"}[x])
    verbal = st.selectbox("Resposta Verbal", [5,4,3,2,1], format_func=lambda x: f"{x} - "+{5:"Orientada",4:"Confusa",3:"Inapropriada",2:"Incompreensível",1:"Nenhuma"}[x])
    motor = st.selectbox("Resposta Motora", [6,5,4,3,2,1], format_func=lambda x: f"{x} - "+{6:"Obedece",5:"Localiza",4:"Retirada",3:"Flexão",2:"Extensão",1:"Nenhuma"}[x])
    gcs_pri, gcs_txt = eval_gcs(eye, verbal, motor)
    if gcs_pri: all_discs.append({'priority': gcs_pri, 'q': gcs_txt})
    st.info(f"**GCS: {eye+verbal+motor}/15**")
    
    st.markdown("#### 📊 AVPU")
    avpu = st.radio("Estado", ["A - Alerta","V - Voz","P - Dor","U - Não responsivo"], horizontal=True)
    avpu_map = {"A - Alerta": None, "V - Voz": 'urgent', "P - Dor": 'very_urgent', "U - Não responsivo": 'immediate'}
    if avpu_map[avpu]: all_discs.append({'priority': avpu_map[avpu], 'q': f'AVPU={avpu[0]}'})
    
    st.markdown("#### 😣 Dor (0-10)")
    pain = st.slider("Intensidade", 0, 10, 0)
    pain_pri, pain_txt = eval_pain(pain)
    if pain_pri: all_discs.append({'priority': pain_pri, 'q': pain_txt})

with col2:
    st.markdown("#### 💓 Sinais Vitais")
    hr = st.number_input("FC (bpm)", 30, 250, 80)
    rr = st.number_input("FR (rpm)", 4, 60, 16)
    sbp = st.number_input("PAS (mmHg)", 40, 280, 120)
    spo2 = st.number_input("SpO₂ (%)", 50, 100, 98)
    temp = st.number_input("Temp (°C)", 30.0, 44.0, 36.5, 0.1)
    st.checkbox("Em uso de O₂")
    all_discs.extend(eval_vitals(hr, rr, sbp, spo2, temp))

with col3:
    st.markdown("#### 🔍 Queixa Principal")
    opts = {k: f"{v['icon']} {v['name']}" for k, v in FLOWCHARTS.items()}
    sel = st.selectbox("Fluxograma", list(opts.keys()), format_func=lambda x: opts[x])
    if sel != st.session_state.fc:
        st.session_state.fc = sel
        st.rerun()

# ============================================================================
# SAFETY
# ============================================================================
st.markdown("""
<div class="safety-box">
    <div class="safety-icon">⚠️</div>
    <div>
        <div class="safety-text-title">Avalie de CIMA para BAIXO</div>
        <div class="safety-text-desc">O primeiro SIM determina a prioridade. Em dúvida, escolha a mais grave.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# FLOWCHART
# ============================================================================
fc = FLOWCHARTS[st.session_state.fc]

st.markdown(f"""
<div class="flowchart-box">
    <div class="flowchart-name">{fc['icon']} {fc['name']}</div>
    <div class="flowchart-name-en">{fc['name_en']}</div>
</div>
""", unsafe_allow_html=True)

by_pri = {}
for d in fc['discriminators']:
    by_pri.setdefault(d['priority'], []).append(d)

determined = None

for pri in PRIORITY_ORDER:
    if pri not in by_pri:
        continue
    p = PRIORITIES[pri]
    
    with st.expander(f"● {p['label']} ({p['time']})", expanded=(pri in ['immediate', 'very_urgent'])):
        for d in by_pri[pri]:
            key = f"d_{st.session_state.fc}_{d['id']}"
            disabled = determined is not None
            
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{d['q']}**")
                st.caption(d['d'])
            with c2:
                if disabled:
                    st.write("—")
                else:
                    ans = st.radio("", ["—", "SIM", "NÃO"], key=key, horizontal=True, label_visibility="collapsed")
                    if ans == "SIM":
                        determined = pri
                        all_discs.append({'priority': pri, 'q': d['q']})

if st.button("🔄 Limpar Respostas"):
    for k in list(st.session_state.keys()):
        if k.startswith('d_'):
            del st.session_state[k]
    st.rerun()

# ============================================================================
# RESULT
# ============================================================================
final_pri, _ = get_highest_priority(all_discs)
with result_ph.container():
    st.markdown(make_result(final_pri, all_discs), unsafe_allow_html=True)

# ============================================================================
# LEGEND
# ============================================================================
st.markdown('<div class="legend-box">', unsafe_allow_html=True)
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
<div class="footer-box">
    <strong>telepatia</strong> · Sistema de Escalas Médicas · Manchester Triage<br>
    <small>Ferramenta de apoio à decisão. Não substitui o julgamento clínico.</small>
</div>
""", unsafe_allow_html=True)
