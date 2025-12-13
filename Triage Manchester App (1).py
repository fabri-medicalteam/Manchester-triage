import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');
    
    * { font-family: 'DM Sans', sans-serif; }
    
    .main-header {
        background: white;
        padding: 15px 25px;
        border-radius: 12px;
        border-bottom: 3px solid #006B3F;
        margin-bottom: 15px;
    }
    
    .logo-text { color: #006B3F; font-size: 24px; font-weight: 500; margin: 0; }
    .subtitle { color: #64748b; font-size: 13px; margin-top: 3px; }
    
    .result-banner {
        padding: 15px 20px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 5px solid;
    }
    
    .priority-immediate { background-color: #FEE2E2; border-color: #DC2626; }
    .priority-very_urgent { background-color: #FFEDD5; border-color: #EA580C; }
    .priority-urgent { background-color: #FEF9C3; border-color: #EAB308; }
    .priority-standard { background-color: #DCFCE7; border-color: #22C55E; }
    .priority-non_urgent { background-color: #DBEAFE; border-color: #3B82F6; }
    
    .category-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        margin: 5px 0;
        cursor: pointer;
    }
    
    .category-card:hover { background: #f0fdf4; border-color: #006B3F; }
    
    .flowchart-btn {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 8px 12px;
        margin: 3px;
        font-size: 13px;
        cursor: pointer;
    }
    
    .flowchart-btn:hover { background: #f0fdf4; border-color: #006B3F; }
    .flowchart-btn.selected { background: #006B3F; color: white; }
    
    .summary-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
    }
    
    .safety-warning {
        background-color: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 12px;
        margin: 10px 0;
        font-size: 13px;
    }
    
    .encaminhamento-box {
        background: linear-gradient(135deg, #006B3F 0%, #004d2d 100%);
        color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
    }
    
    .disc-item {
        padding: 10px 12px;
        border-bottom: 1px solid #f1f5f9;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .disc-item:hover { background: #f8fafc; }
</style>
""", unsafe_allow_html=True)

# Priority configuration
PRIORITIES = {
    'immediate': {'color': '#DC2626', 'label': 'IMEDIATO', 'label_en': 'IMMEDIATE', 'time': '0 min', 'bg': '#FEE2E2',
                  'encaminhamento': 'SALA DE EMERGÊNCIA - Atendimento médico IMEDIATO. Acionar equipe de emergência.'},
    'very_urgent': {'color': '#EA580C', 'label': 'MUITO URGENTE', 'label_en': 'VERY URGENT', 'time': '10 min', 'bg': '#FFEDD5',
                    'encaminhamento': 'SALA AMARELA/LARANJA - Avaliação médica em até 10 minutos. Monitorização contínua.'},
    'urgent': {'color': '#EAB308', 'label': 'URGENTE', 'label_en': 'URGENT', 'time': '60 min', 'bg': '#FEF9C3',
               'encaminhamento': 'CONSULTÓRIO DE URGÊNCIA - Avaliação médica em até 60 minutos. Reavaliação se piora.'},
    'standard': {'color': '#22C55E', 'label': 'PADRÃO', 'label_en': 'STANDARD', 'time': '120 min', 'bg': '#DCFCE7',
                 'encaminhamento': 'SALA DE ESPERA - Atendimento por ordem de chegada. Tempo estimado: 2 horas.'},
    'non_urgent': {'color': '#3B82F6', 'label': 'NÃO URGENTE', 'label_en': 'NON-URGENT', 'time': '240 min', 'bg': '#DBEAFE',
                   'encaminhamento': 'ORIENTAR UBS/AMBULATÓRIO - Pode aguardar até 4h ou ser encaminhado para atenção primária.'}
}

PRIORITY_ORDER = ['immediate', 'very_urgent', 'urgent', 'standard', 'non_urgent']

# ============================================================================
# 52 FLOWCHARTS ORGANIZED BY CATEGORY
# ============================================================================
FLOWCHART_CATEGORIES = {
    'dor': {
        'name': 'Dor',
        'icon': '🔴',
        'flowcharts': [
            {'id': 'headache', 'name': 'Cefaleia', 'name_en': 'Headache'},
            {'id': 'chest_pain', 'name': 'Dor Torácica', 'name_en': 'Chest Pain'},
            {'id': 'abdominal_pain', 'name': 'Dor Abdominal', 'name_en': 'Abdominal Pain'},
            {'id': 'back_pain', 'name': 'Dor Lombar', 'name_en': 'Back Pain'},
            {'id': 'neck_pain', 'name': 'Dor Cervical', 'name_en': 'Neck Pain'},
            {'id': 'sore_throat', 'name': 'Dor de Garganta', 'name_en': 'Sore Throat'},
            {'id': 'testicular_pain', 'name': 'Dor Testicular', 'name_en': 'Testicular Pain'},
            {'id': 'dental_problems', 'name': 'Problemas Dentários', 'name_en': 'Dental Problems'},
        ]
    },
    'respiratorio': {
        'name': 'Respiratório',
        'icon': '🫁',
        'flowcharts': [
            {'id': 'shortness_of_breath', 'name': 'Dispneia no Adulto', 'name_en': 'Shortness of Breath'},
            {'id': 'shortness_of_breath_child', 'name': 'Dispneia na Criança', 'name_en': 'Shortness of Breath in Child'},
            {'id': 'asthma', 'name': 'Asma', 'name_en': 'Asthma'},
        ]
    },
    'trauma': {
        'name': 'Trauma',
        'icon': '🩹',
        'flowcharts': [
            {'id': 'major_trauma', 'name': 'Grande Traumatismo', 'name_en': 'Major Trauma'},
            {'id': 'head_injury', 'name': 'TCE', 'name_en': 'Head Injury'},
            {'id': 'limb_problems', 'name': 'Problemas em Membros', 'name_en': 'Limb Problems'},
            {'id': 'torso_injury', 'name': 'Lesão Toraco-Abdominal', 'name_en': 'Torso Injury'},
            {'id': 'falls', 'name': 'Quedas', 'name_en': 'Falls'},
            {'id': 'assault', 'name': 'Agressão', 'name_en': 'Assault'},
            {'id': 'wounds', 'name': 'Feridas', 'name_en': 'Wounds'},
            {'id': 'burns', 'name': 'Queimaduras', 'name_en': 'Burns and Scalds'},
            {'id': 'bites_stings', 'name': 'Mordeduras e Picadas', 'name_en': 'Bites and Stings'},
        ]
    },
    'neurologico': {
        'name': 'Neurológico',
        'icon': '🧠',
        'flowcharts': [
            {'id': 'unconsciousness', 'name': 'Inconsciência', 'name_en': 'Unconsciousness'},
            {'id': 'seizures', 'name': 'Convulsões', 'name_en': 'Fits'},
            {'id': 'collapsed_adult', 'name': 'Colapso no Adulto', 'name_en': 'Collapsed Adult'},
        ]
    },
    'cardiovascular': {
        'name': 'Cardiovascular',
        'icon': '❤️',
        'flowcharts': [
            {'id': 'palpitations', 'name': 'Palpitações', 'name_en': 'Palpitations'},
        ]
    },
    'gastrointestinal': {
        'name': 'Gastrointestinal',
        'icon': '🫃',
        'flowcharts': [
            {'id': 'vomiting', 'name': 'Vômitos', 'name_en': 'Vomiting'},
            {'id': 'diarrhea', 'name': 'Diarreia', 'name_en': 'Diarrhoea and Vomiting'},
            {'id': 'gi_bleeding', 'name': 'Hemorragia GI', 'name_en': 'GI Bleeding'},
        ]
    },
    'geral': {
        'name': 'Apresentação Geral',
        'icon': '👤',
        'flowcharts': [
            {'id': 'unwell_adult', 'name': 'Indisposição no Adulto', 'name_en': 'Unwell Adult'},
            {'id': 'unwell_child', 'name': 'Indisposição na Criança', 'name_en': 'Unwell Child'},
            {'id': 'worried_parent', 'name': 'Pais Preocupados', 'name_en': 'Worried Parent'},
            {'id': 'crying_baby', 'name': 'Bebê Chorando', 'name_en': 'Crying Baby'},
        ]
    },
    'mental': {
        'name': 'Saúde Mental',
        'icon': '🧩',
        'flowcharts': [
            {'id': 'mental_illness', 'name': 'Doença Mental', 'name_en': 'Mental Illness'},
            {'id': 'self_harm', 'name': 'Autolesão', 'name_en': 'Self Harm'},
            {'id': 'strange_behavior', 'name': 'Comportamento Estranho', 'name_en': 'Behaving Strangely'},
            {'id': 'overdose', 'name': 'Intoxicação/Overdose', 'name_en': 'Overdose and Poisoning'},
            {'id': 'alcohol', 'name': 'Embriaguez Aparente', 'name_en': 'Apparently Drunk'},
        ]
    },
    'pele': {
        'name': 'Pele e Infecções',
        'icon': '🦠',
        'flowcharts': [
            {'id': 'rashes', 'name': 'Erupções Cutâneas', 'name_en': 'Rashes'},
            {'id': 'local_infection', 'name': 'Infecções Locais/Abscessos', 'name_en': 'Local Infection'},
            {'id': 'allergy', 'name': 'Alergia', 'name_en': 'Allergy'},
        ]
    },
    'olhos_ouvidos': {
        'name': 'Olhos, Ouvidos, Nariz',
        'icon': '👁️',
        'flowcharts': [
            {'id': 'eye_problems', 'name': 'Problemas Oftalmológicos', 'name_en': 'Eye Problems'},
            {'id': 'ear_problems', 'name': 'Problemas no Ouvido', 'name_en': 'Ear Problems'},
            {'id': 'facial_problems', 'name': 'Problemas Faciais/Nasais', 'name_en': 'Facial Problems'},
            {'id': 'foreign_body', 'name': 'Corpo Estranho', 'name_en': 'Foreign Body'},
        ]
    },
    'urinario': {
        'name': 'Urológico',
        'icon': '🚰',
        'flowcharts': [
            {'id': 'urinary_problems', 'name': 'Problemas Urinários', 'name_en': 'Urinary Problems'},
        ]
    },
    'gineco_obstetricia': {
        'name': 'Gineco-Obstetrícia',
        'icon': '🤰',
        'flowcharts': [
            {'id': 'pregnancy', 'name': 'Gravidez', 'name_en': 'Pregnancy'},
            {'id': 'pv_bleeding', 'name': 'Sangramento Vaginal', 'name_en': 'PV Bleeding'},
            {'id': 'sexual_assault', 'name': 'Agressão Sexual', 'name_en': 'Sexual Assault'},
            {'id': 'sti', 'name': 'DST', 'name_en': 'Sexually Transmitted Infection'},
        ]
    },
    'outros': {
        'name': 'Outros',
        'icon': '📋',
        'flowcharts': [
            {'id': 'diabetes', 'name': 'Diabetes', 'name_en': 'Diabetes'},
            {'id': 'chemical_exposure', 'name': 'Exposição Química', 'name_en': 'Chemical Exposure'},
            {'id': 'electrical_injury', 'name': 'Lesão Elétrica', 'name_en': 'Electrical Injury'},
            {'id': 'irritable_child', 'name': 'Criança Irritada', 'name_en': 'Irritable Child'},
            {'id': 'limping_child', 'name': 'Criança Mancando', 'name_en': 'Limping Child'},
        ]
    }
}

# Discriminators for each flowchart (starting with headache as complete example)
FLOWCHART_DISCRIMINATORS = {
    'headache': [
        {'id': 'airway_compromise', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, incapacidade de manter VA pérvia', 'critical': True},
        {'id': 'inadequate_breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, uso musculatura acessória, cianose', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco, hipotensão', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'active_seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Movimentos tônico-clônicos', 'critical': True},
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
    ],
    'chest_pain': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, esforço grave', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco, hipotensão', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'cardiac_pain', 'priority': 'very_urgent', 'question': 'Dor cardíaca?', 'desc': 'Precordial, opressiva, irradiação braço/mandíbula', 'critical': True},
        {'id': 'acute_sob', 'priority': 'very_urgent', 'question': 'Dispneia aguda?', 'desc': 'Falta de ar súbita', 'critical': True},
        {'id': 'abnormal_pulse', 'priority': 'very_urgent', 'question': 'Pulso anormal?', 'desc': 'FC <40 ou >130, irregular', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, síncope', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'pleuritic', 'priority': 'very_urgent', 'question': 'Dor pleurítica aguda?', 'desc': 'Ventilatório-dependente', 'critical': True},
        {'id': 'hx_cardiac', 'priority': 'very_urgent', 'question': 'Cardiopatia + dor atual?', 'desc': 'História cardíaca conhecida', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
        {'id': 'recent', 'priority': 'urgent', 'question': 'Início recente (<7 dias)?', 'desc': 'Última semana', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?', 'desc': 'Dor conhecida', 'critical': False},
    ],
    'abdominal_pain': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR anormal', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'peritonism', 'priority': 'very_urgent', 'question': 'Sinais de peritonismo?', 'desc': 'Abdome em tábua, Blumberg+', 'critical': True},
        {'id': 'pulsatile_mass', 'priority': 'very_urgent', 'question': 'Massa pulsátil?', 'desc': 'Suspeita de aneurisma', 'critical': True},
        {'id': 'pregnant_bleed', 'priority': 'very_urgent', 'question': 'Gestante + sangramento?', 'desc': 'Sangramento vaginal na gravidez', 'critical': True},
        {'id': 'gi_bleed', 'priority': 'very_urgent', 'question': 'Melena/hematêmese?', 'desc': 'Sangue nas fezes/vômito', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
        {'id': 'vomiting', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Múltiplos episódios', 'critical': False},
        {'id': 'pregnant', 'priority': 'urgent', 'question': 'Gestante?', 'desc': 'Gravidez', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Dor habitual', 'critical': False},
    ],
    'shortness_of_breath': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, estridor', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR <10 ou >30, cianose', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'severe_distress', 'priority': 'very_urgent', 'question': 'Desconforto grave?', 'desc': 'Não fala frases completas', 'critical': True},
        {'id': 'stridor', 'priority': 'very_urgent', 'question': 'Estridor?', 'desc': 'Som agudo inspiratório', 'critical': True},
        {'id': 'low_spo2', 'priority': 'very_urgent', 'question': 'SpO₂ <94%?', 'desc': 'Saturação baixa', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, agitação', 'critical': True},
        {'id': 'acute_onset', 'priority': 'very_urgent', 'question': 'Início súbito?', 'desc': 'Dispneia abrupta', 'critical': True},
        {'id': 'chest_pain', 'priority': 'very_urgent', 'question': 'Dor torácica?', 'desc': 'Dor + dispneia', 'critical': True},
        {'id': 'mod_distress', 'priority': 'urgent', 'question': 'Desconforto moderado?', 'desc': 'Fala com dificuldade', 'critical': False},
        {'id': 'wheeze', 'priority': 'urgent', 'question': 'Sibilância?', 'desc': 'Chiado', 'critical': False},
        {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
        {'id': 'mild_sob', 'priority': 'standard', 'question': 'Dispneia leve?', 'desc': 'Aos esforços', 'critical': False},
        {'id': 'chronic', 'priority': 'non_urgent', 'question': 'DPOC/Asma estável?', 'desc': 'Sem piora', 'critical': False},
    ],
    'unwell_adult': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR anormal', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Atividade convulsiva', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão aguda', 'critical': True},
        {'id': 'purpura', 'priority': 'very_urgent', 'question': 'Púrpura/petéquias?', 'desc': 'Rash não branqueável', 'critical': True},
        {'id': 'meningism', 'priority': 'very_urgent', 'question': 'Sinais de meningismo?', 'desc': 'Rigidez nuca', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'very_hot', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
        {'id': 'vomiting', 'priority': 'urgent', 'question': 'Vômitos persistentes?', 'desc': 'Múltiplos episódios', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Sem mudança', 'critical': False},
    ],
    'limb_problems': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'exsanguinating', 'priority': 'immediate', 'question': 'Hemorragia exsanguinante?', 'desc': 'Sangramento maciço', 'critical': True},
        {'id': 'no_pulse', 'priority': 'very_urgent', 'question': 'Sem pulso distal?', 'desc': 'Membro sem pulso', 'critical': True},
        {'id': 'open_fracture', 'priority': 'very_urgent', 'question': 'Fratura exposta?', 'desc': 'Osso visível', 'critical': True},
        {'id': 'gross_deformity', 'priority': 'very_urgent', 'question': 'Deformidade grosseira?', 'desc': 'Angulação óbvia', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'cold_limb', 'priority': 'very_urgent', 'question': 'Membro frio/pálido?', 'desc': 'Isquemia', 'critical': True},
        {'id': 'neurovascular', 'priority': 'very_urgent', 'question': 'Déficit neurovascular?', 'desc': 'Parestesias, paresia', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'unable_weight', 'priority': 'urgent', 'question': 'Incapaz de apoiar peso?', 'desc': 'Não consegue andar', 'critical': False},
        {'id': 'hot_joint', 'priority': 'urgent', 'question': 'Articulação quente?', 'desc': 'Sinais inflamatórios', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico?', 'desc': 'Sem mudança', 'critical': False},
    ],
    'wounds': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Ferida cervical', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'exsanguinating', 'priority': 'immediate', 'question': 'Hemorragia exsanguinante?', 'desc': 'Sangramento maciço', 'critical': True},
        {'id': 'uncontrolled_bleed', 'priority': 'very_urgent', 'question': 'Sangramento não controlado?', 'desc': 'Hemorragia ativa', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'amputation', 'priority': 'very_urgent', 'question': 'Amputação?', 'desc': 'Perda de segmento', 'critical': True},
        {'id': 'neurovascular', 'priority': 'very_urgent', 'question': 'Déficit neurovascular?', 'desc': 'Perda sensibilidade', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'large_wound', 'priority': 'urgent', 'question': 'Ferida grande (>5cm)?', 'desc': 'Necessita sutura', 'critical': False},
        {'id': 'deep_wound', 'priority': 'urgent', 'question': 'Ferida profunda?', 'desc': 'Atinge músculo', 'critical': False},
        {'id': 'facial', 'priority': 'urgent', 'question': 'Ferida em face?', 'desc': 'Risco estético', 'critical': False},
        {'id': 'bite', 'priority': 'urgent', 'question': 'Mordedura?', 'desc': 'Alto risco infeccioso', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'small_wound', 'priority': 'standard', 'question': 'Ferida pequena?', 'desc': '<5cm', 'critical': False},
        {'id': 'old_wound', 'priority': 'non_urgent', 'question': 'Ferida antiga (>24h)?', 'desc': 'Fora da janela', 'critical': False},
    ],
    'falls': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR anormal', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, amnésia', 'critical': True},
        {'id': 'high_fall', 'priority': 'very_urgent', 'question': 'Queda de altura (>2m)?', 'desc': 'Alta energia', 'critical': True},
        {'id': 'head_injury', 'priority': 'very_urgent', 'question': 'Trauma craniano?', 'desc': 'Hematoma, laceração', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'deformity', 'priority': 'very_urgent', 'question': 'Deformidade grosseira?', 'desc': 'Fratura óbvia', 'critical': True},
        {'id': 'anticoagulant', 'priority': 'very_urgent', 'question': 'Anticoagulante + TCE?', 'desc': 'Risco sangramento', 'critical': True},
        {'id': 'neck_pain', 'priority': 'very_urgent', 'question': 'Dor cervical?', 'desc': 'Suspeita lesão cervical', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'unable_walk', 'priority': 'urgent', 'question': 'Incapaz de andar?', 'desc': 'Não deambula', 'critical': False},
        {'id': 'elderly', 'priority': 'urgent', 'question': 'Idoso (≥65)?', 'desc': 'Maior risco', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'trivial', 'priority': 'non_urgent', 'question': 'Queda trivial?', 'desc': 'Sem lesão', 'critical': False},
    ],
    'vomiting': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução, aspiração', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pele fria, pulso fraco', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'hematemesis', 'priority': 'very_urgent', 'question': 'Sangue no vômito?', 'desc': 'Hematêmese', 'critical': True},
        {'id': 'severe_dehydration', 'priority': 'very_urgent', 'question': 'Desidratação grave?', 'desc': 'Olhos fundos, confusão', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor abdominal intensa?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'projectile', 'priority': 'very_urgent', 'question': 'Vômito em jato?', 'desc': 'Suspeita obstrução', 'critical': True},
        {'id': 'meningism', 'priority': 'very_urgent', 'question': 'Sinais de meningismo?', 'desc': 'Rigidez nuca', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'hot', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
        {'id': 'persistent', 'priority': 'urgent', 'question': 'Vômitos >24h?', 'desc': 'Não tolera líquidos', 'critical': False},
        {'id': 'diabetes', 'priority': 'urgent', 'question': 'Diabético?', 'desc': 'Risco cetoacidose', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'single_episode', 'priority': 'non_urgent', 'question': 'Episódio único?', 'desc': 'Sem outros sintomas', 'critical': False},
    ],
    'head_injury': [
        {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução', 'critical': True},
        {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR anormal', 'critical': True},
        {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Pensar lesão associada', 'critical': True},
        {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo? GCS ≤8?', 'desc': 'AVPU = U', 'critical': True},
        {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Atividade convulsiva', 'critical': True},
        {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'GCS <15, confusão', 'critical': True},
        {'id': 'focal_deficit', 'priority': 'very_urgent', 'question': 'Déficit neurológico focal?', 'desc': 'Hemiparesia, anisocoria', 'critical': True},
        {'id': 'skull_signs', 'priority': 'very_urgent', 'question': 'Sinais fratura crânio?', 'desc': 'Battle, guaxinim, liquorreia', 'critical': True},
        {'id': 'severe_mechanism', 'priority': 'very_urgent', 'question': 'Mecanismo grave?', 'desc': 'Alta energia', 'critical': True},
        {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Cefaleia intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
        {'id': 'anticoagulant', 'priority': 'very_urgent', 'question': 'Uso de anticoagulante?', 'desc': 'Risco sangramento IC', 'critical': True},
        {'id': 'vomiting', 'priority': 'very_urgent', 'question': 'Vômitos após TCE?', 'desc': 'Sinal de HIC', 'critical': True},
        {'id': 'amnesia', 'priority': 'very_urgent', 'question': 'Amnésia do evento?', 'desc': 'Não lembra do trauma', 'critical': True},
        {'id': 'loc', 'priority': 'very_urgent', 'question': 'Perda de consciência?', 'desc': 'Mesmo breve', 'critical': True},
        {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Cefaleia moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
        {'id': 'scalp_wound', 'priority': 'urgent', 'question': 'Ferida em couro cabeludo?', 'desc': 'Laceração', 'critical': False},
        {'id': 'elderly', 'priority': 'urgent', 'question': 'Idoso (≥65)?', 'desc': 'Maior risco', 'critical': False},
        {'id': 'mild_pain', 'priority': 'standard', 'question': 'Cefaleia leve (1-4)?', 'desc': 'Tolerável', 'critical': False},
        {'id': 'minor', 'priority': 'non_urgent', 'question': 'Trauma menor, assintomático?', 'desc': 'Sem sintomas', 'critical': False},
    ],
}

# Generic discriminators for flowcharts not yet fully implemented
GENERIC_DISCRIMINATORS = [
    {'id': 'airway', 'priority': 'immediate', 'question': 'Comprometimento de via aérea?', 'desc': 'Obstrução ou incapacidade de manter VA', 'critical': True},
    {'id': 'breathing', 'priority': 'immediate', 'question': 'Respiração inadequada?', 'desc': 'FR anormal, esforço respiratório', 'critical': True},
    {'id': 'shock', 'priority': 'immediate', 'question': 'Sinais de choque?', 'desc': 'Hipotensão, pele fria, pulso fraco', 'critical': True},
    {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Não responsivo?', 'desc': 'AVPU = U', 'critical': True},
    {'id': 'seizure', 'priority': 'immediate', 'question': 'Convulsão ativa?', 'desc': 'Atividade convulsiva presente', 'critical': True},
    {'id': 'severe_hemorrhage', 'priority': 'immediate', 'question': 'Hemorragia exsanguinante?', 'desc': 'Sangramento não controlável', 'critical': True},
    {'id': 'altered_mental', 'priority': 'very_urgent', 'question': 'Alteração da consciência?', 'desc': 'Confusão, GCS <15', 'critical': True},
    {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa (8-10)?', 'desc': 'Dor insuportável', 'critical': False},
    {'id': 'high_fever', 'priority': 'very_urgent', 'question': 'Temp ≥41°C?', 'desc': 'Hipertermia', 'critical': True},
    {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada (5-7)?', 'desc': 'Dor significativa', 'critical': False},
    {'id': 'fever', 'priority': 'urgent', 'question': 'Temp 38.5-40.9°C?', 'desc': 'Febre', 'critical': False},
    {'id': 'acute', 'priority': 'urgent', 'question': 'Início agudo?', 'desc': 'Nas últimas horas', 'critical': False},
    {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve (1-4)?', 'desc': 'Dor tolerável', 'critical': False},
    {'id': 'recent', 'priority': 'standard', 'question': 'Problema recente?', 'desc': 'Últimos dias', 'critical': False},
    {'id': 'chronic', 'priority': 'non_urgent', 'question': 'Problema crônico estável?', 'desc': 'Sem alteração do padrão', 'critical': False},
]

def get_discriminators(flowchart_id):
    """Get discriminators for a flowchart, using generic if not implemented"""
    return FLOWCHART_DISCRIMINATORS.get(flowchart_id, GENERIC_DISCRIMINATORS)

def get_all_flowcharts():
    """Get flat list of all flowcharts"""
    all_fc = []
    for cat_id, cat_data in FLOWCHART_CATEGORIES.items():
        for fc in cat_data['flowcharts']:
            fc['category'] = cat_id
            fc['category_name'] = cat_data['name']
            fc['icon'] = cat_data['icon']
            all_fc.append(fc)
    return all_fc

def search_flowcharts(query, flowcharts):
    """Search flowcharts by name"""
    if not query:
        return flowcharts
    query = query.lower()
    return [fc for fc in flowcharts if query in fc['name'].lower() or query in fc['name_en'].lower()]

# Initialize session state
if 'flowchart_answers' not in st.session_state:
    st.session_state.flowchart_answers = {}
if 'selected_flowchart' not in st.session_state:
    st.session_state.selected_flowchart = None
if 'patient_info' not in st.session_state:
    st.session_state.patient_info = {'name': '', 'age': '', 'complaint': ''}
if 'show_summary' not in st.session_state:
    st.session_state.show_summary = False

# Header
st.markdown("""
<div class="main-header">
    <div style="display: flex; align-items: center; gap: 12px;">
        <svg width="40" height="40" viewBox="0 0 50 50" fill="none">
            <g transform="translate(5, 5)">
                <path d="M17 3 C17 1.5, 18.5 0, 20 0 L22 0 C23.5 0, 25 1.5, 25 3 L25 15 L25 27 L25 37 C25 38.5, 23.5 40, 22 40 L20 40 C18.5 40, 17 38.5, 17 37 L17 27 L17 15 Z" fill="none" stroke="#006B3F" stroke-width="3"/>
                <path d="M3 17 C1.5 17, 0 18.5, 0 20 L0 22 C0 23.5, 1.5 25, 3 25 L15 25 L27 25 L37 25 C38.5 25, 40 23.5, 40 22 L40 20 C40 18.5, 38.5 17, 37 17 L27 17 L15 17 Z" fill="none" stroke="#006B3F" stroke-width="3"/>
            </g>
        </svg>
        <div>
            <p class="logo-text">telepatia</p>
            <p class="subtitle">Sistema de Triagem de Manchester</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Layout
col_left, col_right = st.columns([2, 3])

with col_left:
    st.markdown("### 🔍 Selecionar Fluxograma")
    
    # Search box
    search_query = st.text_input("Buscar fluxograma...", placeholder="Ex: cefaleia, dor, dispneia...")
    
    all_flowcharts = get_all_flowcharts()
    filtered = search_flowcharts(search_query, all_flowcharts)
    
    if search_query:
        # Show search results
        st.markdown(f"**{len(filtered)} resultado(s)**")
        for fc in filtered:
            if st.button(f"{fc['icon']} {fc['name']}", key=f"btn_{fc['id']}", use_container_width=True):
                st.session_state.selected_flowchart = fc['id']
                st.session_state.flowchart_answers = {}
                st.session_state.show_summary = False
                st.rerun()
    else:
        # Show categories
        for cat_id, cat_data in FLOWCHART_CATEGORIES.items():
            with st.expander(f"{cat_data['icon']} {cat_data['name']} ({len(cat_data['flowcharts'])})"):
                for fc in cat_data['flowcharts']:
                    selected = st.session_state.selected_flowchart == fc['id']
                    btn_type = "primary" if selected else "secondary"
                    if st.button(fc['name'], key=f"cat_{fc['id']}", use_container_width=True, type=btn_type):
                        st.session_state.selected_flowchart = fc['id']
                        st.session_state.flowchart_answers = {}
                        st.session_state.show_summary = False
                        st.rerun()

with col_right:
    if st.session_state.selected_flowchart:
        # Find selected flowchart info
        fc_info = next((fc for fc in all_flowcharts if fc['id'] == st.session_state.selected_flowchart), None)
        
        if fc_info:
            st.markdown(f"### {fc_info['icon']} {fc_info['name']}")
            st.caption(f"{fc_info['name_en']} | Categoria: {fc_info['category_name']}")
            
            # Safety warning
            st.markdown("""
            <div class="safety-warning">
                ⚠️ <strong>Avalie de CIMA para BAIXO.</strong> O primeiro SIM determina a prioridade. Em dúvida, escolha a mais grave.
            </div>
            """, unsafe_allow_html=True)
            
            # Get discriminators
            discriminators = get_discriminators(fc_info['id'])
            
            # Calculate result
            result = None
            for disc in discriminators:
                if st.session_state.flowchart_answers.get(disc['id']) == True:
                    result = {
                        'priority': disc['priority'],
                        'discriminator': disc['question'],
                        'critical': disc['critical']
                    }
                    break
            
            # Show result banner if we have one
            if result:
                p = PRIORITIES[result['priority']]
                st.markdown(f"""
                <div class="result-banner priority-{result['priority']}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <span style="font-size: 22px; font-weight: 700; color: {p['color']};">{p['label']}</span>
                            <span style="color: #64748b; margin-left: 8px; font-size: 14px;">{p['time']}</span>
                        </div>
                        {'<span style="background:#dc2626;color:white;padding:3px 8px;border-radius:4px;font-size:11px;">CRÍTICO</span>' if result['critical'] else ''}
                    </div>
                    <div style="font-size: 13px; color: #475569; margin-top: 5px;">Discriminador: {result['discriminator']}</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Discriminator questions grouped by priority
            current_priority = None
            for disc in discriminators:
                # Check if higher priority was already positive
                disc_idx = discriminators.index(disc)
                higher_positive = any(st.session_state.flowchart_answers.get(discriminators[i]['id']) == True for i in range(disc_idx))
                
                # Priority header
                if disc['priority'] != current_priority:
                    current_priority = disc['priority']
                    p = PRIORITIES[current_priority]
                    st.markdown(f"""
                    <div style="background:{p['bg']};border-left:3px solid {p['color']};padding:6px 10px;margin-top:10px;border-radius:0 4px 4px 0;">
                        <span style="color:{p['color']};font-weight:600;font-size:13px;">● {p['label']} ({p['time']})</span>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Question row
                col1, col2 = st.columns([3, 1])
                with col1:
                    critical_mark = "🔴 " if disc['critical'] else ""
                    st.markdown(f"**{critical_mark}{disc['question']}**")
                    st.caption(disc['desc'])
                
                with col2:
                    answer = st.radio(
                        f"r_{disc['id']}",
                        options=["—", "SIM", "NÃO"],
                        key=disc['id'],
                        horizontal=True,
                        label_visibility="collapsed",
                        disabled=higher_positive
                    )
                    if answer == "SIM":
                        st.session_state.flowchart_answers[disc['id']] = True
                    elif answer == "NÃO":
                        st.session_state.flowchart_answers[disc['id']] = False
            
            # Actions
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("🔄 Limpar", use_container_width=True):
                    st.session_state.flowchart_answers = {}
                    st.session_state.show_summary = False
                    st.rerun()
            with col_b:
                if st.button("📋 Gerar Resumo", use_container_width=True, type="primary", disabled=result is None):
                    st.session_state.show_summary = True
                    st.rerun()
            
            # Summary section
            if result and st.session_state.show_summary:
                st.markdown("---")
                st.markdown("### 📋 Resumo do Atendimento")
                
                p = PRIORITIES[result['priority']]
                
                # Answered discriminators
                answered_yes = [d for d in discriminators if st.session_state.flowchart_answers.get(d['id']) == True]
                answered_no = [d for d in discriminators if st.session_state.flowchart_answers.get(d['id']) == False]
                
                st.markdown(f"""
                <div class="summary-box">
                    <h4 style="margin:0 0 15px 0;color:#334155;">Dados da Triagem</h4>
                    <table style="width:100%;font-size:14px;">
                        <tr><td style="padding:5px 0;color:#64748b;width:150px;">Data/Hora:</td><td><strong>{datetime.now().strftime('%d/%m/%Y %H:%M')}</strong></td></tr>
                        <tr><td style="padding:5px 0;color:#64748b;">Fluxograma:</td><td><strong>{fc_info['name']}</strong></td></tr>
                        <tr><td style="padding:5px 0;color:#64748b;">Categoria:</td><td>{fc_info['category_name']}</td></tr>
                    </table>
                </div>
                """, unsafe_allow_html=True)
                
                # Classification
                st.markdown(f"""
                <div class="result-banner priority-{result['priority']}" style="margin:10px 0;">
                    <div style="font-size:12px;color:#64748b;margin-bottom:5px;">CLASSIFICAÇÃO</div>
                    <div style="font-size:28px;font-weight:700;color:{p['color']};">{p['label']}</div>
                    <div style="font-size:16px;color:{p['color']};margin-top:5px;">Tempo máximo: {p['time']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Discriminator that determined priority
                st.markdown(f"""
                <div class="summary-box">
                    <h4 style="margin:0 0 10px 0;color:#334155;">Discriminador Determinante</h4>
                    <div style="background:{p['bg']};padding:10px;border-radius:6px;border-left:4px solid {p['color']};">
                        <strong>{result['discriminator']}</strong>
                        {'<span style="background:#dc2626;color:white;padding:2px 6px;border-radius:3px;font-size:10px;margin-left:8px;">CRÍTICO</span>' if result['critical'] else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Other positive discriminators
                if len(answered_yes) > 1:
                    st.markdown("**Outros discriminadores positivos:**")
                    for d in answered_yes[1:]:
                        st.markdown(f"- {d['question']}")
                
                # Encaminhamento
                st.markdown(f"""
                <div class="encaminhamento-box">
                    <div style="font-size:12px;opacity:0.8;margin-bottom:5px;">ENCAMINHAMENTO</div>
                    <div style="font-size:16px;font-weight:600;">{p['encaminhamento']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Safety footer
                st.markdown("""
                <div style="background:#f8fafc;border-radius:6px;padding:12px;font-size:12px;color:#64748b;margin-top:15px;">
                    <strong>⚠️ Aviso:</strong> Este sistema é ferramenta de apoio à decisão clínica. 
                    A classificação final deve considerar o julgamento do profissional de saúde.
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="text-align:center;padding:60px 20px;color:#94a3b8;">
            <div style="font-size:48px;margin-bottom:15px;">🔍</div>
            <div style="font-size:16px;">Selecione um fluxograma para iniciar a triagem</div>
            <div style="font-size:13px;margin-top:10px;">Use a busca ou navegue pelas categorias</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#64748b;font-size:12px;padding:10px;">
    <strong style="color:#006B3F;">telepatia</strong> | Sistema de Escalas Médicas | 52 Fluxogramas Manchester
</div>
""", unsafe_allow_html=True)
