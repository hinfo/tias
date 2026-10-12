# SCHEMA DO BANCO DE DADOS DO COMIC - https://comic.lapinf.ufn.edu.br


class DbSchema:
    def get_schema(self) -> str:
        schema = """
    {
        "avaliacao_avaliacao": [
            {
                "nome": "id",
                "tipo": "int(11)",
            },
            {
                "nome": "dt_avaliacao_responsavel",
                "tipo": "datetime(6)",
            },
            {
                "nome": "tem_introducao_responsavel",
                "tipo": "varchar(25)",
            },
            {
                "nome": "tem_justificativa_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_objetivos_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_desenho_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_local_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_amostra_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_inclusao_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_coleta_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_coleta_instrumento_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_etica_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_riscos_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_assentimento_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_consentimento_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_confidencialidade_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_exequivel_estudo_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_cronograma_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_orcamento_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_orcamento_agencia_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_referencias_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_assitencia_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_relevancia_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_mudanca_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_nova_pratica_assistencial_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_produto_responsavel",
                "tipo": "varchar(25)"
            },
            {
                "nome": "parecer_avaliador_responsavel",
                "tipo": "longtext"
            },
            {
                "nome": "dt_avaliacao_suplente",
                "tipo": "datetime(6)"
            },
            {
                "nome": "tem_introducao_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_justificativa_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_objetivos_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_desenho_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_local_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_amostra_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_inclusao_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_coleta_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_coleta_instrumento_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_etica_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_riscos_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_assentimento_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_consentimento_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_confidencialidade_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_metodologia_exequivel_estudo_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_cronograma_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_orcamento_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_orcamento_agencia_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_referencias_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_assitencia_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_relevancia_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_mudanca_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_nova_pratica_assistencial_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "tem_produto_suplente",
                "tipo": "varchar(25)"
            },
            {
                "nome": "parecer_avaliador_suplente",
                "tipo": "longtext"
            },
            {
                "nome": "avaliador_responsavel_id",
                "tipo": "int(11)",
            },
            {
                "nome": "avaliador_suplente_id",
                "tipo": "int(11)",
            {
                "nome": "submissao_id",
                "tipo": "int(11)",
            }
        ],
        "comissao_comissao": [
            {
                "nome": "id"
                "tipo": "varchar(25)",
            {
                "nome": "avaliacao_comissao_id",
                "tipo": "int(11)"
            {
                "nome": "arquivo_parecer_comissao_pendencia",
                "tipo": "varchar(100)",
            {
                "nome": "comentario",
                "tipo": "longtext"
            },
            {
                "nome": "dt_trancado",
                "tipo": "date"
            },
            {
                "nome": "slug",
                "tipo": "varchar(200)",
                "chave": "MUL"
            }
        ],
        "edital_edital": [
            {
                "nome": "id",
                "tipo": "int(11)",
            },
            {
                "nome": "numero",
                "tipo": "varchar(20)",
            },
        ],
        "instituicao_instituicao": [

                "tipo": "varchar(100)",
            },
        ],
        "submissao_submissao": [

                "tipo": "varchar(150)",
            },
            {
                "nome": "grupo_pesquisa",
                "tipo": "varchar(50)",
            {
                "nome": "titulo",
                "tipo": "longtext",
            },
            {
                "nome": "resumo",
                "tipo": "longtext",
            },
            {
                "nome": "arquivo_comite_etica",
                "tipo": "varchar(100)",
            {
                "nome": "registros_apos_aprovacao",
                "tipo": "longtext"
            },
            {
                "nome": "dt_atualizacao_submissao",
                "tipo": "datetime(6)"
            },
            {
                "nome": "arquivo_relatorio_final",
                "tipo": "varchar(100)"
            },
            {
                "nome": "arquivo_relatorio_parcial",
                "tipo": "varchar(100)"
            },
            {
                "nome": "arquivo_emenda1",
                "tipo": "varchar(100)"
            },
            {
                "nome": "arquivo_emenda2",
                "tipo": "varchar(100)"
            },
            {
                "nome": "arquivo_emenda3",
                "tipo": "varchar(100)"
            },
            {
                "nome": "dt_cadastro_submissao",
                "tipo": "datetime(6)",
            },
            {
                "nome": "slug",
                "tipo": "varchar(200)",
        ],
        "submissao_submissao_colaborador": [
            {
                "nome": "id"
                "tipo": "int(11)",
            }
                "tipo": "int(11)",
            }
                "tipo": "varchar(128)"
            {
                "nome": "cpf",
                "tipo": "varchar(14)",
            {
                "nome": "rg",
                "tipo": "varchar(14)"
            },
            {
                "nome": "matricula",
                "tipo": "varchar(10)"
            },
            {
                "nome": "lattes",
                "tipo": "varchar(100)"
            },
            {
                "nome": "area_conhecimento_cnpq",
                "tipo": "varchar(50)"
            },
            {
                "nome": "curso_graduacao_vinculado",
                "tipo": "varchar(50)",
            },
            {
                "nome": "curso_pos_graduacao",
                "tipo": "varchar(50)",
            {
                "nome": "grupo_pesquisa",
                "tipo": "varchar(50)",
            {
                "nome": "is_active",
                "tipo": "tinyint(1)",
            },
            {
                "nome": "instituicao_id",
                "tipo": "int(11)",
            {
                "nome": "slug",
                "tipo": "varchar(200)",
        ]
    }
    """
        return schema
