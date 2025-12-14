import streamlit as st

st.set_page_config(page_title="Triagem de Manchester | Telepatia", page_icon="🏥", layout="wide", initial_sidebar_state="collapsed")

# Logo SVG oficial Telepatia
LOGO = '<svg width="160" height="36" viewBox="0 0 918 396" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M793.982 240.744C780.094 240.744 770.67 233.8 770.67 222.268C770.67 209.62 779.474 202.552 796.09 202.552H814.69V198.212C814.69 189.656 808.862 185.068 798.942 185.068C789.642 185.068 784.062 189.284 782.822 195.732H772.654C774.142 183.332 784.186 176.016 799.438 176.016C815.558 176.016 824.858 184.076 824.858 198.832V226.484C824.858 229.832 826.098 230.7 828.95 230.7H832.174V240H826.594C818.534 240 815.186 236.28 815.186 230.452V230.204C811.466 235.908 804.894 240.744 793.982 240.744ZM794.726 232.064C807.374 232.064 814.69 224.748 814.69 214.208V211.108H795.098C786.046 211.108 780.962 214.456 780.962 221.648C780.962 228.344 786.294 232.064 794.726 232.064Z" fill="#1F2937"/><path d="M748.456 240V176.76H758.624V240H748.456ZM753.54 165.972C749.944 165.972 747.092 163.244 747.092 159.524C747.092 155.804 749.944 153.076 753.54 153.076C757.136 153.076 759.988 155.804 759.988 159.524C759.988 163.244 757.136 165.972 753.54 165.972Z" fill="#1F2937"/><path d="M726.911 240C714.759 240 710.419 234.668 710.419 223.508V186.06H699.011V176.76H710.419V159.028H720.587V176.76H737.947V186.06H720.587V223.384C720.587 228.716 722.447 230.7 727.903 230.7H737.947V240H726.911Z" fill="#1F2937"/><path d="M660.537 240.744C646.649 240.744 637.225 233.8 637.225 222.268C637.225 209.62 646.029 202.552 662.645 202.552H681.245V198.212C681.245 189.656 675.417 185.068 665.497 185.068C656.197 185.068 650.617 189.284 649.377 195.732H639.209C640.697 183.332 650.741 176.016 665.993 176.016C682.113 176.016 691.413 184.076 691.413 198.832V226.484C691.413 229.832 692.653 230.7 695.505 230.7H698.729V240H693.149C685.089 240 681.741 236.28 681.741 230.452V230.204C678.021 235.908 671.449 240.744 660.537 240.744ZM661.281 232.064C673.929 232.064 681.245 224.748 681.245 214.208V211.108H661.653C652.601 211.108 647.517 214.456 647.517 221.648C647.517 228.344 652.849 232.064 661.281 232.064Z" fill="#1F2937"/><path d="M565.725 264.8V176.76H574.529L575.893 186.928C580.109 181.1 586.929 176.016 597.593 176.016C615.077 176.016 627.973 187.796 627.973 208.38C627.973 227.724 615.077 240.744 597.593 240.744C586.929 240.744 579.737 236.404 575.893 230.328V264.8H565.725ZM596.601 231.692C609.125 231.692 617.557 222.144 617.557 208.38C617.557 194.616 609.125 185.068 596.601 185.068C584.201 185.068 575.769 194.616 575.769 208.132C575.769 222.02 584.201 231.692 596.601 231.692Z" fill="#1F2937"/><path d="M525.225 240.744C506.253 240.744 493.853 227.724 493.853 208.38C493.853 189.16 506.005 176.016 523.861 176.016C541.593 176.016 553.621 187.548 553.621 206.768V210.364H504.517V211.232C504.517 223.26 512.453 231.692 524.481 231.692C533.657 231.692 540.601 226.98 542.709 218.796H553.001C550.521 231.444 539.857 240.744 525.225 240.744ZM504.889 201.808H542.957C541.965 191.02 534.525 184.944 523.985 184.944C514.685 184.944 506.005 191.268 504.889 201.808Z" fill="#1F2937"/><path d="M471.514 240V153.2H481.682V240H471.514Z" fill="#1F2937"/><path d="M431.014 240.744C412.042 240.744 399.642 227.724 399.642 208.38C399.642 189.16 411.794 176.016 429.65 176.016C447.382 176.016 459.41 187.548 459.41 206.768V210.364H410.306V211.232C410.306 223.26 418.242 231.692 430.27 231.692C439.446 231.692 446.39 226.98 448.498 218.796H458.79C456.31 231.444 445.646 240.744 431.014 240.744ZM410.678 201.808H448.746C447.754 191.02 440.314 184.944 429.774 184.944C420.474 184.944 411.794 191.268 410.678 201.808Z" fill="#1F2937"/><path d="M382.52 240C370.368 240 366.028 234.668 366.028 223.508V186.06H354.62V176.76H366.028V159.028H376.196V176.76H393.556V186.06H376.196V223.384C376.196 228.716 378.056 230.7 383.512 230.7H393.556V240H382.52Z" fill="#1F2937"/><path d="M196.147 84C218.966 84 237.464 102.652 237.464 125.66V155.417H260.977C267.55 155.417 272.879 160.747 272.879 167.32C272.879 173.894 267.55 179.223 260.977 179.224H225.659C219.14 179.224 213.855 173.938 213.854 167.419V125.66C213.606 115.552 205.774 107.806 196.147 107.806C186.368 107.806 178.44 115.8 178.439 125.66V167.419C178.439 173.938 173.154 179.223 166.635 179.224H126.398V179.25C125.975 179.232 125.647 179.223 125.317 179.223C115.538 179.223 107.611 187.217 107.61 197.077C107.61 206.938 115.538 214.932 125.317 214.932C125.647 214.932 125.975 214.921 126.301 214.903V214.934H166.635C173.154 214.933 178.439 220.218 178.439 226.737V268.495C178.44 278.356 186.368 286.35 196.147 286.35C205.774 286.349 213.606 278.603 213.849 268.956V226.737C213.855 220.218 219.14 214.933 225.659 214.933H266.878V214.933C276.603 214.932 284.435 207.186 284.678 197.539C284.684 190.504 290.013 185.175 296.587 185.175H314.098C320.671 185.175 326.001 190.504 326.001 197.078C326.001 203.652 320.671 208.98 314.098 208.98H306.58C301.5 226.189 285.693 238.738 266.977 238.738H237.464V268.495C237.464 291.503 218.966 310.155 196.147 310.155C173.484 310.155 155.085 291.757 154.835 268.966V238.738H126.398C125.742 238.732 125.53 238.737 125.317 238.737C102.499 238.737 84 220.085 84 197.077C84 174.069 102.499 155.417 125.317 155.417H154.83V125.562C154.836 125.199 155.081 102.403 196.147 84Z" fill="url(#g1)"/><defs><linearGradient id="g1" x1="251" y1="255" x2="125" y2="156" gradientUnits="userSpaceOnUse"><stop stop-color="#068450"/><stop offset=".42" stop-color="#38A64A"/><stop offset="1" stop-color="#2FA879"/></linearGradient></defs></svg>'

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
*{font-family:'IBM Plex Sans',sans-serif!important}
#MainMenu,footer,.stDeployButton{display:none!important}
</style>""", unsafe_allow_html=True)

P = {'immediate':{'c':'#DC2626','l':'IMEDIATO','e':'IMMEDIATE','t':'0 min','x':'#991B1B','b':'#FEE2E2'},
     'very_urgent':{'c':'#EA580C','l':'MUITO URGENTE','e':'VERY URGENT','t':'10 min','x':'#9A3412','b':'#FFEDD5'},
     'urgent':{'c':'#CA8A04','l':'URGENTE','e':'URGENT','t':'60 min','x':'#713F12','b':'#FEF9C3'},
     'standard':{'c':'#16A34A','l':'PADRÃO','e':'STANDARD','t':'120 min','x':'#166534','b':'#DCFCE7'},
     'non_urgent':{'c':'#2563EB','l':'NÃO URGENTE','e':'NON-URGENT','t':'240 min','x':'#1E40AF','b':'#DBEAFE'}}
PO = ['immediate','very_urgent','urgent','standard','non_urgent']

F = {
'headache':{'n':'Cefaleia','e':'Headache','i':'🤕','d':[
    {'id':'a1','p':'immediate','q':'Comprometimento de via aérea?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR <10 ou >30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'a4','p':'immediate','q':'Não responsivo?','d':'AVPU=U'},
    {'id':'a5','p':'immediate','q':'Convulsão ativa?','d':'Tônico-clônicos'},
    {'id':'b1','p':'very_urgent','q':'Alteração da consciência?','d':'GCS<15'},
    {'id':'b2','p':'very_urgent','q':'Déficit neurológico focal?','d':'Hemiparesia'},
    {'id':'b3','p':'very_urgent','q':'Sinais de meningismo?','d':'Rigidez nuca'},
    {'id':'b4','p':'very_urgent','q':'Cefaleia súbita intensa?','d':'Thunderclap'},
    {'id':'b5','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'b6','p':'very_urgent','q':'Púrpura/petéquias?','d':'Não somem'},
    {'id':'b7','p':'very_urgent','q':'Temp ≥41°C?','d':'Hipertermia'},
    {'id':'c1','p':'urgent','q':'Dor moderada (5-7)?','d':'Interfere'},
    {'id':'c2','p':'urgent','q':'Temp 38.5-40.9°C?','d':'Febre'},
    {'id':'c3','p':'urgent','q':'Vômitos persistentes?','d':'Múltiplos'},
    {'id':'d1','p':'standard','q':'Dor leve (1-4)?','d':'Tolerável'},
    {'id':'d2','p':'standard','q':'Temp 37.5-38.4°C?','d':'Febrícula'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Habitual'}]},
'chest_pain':{'n':'Dor Torácica','e':'Chest Pain','i':'💔','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'b1','p':'very_urgent','q':'Dor cardíaca típica?','d':'Precordial'},
    {'id':'b2','p':'very_urgent','q':'Dispneia aguda?','d':'Súbito'},
    {'id':'b3','p':'very_urgent','q':'Pulso anormal?','d':'Irregular'},
    {'id':'b4','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'b5','p':'very_urgent','q':'SpO₂ <95%?','d':'Baixa'},
    {'id':'c1','p':'urgent','q':'Dor pleurítica?','d':'Respiração'},
    {'id':'c2','p':'urgent','q':'Dor moderada (5-7)?','d':'Significativa'},
    {'id':'c3','p':'urgent','q':'História cardíaca?','d':'IAM prévio'},
    {'id':'d1','p':'standard','q':'Dor leve (1-4)?','d':'Tolerável'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Habitual'}]},
'abdominal_pain':{'n':'Dor Abdominal','e':'Abdominal Pain','i':'🤢','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'a4','p':'immediate','q':'Hemorragia grave?','d':'Hematêmese'},
    {'id':'b1','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'b2','p':'very_urgent','q':'Peritonismo?','d':'Rigidez'},
    {'id':'b3','p':'very_urgent','q':'Fezes escuras/sangue?','d':'Melena'},
    {'id':'b4','p':'very_urgent','q':'Vômitos persistentes?','d':'Não tolera'},
    {'id':'c1','p':'urgent','q':'Dor moderada (5-7)?','d':'Significativa'},
    {'id':'c2','p':'urgent','q':'Febre 38.5-40.9°C?','d':'Febre'},
    {'id':'c3','p':'urgent','q':'Possível gravidez?','d':'Amenorreia'},
    {'id':'d1','p':'standard','q':'Dor leve (1-4)?','d':'Tolerável'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Habitual'}]},
'shortness_of_breath':{'n':'Dispneia','e':'Shortness of Breath','i':'😮‍💨','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'b1','p':'very_urgent','q':'SpO₂ <95%?','d':'Baixa'},
    {'id':'b2','p':'very_urgent','q':'Incapaz falar frases?','d':'Entrecortada'},
    {'id':'b3','p':'very_urgent','q':'Estridor?','d':'Inspiratório'},
    {'id':'b4','p':'very_urgent','q':'Sibilância grave?','d':'Audível'},
    {'id':'c1','p':'urgent','q':'Sibilância moderada?','d':'Broncoespasmo'},
    {'id':'c2','p':'urgent','q':'Dor pleurítica?','d':'Respiração'},
    {'id':'c3','p':'urgent','q':'Febre 38.5-40.9°C?','d':'Febre'},
    {'id':'d1','p':'standard','q':'Febrícula?','d':'37.5-38.4°C'},
    {'id':'e1','p':'non_urgent','q':'Dispneia crônica?','d':'Habitual'}]},
'unwell_adult':{'n':'Indisposição Adulto','e':'Unwell Adult','i':'🤒','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'a4','p':'immediate','q':'Não responsivo?','d':'AVPU=U'},
    {'id':'b1','p':'very_urgent','q':'Alteração consciência?','d':'Confusão'},
    {'id':'b2','p':'very_urgent','q':'Temp ≥41°C?','d':'Hipertermia'},
    {'id':'b3','p':'very_urgent','q':'Temp ≤35°C?','d':'Hipotermia'},
    {'id':'b4','p':'very_urgent','q':'Púrpura/petéquias?','d':'Não somem'},
    {'id':'b5','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'c1','p':'urgent','q':'Febre 38.5-40.9°C?','d':'Febre'},
    {'id':'c2','p':'urgent','q':'Dor moderada (5-7)?','d':'Significativa'},
    {'id':'d1','p':'standard','q':'Febrícula?','d':'37.5-38.4°C'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Habitual'}]},
'limb_problems':{'n':'Problemas Membros','e':'Limb Problems','i':'🦵','d':[
    {'id':'a1','p':'immediate','q':'Hemorragia grave/choque?','d':'Arterial'},
    {'id':'b1','p':'very_urgent','q':'Ausência pulso distal?','d':'Frio'},
    {'id':'b2','p':'very_urgent','q':'Fratura exposta?','d':'Osso visível'},
    {'id':'b3','p':'very_urgent','q':'Deformidade grosseira?','d':'Angulação'},
    {'id':'b4','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'c1','p':'urgent','q':'Dor moderada (5-7)?','d':'Significativa'},
    {'id':'c2','p':'urgent','q':'Incapaz apoiar peso?','d':'Não anda'},
    {'id':'c3','p':'urgent','q':'Edema significativo?','d':'Inchaço'},
    {'id':'d1','p':'standard','q':'Dor leve (1-4)?','d':'Tolerável'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Habitual'}]},
'wounds':{'n':'Feridas','e':'Wounds','i':'🩹','d':[
    {'id':'a1','p':'immediate','q':'Hemorragia grave/choque?','d':'Arterial'},
    {'id':'b1','p':'very_urgent','q':'Sangramento não controlado?','d':'Não cede'},
    {'id':'b2','p':'very_urgent','q':'Amputação?','d':'Perda parte'},
    {'id':'b3','p':'very_urgent','q':'Lesão tendão/nervo?','d':'Déficit'},
    {'id':'b4','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'c1','p':'urgent','q':'Ferida profunda?','d':'Estruturas'},
    {'id':'c2','p':'urgent','q':'Ferida contaminada?','d':'Sujeira'},
    {'id':'c3','p':'urgent','q':'Necessita sutura?','d':'Bordas'},
    {'id':'d1','p':'standard','q':'Ferida superficial?','d':'Abrasão'},
    {'id':'e1','p':'non_urgent','q':'Ferida crônica?','d':'Úlcera'}]},
'falls':{'n':'Quedas','e':'Falls','i':'⬇️','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'a4','p':'immediate','q':'Não responsivo?','d':'AVPU=U'},
    {'id':'b1','p':'very_urgent','q':'Alteração consciência?','d':'Confusão'},
    {'id':'b2','p':'very_urgent','q':'Dor na coluna?','d':'Cervical'},
    {'id':'b3','p':'very_urgent','q':'Dor intensa (8-10)?','d':'Insuportável'},
    {'id':'b4','p':'very_urgent','q':'Deformidade?','d':'Angulação'},
    {'id':'b5','p':'very_urgent','q':'Anticoagulante+TCE?','d':'Warfarina'},
    {'id':'c1','p':'urgent','q':'Dor no quadril?','d':'Imóvel'},
    {'id':'c2','p':'urgent','q':'Trauma craniano?','d':'Bateu cabeça'},
    {'id':'d1','p':'standard','q':'Dor leve (1-4)?','d':'Tolerável'},
    {'id':'e1','p':'non_urgent','q':'Quedas recorrentes?','d':'Investigar'}]},
'vomiting':{'n':'Vômitos','e':'Vomiting','i':'🤮','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Sinais de choque?','d':'Desidratação'},
    {'id':'b1','p':'very_urgent','q':'Hematêmese?','d':'Sangue vivo'},
    {'id':'b2','p':'very_urgent','q':'Vômito borra café?','d':'Digerido'},
    {'id':'b3','p':'very_urgent','q':'Desidratação grave?','d':'Letargia'},
    {'id':'b4','p':'very_urgent','q':'Dor abdominal intensa?','d':'Insuportável'},
    {'id':'c1','p':'urgent','q':'Desidratação moderada?','d':'Sede'},
    {'id':'c2','p':'urgent','q':'Vômitos persistentes?','d':'Não tolera'},
    {'id':'c3','p':'urgent','q':'Febre 38.5-40.9°C?','d':'Febre'},
    {'id':'d1','p':'standard','q':'Vômitos ocasionais?','d':'Tolera'},
    {'id':'e1','p':'non_urgent','q':'Problema crônico?','d':'Náuseas'}]},
'head_injury':{'n':'TCE','e':'Head Injury','i':'🤕','d':[
    {'id':'a1','p':'immediate','q':'Via aérea comprometida?','d':'Obstrução'},
    {'id':'a2','p':'immediate','q':'Respiração inadequada?','d':'FR<10/>30'},
    {'id':'a3','p':'immediate','q':'Sinais de choque?','d':'Hipotensão'},
    {'id':'a4','p':'immediate','q':'GCS ≤8?','d':'Não responsivo'},
    {'id':'a5','p':'immediate','q':'Convulsão pós-trauma?','d':'Crise'},
    {'id':'b1','p':'very_urgent','q':'Alteração consciência?','d':'GCS 9-14'},
    {'id':'b2','p':'very_urgent','q':'Déficit neurológico?','d':'Anisocoria'},
    {'id':'b3','p':'very_urgent','q':'Sinais fratura crânio?','d':'Battle'},
    {'id':'b4','p':'very_urgent','q':'Anticoagulante?','d':'Warfarina'},
    {'id':'b5','p':'very_urgent','q':'Alta energia?','d':'Queda>1m'},
    {'id':'b6','p':'very_urgent','q':'Vômitos repetidos?','d':'≥2x'},
    {'id':'c1','p':'urgent','q':'Amnésia do evento?','d':'Não lembra'},
    {'id':'c2','p':'urgent','q':'Perda consciência?','d':'Breve'},
    {'id':'c3','p':'urgent','q':'Cefaleia intensa?','d':'Pós-trauma'},
    {'id':'c4','p':'urgent','q':'Idade ≥65?','d':'Risco'},
    {'id':'d1','p':'standard','q':'Ferida couro cabeludo?','d':'Sutura'},
    {'id':'e1','p':'non_urgent','q':'Avaliação tardia?','d':'>24h'}]}
}

def hp(d):
    if not d: return 'non_urgent',[]
    pv={p:i for i,p in enumerate(PO)}
    h='non_urgent';hd=[]
    for x in d:
        if pv.get(x['p'],99)<pv.get(h,99): h=x['p'];hd=[x]
        elif x['p']==h: hd.append(x)
    return h,hd

def eg(e,v,m):
    g=e+v+m
    if g<=8: return 'immediate',f"GCS {g}"
    elif g<=12: return 'very_urgent',f"GCS {g}"
    elif g<=14: return 'urgent',f"GCS {g}"
    return None,f"GCS {g}"

def ev(hr,rr,sbp,sp,t):
    r=[]
    if hr<40 or hr>150: r.append({'p':'immediate','q':f'FC {hr}'})
    elif hr<50 or hr>130: r.append({'p':'very_urgent','q':f'FC {hr}'})
    if rr<10 or rr>30: r.append({'p':'immediate','q':f'FR {rr}'})
    elif rr<12 or rr>25: r.append({'p':'very_urgent','q':f'FR {rr}'})
    if sbp<80: r.append({'p':'immediate','q':f'PAS {sbp}'})
    elif sbp<90 or sbp>200: r.append({'p':'very_urgent','q':f'PAS {sbp}'})
    if sp<90: r.append({'p':'immediate','q':f'SpO₂ {sp}%'})
    elif sp<94: r.append({'p':'very_urgent','q':f'SpO₂ {sp}%'})
    if t>=41 or t<=32: r.append({'p':'immediate','q':f'Temp {t}°C'})
    elif t>=40 or t<=35: r.append({'p':'very_urgent','q':f'Temp {t}°C'})
    elif t>=38.5: r.append({'p':'urgent','q':f'Temp {t}°C'})
    elif t>=37.5: r.append({'p':'standard','q':f'Temp {t}°C'})
    return r

def ep(p):
    if p>=8: return 'very_urgent',f'Dor {p}/10'
    elif p>=5: return 'urgent',f'Dor {p}/10'
    elif p>=1: return 'standard',f'Dor {p}/10'
    return None,None

if 'fc' not in st.session_state: st.session_state.fc='headache'

# Header
st.markdown(f'<div style="background:#FFF;padding:16px 24px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,.06);margin-bottom:20px;display:flex;align-items:center;gap:16px;">{LOGO}<div style="width:1px;height:30px;background:#E5E7EB;"></div><span style="font-size:16px;font-weight:500;color:#6B7280;">Sistema de Triagem de Manchester</span></div>', unsafe_allow_html=True)

rph=st.empty()
ad=[]

c1,c2,c3=st.columns(3)

with c1:
    st.markdown("#### 🧠 Consciência")
    e=st.selectbox("Abertura Ocular",[4,3,2,1],format_func=lambda x:f"{x}-"+{4:"Espontânea",3:"Comando",2:"Dor",1:"Nenhuma"}[x])
    v=st.selectbox("Resposta Verbal",[5,4,3,2,1],format_func=lambda x:f"{x}-"+{5:"Orientada",4:"Confusa",3:"Inapropriada",2:"Incompreensível",1:"Nenhuma"}[x])
    m=st.selectbox("Resposta Motora",[6,5,4,3,2,1],format_func=lambda x:f"{x}-"+{6:"Obedece",5:"Localiza",4:"Retirada",3:"Flexão",2:"Extensão",1:"Nenhuma"}[x])
    gp,gt=eg(e,v,m)
    if gp: ad.append({'p':gp,'q':gt})
    st.info(f"**GCS: {e+v+m}/15**")
    st.markdown("#### 📊 AVPU")
    av=st.radio("",["A-Alerta","V-Voz","P-Dor","U-Não responsivo"],horizontal=True)
    am={"A-Alerta":None,"V-Voz":'urgent',"P-Dor":'very_urgent',"U-Não responsivo":'immediate'}
    if am[av]: ad.append({'p':am[av],'q':f'AVPU={av[0]}'})
    st.markdown("#### 😣 Dor")
    pa=st.slider("",0,10,0)
    pp,pt=ep(pa)
    if pp: ad.append({'p':pp,'q':pt})

with c2:
    st.markdown("#### 💓 Sinais Vitais")
    hr=st.number_input("FC (bpm)",30,250,80)
    rr=st.number_input("FR (rpm)",4,60,16)
    sbp=st.number_input("PAS (mmHg)",40,280,120)
    sp=st.number_input("SpO₂ (%)",50,100,98)
    t=st.number_input("Temp (°C)",30.0,44.0,36.5,0.1)
    st.checkbox("Em uso de O₂")
    ad.extend(ev(hr,rr,sbp,sp,t))

with c3:
    st.markdown("#### 🔍 Queixa Principal")
    op={k:f"{v['i']} {v['n']}" for k,v in F.items()}
    sl=st.selectbox("Fluxograma",list(op.keys()),format_func=lambda x:op[x])
    if sl!=st.session_state.fc: st.session_state.fc=sl;st.rerun()

st.markdown('<div style="background:#1F2937;padding:16px 20px;border-radius:12px;display:flex;align-items:center;gap:16px;margin:20px 0;"><div style="width:40px;height:40px;background:#374151;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;">⚠️</div><div><div style="font-weight:600;font-size:15px;color:#FFF;">Avalie de CIMA para BAIXO</div><div style="font-size:13px;color:#9CA3AF;margin-top:2px;">O primeiro SIM determina a prioridade.</div></div></div>', unsafe_allow_html=True)

fc=F[st.session_state.fc]
st.markdown(f'<div style="background:#FFF;border:1px solid #E5E7EB;border-radius:12px;padding:20px 24px;margin-bottom:16px;"><div style="font-size:20px;font-weight:600;color:#111827;">{fc["i"]} {fc["n"]}</div><div style="font-size:14px;color:#6B7280;margin-top:4px;">{fc["e"]}</div></div>', unsafe_allow_html=True)

bp={}
for d in fc['d']: bp.setdefault(d['p'],[]).append(d)
det=None

for pr in PO:
    if pr not in bp: continue
    p=P[pr]
    with st.expander(f"● {p['l']} ({p['t']})",expanded=(pr in['immediate','very_urgent'])):
        for d in bp[pr]:
            k=f"d_{st.session_state.fc}_{d['id']}"
            dis=det is not None
            c1,c2=st.columns([4,1])
            with c1: st.markdown(f"**{d['q']}**");st.caption(d['d'])
            with c2:
                if dis: st.write("—")
                else:
                    an=st.radio("",["—","SIM","NÃO"],key=k,horizontal=True,label_visibility="collapsed")
                    if an=="SIM": det=pr;ad.append({'p':pr,'q':d['q']})

if st.button("🔄 Limpar"):
    for k in list(st.session_state.keys()):
        if k.startswith('d_'): del st.session_state[k]
    st.rerun()

fp,_=hp(ad)
p=P[fp]
tg="".join([f'<span style="display:inline-flex;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;color:#FFF;background:{P[x["p"]]["c"]};margin-right:6px;">{x.get("q","")[:20]}</span>' for x in ad[:4]])

with rph.container():
    st.markdown(f'<div style="background:{p["b"]};padding:20px 24px;border-radius:12px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;border-left:5px solid {p["c"]};"><div style="display:flex;flex-direction:column;gap:6px;"><div><span style="font-size:24px;font-weight:700;color:{p["x"]};">{p["l"]}</span><span style="font-size:14px;font-weight:500;color:{p["x"]};margin-left:8px;opacity:.8;">{p["e"]}</span></div><div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:6px;">{tg}</div></div><div style="font-size:28px;font-weight:700;color:{p["x"]};">{p["t"]}</div></div>', unsafe_allow_html=True)

lg="".join([f'<div style="display:flex;align-items:center;gap:8px;padding:8px 12px;background:#FFF;border-radius:8px;border:1px solid #E5E7EB;"><div style="width:4px;height:24px;border-radius:2px;background:{v["c"]};"></div><div><div style="font-size:12px;font-weight:600;color:{v["x"]};">{v["l"]}</div><div style="font-size:11px;color:#6B7280;">{v["t"]}</div></div></div>' for k,v in P.items()])
st.markdown(f'<div style="background:#F9FAFB;border:1px solid #E5E7EB;border-radius:12px;padding:16px;margin-top:20px;display:flex;flex-wrap:wrap;gap:12px;">{lg}</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#FFF;border:1px solid #E5E7EB;border-radius:12px;padding:16px;text-align:center;margin-top:24px;font-size:13px;color:#6B7280;"><strong style="color:#006B3F;">telepatia</strong> · Sistema de Escalas Médicas · Manchester Triage<br><small>Ferramenta de apoio à decisão. Não substitui o julgamento clínico.</small></div>', unsafe_allow_html=True)
