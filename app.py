import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Anatomia do Abdome",
    page_icon=" anatomical_heart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- DADOS DOS ÓRGÃOS (FLUXOGRAMAS E TEXTOS) ---
# Os dados foram extraídos do PDF fornecido.
# Os fluxogramas são gerados usando a linguagem DOT do Graphviz.

ORGAN_DATA = {
    "Visão Geral": {
        "description": """
        Esta seção oferece uma visão geral da irrigação arterial, drenagem venosa e inervação das vísceras abdominais.
        Use os fluxogramas para entender as principais artérias, como o **Tronco Celíaco**, a **Artéria Mesentérica Superior** e a **Artéria Mesentérica Inferior**,
        e a formação do sistema venoso porta.
        """,
        "arterial_dot": """
        digraph {
            rankdir="TB";
            splines=ortho;

            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            "Aorta Abdominal" [width=3, height=1];

            subgraph cluster_celiac {
                label="Tronco Celíaco (Intestino Anterior)";
                style="rounded";
                color="#457b9d";
                node [fillcolor="#a8dadc"];
                "A. Gástrica Esquerda"; "A. Esplênica"; "A. Hepática Comum";
            }

            subgraph cluster_sma {
                label="A. Mesentérica Superior (Intestino Médio)";
                style="rounded";
                color="#457b9d";
                node [fillcolor="#a8dadc"];
                "Aa. Jejuno-ileais"; "A. Ileocólica"; "A. Cólica Direita"; "A. Cólica Média";
            }

            subgraph cluster_ima {
                label="A. Mesentérica Inferior (Intestino Posterior)";
                style="rounded";
                color="#457b9d";
                node [fillcolor="#a8dadc"];
                "A. Cólica Esquerda"; "Aa. Sigmóideas"; "A. Retal Superior";
            }

            "Aorta Abdominal" -> "Tronco Celíaco" [lhead=cluster_celiac];
            "Aorta Abdominal" -> "A. Mesentérica Superior" [lhead=cluster_sma];
            "Aorta Abdominal" -> "A. Mesentérica Inferior" [lhead=cluster_ima];

            "A. Gástrica Esquerda" -> "Estômago, Esôfago";
            "A. Esplênica" -> "Baço, Pâncreas, Estômago";
            "A. Hepática Comum" -> "Fígado, Vesícula Biliar, Estômago, Duodeno";

            "Aa. Jejuno-ileais" -> "Jejuno, Íleo";
            "A. Ileocólica" -> "Íleo terminal, Ceco, Apêndice, Colo Ascendente";
            "A. Cólica Direita" -> "Colo Ascendente";
            "A. Cólica Média" -> "Colo Transverso";

            "A. Cólica Esquerda" -> "Colo Descendente";
            "Aa. Sigmóideas" -> "Colo Sigmóide";
            "A. Retal Superior" -> "Reto";

        }
        """,
        "venous_dot": """
        digraph {
            rankdir="TB";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];

            "Veia Porta Hepática" [width=3, height=1, fillcolor="#1e6091", fontcolor=white];

            "V. Esplênica" [width=2];
            "V. Mesentérica Superior" [width=2];
            "V. Mesentérica Inferior" [width=2];
            "Vv. Gástricas (E/D)" [width=2];

            "V. Mesentérica Inferior" -> "V. Esplênica";
            "V. Esplênica" -> "Veia Porta Hepática";
            "V. Mesentérica Superior" -> "Veia Porta Hepática";
            "Vv. Gástricas (E/D)" -> "Veia Porta Hepática";

            "Veia Porta Hepática" -> "Capilares Sinusoides (Fígado)";
            "Capilares Sinusoides (Fígado)" -> "Vv. Hepáticas";
            "Vv. Hepáticas" -> "V. Cava Inferior (Sistema Sistêmico)";

            {rank=same; "V. Esplênica"; "V. Mesentérica Superior"; "Vv. Gástricas (E/D)"}
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";

            subgraph cluster_para {
                label="Parassimpático (Descansa e Digerir)";
                style="rounded";
                color=blue;
                node [shape=box, style="rounded,filled", fillcolor="#cfe1f7"];
                "N. Vago (NC X)" -> "Intestino Anterior e Médio (até 2/3 do Colo Transverso)";
                "Nn. Esplâncnicos Pélvicos (S2-S4)" -> "Intestino Posterior (a partir de 1/3 do Colo Transverso)";
            }

            subgraph cluster_simpa {
                label="Simpático (Luta ou Fuga)";
                style="rounded";
                color=red;
                node [shape=box, style="rounded,filled", fillcolor="#f7cfd6"];
                "Nn. Esplâncnicos Torácicos (T5-T12)" -> "Gânglios Pré-vertebrais (Celíaco, Mesentérico Superior)";
                "Nn. Esplâncnicos Lombares (L1-L2)" -> "Gânglio Mesentérico Inferior";
                "Gânglios Pré-vertebrais (Celíaco, Mesentérico Superior)" -> "Intestino Anterior e Médio";
                "Gânglio Mesentérico Inferior" -> "Intestino Posterior";
            }
        }
        """,
    },
    "Estômago": {
        "description": """
        O estômago possui uma rica rede vascular derivada do **tronco celíaco**. Sua inervação dupla, parassimpática pelo **nervo vago** e simpática pelos **nervos esplâncnicos**, regula a secreção e a motilidade.
        """,
        "arterial_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            "Tronco Celíaco" -> "A. Gástrica Esquerda" [label="Curvatura menor (esq)"];
            "Tronco Celíaco" -> "A. Esplênica";
            "Tronco Celíaco" -> "A. Hepática Comum";

            "A. Esplênica" -> "Aa. Gástricas Curtas" [label="Fundo gástrico"];
            "A. Esplênica" -> "A. Gastromental Esquerda" [label="Curvatura maior (esq)"];
            "A. Hepática Comum" -> "A. Gástrica Direita" [label="Curvatura menor (dir)"];
            "A. Hepática Comum" -> "A. Gastroduodenal";
            "A. Gastroduodenal" -> "A. Gastromental Direita" [label="Curvatura maior (dir)"];
        }
        """,
        "venous_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];

            "V. Porta Hepática" [fillcolor="#1e6091", fontcolor=white];

            "V. Gástrica Esquerda" -> "V. Porta Hepática";
            "V. Gástrica Direita" -> "V. Porta Hepática";
            "V. Gastromental Esquerda" -> "V. Esplênica";
            "V. Gastromental Direita" -> "V. Mesentérica Superior";
            "V. Esplênica" -> "V. Porta Hepática" [style=dashed, label="une-se à VMS"];
            "V. Mesentérica Superior" -> "V. Porta Hepática" [style=dashed];
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
            subgraph cluster_para {
                label="Parassimpático"; style="rounded"; color=blue;
                node [shape=box, style="rounded,filled", fillcolor="#cfe1f7"];
                "Nervo Vago (NC X)" -> {"Tronco Vagal Anterior"; "Tronco Vagal Posterior"};
                {"Tronco Vagal Anterior"; "Tronco Vagal Posterior"} -> "Estômago (secreção e motilidade)";
            }
            subgraph cluster_simpa {
                label="Simpático"; style="rounded"; color=red;
                node [shape=box, style="rounded,filled", fillcolor="#f7cfd6"];
                "Medula (T6-T9)" -> "N. Esplâncnico Maior" -> "Gânglio Celíaco" -> "Estômago (vasoconstrição)";
            }
        }
        """,
    },
    "Fígado e Vesícula Biliar": {
        "description": """
        O fígado possui uma irrigação dupla única: a **artéria hepática** (25%, rica em O2) e a **veia porta** (75%, rica em nutrientes). A vesícula biliar é irrigada pela **artéria cística**.
        """,
        "arterial_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            "A. Hepática Comum" -> "A. Hepática Própria" -> {"A. Hepática Direita"; "A. Hepática Esquerda"};
            "A. Hepática Direita" -> "A. Cística" -> "Vesícula Biliar";
            {"A. Hepática Direita"; "A. Hepática Esquerda"} -> "Fígado";
        }
        """,
        "venous_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];

            "V. Cava Inferior" [fillcolor="#1e6091", fontcolor=white];

            "Fígado (Sinusoides)" -> {"V. Hepática Direita"; "V. Hepática Intermédia"; "V. Hepática Esquerda"};
            {"V. Hepática Direita"; "V. Hepática Intermédia"; "V. Hepática Esquerda"} -> "V. Cava Inferior";
            "Vesícula Biliar" -> "Vv. Císticas" -> "Fígado (Sinusoides) / V. Porta";
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
             node [shape=box, style="rounded"];
            subgraph cluster_simpa {
                label="Simpático"; style="rounded"; color=red;
                node [fillcolor="#f7cfd6"];
                "Plexo Celíaco" -> "Plexo Hepático" -> "Fígado e Vesícula";
            }
            subgraph cluster_para {
                label="Parassimpático"; style="rounded"; color=blue;
                node [fillcolor="#cfe1f7"];
                "Troncos Vagais" -> "Plexo Hepático" -> "Fígado e Vesícula";
            }
            "N. Frênico Direito" -> "Vesícula Biliar (cápsula)" [label="Dor somática referida no ombro"];
        }
        """,
    },
    "Intestino Delgado": {
        "description": """
        O duodeno tem irrigação dupla (tronco celíaco e A. mesentérica superior), marcando a transição entre o intestino anterior e médio. O jejuno e o íleo são irrigados exclusivamente pela **artéria mesentérica superior** através de uma rede de arcos arteriais.
        """,
        "arterial_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            subgraph cluster_duodeno {
                label="Duodeno";
                "A. Gastroduodenal" -> "A. Pancreaticoduodenal Superior" -> "Duodeno Proximal";
                "A. Mesentérica Superior" -> "A. Pancreaticoduodenal Inferior" -> "Duodeno Distal";
            }
            subgraph cluster_jejunoileo {
                label="Jejuno e Íleo";
                "A. Mesentérica Superior" -> "Aa. Jejuno-ileais" -> "Arcos Arteriais" -> "Vasos Retos" -> "Jejuno e Íleo";
            }
        }
        """,
        "venous_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];
            "V. Porta Hepática" [fillcolor="#1e6091", fontcolor=white];
            "V. Mesentérica Superior" -> "V. Porta Hepática";
            "Vv. Pancreaticoduodenais" -> "V. Mesentérica Superior";
            "Vv. Jejuno-ileais" -> "V. Mesentérica Superior";
            "Duodeno" -> "Vv. Pancreaticoduodenais";
            "Jejuno e Íleo" -> "Vv. Jejuno-ileais";
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
            subgraph cluster_para {
                label="Parassimpático"; style="rounded"; color=blue;
                node [shape=box, style="rounded,filled", fillcolor="#cfe1f7"];
                "N. Vago (NC X)" -> "Plexo Mesentérico Superior" -> "Intestino Delgado";
            }
            subgraph cluster_simpa {
                label="Simpático"; style="rounded"; color=red;
                node [shape=box, style="rounded,filled", fillcolor="#f7cfd6"];
                "Nn. Esplâncnicos (T8-T10)" -> "Gânglio Mesentérico Superior" -> "Intestino Delgado";
            }
        }
        """,
    },
    "Intestino Grosso": {
        "description": """
        A irrigação é dividida: a **A. Mesentérica Superior** supre o ceco, apêndice, colo ascendente e 2/3 proximais do transverso. A **A. Mesentérica Inferior** supre o 1/3 distal do transverso, descendente, sigmoide e reto superior. A **Arcada de Drummond** (artéria marginal) conecta os dois sistemas.
        """,
        "arterial_dot": """
        digraph {
            rankdir="TB";
            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            subgraph cluster_sup {
                label = "Da A. Mesentérica Superior";
                "A. Ileocólica" -> "Ceco, Apêndice, Íleo Terminal";
                "A. Cólica Direita" -> "Colo Ascendente";
                "A. Cólica Média" -> "Colo Transverso (2/3 proximais)";
            }
            subgraph cluster_inf {
                label = "Da A. Mesentérica Inferior";
                "A. Cólica Esquerda" -> "Colo Transverso (1/3 distal), Colo Descendente";
                "Aa. Sigmóideas" -> "Colo Sigmóide";
            }
             "A. Cólica Média" -> "A. Cólica Esquerda" [label="Artéria Marginal (Drummond)", style=dashed, dir=both];
        }
        """,
        "venous_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];

            "V. Porta Hepática" [fillcolor="#1e6091", fontcolor=white];

            "Colo Ascendente e Transverso Proximal" -> "V. Mesentérica Superior" -> "V. Porta Hepática";
            "Colo Descendente e Sigmóide" -> "V. Mesentérica Inferior" -> "V. Esplênica" -> "V. Porta Hepática";
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
            node [shape=box, style="rounded"];
             subgraph cluster_prox {
                label="Até 2/3 do Colo Transverso (Intestino Médio)";
                "Parassimpático (N. Vago)" [style="rounded,filled", fillcolor="#cfe1f7"];
                "Simpático (Nn. Esplâncnicos Torácicos)" [style="rounded,filled", fillcolor="#f7cfd6"];
             }

             subgraph cluster_dist {
                label="A partir de 1/3 do Colo Transverso (Intestino Posterior)";
                "Parassimpático (Nn. Esplâncnicos Pélvicos S2-S4)" [style="rounded,filled", fillcolor="#cfe1f7"];
                "Simpático (Nn. Esplâncnicos Lombares)" [style="rounded,filled", fillcolor="#f7cfd6"];
             }
        }
        """,
    },
     "Rins e Suprarrenais": {
        "description": """
        Os rins recebem um alto fluxo sanguíneo diretamente da aorta abdominal através das **artérias renais**. As glândulas suprarrenais têm uma irrigação tríplice complexa de diferentes fontes. A drenagem venosa é assimétrica, especialmente para a veia suprarrenal e gonadal esquerdas.
        """,
        "arterial_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#fde0dd"];
            edge [color="#e63946"];

            "Aorta Abdominal" -> "A. Renal" -> "Aa. Segmentares" -> "Rim";

            subgraph cluster_supra {
                label = "Glândula Suprarrenal";
                "A. Frênica Inferior" -> "A. Suprarrenal Superior";
                "Aorta Abdominal" -> "A. Suprarrenal Média";
                "A. Renal" -> "A. Suprarrenal Inferior";
            }
        }
        """,
        "venous_dot": """
        digraph {
            rankdir="LR";
            node [shape=box, style="rounded,filled", fillcolor="#d9ed92"];
            edge [color="#1a759f"];

            "V. Cava Inferior" [fillcolor="#1e6091", fontcolor=white];
            "V. Renal Esquerda" [width=2.5];

            "Rim Direito" -> "V. Renal Direita" -> "V. Cava Inferior";
            "Rim Esquerdo" -> "V. Renal Esquerda";

            "G. Suprarrenal Direita" -> "V. Suprarrenal Direita" -> "V. Cava Inferior";
            "G. Suprarrenal Esquerda" -> "V. Suprarrenal Esquerda" -> "V. Renal Esquerda";
            "Gônada Esquerda" -> "V. Gonadal Esquerda" -> "V. Renal Esquerda";
            
            "V. Renal Esquerda" -> "V. Cava Inferior" [constraint=false];
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
            node [shape=box, style="rounded,filled", fillcolor="#f7cfd6"];

            subgraph cluster_rim {
                label="Rins";
                "Nn. Esplâncnicos (T10-L1)" -> "Plexo Renal" -> "Rins (regulação do fluxo sanguíneo)";
            }

             subgraph cluster_supra {
                label="Glândula Suprarrenal";
                 "Nn. Esplâncnicos" -> "Medula da Suprarrenal" [label="Sinapse direta em células cromafins \\n (liberação de catecolaminas)"];
             }
        }
        """,
    },
}

# --- DADOS DOS QUIZZES ---
QUICK_QUIZ_QUESTIONS = [
    {
        "question": "O tronco celíaco é um ramo direto de qual grande artéria?",
        "options": ["Artéria Mesentérica Superior", "Aorta Abdominal", "Artéria Hepática Comum", "Artéria Esplênica"],
        "answer": "Aorta Abdominal",
        "explanation": "O tronco celíaco, a artéria mesentérica superior e a inferior são os três principais ramos anteriores da aorta abdominal que irrigam o trato gastrointestinal."
    },
    {
        "question": "A veia mesentérica superior e a veia esplênica se unem para formar qual importante veia?",
        "options": ["Veia Cava Inferior", "Veia Renal", "Veia Porta Hepática", "Veia Gástrica"],
        "answer": "Veia Porta Hepática",
        "explanation": "A união da veia mesentérica superior e da veia esplênica forma a veia porta hepática, que leva o sangue rico em nutrientes do intestino para o fígado."
    },
    {
        "question": "A inervação parassimpática do estômago e do intestino delgado é fornecida principalmente por qual nervo?",
        "options": ["Nervo Frênico", "Nervo Esplâncnico Maior", "Nervo Vago (NC X)", "Nervos Esplâncnicos Pélvicos"],
        "answer": "Nervo Vago (NC X)",
        "explanation": "O nervo vago é responsável pela inervação parassimpática da maioria das vísceras abdominais, promovendo a digestão ('descansar e digerir')."
    },
    {
        "question": "Qual artéria é a principal fonte de irrigação para o jejuno, íleo e colo ascendente?",
        "options": ["Artéria Mesentérica Inferior", "Tronco Celíaco", "Artéria Mesentérica Superior", "Artéria Ileocólica"],
        "answer": "Artéria Mesentérica Superior",
        "explanation": "A Artéria Mesentérica Superior (AMS) irriga todas as estruturas derivadas do intestino médio embrionário."
    },
    {
        "question": "A drenagem venosa da veia suprarrenal esquerda ocorre tipicamente em qual veia?",
        "options": ["Veia Cava Inferior", "Veia Renal Esquerda", "Veia Esplênica", "Veia Porta Hepática"],
        "answer": "Veia Renal Esquerda",
        "explanation": "A veia suprarrenal esquerda (assim como a gonadal esquerda) drena para a veia renal esquerda antes de atingir a veia cava inferior. A direita drena diretamente para a cava."
    }
]

CLINICAL_QUIZ_QUESTIONS = [
    {
        "question": "Um paciente com cirrose hepática desenvolve varizes esofágicas com risco de sangramento. Qual anastomose portossistêmica é responsável por essa condição?",
        "options": ["Veias paraumbilicais e epigástricas", "Veias retais superiores e médias/inferiores", "Veia gástrica esquerda e veias esofágicas (sistema ázigo)", "Veias cólicas e retroperitoneais"],
        "answer": "Veia gástrica esquerda e veias esofágicas (sistema ázigo)",
        "explanation": "Na hipertensão portal, o sangue não consegue passar facilmente pelo fígado. Ele busca rotas alternativas para o sistema sistêmico. O fluxo retrógrado pela veia gástrica esquerda para as veias esofágicas causa a dilatação destas, formando varizes."
    },
    {
        "question": "Durante uma apendicectomia, a ligadura da artéria apendicular é crucial. Esta artéria é um ramo terminal de qual artéria?",
        "options": ["Artéria Cólica Direita", "Artéria Mesentérica Inferior", "Artéria Ileocólica", "Artéria Gástrica Direita"],
        "answer": "Artéria Ileocólica",
        "explanation": "A artéria ileocólica, um ramo da mesentérica superior, irriga a junção ileocecal e dá origem à artéria apendicular. Sua ligadura é essencial para remover o apêndice com segurança."
    },
    {
        "question": "Um paciente sofre um trauma abdominal com lesão na cauda do pâncreas e no baço. A remoção cirúrgica desses órgãos (esplenopancreatectomia distal) exige o controle de qual grande vaso que passa posteriormente a eles?",
        "options": ["Artéria e Veia Mesentérica Superior", "Aorta Abdominal", "Artéria e Veia Esplênica", "Veia Cava Inferior"],
        "answer": "Artéria e Veia Esplênica",
        "explanation": "A artéria e a veia esplênica têm um trajeto íntimo com a cauda e o corpo do pâncreas em direção ao hilo esplênico, sendo os principais vasos a serem controlados nesse procedimento."
    },
    {
        "question": "Um paciente com dor de colecistite aguda (inflamação da vesícula biliar) refere dor no ombro direito. Essa dor referida é mediada por fibras de qual nervo?",
        "options": ["Nervo Vago", "Nervo Esplâncnico Maior", "Nervo Intercostal", "Nervo Frênico"],
        "answer": "Nervo Frênico",
        "explanation": "A inflamação da vesícula pode irritar o diafragma adjacente. O diafragma é inervado pelo nervo frênico (C3-C5), que compartilha as mesmas raízes espinhais da inervação sensitiva do ombro. Isso causa a dor referida."
    },
    {
        "question": "A oclusão aguda da Artéria Mesentérica Superior é uma emergência vascular. Qual segmento do intestino grosso seria mais provavelmente poupado de isquemia severa neste caso?",
        "options": ["Ceco", "Colo Ascendente", "Colo Transverso (metade direita)", "Colo Descendente"],
        "answer": "Colo Descendente",
        "explanation": "O colo descendente é irrigado pela artéria cólica esquerda, um ramo da Artéria Mesentérica Inferior. Portanto, uma oclusão da Mesentérica Superior não o afetaria diretamente."
    }
]

# --- FUNÇÕES DO APP ---

def show_organ_explorer():
    """Mostra a interface de exploração dos órgãos."""
    st.sidebar.header("Selecione um Órgão")
    organ_list = list(ORGAN_DATA.keys())
    selected_organ = st.sidebar.radio(
        "Navegue pelas estruturas:",
        organ_list,
        label_visibility="collapsed"
    )

    st.header(f"Detalhes de: {selected_organ}")
    st.markdown(ORGAN_DATA[selected_organ].get("description", ""))

    # Abas para cada sistema
    tab1, tab2, tab3 = st.tabs(["Vascularização Arterial", "Drenagem Venosa", "Inervação"])

    with tab1:
        st.subheader("Fluxograma da Irrigação Arterial")
        if ORGAN_DATA[selected_organ]["arterial_dot"]:
            st.graphviz_chart(ORGAN_DATA[selected_organ]["arterial_dot"])
        else:
            st.warning("Fluxograma não disponível.")

    with tab2:
        st.subheader("Fluxograma da Drenagem Venosa")
        if ORGAN_DATA[selected_organ]["venous_dot"]:
            st.graphviz_chart(ORGAN_DATA[selected_organ]["venous_dot"])
        else:
            st.warning("Fluxograma não disponível.")

    with tab3:
        st.subheader("Fluxograma da Inervação")
        if ORGAN_DATA[selected_organ]["innervation_dot"]:
            st.graphviz_chart(ORGAN_DATA[selected_organ]["innervation_dot"])
        else:
            st.warning("Fluxograma não disponível.")

def run_quiz(quiz_type, questions):
    """Executa a interface do quiz."""
    st.header(f"Quiz: {quiz_type}")
    st.write("Teste seus conhecimentos! Selecione a resposta correta e clique em 'Confirmar'.")

    # Inicializa o estado da sessão para o quiz
    if f'quiz_{quiz_type}_started' not in st.session_state:
        st.session_state[f'quiz_{quiz_type}_started'] = True
        st.session_state[f'quiz_{quiz_type}_current_question'] = 0
        st.session_state[f'quiz_{quiz_type}_score'] = 0
        st.session_state[f'quiz_{quiz_type}_answered'] = False
        st.session_state[f'quiz_{quiz_type}_user_answer'] = None

    q_idx = st.session_state[f'quiz_{quiz_type}_current_question']

    if q_idx < len(questions):
        question_data = questions[q_idx]

        st.subheader(f"Pergunta {q_idx + 1}/{len(questions)}")
        st.markdown(f"**{question_data['question']}**")

        # Mostra as opções de resposta
        user_answer = st.radio(
            "Selecione uma opção:",
            question_data["options"],
            key=f'radio_{quiz_type}_{q_idx}',
            disabled=st.session_state[f'quiz_{quiz_type}_answered']
        )
        st.session_state[f'quiz_{quiz_type}_user_answer'] = user_answer

        col1, col2 = st.columns(2)
        with col1:
             # Botão de confirmar
            if not st.session_state[f'quiz_{quiz_type}_answered']:
                if st.button("Confirmar Resposta", key=f'confirm_{quiz_type}_{q_idx}'):
                    st.session_state[f'quiz_{quiz_type}_answered'] = True
                    if st.session_state[f'quiz_{quiz_type}_user_answer'] == question_data['answer']:
                        st.session_state[f'quiz_{quiz_type}_score'] += 1
                    st.rerun()

        # Mostra o resultado e o botão para a próxima pergunta
        if st.session_state[f'quiz_{quiz_type}_answered']:
            user_ans = st.session_state[f'quiz_{quiz_type}_user_answer']
            correct_ans = question_data['answer']
            if user_ans == correct_ans:
                st.success(f"Correto! A resposta é **{correct_ans}**.")
            else:
                st.error(f"Incorreto. A resposta correta é **{correct_ans}**.")
            
            st.info(f"**Justificativa:** {question_data['explanation']}")

            with col2:
                if st.button("Próxima Pergunta →", key=f'next_{quiz_type}_{q_idx}'):
                    st.session_state[f'quiz_{quiz_type}_current_question'] += 1
                    st.session_state[f'quiz_{quiz_type}_answered'] = False
                    st.session_state[f'quiz_{quiz_type}_user_answer'] = None
                    st.rerun()
    else:
        # Fim do quiz
        score = st.session_state[f'quiz_{quiz_type}_score']
        total = len(questions)
        st.balloons()
        st.success(f"Quiz finalizado! Sua pontuação: **{score}/{total}**")

        if st.button("Reiniciar Quiz", key=f'restart_{quiz_type}'):
            # Reseta o estado da sessão para este quiz
            st.session_state[f'quiz_{quiz_type}_started'] = False
            del st.session_state[f'quiz_{quiz_type}_current_question']
            del st.session_state[f'quiz_{quiz_type}_score']
            del st.session_state[f'quiz_{quiz_type}_answered']
            del st.session_state[f'quiz_{quiz_type}_user_answer']
            st.rerun()


# --- INTERFACE PRINCIPAL ---

st.title(" 🧠 App Interativo: Vascularização e Inervação do Abdome")
st.markdown("Bem-vindo! Este aplicativo foi desenvolvido para auxiliar no estudo da anatomia abdominal com base no material de aula.")
st.markdown("Use o menu à esquerda para navegar entre a exploração dos órgãos e os quizzes.")

# Seleção do modo do app na barra lateral
st.sidebar.title("Menu de Navegação")
app_mode = st.sidebar.selectbox(
    "Escolha uma seção:",
    ["Explorar Órgãos", "Quiz Rápido", "Quiz Clínico"]
)

# Lógica para exibir a seção selecionada
if app_mode == "Explorar Órgãos":
    show_organ_explorer()
elif app_mode == "Quiz Rápido":
    run_quiz("Rápido", QUICK_QUIZ_QUESTIONS)
elif app_mode == "Quiz Clínico":
    run_quiz("Clínico", CLINICAL_QUIZ_QUESTIONS)
