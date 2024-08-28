import streamlit as st
import datetime
import uuid

def aditivos():
    ###Função tabela de aditivos
    st.markdown(
        """
        <style>
        /* Mudar a cor de fundo da sidebar */
        [data-testid="stSidebar"] {
            background-color: #034001; /* Escolha a cor que você deseja */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.expander("Aditivos"):
    
        with st.form(key=f'sideform_{form_id}', clear_on_submit=False):
            st.markdown(
                """
                <h1 style='color: #ffffff; font-size: 30px;'>Tabela aditivos:</h1>
                """, 
                unsafe_allow_html=True
            )
            first_column, second_column, third_column = st.columns([1.2,1,1])
            submit_button_sidebar = st.form_submit_button("Salvar")
            with first_column:
                # Label para "Aditivo"
                st.markdown(
                    """
                    <style>
                    .custom-label-aditivo {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 38px; /* Alinha verticalmente com o input */
                    }
                    </style>
                    <p class="custom-label-aditivo">Aditivo:</p>
                    """,
                    unsafe_allow_html=True
                )
                

                # Label para "Enzima Amilex"
                st.markdown(
                    """
                    <style>
                    .custom-label-enzima {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 36px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-enzima">Enzima Amilex:</p>
                    """,
                    unsafe_allow_html=True
                )

                # Label para "Cloreto de Cálcio"
                st.markdown(
                    """
                    <style>
                    .custom-label-cloreto {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 40px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-cloreto">Cloreto de Cálcio:</p>
                    """,
                    unsafe_allow_html=True
                )

                # Label para "Ácido Lático/Fosfórico"
                st.markdown(
                    """
                    <style>
                    .custom-label-acido {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 40px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-acido">Ácid Lático /Fosfórico:</p>
                    """,
                    unsafe_allow_html=True
                )

                # Label para "Sulfato de Zinco"
                st.markdown(
                    """
                    <style>
                    .custom-label-sulfato {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 40px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-sulfato">Sulfato de Zinco:</p>
                    """,
                    unsafe_allow_html=True
                )

                # Label para "Lupulo Resina Pura"
                st.markdown(
                    """
                    <style>
                    .custom-label-lupulo {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 17px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 40px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-lupulo">Lupulo resina pura:</p>
                    """,
                    unsafe_allow_html=True
                )

                # Label para "Maxflow 4G"
                st.markdown(
                    """
                    <style>
                    .custom-label-maxflow {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        display: flex;
                        align-items: center;
                        height: 40px; /* Alinha verticalmente com o input */
                        
                    }
                    </style>
                    <p class="custom-label-maxflow">Maxflow 4G:</p>
                    """,
                    unsafe_allow_html=True
                )


            with second_column:
                st.markdown(
                    """
                    <style>
                    .custom-label {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        height: 38px; /* Alinha verticalmente com o input */
                        margin-bottom: 5px; /* Espaçamento entre labels */
                    }
                    </style>
                    <p class="custom-label">Quant:</p>
                    """,
                    unsafe_allow_html=True
                )

                input_enzima_amilex_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_enzima_amilex_quant_{form_id}")
                input_cloreto_de_calcio_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_cloreto_de_calcio_quant_{form_id}")
                input_acido_latico_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_acido_latico_quant_{form_id}")
                input_sulfato_de_zinco_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_sulfato_de_zinco_quant_{form_id}")
                input_lupulo_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_lupulo_quant_{form_id}")
                input_maxflow_quant = st.text_input("", label_visibility="collapsed", key=f"input_input_maxflow_quant_{form_id}")



            with third_column:
                st.markdown(
                    """
                    <style>
                    .custom-label {
                        color: #ffffff;  /* Cor da fonte */
                        font-size: 18px; /* Tamanho da fonte */
                        font-weight: bold; /* Negrito opcional */
                        height: 45px; /* Alinha verticalmente com o input */
                        margin-bottom: 5px; /* Espaçamento entre labels */
                    }
                    </style>
                    <p class="custom-label">Cl/Lote:</p>
                    """,
                    unsafe_allow_html=True
                )
                input_enzima_amilex_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_enzima_amilex_cl_lote_{form_id}")
                input_cloreto_de_calcio_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_cloreto_de_calcio_cl_lote_{form_id}")
                input_acido_latico_quant_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_acido_latico_cl_lote_{form_id}")
                input_sulfato_de_zinco_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_sulfato_de_zinco_cl_lote_{form_id}")
                input_lupulo_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_lupulo_cl_lote_{form_id}")
                input_maxflow_cl_lote = st.text_input("", label_visibility="collapsed", key=f"input_input_maxflow_cl_lote_{form_id}")
    st.markdown("---")

def info_fabrico_principal():
    
    ### função para pegar informações principais do fabrico
    with st.container():
        ############################# Criação de colunas ###############################
        first_column, second_column, third_column, fourth_column = st.columns(4)
        
        with first_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Fabrico:</p>
                """,
                unsafe_allow_html=True
            )

            input_Fabrico = st.text_input("",label_visibility="collapsed",key=f"input_fabrico_{form_id}")
        ## Coluna 2
        with second_column:

            st.markdown(
                """
                <style>
                .custom-label {
                    color: #034001;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Data:</p>
                """,
                unsafe_allow_html=True
            )

            selected_date = st.date_input(
                "Data do Fabrico",
                datetime.date.today(),
                label_visibility="collapsed"
            )
        with third_column:

            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Ord. de Produto:</p>
                """,
                unsafe_allow_html=True
            )

            input_ordem_do_produto = st.text_input("",label_visibility="collapsed", key=f"input_ordem_do_produto_{form_id}")
    st.markdown("---")

def cara_da_pagina():
    
    ### Definine a cor e o titulo da pagina
    first_column, second_column  = st.columns([5,2])
    with first_column:
        st.image("img/Heineken-Logo.png",use_column_width=True)

    ####################################### DEFININDO COR DA PAGINA #######################################

    st.markdown(
        """
        <style>
        /* Cor de fundo para toda a página */
        .stApp {
            background-color: #025918;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def input_silo():
    
    with st.container():
        first_column, second_column, third_column, fourth_column, fifth_column, sixth_column = st.columns(6)
        with first_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Silo:</p>
                """,
                unsafe_allow_html=True
            )
        

            input_silo1 = st.selectbox(
                "Silo 1",  # Label para o primeiro selectbox
                ("1","2","3","4","5","6","7","8","9"),
                label_visibility="collapsed",
                key=f"silo1_{form_id}"  # Chave única para o primeiro selectbox
            )

            input_silo2 = st.selectbox(
                "Silo 2",  # Label para o primeiro selectbox
                ("1","2","3","4","5","6","7","8","9"),
                label_visibility="collapsed",
                key=f"silo2_{form_id}"  # Chave única para o primeiro selectbox
            )
            input_silo3 = st.selectbox(
                "Silo 3",  # Label para o primeiro selectbox
                ("1","2","3","4","5","6","7","8","9"),
                label_visibility="collapsed",
                key=f"silo3_{form_id}"  # Chave única para o primeiro selectbox
            )
            input_silo1 = st.selectbox(
                "Silo 4",  # Label para o primeiro selectbox
                ("1","2","3","4","5","6","7","8","9"),
                label_visibility="collapsed",
                key=f"silo4_{form_id}"  # Chave única para o primeiro selectbox
            )
            

        with second_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Malte:</p>
                """,
                unsafe_allow_html=True
            )

            input_malte1 = st.text_input("",key=f"input_malte1_{form_id}",label_visibility="collapsed")
            input_malte2 = st.text_input("",key=f"input_malte2_{form_id}",label_visibility="collapsed")
            input_malte3 = st.text_input("",key=f"input_malte3_{form_id}",label_visibility="collapsed")
            input_malte4 = st.text_input("",key=f"input_malte4_{form_id}",label_visibility="collapsed")
            
            st.markdown(
                """
                <style>
                .custom-label-torrado {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                    text-align: center; /* Centraliza o texto */
                }
                </style>
                <p class="custom-label-torrado ">Malte torrado:</p>
                """,
                unsafe_allow_html=True
            )


        with third_column:
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Rend:</p>
                """,
                unsafe_allow_html=True
            )

            input_rendimento1 = st.text_input("",key=f"input_rendimento1_{form_id}",label_visibility="collapsed")
            input_rendimento2 = st.text_input("",key=f"input_rendimento2_{form_id}",label_visibility="collapsed")
            input_rendimento3 = st.text_input("",key=f"input_rendimento3_{form_id}",label_visibility="collapsed")
            input_rendimento4 = st.text_input("",key=f"input_rendimento4_{form_id}",label_visibility="collapsed")
            input_rendimento_malte_torrado = st.text_input("",key=f"input_rendimento_malte_torrado_{form_id}",label_visibility="collapsed")
            
            
        with fourth_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Tipo:</p>
                """,
                unsafe_allow_html=True
            )

            input_tipo1 = st.selectbox(
                "tipo 1",  # Label para o primeiro selectbox
                ("A","B"),
                label_visibility="collapsed",
                key=f"tipo1_{form_id}"  # Chave única para o primeiro selectbox
            )

            input_tipo2 = st.selectbox(
                "tipo 2",  # Label para o primeiro selectbox
                ("A","B"),
                label_visibility="collapsed",
                key=f"tipo2_{form_id}"  # Chave única para o primeiro selectbox
            )
            
            input_tipo3 = st.selectbox(
                "tipo 3",  # Label para o primeiro selectbox
                ("A","B"),
                label_visibility="collapsed",
                key=f"tipo3_{form_id}"  # Chave única para o primeiro selectbox
            )

            input_tipo4 = st.selectbox(
                "tipo 4",  # Label para o primeiro selectbox
                ("A","B"),
                label_visibility="collapsed",
                key=f"tipo4_{form_id}"  # Chave única para o primeiro selectbox
            )

            st.markdown(
                """
                <style>
                .custom-label-torrado  {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                    text-align: center; /* Centraliza o texto */
                }
                </style>
                <p class="custom-label-torrado ">torrado:</p>
                """,
                unsafe_allow_html=True
            )


        with fifth_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Cl/Lote:</p>
                """,
                unsafe_allow_html=True
            )

            input_Cl_lote1 = st.text_input("",key=f"input_Cl_lote1_{form_id}",label_visibility="collapsed")
            input_Cl_lote2 = st.text_input("",key=f"input_Cl_lote2_{form_id}",label_visibility="collapsed")
            input_Cl_lote3 = st.text_input("",key=f"input_Cl_lote3_{form_id}",label_visibility="collapsed")
            input_Cl_lote4 = st.text_input("",key=f"input_Cl_lote4_{form_id}",label_visibility="collapsed")
            input_Cl_lote_torrado = st.text_input("",key=f"input_Cl_lote_torrado_{form_id}",label_visibility="collapsed")


        with sixth_column:
            
            st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Quant(KG):</p>
                """,
                unsafe_allow_html=True
            )

            input_quantidade1 = st.text_input("",key=f"input_quantidade1_{form_id}", label_visibility="collapsed")
            input_quantidade2 = st.text_input("",key=f"input_quantidade2_{form_id}", label_visibility="collapsed")
            input_quantidade3 = st.text_input("",key=f"input_quantidade3_{form_id}", label_visibility="collapsed")
            input_quantidade4 = st.text_input("",key=f"input_quantidade4_{form_id}", label_visibility="collapsed")
            input_quantidade_torrado = st.text_input("",key=f"input_quantidade_torrado_{form_id}", label_visibility="collapsed")
    st.markdown("---")

def input_total():
    
    with st.container():
        first_column, second_column, third_column = st.columns([3,2,1])

        with second_column:
            st.markdown(
                """
                <style>
                .custom-label-right {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                    text-align: right; /* Alinhamento à direita */
                    display: flex;
                    justify-content: flex-end;
                }
                </style>
                <p class="custom-label-right">Total de matéria prima:</p>
                """,
                unsafe_allow_html=True
            )


            st.markdown(
                """
                <style>
                .custom-label-right {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                    text-align: right; /* Alinhamento à direita */
                    display: flex;
                    justify-content: flex-end;
                }
                </style>
                <p class="custom-label-right">Total de Extrato:</p>
                """,
                unsafe_allow_html=True
            )


        with third_column:
            input_total_materia_prima = st.text_input("",key=f"total materia prima_{form_id}",label_visibility="collapsed")
            input_total_extrato = st.text_input("",key=f"total extrato_{form_id}",label_visibility="collapsed")

    with st.container():
        first_column, second_column, third_column = st.columns([4,1,1])
        with first_column:
            st.markdown(
                """
                <style>
                .custom-label-center {
                    color: #111111;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                    text-align: center; /* Centraliza o texto */
                }
                </style>
                <p class="custom-label-right">Rel. (%) Malte HNK MDV A / Malte Agrária:</p>
                """,
                unsafe_allow_html=True
            )
        with second_column:
            input_rel_malte_hnk = st.text_input("",key=f"rel_malte_hnk_{form_id}",label_visibility="collapsed")
        with third_column:
            input_rel_malte_agraria = st.text_input("",key=f"rel_malte_agraria_{form_id}",label_visibility="collapsed")

    st.markdown("---")

def input_tempo_descida_moagem():
    with st.container():
        
        st.markdown(
                """
                <style>
                .custom-label {
                    color: #ffffff;  /* Cor da fonte */
                    font-size: 18px; /* Tamanho da fonte */
                    font-weight: bold; /* Negrito opcional */
                }
                </style>
                <p class="custom-label">Tempo Inicio moagem até descida do Fab:</p>
                """,
                unsafe_allow_html=True
            )
        first_column, second_column = st.columns([1,3])
        with first_column:
            time = st.time_input("",label_visibility="collapsed")
        ##with second_column:
            
    st.markdown("---")
############################################## PAGINA #################################################
cara_da_pagina()

########################################### Gerar ID único ##############################################
if "form_id" not in st.session_state:
    st.session_state.form_id = str(uuid.uuid4())  # Gera um ID único

form_id = st.session_state.form_id


############################################# SIDEBAR FORMS ############################################
with st.sidebar:
    aditivos()
    
    
####################################### CRIANDO FORMS DO FABRICO #######################################
with st.form(key=f'form_{form_id}', clear_on_submit=False):
    
    info_fabrico_principal()
    input_silo()
    ############################ Container tempo incio de moagem até descida ###########################    
    
    input_tempo_descida_moagem()

    ############################### Container soma de total ###############################
    
    input_total()

    #################################### Container Relação Malte #####################################
    
            

    submit_button = st.form_submit_button("Salvar")
            

    


    

        
