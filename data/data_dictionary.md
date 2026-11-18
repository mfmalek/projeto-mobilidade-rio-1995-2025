# Dicionário de Dados - Mobilidade Urbana no Rio de Janeiro (1995-2025)

Este documento descreve as variáveis presentes no conjunto de dados tratado (`data/processed/passageiros_rio_tratado.csv.gz`), seguindo os princípios FAIR de interoperabilidade.

| Variável | Tipo Primitivo | Unidade | Descrição / Significado de Negócio |
| :--- | :--- | :--- | :--- |
| `ano` | `int` | Anos (1995-2025) | Ano de referência da observação estatística. |
| `onibus` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros transportados pelo sistema rodoviário (ônibus municipais/intermunicipais regulados). |
| `metro` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros transportados pelo sistema metroviário (MetrôRio). |
| `trem` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros transportados pelo sistema ferroviário de trens urbanos (SuperVia/Flumitrens). |
| `bonde` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros transportados pelos bondes (ex: Bondes de Santa Teresa). |
| `hidroviario` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros no transporte aquaviário/barcas (CCR Barcas / Conerj / Transtur). |
| `aeroviario` | `float` | Passageiros ($\times 1000$) | Média diária de passageiros movimentados nos aeroportos localizados no município (Santos Dumont / Galeão). |
| `total_passageiros` | `float` | Passageiros ($\times 1000$) | Soma do movimento médio diário de todos os modais no respectivo ano (métrica derivada). |