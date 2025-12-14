import streamlit as st

st.set_page_config(
    page_title="Triagem de Manchester | Telepatia",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Global
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'IBM Plex Sans', sans-serif !important;
}

#MainMenu, footer, .stDeployButton, header {
    display: none !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
}

.stSelectbox > div > div,
.stNumberInput > div > div > input,
.stSlider > div > div {
    font-family: 'IBM Plex Sans', sans-serif !important;
}

.stTextArea textarea {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 14px !important;
}

/* Force light mode */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #FFFFFF !important;
    color: #111827 !important;
}
[data-testid="stSidebar"], [data-testid="stHeader"] {
    background-color: #FFFFFF !important;
}
.stTextInput>div>div>input, .stNumberInput>div>div>input, .stTextArea>div>div>textarea {
    background-color: #FFFFFF !important;
    color: #111827 !important;
}

/* Mobile responsive */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    [data-testid="column"] {
        width: 100% !important;
        flex: 100% !important;
        min-width: 100% !important;
    }
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }
    .stCheckbox {
        padding: 8px 0 !important;
    }
    .stCheckbox label {
        font-size: 14px !important;
    }
    .stNumberInput, .stSelectbox {
        margin-bottom: 0.5rem !important;
    }
}

/* Touch-friendly elements */
.stCheckbox > label {
    padding: 10px 0 !important;
    cursor: pointer !important;
}
.stCheckbox > label > div[data-testid="stCheckbox"] {
    min-height: 44px !important;
    display: flex !important;
    align-items: center !important;
}
.stRadio > div {
    gap: 8px !important;
}
.stRadio label {
    padding: 8px 12px !important;
}
</style>
""", unsafe_allow_html=True)

# Logo SVG Telepatia
LOGO_SVG = '''<svg width="180" height="42" viewBox="0 0 918 396" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M793.982 240.744C780.094 240.744 770.67 233.8 770.67 222.268C770.67 209.62 779.474 202.552 796.09 202.552H814.69V198.212C814.69 189.656 808.862 185.068 798.942 185.068C789.642 185.068 784.062 189.284 782.822 195.732H772.654C774.142 183.332 784.186 176.016 799.438 176.016C815.558 176.016 824.858 184.076 824.858 198.832V226.484C824.858 229.832 826.098 230.7 828.95 230.7H832.174V240H826.594C818.534 240 815.186 236.28 815.186 230.452V230.204C811.466 235.908 804.894 240.744 793.982 240.744ZM794.726 232.064C807.374 232.064 814.69 224.748 814.69 214.208V211.108H795.098C786.046 211.108 780.962 214.456 780.962 221.648C780.962 228.344 786.294 232.064 794.726 232.064Z" fill="#1F2937"/>
<path d="M748.456 240V176.76H758.624V240H748.456ZM753.54 165.972C749.944 165.972 747.092 163.244 747.092 159.524C747.092 155.804 749.944 153.076 753.54 153.076C757.136 153.076 759.988 155.804 759.988 159.524C759.988 163.244 757.136 165.972 753.54 165.972Z" fill="#1F2937"/>
<path d="M726.911 240C714.759 240 710.419 234.668 710.419 223.508V186.06H699.011V176.76H710.419V159.028H720.587V176.76H737.947V186.06H720.587V223.384C720.587 228.716 722.447 230.7 727.903 230.7H737.947V240H726.911Z" fill="#1F2937"/>
<path d="M660.537 240.744C646.649 240.744 637.225 233.8 637.225 222.268C637.225 209.62 646.029 202.552 662.645 202.552H681.245V198.212C681.245 189.656 675.417 185.068 665.497 185.068C656.197 185.068 650.617 189.284 649.377 195.732H639.209C640.697 183.332 650.741 176.016 665.993 176.016C682.113 176.016 691.413 184.076 691.413 198.832V226.484C691.413 229.832 692.653 230.7 695.505 230.7H698.729V240H693.149C685.089 240 681.741 236.28 681.741 230.452V230.204C678.021 235.908 671.449 240.744 660.537 240.744ZM661.281 232.064C673.929 232.064 681.245 224.748 681.245 214.208V211.108H661.653C652.601 211.108 647.517 214.456 647.517 221.648C647.517 228.344 652.849 232.064 661.281 232.064Z" fill="#1F2937"/>
<path d="M565.725 264.8V176.76H574.529L575.893 186.928C580.109 181.1 586.929 176.016 597.593 176.016C615.077 176.016 627.973 187.796 627.973 208.38C627.973 227.724 615.077 240.744 597.593 240.744C586.929 240.744 579.737 236.404 575.893 230.328V264.8H565.725ZM596.601 231.692C609.125 231.692 617.557 222.144 617.557 208.38C617.557 194.616 609.125 185.068 596.601 185.068C584.201 185.068 575.769 194.616 575.769 208.132C575.769 222.02 584.201 231.692 596.601 231.692Z" fill="#1F2937"/>
<path d="M525.225 240.744C506.253 240.744 493.853 227.724 493.853 208.38C493.853 189.16 506.005 176.016 523.861 176.016C541.593 176.016 553.621 187.548 553.621 206.768V210.364H504.517V211.232C504.517 223.26 512.453 231.692 524.481 231.692C533.657 231.692 540.601 226.98 542.709 218.796H553.001C550.521 231.444 539.857 240.744 525.225 240.744ZM504.889 201.808H542.957C541.965 191.02 534.525 184.944 523.985 184.944C514.685 184.944 506.005 191.268 504.889 201.808Z" fill="#1F2937"/>
<path d="M471.514 240V153.2H481.682V240H471.514Z" fill="#1F2937"/>
<path d="M431.014 240.744C412.042 240.744 399.642 227.724 399.642 208.38C399.642 189.16 411.794 176.016 429.65 176.016C447.382 176.016 459.41 187.548 459.41 206.768V210.364H410.306V211.232C410.306 223.26 418.242 231.692 430.27 231.692C439.446 231.692 446.39 226.98 448.498 218.796H458.79C456.31 231.444 445.646 240.744 431.014 240.744ZM410.678 201.808H448.746C447.754 191.02 440.314 184.944 429.774 184.944C420.474 184.944 411.794 191.268 410.678 201.808Z" fill="#1F2937"/>
<path d="M382.52 240C370.368 240 366.028 234.668 366.028 223.508V186.06H354.62V176.76H366.028V159.028H376.196V176.76H393.556V186.06H376.196V223.384C376.196 228.716 378.056 230.7 383.512 230.7H393.556V240H382.52Z" fill="#1F2937"/>
<path d="M196.147 84C218.966 84 237.464 102.652 237.464 125.66V155.417H260.977C267.55 155.417 272.879 160.747 272.879 167.32C272.879 173.894 267.55 179.223 260.977 179.224H225.659C219.14 179.224 213.855 173.938 213.854 167.419V125.66C213.606 115.552 205.774 107.806 196.147 107.806C186.368 107.806 178.44 115.8 178.439 125.66V167.419C178.439 173.938 173.154 179.223 166.635 179.224H126.398V179.25C125.975 179.232 125.647 179.223 125.317 179.223C115.538 179.223 107.611 187.217 107.61 197.077C107.61 206.938 115.538 214.932 125.317 214.932C125.647 214.932 125.975 214.921 126.301 214.903V214.934H166.635C173.154 214.933 178.439 220.218 178.439 226.737V268.495C178.44 278.356 186.368 286.35 196.147 286.35C205.774 286.349 213.606 278.603 213.849 268.956V226.737C213.855 220.218 219.14 214.933 225.659 214.933H266.878C276.603 214.932 284.435 207.186 284.678 197.539C284.684 190.504 290.013 185.175 296.587 185.175H314.098C320.671 185.175 326.001 190.504 326.001 197.078C326.001 203.652 320.671 208.98 314.098 208.98H306.58C301.5 226.189 285.693 238.738 266.977 238.738H237.464V268.495C237.464 291.503 218.966 310.155 196.147 310.155C173.484 310.155 155.085 291.757 154.835 268.966V238.738H126.398C125.742 238.732 125.53 238.737 125.317 238.737C102.499 238.737 84 220.085 84 197.077C84 174.069 102.499 155.417 125.317 155.417H154.83V125.562C154.836 125.199 155.081 102.403 196.147 84Z" fill="url(#grad1)"/>
<defs><linearGradient id="grad1" x1="251" y1="255" x2="125" y2="156" gradientUnits="userSpaceOnUse">
<stop stop-color="#068450"/><stop offset=".42" stop-color="#38A64A"/><stop offset="1" stop-color="#2FA879"/>
</linearGradient></defs></svg>'''

# Dados
P = {
    'immediate': {'c':'#DC2626','l':'IMEDIATO','t':'0 min','bg':'#FEE2E2','tx':'#991B1B'},
    'very_urgent': {'c':'#EA580C','l':'MUITO URGENTE','t':'10 min','bg':'#FFEDD5','tx':'#9A3412'},
    'urgent': {'c':'#CA8A04','l':'URGENTE','t':'60 min','bg':'#FEF9C3','tx':'#713F12'},
    'standard': {'c':'#16A34A','l':'PADRÃO','t':'120 min','bg':'#DCFCE7','tx':'#166534'},
    'non_urgent': {'c':'#2563EB','l':'NÃO URGENTE','t':'240 min','bg':'#DBEAFE','tx':'#1E40AF'}
}
PO = ['immediate','very_urgent','urgent','standard','non_urgent']

F = {
    'headache': {'n':'Cefaleia','d':[
        {'id':'h1','p':'immediate','q':'Comprometimento de via aérea','desc':'Obstrução ou incapacidade de manter'},
        {'id':'h2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30, cianose'},
        {'id':'h3','p':'immediate','q':'Choque','desc':'Pele fria, pulso fraco, hipotensão'},
        {'id':'h4','p':'immediate','q':'Não responsivo','desc':'AVPU = U'},
        {'id':'h5','p':'immediate','q':'Convulsão ativa','desc':'Movimentos tônico-clônicos'},
        {'id':'h6','p':'very_urgent','q':'Déficit neurológico focal','desc':'Hemiparesia, afasia, anisocoria'},
        {'id':'h7','p':'very_urgent','q':'Sinais de meningismo','desc':'Rigidez de nuca, fotofobia'},
        {'id':'h8','p':'very_urgent','q':'Cefaleia súbita intensa','desc':'Pior dor da vida, thunderclap'},
        {'id':'h9','p':'very_urgent','q':'Alteração da consciência','desc':'GCS <15, confusão'},
        {'id':'h10','p':'very_urgent','q':'Hipertermia grave','desc':'Temperatura >= 41°C'},
        {'id':'h11','p':'urgent','q':'Febre','desc':'Temperatura 38.5-40.9°C'},
        {'id':'h12','p':'urgent','q':'Vômitos persistentes','desc':'Múltiplos episódios'},
        {'id':'h13','p':'standard','q':'Febrícula','desc':'Temperatura 37.5-38.4°C'},
        {'id':'h14','p':'non_urgent','q':'Cefaleia crônica sem alarme','desc':'Padrão habitual'}]},
    'chest_pain': {'n':'Dor Torácica','d':[
        {'id':'cp1','p':'immediate','q':'Comprometimento de via aérea','desc':'Obstrução'},
        {'id':'cp2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30'},
        {'id':'cp3','p':'immediate','q':'Choque','desc':'Hipotensão, pele fria'},
        {'id':'cp4','p':'very_urgent','q':'Dor cardíaca típica','desc':'Precordial, opressão, irradiação'},
        {'id':'cp5','p':'very_urgent','q':'Dispneia aguda','desc':'Início súbito'},
        {'id':'cp6','p':'very_urgent','q':'Pulso anormal','desc':'Muito rápido, lento ou irregular'},
        {'id':'cp7','p':'very_urgent','q':'Hipóxia','desc':'SpO2 <95% em ar ambiente'},
        {'id':'cp8','p':'urgent','q':'Dor pleurítica','desc':'Piora com respiração'},
        {'id':'cp9','p':'urgent','q':'História cardíaca','desc':'IAM prévio, angina, stent'},
        {'id':'cp10','p':'standard','q':'Dor torácica leve','desc':'Sem sinais de alarme'},
        {'id':'cp11','p':'non_urgent','q':'Dor crônica','desc':'Padrão habitual'}]},
    'abdominal_pain': {'n':'Dor Abdominal','d':[
        {'id':'ab1','p':'immediate','q':'Comprometimento de via aérea','desc':'Obstrução'},
        {'id':'ab2','p':'immediate','q':'Choque','desc':'Hipotensão, taquicardia'},
        {'id':'ab3','p':'immediate','q':'Hemorragia grave','desc':'Hematêmese volumosa'},
        {'id':'ab4','p':'very_urgent','q':'Peritonismo','desc':'Rigidez abdominal, descompressão +'},
        {'id':'ab5','p':'very_urgent','q':'Sangramento GI','desc':'Melena, hematoquezia'},
        {'id':'ab6','p':'very_urgent','q':'Vômitos persistentes','desc':'Não tolera líquidos'},
        {'id':'ab7','p':'urgent','q':'Febre com dor abdominal','desc':'Temperatura >= 38.5°C'},
        {'id':'ab8','p':'urgent','q':'Possível gravidez','desc':'Idade fértil, amenorreia'},
        {'id':'ab9','p':'standard','q':'Dor abdominal leve','desc':'Sem sinais de alarme'},
        {'id':'ab10','p':'non_urgent','q':'Dor crônica','desc':'Padrão habitual'}]},
    'shortness_of_breath': {'n':'Dispneia','d':[
        {'id':'sb1','p':'immediate','q':'Via aérea comprometida','desc':'Obstrução, estridor grave'},
        {'id':'sb2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30, cianose'},
        {'id':'sb3','p':'immediate','q':'Choque','desc':'Hipotensão'},
        {'id':'sb4','p':'very_urgent','q':'Hipóxia grave','desc':'SpO2 <92%'},
        {'id':'sb5','p':'very_urgent','q':'Incapaz de falar frases','desc':'Fala entrecortada'},
        {'id':'sb6','p':'very_urgent','q':'Estridor','desc':'Som inspiratório agudo'},
        {'id':'sb7','p':'urgent','q':'Sibilância','desc':'Broncoespasmo audível'},
        {'id':'sb8','p':'urgent','q':'Febre com dispneia','desc':'Possível pneumonia'},
        {'id':'sb9','p':'standard','q':'Dispneia leve','desc':'Aos esforços, sem hipóxia'},
        {'id':'sb10','p':'non_urgent','q':'Dispneia crônica','desc':'Padrão habitual'}]},
    'unwell_adult': {'n':'Indisposição no Adulto','d':[
        {'id':'ua1','p':'immediate','q':'Via aérea comprometida','desc':'Obstrução'},
        {'id':'ua2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30'},
        {'id':'ua3','p':'immediate','q':'Choque','desc':'Hipotensão, pele fria'},
        {'id':'ua4','p':'immediate','q':'Não responsivo','desc':'AVPU = U'},
        {'id':'ua5','p':'very_urgent','q':'Alteração da consciência','desc':'Confusão, letargia'},
        {'id':'ua6','p':'very_urgent','q':'Hipertermia ou hipotermia','desc':'>= 41°C ou <= 35°C'},
        {'id':'ua7','p':'very_urgent','q':'Púrpura com febre','desc':'Petéquias não branqueáveis'},
        {'id':'ua8','p':'urgent','q':'Febre','desc':'Temperatura >= 38.5°C'},
        {'id':'ua9','p':'standard','q':'Febrícula','desc':'Temperatura 37.5-38.4°C'},
        {'id':'ua10','p':'non_urgent','q':'Sintomas crônicos','desc':'Padrão habitual'}]},
    'limb_problems': {'n':'Problemas em Membros','d':[
        {'id':'lp1','p':'immediate','q':'Hemorragia grave','desc':'Sangramento arterial'},
        {'id':'lp2','p':'very_urgent','q':'Ausência de pulso distal','desc':'Membro frio, pálido'},
        {'id':'lp3','p':'very_urgent','q':'Fratura exposta','desc':'Osso visível'},
        {'id':'lp4','p':'very_urgent','q':'Deformidade grosseira','desc':'Angulação anormal'},
        {'id':'lp5','p':'urgent','q':'Incapaz de apoiar peso','desc':'Não consegue deambular'},
        {'id':'lp6','p':'urgent','q':'Edema significativo','desc':'Inchaço importante'},
        {'id':'lp7','p':'standard','q':'Dor leve em membro','desc':'Mobilidade preservada'},
        {'id':'lp8','p':'non_urgent','q':'Dor crônica','desc':'Padrão habitual'}]},
    'wounds': {'n':'Feridas','d':[
        {'id':'w1','p':'immediate','q':'Hemorragia grave','desc':'Sangramento arterial, choque'},
        {'id':'w2','p':'very_urgent','q':'Sangramento não controlado','desc':'Não cede com pressão'},
        {'id':'w3','p':'very_urgent','q':'Amputação','desc':'Perda de parte do corpo'},
        {'id':'w4','p':'very_urgent','q':'Lesão de tendão ou nervo','desc':'Déficit motor ou sensitivo'},
        {'id':'w5','p':'urgent','q':'Ferida profunda','desc':'Exposição de estruturas'},
        {'id':'w6','p':'urgent','q':'Ferida contaminada','desc':'Sujeira, mordida'},
        {'id':'w7','p':'standard','q':'Ferida necessitando sutura','desc':'Bordas separadas'},
        {'id':'w8','p':'non_urgent','q':'Ferida superficial','desc':'Abrasão, corte pequeno'}]},
    'falls': {'n':'Quedas','d':[
        {'id':'f1','p':'immediate','q':'Via aérea comprometida','desc':'Obstrução'},
        {'id':'f2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30'},
        {'id':'f3','p':'immediate','q':'Choque','desc':'Hipotensão'},
        {'id':'f4','p':'immediate','q':'Não responsivo','desc':'AVPU = U'},
        {'id':'f5','p':'very_urgent','q':'Alteração da consciência','desc':'Confusão pós-queda'},
        {'id':'f6','p':'very_urgent','q':'Dor na coluna','desc':'Cervical ou lombar'},
        {'id':'f7','p':'very_urgent','q':'Deformidade','desc':'Angulação de membro'},
        {'id':'f8','p':'very_urgent','q':'Anticoagulante + TCE','desc':'Risco de sangramento'},
        {'id':'f9','p':'urgent','q':'Dor no quadril','desc':'Incapaz de movimentar'},
        {'id':'f10','p':'urgent','q':'Trauma craniano','desc':'Bateu a cabeça'},
        {'id':'f11','p':'standard','q':'Queda sem sinais de alarme','desc':'Deambulando'},
        {'id':'f12','p':'non_urgent','q':'Quedas recorrentes','desc':'Para investigação'}]},
    'vomiting': {'n':'Vômitos','d':[
        {'id':'v1','p':'immediate','q':'Via aérea comprometida','desc':'Risco de aspiração'},
        {'id':'v2','p':'immediate','q':'Choque','desc':'Desidratação grave'},
        {'id':'v3','p':'very_urgent','q':'Hematêmese','desc':'Sangue vivo ou borra de café'},
        {'id':'v4','p':'very_urgent','q':'Desidratação grave','desc':'Letargia, olhos fundos'},
        {'id':'v5','p':'urgent','q':'Desidratação moderada','desc':'Sede intensa, oligúria'},
        {'id':'v6','p':'urgent','q':'Vômitos persistentes','desc':'Não tolera líquidos'},
        {'id':'v7','p':'standard','q':'Vômitos ocasionais','desc':'Tolera líquidos'},
        {'id':'v8','p':'non_urgent','q':'Náuseas crônicas','desc':'Padrão habitual'}]},
    'head_injury': {'n':'Traumatismo Craniano','d':[
        {'id':'hi1','p':'immediate','q':'Via aérea comprometida','desc':'Obstrução'},
        {'id':'hi2','p':'immediate','q':'Respiração inadequada','desc':'FR <10 ou >30'},
        {'id':'hi3','p':'immediate','q':'Choque','desc':'Hipotensão'},
        {'id':'hi4','p':'immediate','q':'GCS menor ou igual a 8','desc':'Coma'},
        {'id':'hi5','p':'immediate','q':'Convulsão pós-trauma','desc':'Crise convulsiva'},
        {'id':'hi6','p':'very_urgent','q':'Alteração da consciência','desc':'GCS 9-14'},
        {'id':'hi7','p':'very_urgent','q':'Déficit neurológico','desc':'Anisocoria, hemiparesia'},
        {'id':'hi8','p':'very_urgent','q':'Sinais de fratura de crânio','desc':'Battle, olhos de guaxinim'},
        {'id':'hi9','p':'very_urgent','q':'Anticoagulante','desc':'Maior risco de sangramento'},
        {'id':'hi10','p':'very_urgent','q':'Mecanismo de alta energia','desc':'Queda >1m, ejeção'},
        {'id':'hi11','p':'urgent','q':'Perda de consciência','desc':'Mesmo que breve'},
        {'id':'hi12','p':'urgent','q':'Amnésia do evento','desc':'Não lembra do ocorrido'},
        {'id':'hi13','p':'urgent','q':'Cefaleia persistente','desc':'Pós-trauma'},
        {'id':'hi14','p':'standard','q':'TCE leve sem alarme','desc':'GCS 15, sem perda consciência'},
        {'id':'hi15','p':'non_urgent','q':'Avaliação tardia','desc':'>24h, assintomático'}]}
}

# Funções
def get_priority(items):
    if not items: return 'non_urgent'
    pv = {p:i for i,p in enumerate(PO)}
    best = 'non_urgent'
    for x in items:
        if pv.get(x['p'], 99) < pv.get(best, 99):
            best = x['p']
    return best

def eval_gcs(e, v, m):
    g = e + v + m
    if g <= 8: return 'immediate', g
    elif g <= 12: return 'very_urgent', g
    elif g <= 14: return 'urgent', g
    return None, g

def eval_vitals(hr, rr, sbp, spo2, temp):
    r = []
    if hr < 40 or hr > 150: r.append({'p':'immediate','q':f'FC {hr} bpm'})
    elif hr < 50 or hr > 130: r.append({'p':'very_urgent','q':f'FC {hr} bpm'})
    if rr < 10 or rr > 30: r.append({'p':'immediate','q':f'FR {rr} rpm'})
    elif rr < 12 or rr > 25: r.append({'p':'very_urgent','q':f'FR {rr} rpm'})
    if sbp < 80: r.append({'p':'immediate','q':f'PAS {sbp} mmHg'})
    elif sbp < 90 or sbp > 200: r.append({'p':'very_urgent','q':f'PAS {sbp} mmHg'})
    if spo2 < 90: r.append({'p':'immediate','q':f'SpO2 {spo2}%'})
    elif spo2 < 94: r.append({'p':'very_urgent','q':f'SpO2 {spo2}%'})
    if temp >= 41 or temp <= 32: r.append({'p':'immediate','q':f'Temp {temp}C'})
    elif temp >= 40 or temp <= 35: r.append({'p':'very_urgent','q':f'Temp {temp}C'})
    elif temp >= 38.5: r.append({'p':'urgent','q':f'Temp {temp}C'})
    return r

def eval_pain(p):
    if p >= 8: return 'very_urgent', f'Dor {p}/10'
    elif p >= 5: return 'urgent', f'Dor {p}/10'
    elif p >= 1: return 'standard', f'Dor {p}/10'
    return None, None

def generate_summary(findings, fc_name, gcs, priority, pain):
    lines = []
    lines.append(f"CLASSIFICAÇÃO: {P[priority]['l']} - Tempo alvo: {P[priority]['t']}")
    lines.append(f"Fluxograma: {fc_name}")
    lines.append(f"GCS: {gcs}/15")
    if pain > 0:
        lines.append(f"Dor: {pain}/10")
    if findings:
        lines.append("")
        lines.append("Achados positivos:")
        for f in findings:
            lines.append(f"  - {f['q']}")
    return "\n".join(lines)

# Session state
if 'fc' not in st.session_state:
    st.session_state.fc = 'headache'

# ========== HEADER ==========
st.markdown(f'''
<div style="background: #FFFFFF; padding: 16px 20px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 20px;">
    <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
        {LOGO_SVG}
        <div>
            <div style="font-size: 18px; font-weight: 600; color: #111827; letter-spacing: -0.02em;">Sistema de Triagem de Manchester</div>
            <div style="font-size: 13px; color: #6B7280; margin-top: 2px;">Ferramenta de apoio à decisão clínica</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# Placeholder para resultado no topo
result_placeholder = st.empty()

# Lista de achados
findings = []

# ========== LINHA 1: GCS + Sinais Vitais ==========
st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('''
    <div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
        Escala de Coma de Glasgow
    </div>
    ''', unsafe_allow_html=True)
    
    g1, g2, g3 = st.columns(3)
    with g1:
        eye = st.selectbox("Abertura Ocular", [4,3,2,1], 
            format_func=lambda x: {4:"4 - Espontânea", 3:"3 - Ao comando", 2:"2 - À dor", 1:"1 - Nenhuma"}[x])
    with g2:
        verbal = st.selectbox("Resposta Verbal", [5,4,3,2,1],
            format_func=lambda x: {5:"5 - Orientada", 4:"4 - Confusa", 3:"3 - Inapropriada", 2:"2 - Incompreensível", 1:"1 - Nenhuma"}[x])
    with g3:
        motor = st.selectbox("Resposta Motora", [6,5,4,3,2,1],
            format_func=lambda x: {6:"6 - Obedece", 5:"5 - Localiza", 4:"4 - Retirada", 3:"3 - Flexão", 2:"2 - Extensão", 1:"1 - Nenhuma"}[x])
    
    gcs_pri, gcs_val = eval_gcs(eye, verbal, motor)
    if gcs_pri:
        findings.append({'p': gcs_pri, 'q': f'GCS {gcs_val}'})
    
    gc1, gc2 = st.columns([1, 2])
    with gc1:
        st.markdown(f'''
        <div style="background: #F3F4F6; padding: 12px 16px; border-radius: 8px; text-align: center;">
            <div style="font-size: 12px; color: #6B7280;">GCS Total</div>
            <div style="font-size: 28px; font-weight: 700; color: #111827;">{gcs_val}</div>
        </div>
        ''', unsafe_allow_html=True)
    with gc2:
        st.markdown('<div style="font-size: 13px; color: #6B7280; margin-bottom: 8px;">AVPU</div>', unsafe_allow_html=True)
        avpu = st.radio("avpu", ["Alerta", "Responde à Voz", "Responde à Dor", "Não Responde"], 
                       horizontal=True, label_visibility="collapsed")
        avpu_map = {"Alerta": None, "Responde à Voz": 'urgent', "Responde à Dor": 'very_urgent', "Não Responde": 'immediate'}
        if avpu_map[avpu]:
            findings.append({'p': avpu_map[avpu], 'q': f'AVPU: {avpu}'})

with col2:
    st.markdown('''
    <div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
        Sinais Vitais
    </div>
    ''', unsafe_allow_html=True)
    
    v1, v2, v3 = st.columns(3)
    with v1:
        hr = st.number_input("FC (bpm)", 30, 250, 80)
        sbp = st.number_input("PAS (mmHg)", 40, 280, 120)
    with v2:
        rr = st.number_input("FR (rpm)", 4, 60, 16)
        spo2 = st.number_input("SpO2 (%)", 50, 100, 98)
    with v3:
        temp = st.number_input("Temp (C)", 30.0, 44.0, 36.5, 0.1)
        st.checkbox("Oxigênio suplementar")
    
    findings.extend(eval_vitals(hr, rr, sbp, spo2, temp))

# ========== LINHA 2: Escala de Dor ==========
st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
st.markdown('''
<div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
    Escala de Dor
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
    <div style="flex:1; text-align:center; padding:10px; background:#22C55E; border-radius:6px 0 0 6px;">
        <div style="font-size:14px; color:#FFF; font-weight:600;">0</div>
        <div style="font-size:11px; color:#FFF;">Sem dor</div>
    </div>
    <div style="flex:1; text-align:center; padding:10px; background:#84CC16;">
        <div style="font-size:14px; color:#FFF; font-weight:600;">1-3</div>
        <div style="font-size:11px; color:#FFF;">Leve</div>
    </div>
    <div style="flex:1; text-align:center; padding:10px; background:#EAB308;">
        <div style="font-size:14px; color:#FFF; font-weight:600;">4-6</div>
        <div style="font-size:11px; color:#FFF;">Moderada</div>
    </div>
    <div style="flex:1; text-align:center; padding:10px; background:#F97316;">
        <div style="font-size:14px; color:#FFF; font-weight:600;">7-8</div>
        <div style="font-size:11px; color:#FFF;">Intensa</div>
    </div>
    <div style="flex:1; text-align:center; padding:10px; background:#DC2626; border-radius:0 6px 6px 0;">
        <div style="font-size:14px; color:#FFF; font-weight:600;">9-10</div>
        <div style="font-size:11px; color:#FFF;">Insuportável</div>
    </div>
</div>
''', unsafe_allow_html=True)

pain = st.slider("Intensidade da dor", 0, 10, 0, label_visibility="collapsed")
pain_pri, pain_txt = eval_pain(pain)
if pain_pri:
    findings.append({'p': pain_pri, 'q': pain_txt})

# ========== LINHA 3: Seletor de Fluxograma ==========
st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
st.markdown('''
<div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
    Queixa Principal
</div>
''', unsafe_allow_html=True)

flowchart_options = {k: v['n'] for k, v in F.items()}
selected_fc = st.selectbox("Selecione o fluxograma", list(flowchart_options.keys()), 
                           format_func=lambda x: flowchart_options[x], label_visibility="collapsed")

if selected_fc != st.session_state.fc:
    st.session_state.fc = selected_fc
    st.rerun()

# ========== LINHA 4: Discriminadores ==========
st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)

fc_data = F[st.session_state.fc]
st.markdown(f'''
<div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
    Discriminadores: {fc_data['n']}
</div>
<div style="background: #FEF3C7; border-left: 4px solid #F59E0B; padding: 12px 16px; border-radius: 0 8px 8px 0; margin-bottom: 20px;">
    <span style="font-weight: 500; color: #92400E;">Avalie de cima para baixo. O primeiro SIM determina a prioridade.</span>
</div>
''', unsafe_allow_html=True)

# Agrupar por prioridade
disc_by_pri = {}
for d in fc_data['d']:
    disc_by_pri.setdefault(d['p'], []).append(d)

determined = None

for pri in PO:
    if pri not in disc_by_pri:
        continue
    
    p = P[pri]
    
    st.markdown(f'''
    <div style="background: {p['bg']}; border-left: 4px solid {p['c']}; padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 16px 0 12px 0;">
        <span style="font-weight: 600; color: {p['tx']}; font-size: 14px;">{p['l']}</span>
        <span style="color: {p['tx']}; opacity: 0.7; margin-left: 8px; font-size: 13px;">Tempo alvo: {p['t']}</span>
    </div>
    ''', unsafe_allow_html=True)
    
    for disc in disc_by_pri[pri]:
        key = f"d_{st.session_state.fc}_{disc['id']}"
        disabled = determined is not None
        
        col_check, col_text = st.columns([0.05, 0.95])
        with col_check:
            if disabled:
                st.markdown('<div style="color: #9CA3AF;">—</div>', unsafe_allow_html=True)
            else:
                checked = st.checkbox("", key=key, label_visibility="collapsed")
                if checked:
                    determined = pri
                    findings.append({'p': pri, 'q': disc['q']})
        with col_text:
            opacity = "0.4" if disabled else "1"
            st.markdown(f'''
            <div style="opacity: {opacity}; padding: 4px 0;">
                <span style="font-weight: 500; color: #1F2937;">{disc['q']}</span>
                <span style="color: #6B7280; font-size: 13px; margin-left: 8px;">{disc['desc']}</span>
            </div>
            ''', unsafe_allow_html=True)

# Botão limpar
st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)
if st.button("Limpar todas as respostas"):
    for k in list(st.session_state.keys()):
        if k.startswith('d_'):
            del st.session_state[k]
    st.rerun()

# ========== RESULTADO (calculado) ==========
final_priority = get_priority(findings)
p_result = P[final_priority]

findings_tags = "".join([
    f'<span style="display: inline-block; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: 500; color: #FFF; background: {P[f["p"]]["c"]}; margin: 2px 4px 2px 0;">{f["q"]}</span>'
    for f in findings[:6]
])

# Resultado no TOPO
with result_placeholder.container():
    st.markdown(f'''
    <div style="background: {p_result['bg']}; border: 2px solid {p_result['c']}; border-radius: 16px; padding: 16px 20px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
            <div>
                <div style="font-size: 12px; color: {p_result['tx']}; opacity: 0.8;">Classificação de Risco</div>
                <div style="font-size: 24px; font-weight: 700; color: {p_result['tx']}; letter-spacing: -0.02em;">{p_result['l']}</div>
                <div style="margin-top: 8px; font-size: 11px;">{findings_tags if findings_tags else '<span style="color: #6B7280;">Nenhum achado</span>'}</div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 12px; color: {p_result['tx']}; opacity: 0.8;">Tempo Alvo</div>
                <div style="font-size: 28px; font-weight: 700; color: {p_result['tx']};">{p_result['t']}</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# ========== LEGENDA DE TEMPOS (Full Width) ==========
st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
st.markdown('''
<div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
    Categorias de Prioridade
</div>
''', unsafe_allow_html=True)

st.markdown(f'''
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 8px;">
    <div style="background: {P['immediate']['bg']}; border-left: 4px solid {P['immediate']['c']}; padding: 12px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 12px; font-weight: 600; color: {P['immediate']['tx']};">{P['immediate']['l']}</div>
        <div style="font-size: 18px; font-weight: 700; color: {P['immediate']['tx']}; margin-top: 2px;">{P['immediate']['t']}</div>
    </div>
    <div style="background: {P['very_urgent']['bg']}; border-left: 4px solid {P['very_urgent']['c']}; padding: 12px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 12px; font-weight: 600; color: {P['very_urgent']['tx']};">{P['very_urgent']['l']}</div>
        <div style="font-size: 18px; font-weight: 700; color: {P['very_urgent']['tx']}; margin-top: 2px;">{P['very_urgent']['t']}</div>
    </div>
    <div style="background: {P['urgent']['bg']}; border-left: 4px solid {P['urgent']['c']}; padding: 12px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 12px; font-weight: 600; color: {P['urgent']['tx']};">{P['urgent']['l']}</div>
        <div style="font-size: 18px; font-weight: 700; color: {P['urgent']['tx']}; margin-top: 2px;">{P['urgent']['t']}</div>
    </div>
    <div style="background: {P['standard']['bg']}; border-left: 4px solid {P['standard']['c']}; padding: 12px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 12px; font-weight: 600; color: {P['standard']['tx']};">{P['standard']['l']}</div>
        <div style="font-size: 18px; font-weight: 700; color: {P['standard']['tx']}; margin-top: 2px;">{P['standard']['t']}</div>
    </div>
    <div style="background: {P['non_urgent']['bg']}; border-left: 4px solid {P['non_urgent']['c']}; padding: 12px; border-radius: 0 8px 8px 0;">
        <div style="font-size: 12px; font-weight: 600; color: {P['non_urgent']['tx']};">{P['non_urgent']['l']}</div>
        <div style="font-size: 18px; font-weight: 700; color: {P['non_urgent']['tx']}; margin-top: 2px;">{P['non_urgent']['t']}</div>
    </div>
</div>
''', unsafe_allow_html=True)

# ========== RESULTADO FINAL + RESUMO ==========
st.markdown('<div style="height: 24px;"></div>', unsafe_allow_html=True)
st.markdown('''
<div style="font-size: 16px; font-weight: 600; color: #374151; margin-bottom: 16px; padding-bottom: 8px; border-bottom: 2px solid #E5E7EB;">
    Resultado da Classificação
</div>
''', unsafe_allow_html=True)

# Resultado duplicado no final
st.markdown(f'''
<div style="background: {p_result['bg']}; border: 2px solid {p_result['c']}; border-radius: 16px; padding: 16px 20px; margin-bottom: 20px;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px;">
        <div>
            <div style="font-size: 12px; color: {p_result['tx']}; opacity: 0.8;">Classificação de Risco</div>
            <div style="font-size: 24px; font-weight: 700; color: {p_result['tx']}; letter-spacing: -0.02em;">{p_result['l']}</div>
            <div style="margin-top: 8px; font-size: 11px;">{findings_tags if findings_tags else '<span style="color: #6B7280;">Nenhum achado</span>'}</div>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 12px; color: {p_result['tx']}; opacity: 0.8;">Tempo Alvo</div>
            <div style="font-size: 28px; font-weight: 700; color: {p_result['tx']};">{p_result['t']}</div>
        </div>
    </div>
</div>
''', unsafe_allow_html=True)

# Campo de resumo
st.markdown('''
<div style="font-size: 14px; font-weight: 500; color: #374151; margin-bottom: 8px;">
    Resumo da Classificação
</div>
''', unsafe_allow_html=True)

summary_text = generate_summary(findings, fc_data['n'], gcs_val, final_priority, pain)
st.text_area("Resumo", value=summary_text, height=180, label_visibility="collapsed")

# ========== FOOTER ==========
st.markdown('''
<div style="margin-top: 32px; padding: 16px; text-align: center; border-top: 1px solid #E5E7EB;">
    <div style="font-size: 12px; color: #6B7280;">
        <strong style="color: #059669;">telepatia.ai</strong> · Protocolo de Manchester
    </div>
    <div style="font-size: 11px; color: #9CA3AF; margin-top: 4px;">
        Ferramenta de apoio. Não substitui o julgamento clínico.
    </div>
</div>
''', unsafe_allow_html=True)
