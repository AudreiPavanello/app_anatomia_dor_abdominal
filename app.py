import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Anatomia do Abdome",
    layout="wide",
    initial_sidebar_state="expanded",
)

ORGAN_DATA = {
    "Visão Geral": {
        "description": """
        Esta seção oferece uma visão geral da irrigação arterial, drenagem venosa e inervação das vísceras abdominais.
        A irrigação do trato gastrointestinal é dividida em três territórios principais, baseados na sua origem embrionária e suprimento arterial:
        - **Intestino Anterior:** Suprido pelo **Tronco Celíaco**.
        - **Intestino Médio:** Suprido pela **Artéria Mesentérica Superior**.
        - **Intestino Posterior:** Suprido pela **Artéria Mesentérica Inferior**.
        """,
        "arterial_dot": """
        # Este DOT principal foi substituído pela lógica de 3 gráficos separados na função show_organ_explorer
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

            "V. Mesentérica Inferior" -> "V. Esplênica" [label="Drena para"];
            "V. Esplênica" -> "Veia Porta Hepática" [label="Une-se com a VMS para formar"];
            "V. Mesentérica Superior" -> "Veia Porta Hepática";
            "Vv. Gástricas (E/D)" -> "Veia Porta Hepática" [label="Drenam diretamente para"];

            "Veia Porta Hepática" -> "Capilares Sinusoides (Fígado)";
            "Capilares Sinusoides (Fígado)" -> "Vv. Hepáticas";
            "Vv. Hepáticas" -> "V. Cava Inferior (Circulação Sistêmica)";
        }
        """,
        "innervation_dot": """
        digraph {
            rankdir="TB";
            subgraph cluster_para {
                label="Parassimpático (Descansar e Digerir)";
                style="rounded"; color=blue;
                node [shape=box, style="rounded,filled", fillcolor="#cfe1f7"];
                "N. Vago (NC X)" -> "Intestino Anterior e Médio (até 2/3 do Colo Transverso)";
                "Nn. Esplâncnicos Pélvicos (S2-S4)" -> "Intestino Posterior (a partir de 1/3 do Colo Transverso)";
            }
            subgraph cluster_simpa {
                label="Simpático (Luta ou Fuga)";
                style="rounded"; color=red;
                node [shape=box, style="rounded,filled", fillcolor="#f7cfd6"];
                "Nn. Esplâncnicos Torácicos (T5-T12)" -> "Gânglios Pré-vertebrais (Celíaco, Mesentérico Superior)";
                "Nn. Esplâncnicos Lombares (L1-L2)" -> "Gânglio Mesentérico Inferior";
            }
        }
        """,
        "clinical": {
            "description": """
            ### Correlação Clínica: Hipertensão Portal
            Quando o fluxo sanguíneo através do fígado é obstruído (comumente por cirrose), a pressão na **veia porta** aumenta drasticamente. O sangue é forçado a encontrar rotas alternativas para retornar à circulação sistêmica através de **anastomoses portossistêmicas**. A dilatação dessas veias pode levar a condições graves:
            - **Varizes Esofágicas:** Conexão entre a veia gástrica esquerda (portal) e as veias esofágicas (sistêmicas). Sua ruptura causa hemorragia digestiva fatal.
            - **Cabeça de Medusa :** Conexão entre as veias paraumbilicais (portal) e as veias epigástricas da parede abdominal (sistêmicas).
            - **Hemorroidas Internas:** Conexão entre a veia retal superior (portal) e as veias retais média/inferior (sistêmicas).
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Causa (Ex: Cirrose Hepática)" [fillcolor="#f7cfd6"];
                "Bloqueio do Fluxo no Fígado" [fillcolor="#fde0dd"];
                "Hipertensão Portal" [fillcolor="#e63946", fontcolor=white, style="rounded,filled"];
                "Fluxo Retrógrado" [fillcolor="#fde0dd"];
                "Dilatação das Anastomoses" [fillcolor="#fde0dd"];

                subgraph cluster_sinais {
                    label="Sinais Clínicos";
                    node [fillcolor="#a8dadc"];
                    "Varizes Esofágicas"; "Cabeça de Medusa"; "Hemorroidas";
                }
                "Causa (Ex: Cirrose Hepática)" -> "Bloqueio do Fluxo no Fígado" -> "Hipertensão Portal" -> "Fluxo Retrógrado" -> "Dilatação das Anastomoses" -> {"Varizes Esofágicas", "Cabeça de Medusa", "Hemorroidas"};
            }
            """
        }
    },
    "Estômago": {
        "description": "O estômago possui uma rica rede vascular derivada do **tronco celíaco**. Sua inervação dupla, parassimpática pelo **nervo vago** e simpática pelos **nervos esplâncnicos**, regula a secreção e a motilidade.",
        "arterial_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#fde0dd\"]; edge [color=\"#e63946\"]; \"Tronco Celíaco\" -> \"A. Gástrica Esquerda\" [label=\"Curvatura menor (esq)\"]; \"Tronco Celíaco\" -> \"A. Esplênica\"; \"Tronco Celíaco\" -> \"A. Hepática Comum\"; \"A. Esplênica\" -> \"Aa. Gástricas Curtas\" [label=\"Fundo gástrico\"]; \"A. Esplênica\" -> \"A. Gastromental Esquerda\" [label=\"Curvatura maior (esq)\"]; \"A. Hepática Comum\" -> \"A. Gástrica Direita\" [label=\"Curvatura menor (dir)\"]; \"A. Hepática Comum\" -> \"A. Gastroduodenal\"; \"A. Gastroduodenal\" -> \"A. Gastromental Direita\" [label=\"Curvatura maior (dir)\"]; }",
        "venous_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#d9ed92\"]; edge [color=\"#1a759f\"]; \"V. Porta Hepática\" [fillcolor=\"#1e6091\", fontcolor=white]; \"V. Gástrica Esquerda\" -> \"V. Porta Hepática\"; \"V. Gástrica Direita\" -> \"V. Porta Hepática\"; \"V. Gastromental Esquerda\" -> \"V. Esplênica\"; \"V. Gastromental Direita\" -> \"V. Mesentérica Superior\"; \"V. Esplênica\" -> \"V. Porta Hepática\" [style=dashed, label=\"une-se à VMS\"]; \"V. Mesentérica Superior\" -> \"V. Porta Hepática\" [style=dashed]; }",
        "innervation_dot": "digraph { rankdir=\"TB\"; subgraph cluster_para { label=\"Parassimpático\"; style=\"rounded\"; color=blue; node [shape=box, style=\"rounded,filled\", fillcolor=\"#cfe1f7\"]; \"Nervo Vago (NC X)\" -> {\"Tronco Vagal Anterior\"; \"Tronco Vagal Posterior\"}; {\"Tronco Vagal Anterior\"; \"Tronco Vagal Posterior\"} -> \"Estômago (secreção e motilidade)\"; } subgraph cluster_simpa { label=\"Simpático\"; style=\"rounded\"; color=red; node [shape=box, style=\"rounded,filled\", fillcolor=\"#f7cfd6\"]; \"Medula (T6-T9)\" -> \"N. Esplâncnico Maior\" -> \"Gânglio Celíaco\" -> \"Estômago (vasoconstrição)\"; } }",
        "clinical": {
            "description": """
            ### Correlação Clínica: Úlcera Gástrica Perfurada
            A **artéria esplênica** tem um trajeto ao longo da margem superior do pâncreas, passando **posteriormente** ao estômago. Uma úlcera péptica profunda na parede posterior do estômago pode erodir completamente a parede gástrica e atingir a artéria esplênica. A perfuração desta artéria calibrosa resulta em uma **hemorragia massiva** para dentro da cavidade abdominal, uma emergência cirúrgica com alta mortalidade.
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Úlcera Péptica Profunda (Parede Posterior)" [fillcolor="#f7cfd6"];
                "Erosão da Parede Gástrica" [fillcolor="#fde0dd"];
                "Atinge a Artéria Esplênica" [label="Atinge a Artéria Esplênica\\n(trajeto posterior)", fillcolor="#fde0dd"];
                "Hemorragia Massiva" [label="Hemorragia Massiva -> Choque", fillcolor="#e63946", fontcolor=white];
                
                "Úlcera Péptica Profunda (Parede Posterior)" -> "Erosão da Parede Gástrica" -> "Atinge a Artéria Esplênica" -> "Hemorragia Massiva";
            }
            """
        }
    },
    "Fígado e Vesícula Biliar": {
        "description": "O fígado possui uma irrigação dupla única: a **artéria hepática** (25%, rica em O2) e a **veia porta** (75%, rica em nutrientes). A vesícula biliar é irrigada pela **artéria cística**.",
        "arterial_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#fde0dd\"]; edge [color=\"#e63946\"]; \"A. Hepática Comum\" -> \"A. Hepática Própria\" -> {\"A. Hepática Direita\"; \"A. Hepática Esquerda\"}; \"A. Hepática Direita\" -> \"A. Cística\" -> \"Vesícula Biliar\"; {\"A. Hepática Direita\"; \"A. Hepática Esquerda\"} -> \"Fígado\"; }",
        "venous_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#d9ed92\"]; edge [color=\"#1a759f\"]; \"V. Cava Inferior\" [fillcolor=\"#1e6091\", fontcolor=white]; \"Fígado (Sinusoides)\" -> {\"V. Hepática Direita\"; \"V. Hepática Intermédia\"; \"V. Hepática Esquerda\"}; {\"V. Hepática Direita\"; \"V. Hepática Intermédia\"; \"V. Hepática Esquerda\"} -> \"V. Cava Inferior\"; \"Vesícula Biliar\" -> \"Vv. Císticas\" -> \"Fígado (Sinusoides) / V. Porta\"; }",
        "innervation_dot": "digraph { rankdir=\"TB\"; node [shape=box, style=\"rounded\"]; subgraph cluster_simpa { label=\"Simpático\"; style=\"rounded\"; color=red; node [fillcolor=\"#f7cfd6\"]; \"Plexo Celíaco\" -> \"Plexo Hepático\" -> \"Fígado e Vesícula\"; } subgraph cluster_para { label=\"Parassimpático\"; style=\"rounded\"; color=blue; node [fillcolor=\"#cfe1f7\"]; \"Troncos Vagais\" -> \"Plexo Hepático\" -> \"Fígado e Vesícula\"; } \"N. Frênico Direito\" -> \"Vesícula Biliar (cápsula)\" [label=\"Dor somática referida no ombro\"]; }",
        "clinical": {
            "description": """
            ### Correlação Clínica: Triângulo de Calot e Colecistectomia
            A **colecistectomia** (remoção da vesícula biliar) é uma das cirurgias mais comuns. Para realizá-la com segurança, o cirurgião deve identificar as estruturas dentro do **Triângulo Cisto-hepático (de Calot)**. Os limites são:
            - **Superior:** Margem inferior do fígado.
            - **Medial:** Ducto hepático comum.
            - **Lateral:** Ducto cístico.
            
            Dentro deste triângulo, encontra-se a **artéria cística**. A identificação precisa e a ligadura da artéria e do ducto cístico são cruciais para evitar a lesão iatrogênica (acidental) do ducto hepático comum ou da artéria hepática direita, o que teria consequências graves.
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Colecistite Aguda" [fillcolor="#f7cfd6"];
                "Indicação de Cirurgia (Colecistectomia)" [fillcolor="#a8dadc"];
                "Desafio Cirúrgico" [label="Desafio: Anatomia Variável", fillcolor="#fde0dd"];
                "Marco Anatômico Chave" [label="Marco Anatômico Chave:\\nTriângulo de Calot", fillcolor="#d9ed92"];
                "Objetivo" [label="Objetivo: Ligar A. e Ducto Cístico", fillcolor="#1e6091", fontcolor=white];
                "Risco" [label="Risco: Lesão do Colédoco / A. Hepática", fillcolor="#e63946", fontcolor=white];

                "Colecistite Aguda" -> "Indicação de Cirurgia (Colecistectomia)" -> "Desafio Cirúrgico";
                "Desafio Cirúrgico" -> "Marco Anatômico Chave" -> "Objetivo";
                "Marco Anatômico Chave" -> "Risco";
            }
            """
        }
    },
    "Intestino Delgado": {
        "description": "O duodeno tem irrigação dupla (tronco celíaco e A. mesentérica superior), marcando a transição entre o intestino anterior e médio. O jejuno e o íleo são irrigados exclusivamente pela **artéria mesentérica superior** através de uma rede de arcos arteriais.",
        "arterial_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#fde0dd\"]; edge [color=\"#e63946\"]; subgraph cluster_duodeno { label=\"Duodeno\"; \"A. Gastroduodenal\" -> \"A. Pancreaticoduodenal Superior\" -> \"Duodeno Proximal\"; \"A. Mesentérica Superior\" -> \"A. Pancreaticoduodenal Inferior\" -> \"Duodeno Distal\"; } subgraph cluster_jejunoileo { label=\"Jejuno e Íleo\"; \"A. Mesentérica Superior\" -> \"Aa. Jejuno-ileais\" -> \"Arcos Arteriais\" -> \"Vasos Retos\" -> \"Jejuno e Íleo\"; } }",
        "venous_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#d9ed92\"]; edge [color=\"#1a759f\"]; \"V. Porta Hepática\" [fillcolor=\"#1e6091\", fontcolor=white]; \"V. Mesentérica Superior\" -> \"V. Porta Hepática\"; \"Vv. Pancreaticoduodenais\" -> \"V. Mesentérica Superior\"; \"Vv. Jejuno-ileais\" -> \"V. Mesentérica Superior\"; \"Duodeno\" -> \"Vv. Pancreaticoduodenais\"; \"Jejuno e Íleo\" -> \"Vv. Jejuno-ileais\"; }",
        "innervation_dot": "digraph { rankdir=\"TB\"; subgraph cluster_para { label=\"Parassimpático\"; style=\"rounded\"; color=blue; node [shape=box, style=\"rounded,filled\", fillcolor=\"#cfe1f7\"]; \"N. Vago (NC X)\" -> \"Plexo Mesentérico Superior\" -> \"Intestino Delgado\"; } subgraph cluster_simpa { label=\"Simpático\"; style=\"rounded\"; color=red; node [shape=box, style=\"rounded,filled\", fillcolor=\"#f7cfd6\"]; \"Nn. Esplâncnicos (T8-T10)\" -> \"Gânglio Mesentérico Superior\" -> \"Intestino Delgado\"; } }",
        "clinical": {
            "description": """
            ### Correlação Clínica: Isquemia Mesentérica Aguda
            A **Artéria Mesentérica Superior (AMS)** é a única fonte de sangue para todo o intestino delgado (exceto o duodeno proximal) e parte do intestino grosso. Uma **oclusão súbita** da AMS, geralmente por um êmbolo (coágulo) vindo do coração, interrompe drasticamente o fluxo sanguíneo. Isso causa **isquemia** (falta de oxigênio) e rápida **necrose** (morte do tecido) intestinal.
            Clinicamente, é uma emergência catastrófica que se manifesta com dor abdominal súbita e intensa, desproporcional aos achados do exame físico. O diagnóstico e o tratamento rápidos são cruciais para salvar o intestino e a vida do paciente.
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Causa (Ex: Êmbolo Cardíaco)" [fillcolor="#f7cfd6"];
                "Oclusão Aguda da A. Mesentérica Superior" [fillcolor="#fde0dd"];
                "Interrupção do Fluxo Sanguíneo" [fillcolor="#fde0dd"];
                "Isquemia e Necrose Intestinal" [fillcolor="#e63946", fontcolor=white];
                "Emergência Cirúrgica" [fillcolor="#1e6091", fontcolor=white];
                
                "Causa (Ex: Êmbolo Cardíaco)" -> "Oclusão Aguda da A. Mesentérica Superior" -> "Interrupção do Fluxo Sanguíneo" -> "Isquemia e Necrose Intestinal" -> "Emergência Cirúrgica";
            }
            """
        }
    },
    "Intestino Grosso": {
        "description": "A irrigação é dividida: a **A. Mesentérica Superior** supre o ceco, apêndice, colo ascendente e 2/3 proximais do transverso. A **A. Mesentérica Inferior** supre o 1/3 distal do transverso, descendente, sigmoide e reto superior. A **Artéria Marginal do colo (Arco Justacólico)** conecta os dois sistemas.",
        "arterial_dot": "digraph { rankdir=\"TB\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#fde0dd\"]; edge [color=\"#e63946\"]; subgraph cluster_sup { label = \"Da A. Mesentérica Superior\"; \"A. Ileocólica\" -> \"Ceco, Apêndice, Íleo Terminal\"; \"A. Cólica Direita\" -> \"Colo Ascendente\"; \"A. Cólica Média\" -> \"Colo Transverso (2/3 proximais)\"; } subgraph cluster_inf { label = \"Da A. Mesentérica Inferior\"; \"A. Cólica Esquerda\" -> \"Colo Transverso (1/3 distal), Colo Descendente\"; \"Aa. Sigmóideas\" -> \"Colo Sigmoide\"; } \"A. Cólica Média\" -> \"A. Cólica Esquerda\" [label=\"Artéria Marginal do Colo (Arco Justacólico)\", style=dashed, dir=both]; }",
        "venous_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#d9ed92\"]; edge [color=\"#1a759f\"]; \"V. Porta Hepática\" [fillcolor=\"#1e6091\", fontcolor=white]; \"Colo Ascendente e Transverso Proximal\" -> \"V. Mesentérica Superior\" -> \"V. Porta Hepática\"; \"Colo Descendente e Sigmoide\" -> \"V. Mesentérica Inferior\" -> \"V. Esplênica\" -> \"V. Porta Hepática\"; }",
        "innervation_dot": "digraph { rankdir=\"TB\"; node [shape=box, style=\"rounded\"]; subgraph cluster_prox { label=\"Até 2/3 do Colo Transverso (Intestino Médio)\"; \"Parassimpático (N. Vago)\" [style=\"rounded,filled\", fillcolor=\"#cfe1f7\"]; \"Simpático (Nn. Esplâncnicos Torácicos)\" [style=\"rounded,filled\", fillcolor=\"#f7cfd6\"]; } subgraph cluster_dist { label=\"A partir de 1/3 do Colo Transverso (Intestino Posterior)\"; \"Parassimpático (Nn. Esplâncnicos Pélvicos S2-S4)\" [style=\"rounded,filled\", fillcolor=\"#cfe1f7\"]; \"Simpático (Nn. Esplâncnicos Lombares)\" [style=\"rounded,filled\", fillcolor=\"#f7cfd6\"]; } }",
        "clinical": {
            "description": """
            ### Correlação Clínica: Doença Diverticular e Hemorragia
            **Divertículos** são pequenas herniações (bolsas) da mucosa através da camada muscular do colo, formadas em pontos de fraqueza. Esses pontos de fraqueza correspondem exatamente aos locais onde os **vasos retos** (ramos terminais das artérias cólicas) penetram na parede do intestino para irrigá-lo.
            Com o tempo, a parede de um divertículo pode erodir o vaso reto adjacente, causando uma **hemorragia digestiva baixa**, que se manifesta como um sangramento arterial, indolor e de grande volume. É uma das causas mais comuns de sangramento intestinal em idosos.
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Pontos de Fraqueza na Parede do Colo" [label="Pontos de Fraqueza na Parede do Colo\\n(onde os vasos retos penetram)", fillcolor="#f7cfd6"];
                "Formação de Divertículos" [fillcolor="#fde0dd"];
                "Erosão de Vaso Reto" [label="Erosão de Vaso Reto adjacente", fillcolor="#fde0dd"];
                "Hemorragia Digestiva Baixa" [fillcolor="#e63946", fontcolor=white];
                
                "Pontos de Fraqueza na Parede do Colo" -> "Formação de Divertículos" -> "Erosão de Vaso Reto" -> "Hemorragia Digestiva Baixa";
            }
            """
        }
    },
     "Rins e Suprarrenais": {
        "description": "Os rins recebem um alto fluxo sanguíneo diretamente da aorta abdominal através das **artérias renais**. As glândulas suprarrenais têm uma irrigação tríplice complexa. A drenagem venosa é assimétrica, especialmente para a veia suprarrenal e gonadal esquerdas, que drenam para a **veia renal esquerda**.",
        "arterial_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#fde0dd\"]; edge [color=\"#e63946\"]; \"Aorta Abdominal\" -> \"A. Renal\" -> \"Aa. Segmentares\" -> \"Rim\"; subgraph cluster_supra { label = \"Glândula Suprarrenal\"; \"A. Frênica Inferior\" -> \"A. Suprarrenal Superior\"; \"Aorta Abdominal\" -> \"A. Suprarrenal Média\"; \"A. Renal\" -> \"A. Suprarrenal Inferior\"; } }",
        "venous_dot": "digraph { rankdir=\"LR\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#d9ed92\"]; edge [color=\"#1a759f\"]; \"V. Cava Inferior\" [fillcolor=\"#1e6091\", fontcolor=white]; \"V. Renal Esquerda\" [width=2.5]; \"Rim Direito\" -> \"V. Renal Direita\" -> \"V. Cava Inferior\"; \"Rim Esquerdo\" -> \"V. Renal Esquerda\"; \"G. Suprarrenal Direita\" -> \"V. Suprarrenal Direita\" -> \"V. Cava Inferior\"; \"G. Suprarrenal Esquerda\" -> \"V. Suprarrenal Esquerda\" -> \"V. Renal Esquerda\"; \"Gônada Esquerda\" -> \"V. Gonadal Esquerda\" -> \"V. Renal Esquerda\"; \"V. Renal Esquerda\" -> \"V. Cava Inferior\" [constraint=false]; }",
        "innervation_dot": "digraph { rankdir=\"TB\"; node [shape=box, style=\"rounded,filled\", fillcolor=\"#f7cfd6\"]; subgraph cluster_rim { label=\"Rins\"; \"Nn. Esplâncnicos (T10-L1)\" -> \"Plexo Renal\" -> \"Rins (regulação do fluxo sanguíneo)\"; } subgraph cluster_supra { label=\"Glândula Suprarrenal\"; \"Nn. Esplâncnicos\" -> \"Medula da Suprarrenal\" [label=\"Sinapse direta em células cromafins \\n (liberação de catecolaminas)\"]; } }",
        "clinical": {
            "description": """
            ### Correlação Clínica: Síndrome de Quebra-Nozes (Nutcracker)
            A **veia renal esquerda** possui um trajeto mais longo que a direita e passa entre duas artérias de alta pressão: a **aorta abdominal** (posteriormente) e a **artéria mesentérica superior** (anteriormente).
            Em alguns indivíduos, o ângulo entre essas duas artérias é muito agudo, comprimindo a veia renal esquerda como um quebra-nozes. Essa compressão aumenta a pressão na veia, o que pode causar:
            - **Hematúria:** Sangue na urina, por ruptura de pequenas veias no rim.
            - **Dor no Flanco Esquerdo.**
            - **Varicocele:** Dilatação das veias do testículo esquerdo, já que a veia gonadal esquerda drena para a veia renal esquerda.
            """,
            "dot": """
            digraph {
                rankdir=TB;
                node [shape=box, style="rounded,filled"];
                "Anatomia Específica" [label="V. Renal Esquerda entre\\nAorta e A. Mesentérica Superior", fillcolor="#d9ed92"];
                "Compressão da Veia" [label="Compressão da Veia Renal Esquerda", fillcolor="#fde0dd"];
                "Aumento da Pressão Venosa" [fillcolor="#fde0dd"];
                
                subgraph cluster_sinais {
                    label="Sinais e Sintomas";
                    node [fillcolor="#a8dadc"];
                    "Hematúria (sangue na urina)"; "Dor no Flanco Esquerdo"; "Varicocele (em homens)";
                }
                
                "Anatomia Específica" -> "Compressão da Veia" -> "Aumento da Pressão Venosa" -> {"Hematúria (sangue na urina)", "Dor no Flanco Esquerdo", "Varicocele (em homens)"};
            }
            """
        }
    }
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
        "question": "Um paciente é diagnosticado com uma oclusão lenta e progressiva da Artéria Mesentérica Inferior (AMI). Apesar disso, ele não apresenta sintomas de isquemia grave no colo descendente. Qual estrutura anatômica é a principal responsável por manter o fluxo sanguíneo nessa região?",
        "options": ["Tronco Celíaco", "Anastomoses com as artérias ilíacas", "Vasos Retos do Íleo", "Artéria Marginal do colo (Arco Justacólico)"],
        "answer": "Artéria Marginal do colo (Arco Justacólico)",
        "explanation": "A Artéria Marginal do colo (Arco Justacólico) é uma arcada arterial contínua que conecta os ramos da Artéria Mesentérica Superior (via cólica média) e da Inferior (via cólica esquerda). Em oclusões lentas, ela fornece um fluxo colateral vital, prevenindo a isquemia."
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
    st.sidebar.header("Selecione uma Seção")
    organ_list = list(ORGAN_DATA.keys())
    selected_organ = st.sidebar.radio(
        "Navegue pelas estruturas:",
        organ_list,
        label_visibility="collapsed"
    )

    st.header(f"Detalhes de: {selected_organ}")
    st.markdown(ORGAN_DATA[selected_organ].get("description", ""))

    # Abas para cada sistema
    tab1, tab2, tab3, tab4 = st.tabs(["Vascularização Arterial", "Drenagem Venosa", "Inervação", "Correlações Clínicas"])

    with tab1:
        st.subheader("Fluxograma da Irrigação Arterial")
        # Lógica especial para a Visão Geral para dividir o fluxograma
        if selected_organ == "Visão Geral":
            st.markdown("#### 1. Tronco Celíaco (Intestino Anterior)")
            tronco_celiaco_dot = """
            digraph {
                rankdir="LR"; node [shape=box, style="rounded,filled", fillcolor="#fde0dd"]; edge [color="#e63946"];
                "Aorta Abdominal" -> "Tronco Celíaco";
                "Tronco Celíaco" -> {"A. Gástrica Esquerda", "A. Esplênica", "A. Hepática Comum"};
                "A. Gástrica Esquerda" -> "Estômago, Esôfago"; "A. Esplênica" -> "Baço, Pâncreas, Estômago"; "A. Hepática Comum" -> "Fígado, Vesícula, Duodeno";
            }"""
            st.graphviz_chart(tronco_celiaco_dot)

            st.markdown("#### 2. Artéria Mesentérica Superior (Intestino Médio)")
            ams_dot = """
            digraph {
                rankdir="LR"; node [shape=box, style="rounded,filled", fillcolor="#fde0dd"]; edge [color="#e63946"];
                "Aorta Abdominal" -> "A. Mesentérica Superior";
                "A. Mesentérica Superior" -> {"Aa. Jejuno-ileais", "A. Ileocólica", "A. Cólica Direita", "A. Cólica Média"};
                "A. Ileocólica" -> "Íleo, Ceco, Apêndice"; "A. Cólica Direita" -> "Colo Ascendente"; "A. Cólica Média" -> "Colo Transverso";
            }"""
            st.graphviz_chart(ams_dot)

            st.markdown("#### 3. Artéria Mesentérica Inferior (Intestino Posterior)")
            ami_dot = """
            digraph {
                rankdir="LR"; node [shape=box, style="rounded,filled", fillcolor="#fde0dd"]; edge [color="#e63946"];
                "Aorta Abdominal" -> "A. Mesentérica Inferior";
                "A. Mesentérica Inferior" -> {"A. Cólica Esquerda", "Aa. Sigmoideas", "A. Retal Superior"};
                "A. Cólica Esquerda" -> "Colo Descendente"; "Aa. Sigmoideas" -> "Colo Sigmoide"; "A. Retal Superior" -> "Reto";
            }"""
            st.graphviz_chart(ami_dot)
        elif ORGAN_DATA[selected_organ]["arterial_dot"]:
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
            
    with tab4:
        st.subheader("Correlação Clínica Relevante")
        if "clinical" in ORGAN_DATA[selected_organ] and ORGAN_DATA[selected_organ]["clinical"]["dot"]:
            st.markdown(ORGAN_DATA[selected_organ]["clinical"]["description"])
            st.graphviz_chart(ORGAN_DATA[selected_organ]["clinical"]["dot"])
        else:
            st.info("Nenhuma correlação clínica específica adicionada para esta seção ainda.")


def run_quiz(quiz_type, questions):
    """Executa a interface do quiz com a lógica de reinicialização corrigida."""
    st.header(f"Quiz: {quiz_type}")
    st.write("Teste seus conhecimentos! Selecione a resposta correta e clique em 'Confirmar'.")

    # Inicializa o estado da sessão para o quiz se ele não tiver sido iniciado
    if f'quiz_{quiz_type}_started' not in st.session_state:
        st.session_state[f'quiz_{quiz_type}_started'] = True
        st.session_state[f'quiz_{quiz_type}_current_question'] = 0
        st.session_state[f'quiz_{quiz_type}_score'] = 0
        st.session_state[f'quiz_{quiz_type}_answered'] = False
        st.session_state[f'quiz_{quiz_type}_user_answer'] = None

    # Verifica se o quiz terminou antes de tentar acessar a questão atual
    if st.session_state[f'quiz_{quiz_type}_current_question'] < len(questions):
        q_idx = st.session_state[f'quiz_{quiz_type}_current_question']
        question_data = questions[q_idx]

        st.subheader(f"Pergunta {q_idx + 1}/{len(questions)}")
        st.markdown(f"**{question_data['question']}**")

        user_answer = st.radio(
            "Selecione uma opção:",
            question_data["options"],
            key=f'radio_{quiz_type}_{q_idx}',
            disabled=st.session_state[f'quiz_{quiz_type}_answered']
        )
        st.session_state[f'quiz_{quiz_type}_user_answer'] = user_answer

        col1, col2 = st.columns([1, 1.1])
        with col1:
            if not st.session_state[f'quiz_{quiz_type}_answered']:
                if st.button("Confirmar Resposta", key=f'confirm_{quiz_type}_{q_idx}'):
                    st.session_state[f'quiz_{quiz_type}_answered'] = True
                    if st.session_state[f'quiz_{quiz_type}_user_answer'] == question_data['answer']:
                        st.session_state[f'quiz_{quiz_type}_score'] += 1
                    st.rerun()

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
            # LÓGICA CORRIGIDA: Deleta todas as chaves associadas a este quiz
            keys_to_delete = [k for k in st.session_state.keys() if k.startswith(f'quiz_{quiz_type}')]
            for key in keys_to_delete:
                del st.session_state[key]
            st.rerun()


# --- INTERFACE PRINCIPAL ---

st.title(" Vascularização e Inervação do Abdome")
st.markdown("Bem-vindo! Este aplicativo foi desenvolvido para auxiliar no estudo da vascularização e inervação abdominal.")
st.markdown("Use o menu à esquerda para navegar entre a exploração dos órgãos e os quizzes.")

st.sidebar.title("Menu de Navegação")
app_mode = st.sidebar.selectbox(
    "Escolha uma seção:",
    ["Explorar Órgãos", "Quiz Rápido", "Quiz Clínico"]
)

if app_mode == "Explorar Órgãos":
    show_organ_explorer()
elif app_mode == "Quiz Rápido":
    run_quiz("Rápido", QUICK_QUIZ_QUESTIONS)
elif app_mode == "Quiz Clínico":
    run_quiz("Clínico", CLINICAL_QUIZ_QUESTIONS)

st.sidebar.markdown("---")
st.sidebar.caption("Referência Bibliográfica:")
st.sidebar.caption("MOORE, Keith L. Anatomia orientada para a clínica. 8. ed. Rio de Janeiro: Guanabara Koogan, 2019.")