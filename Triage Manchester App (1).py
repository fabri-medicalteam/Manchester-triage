import streamlit as st

# Page config
st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Telepatia branding
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'DM Sans', sans-serif;
    }
    
    .main-header {
        background: white;
        padding: 20px 30px;
        border-radius: 12px;
        border-bottom: 3px solid #006B3F;
        margin-bottom: 20px;
    }
    
    .logo-text {
        color: #006B3F;
        font-size: 28px;
        font-weight: 500;
        margin: 0;
    }
    
    .subtitle {
        color: #64748b;
        font-size: 14px;
        margin-top: 5px;
    }
    
    .result-banner {
        padding: 20px;
        border-radius: 8px;
        margin: 15px 0;
        border-left: 5px solid;
    }
    
    .priority-immediate { background-color: #FEE2E2; border-color: #DC2626; }
    .priority-very_urgent { background-color: #FFEDD5; border-color: #EA580C; }
    .priority-urgent { background-color: #FEF9C3; border-color: #EAB308; }
    .priority-standard { background-color: #DCFCE7; border-color: #22C55E; }
    .priority-non_urgent { background-color: #DBEAFE; border-color: #3B82F6; }
    
    .discriminator-tag {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 12px;
        margin: 2px;
        color: white;
    }
    
    .tag-immediate { background-color: #DC2626; }
    .tag-very_urgent { background-color: #EA580C; }
    .tag-urgent { background-color: #EAB308; }
    .tag-standard { background-color: #22C55E; }
    .tag-non_urgent { background-color: #3B82F6; }
    
    .safety-warning {
        background-color: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 8px;
        padding: 15px;
        margin: 15px 0;
        color: #92400e !important;
    }
    
    .safety-warning strong {
        color: #78350f !important;
    }
    
    .safety-footer {
        background-color: #f8fafc;
        border-radius: 6px;
        padding: 12px;
        font-size: 12px;
        color: #475569 !important;
        margin-top: 20px;
    }
    
    .safety-footer strong {
        color: #334155 !important;
    }
    
    .stButton > button {
        border-radius: 6px;
    }
    
    div[data-testid="stExpander"] {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Priority configuration
PRIORITIES = {
    'immediate': {'color': '#DC2626', 'label': 'IMEDIATO', 'label_en': 'IMMEDIATE', 'time': '0 min', 'bg': '#FEE2E2'},
    'very_urgent': {'color': '#EA580C', 'label': 'MUITO URGENTE', 'label_en': 'VERY URGENT', 'time': '10 min', 'bg': '#FFEDD5'},
    'urgent': {'color': '#EAB308', 'label': 'URGENTE', 'label_en': 'URGENT', 'time': '60 min', 'bg': '#FEF9C3'},
    'standard': {'color': '#22C55E', 'label': 'PADRÃO', 'label_en': 'STANDARD', 'time': '120 min', 'bg': '#DCFCE7'},
    'non_urgent': {'color': '#3B82F6', 'label': 'NÃO URGENTE', 'label_en': 'NON-URGENT', 'time': '240 min', 'bg': '#DBEAFE'}
}

PRIORITY_ORDER = ['immediate', 'very_urgent', 'urgent', 'standard', 'non_urgent']

# Headache flowchart discriminators
HEADACHE_DISCRIMINATORS = [
    # IMMEDIATE
    {'id': 'airway_compromise', 'priority': 'immediate', 'question': 'Há comprometimento de via aérea?', 
     'description': 'Obstrução total ou parcial, incapacidade de manter via aérea pérvia', 'critical': True},
    {'id': 'inadequate_breathing', 'priority': 'immediate', 'question': 'A respiração está inadequada?',
     'description': 'FR <10 ou >30, uso de musculatura acessória, cianose', 'critical': True},
    {'id': 'shock', 'priority': 'immediate', 'question': 'Há sinais de choque?',
     'description': 'Pele fria/pegajosa, pulso fraco, hipotensão, alteração de consciência', 'critical': True},
    {'id': 'unresponsive', 'priority': 'immediate', 'question': 'Paciente não responsivo?',
     'description': 'AVPU = U (não responde a estímulos)', 'critical': True},
    {'id': 'active_seizure', 'priority': 'immediate', 'question': 'Está em convulsão ativa?',
     'description': 'Movimentos tônico-clônicos presentes', 'critical': True},
    
    # VERY URGENT
    {'id': 'altered_consciousness', 'priority': 'very_urgent', 'question': 'Há alteração do nível de consciência?',
     'description': 'GCS <15, confusão aguda, letargia, AVPU = V ou P', 'critical': True},
    {'id': 'focal_neuro_deficit', 'priority': 'very_urgent', 'question': 'Há déficit neurológico focal agudo?',
     'description': 'Hemiparesia, afasia, parestesias unilaterais, alteração visual súbita', 'critical': True},
    {'id': 'meningism', 'priority': 'very_urgent', 'question': 'Há sinais de meningismo?',
     'description': 'Rigidez de nuca, fotofobia, sinal de Kernig/Brudzinski', 'critical': True},
    {'id': 'sudden_onset_severe', 'priority': 'very_urgent', 'question': 'Cefaleia de início súbito e intenso?',
     'description': '"Pior dor de cabeça da vida", início em segundos/minutos (thunderclap)', 'critical': True},
    {'id': 'severe_pain', 'priority': 'very_urgent', 'question': 'Dor intensa? (NRS 8-10)',
     'description': 'Paciente refere dor insuportável', 'critical': False},
    {'id': 'purpura_rash', 'priority': 'very_urgent', 'question': 'Há púrpura ou petéquias?',
     'description': 'Manchas que não desaparecem à digitopressão', 'critical': True},
    {'id': 'very_hot', 'priority': 'very_urgent', 'question': 'Temperatura ≥41°C?',
     'description': 'Hipertermia grave', 'critical': True},
    
    # URGENT
    {'id': 'moderate_pain', 'priority': 'urgent', 'question': 'Dor moderada? (NRS 5-7)',
     'description': 'Dor significativa que interfere nas atividades', 'critical': False},
    {'id': 'hot', 'priority': 'urgent', 'question': 'Temperatura entre 38.5-40.9°C?',
     'description': 'Febre', 'critical': False},
    {'id': 'persistent_vomiting', 'priority': 'urgent', 'question': 'Vômitos persistentes?',
     'description': 'Múltiplos episódios de vômito', 'critical': False},
    {'id': 'history_unconsciousness', 'priority': 'urgent', 'question': 'História de perda de consciência?',
     'description': 'Síncope ou desmaio prévio associado', 'critical': False},
    {'id': 'acute_onset', 'priority': 'urgent', 'question': 'Início agudo? (< 12 horas)',
     'description': 'Cefaleia de início nas últimas 12 horas', 'critical': False},
    
    # STANDARD
    {'id': 'mild_pain', 'priority': 'standard', 'question': 'Dor leve? (NRS 1-4)',
     'description': 'Dor presente mas tolerável', 'critical': False},
    {'id': 'warm', 'priority': 'standard', 'question': 'Temperatura entre 37.5-38.4°C?',
     'description': 'Febrícula', 'critical': False},
    {'id': 'recent_problem', 'priority': 'standard', 'question': 'Problema recente? (< 7 dias)',
     'description': 'Cefaleia iniciada na última semana', 'critical': False},
    
    # NON-URGENT
    {'id': 'chronic_problem', 'priority': 'non_urgent', 'question': 'Problema crônico sem alteração?',
     'description': 'Cefaleia usual, sem novos sintomas ou piora', 'critical': False}
]

# Vital signs evaluation functions
def evaluate_heart_rate(hr):
    if hr <= 0: return None
    if hr < 30 or hr > 180: return ('immediate', f'FC crítica ({hr} bpm)')
    if hr < 40 or hr > 130: return ('very_urgent', f'FC muito anormal ({hr} bpm)')
    if hr < 50 or hr > 110: return ('urgent', f'FC anormal ({hr} bpm)')
    if hr < 60 or hr > 100: return ('standard', f'FC levemente alterada ({hr} bpm)')
    return None

def evaluate_respiratory_rate(rr):
    if rr <= 0: return None
    if rr < 6 or rr > 35: return ('immediate', f'FR crítica ({rr} rpm)')
    if rr < 8 or rr > 25: return ('very_urgent', f'FR muito anormal ({rr} rpm)')
    if rr > 21 or rr < 9: return ('urgent', f'FR anormal ({rr} rpm)')
    if rr < 12 or rr > 20: return ('standard', f'FR levemente alterada ({rr} rpm)')
    return None

def evaluate_sbp(sbp):
    if sbp <= 0: return None
    if sbp < 70 or sbp > 220: return ('immediate', f'PAS crítica ({sbp} mmHg)')
    if sbp < 90 or sbp > 200: return ('very_urgent', f'PAS muito anormal ({sbp} mmHg)')
    if sbp < 100 or sbp > 180: return ('urgent', f'PAS anormal ({sbp} mmHg)')
    if sbp < 110 or sbp > 160: return ('standard', f'PAS levemente alterada ({sbp} mmHg)')
    return None

def evaluate_spo2(spo2, on_oxygen):
    if spo2 <= 0 or spo2 > 100: return None
    if spo2 < 85: return ('immediate', f'SpO2 crítica ({spo2}%)')
    if spo2 < 90 or (on_oxygen and spo2 < 95): return ('very_urgent', f'SpO2 muito baixa ({spo2}%{"em O₂" if on_oxygen else ""})')
    if spo2 < 94: return ('urgent', f'SpO2 baixa ({spo2}%)')
    if spo2 < 96: return ('standard', f'SpO2 levemente reduzida ({spo2}%)')
    return None

def evaluate_temperature(temp):
    if temp <= 0: return None
    if temp < 32 or temp > 42: return ('immediate', f'Temperatura crítica ({temp}°C)')
    if temp < 35 or temp >= 41: return ('very_urgent', f'Temperatura muito anormal ({temp}°C)')
    if temp >= 39: return ('urgent', f'Febre alta ({temp}°C)')
    if temp < 36 or temp >= 38: return ('standard', f'Temperatura alterada ({temp}°C)')
    return None

def evaluate_gcs(gcs):
    if gcs < 3 or gcs > 15: return None
    if gcs <= 8: return ('immediate', f'GCS ≤8 ({gcs}) - coma')
    if gcs <= 12: return ('very_urgent', f'GCS 9-12 ({gcs})')
    if gcs <= 14: return ('urgent', f'GCS 13-14 ({gcs})')
    return None

def evaluate_pain(pain):
    if pain < 0 or pain > 10: return None
    if pain >= 8: return ('very_urgent', f'Dor intensa (NRS {pain})')
    if pain >= 5: return ('urgent', f'Dor moderada (NRS {pain})')
    if pain >= 1: return ('standard', f'Dor leve (NRS {pain})')
    return None

def get_highest_priority(results):
    """Get highest priority from list of (priority, reason) tuples"""
    if not results:
        return 'non_urgent', []
    
    active = []
    highest = 'non_urgent'
    
    for result in results:
        if result:
            priority, reason = result
            active.append({'priority': priority, 'reason': reason})
            if PRIORITY_ORDER.index(priority) < PRIORITY_ORDER.index(highest):
                highest = priority
    
    return highest, active

# Initialize session state
if 'flowchart_answers' not in st.session_state:
    st.session_state.flowchart_answers = {}

# Header
st.markdown("""
<div class="main-header">
    <div style="display: flex; align-items: center; gap: 15px;">
        <svg width="50" height="50" viewBox="0 0 50 50" fill="none">
            <g transform="translate(5, 5)">
                <path d="M17 3 C17 1.5, 18.5 0, 20 0 L22 0 C23.5 0, 25 1.5, 25 3 L25 15 L25 27 L25 37 C25 38.5, 23.5 40, 22 40 L20 40 C18.5 40, 17 38.5, 17 37 L17 27 L17 15 Z" fill="none" stroke="#006B3F" stroke-width="3.5"/>
                <path d="M3 17 C1.5 17, 0 18.5, 0 20 L0 22 C0 23.5, 1.5 25, 3 25 L15 25 L27 25 L37 25 C38.5 25, 40 23.5, 40 22 L40 20 C40 18.5, 38.5 17, 37 17 L27 17 L15 17 Z" fill="none" stroke="#006B3F" stroke-width="3.5"/>
            </g>
        </svg>
        <div>
            <p class="logo-text">telepatia</p>
            <p class="subtitle">Sistema de Triagem de Manchester</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2 = st.tabs(["📋 Avaliação Rápida", "🔄 Fluxograma Cefaleia"])

# TAB 1: Quick Assessment
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Glasgow (GCS)")
        gcs_eye = st.selectbox("Abertura Ocular (E)", 
            options=[4, 3, 2, 1],
            format_func=lambda x: {4: "4 - Espontânea", 3: "3 - Ao comando verbal", 2: "2 - À dor", 1: "1 - Ausente"}[x])
        gcs_verbal = st.selectbox("Resposta Verbal (V)",
            options=[5, 4, 3, 2, 1],
            format_func=lambda x: {5: "5 - Orientado", 4: "4 - Confuso", 3: "3 - Palavras inapropriadas", 2: "2 - Sons incompreensíveis", 1: "1 - Ausente"}[x])
        gcs_motor = st.selectbox("Resposta Motora (M)",
            options=[6, 5, 4, 3, 2, 1],
            format_func=lambda x: {6: "6 - Obedece comandos", 5: "5 - Localiza dor", 4: "4 - Retirada à dor", 3: "3 - Flexão anormal", 2: "2 - Extensão", 1: "1 - Ausente"}[x])
        gcs_total = gcs_eye + gcs_verbal + gcs_motor
        
        gcs_color = "#DC2626" if gcs_total <= 8 else "#EA580C" if gcs_total <= 12 else "#EAB308" if gcs_total <= 14 else "#22C55E"
        st.markdown(f"**GCS Total:** <span style='color:{gcs_color}; font-size: 20px; font-weight: bold;'>{gcs_total}/15</span>", unsafe_allow_html=True)
        
        st.subheader("AVPU")
        avpu = st.radio("Nível de Consciência", ["A - Alerta", "V - Responde à Voz", "P - Responde à Dor", "U - Não Responsivo"], horizontal=True)
        
        st.subheader("Dor (NRS)")
        pain = st.slider("Escala de Dor", 0, 10, 0)
    
    with col2:
        st.subheader("Sinais Vitais")
        heart_rate = st.number_input("FC (bpm)", min_value=0, max_value=300, value=80)
        resp_rate = st.number_input("FR (rpm)", min_value=0, max_value=60, value=16)
        sbp = st.number_input("PAS (mmHg)", min_value=0, max_value=300, value=120)
        spo2 = st.number_input("SpO₂ (%)", min_value=0, max_value=100, value=98)
        on_oxygen = st.checkbox("Em uso de O₂")
        temperature = st.number_input("Temperatura (°C)", min_value=30.0, max_value=45.0, value=36.5, step=0.1)
    
    # Calculate results
    results = []
    
    # GCS
    results.append(evaluate_gcs(gcs_total))
    
    # AVPU
    avpu_map = {"A - Alerta": None, "V - Responde à Voz": ('urgent', 'AVPU: Responde à voz'), 
                "P - Responde à Dor": ('very_urgent', 'AVPU: Responde à dor'), "U - Não Responsivo": ('immediate', 'AVPU: Não responsivo')}
    results.append(avpu_map[avpu])
    
    # Vital signs
    results.append(evaluate_heart_rate(heart_rate))
    results.append(evaluate_respiratory_rate(resp_rate))
    results.append(evaluate_sbp(sbp))
    results.append(evaluate_spo2(spo2, on_oxygen))
    results.append(evaluate_temperature(temperature))
    results.append(evaluate_pain(pain))
    
    # Get final priority
    final_priority, active_discriminators = get_highest_priority(results)
    priority_info = PRIORITIES[final_priority]
    
    # Display result
    st.markdown("---")
    st.markdown(f"""
    <div class="result-banner priority-{final_priority}">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="font-size: 28px; font-weight: 700; color: {priority_info['color']};">{priority_info['label']}</span>
                <span style="color: #64748b; margin-left: 10px;">{priority_info['label_en']}</span>
            </div>
            <span style="font-size: 24px; font-weight: 600; color: {priority_info['color']};">{priority_info['time']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if active_discriminators:
        st.markdown("**Discriminadores ativos:**")
        tags_html = ""
        for d in active_discriminators:
            tags_html += f'<span class="discriminator-tag tag-{d["priority"]}">{d["reason"]}</span> '
        st.markdown(tags_html, unsafe_allow_html=True)

# TAB 2: Headache Flowchart
with tab2:
    st.markdown("""
    <div class="safety-warning">
        <strong>⚠️ Avaliação Sequencial Obrigatória</strong><br>
        Avalie TODOS os discriminadores de cima para baixo. O PRIMEIRO discriminador positivo determina a prioridade. 
        Em caso de dúvida, sempre opte pela categoria mais grave.
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate flowchart result
    flowchart_result = None
    for disc in HEADACHE_DISCRIMINATORS:
        if st.session_state.flowchart_answers.get(disc['id']) == True:
            flowchart_result = {
                'priority': disc['priority'],
                'discriminator': disc['question'],
                'critical': disc['critical']
            }
            break
    
    # Show result if any
    if flowchart_result:
        p = PRIORITIES[flowchart_result['priority']]
        critical_badge = '<span style="background:#dc2626;color:white;padding:2px 8px;border-radius:4px;font-size:11px;margin-left:10px;">CRÍTICO</span>' if flowchart_result['critical'] else ''
        st.markdown(f"""
        <div class="result-banner priority-{flowchart_result['priority']}">
            <span style="font-size: 20px; font-weight: 700; color: {p['color']};">{p['label']}</span>
            <span style="color: #64748b; margin-left: 8px;">{p['time']}</span>
            {critical_badge}
            <br><small style="color: #475569;">Discriminador: {flowchart_result['discriminator']}</small>
        </div>
        """, unsafe_allow_html=True)
    
    # Group discriminators by priority
    current_priority = None
    higher_priority_positive = False
    
    for disc in HEADACHE_DISCRIMINATORS:
        # Check if higher priority was positive
        if st.session_state.flowchart_answers.get(disc['id']) == True:
            higher_priority_positive = True
        
        # Priority header
        if disc['priority'] != current_priority:
            current_priority = disc['priority']
            p = PRIORITIES[current_priority]
            st.markdown(f"""
            <div style="background:{p['bg']};border-left:3px solid {p['color']};padding:8px 12px;margin-top:15px;">
                <span style="color:{p['color']};font-weight:600;">● {p['label']}</span>
                <span style="color:#64748b;font-size:12px;margin-left:8px;">({p['time']})</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Discriminator row
        col1, col2 = st.columns([4, 1])
        
        with col1:
            critical_marker = "🔴 " if disc['critical'] else ""
            st.markdown(f"**{critical_marker}{disc['question']}**")
            st.caption(disc['description'])
        
        with col2:
            # Check if this discriminator should be disabled
            disc_idx = HEADACHE_DISCRIMINATORS.index(disc)
            is_disabled = any(
                st.session_state.flowchart_answers.get(HEADACHE_DISCRIMINATORS[i]['id']) == True 
                for i in range(disc_idx)
            )
            
            answer = st.radio(
                f"resp_{disc['id']}", 
                options=["—", "SIM", "NÃO"],
                key=disc['id'],
                horizontal=True,
                label_visibility="collapsed",
                disabled=is_disabled
            )
            
            if answer == "SIM":
                st.session_state.flowchart_answers[disc['id']] = True
            elif answer == "NÃO":
                st.session_state.flowchart_answers[disc['id']] = False
    
    # Reset button
    if st.button("🔄 Limpar Respostas"):
        st.session_state.flowchart_answers = {}
        st.rerun()
    
    # Safety footer
    st.markdown("""
    <div class="safety-footer">
        <strong>Lembrete de Segurança:</strong> Este sistema é uma ferramenta de apoio à decisão clínica. 
        A classificação final deve sempre considerar o julgamento clínico do profissional de saúde.
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 12px; padding: 20px;">
    <strong style="color: #006B3F;">telepatia</strong> | Sistema de Escalas Médicas<br>
    Baseado em NEWS2 e Manchester Triage System
</div>
""", unsafe_allow_html=True)
