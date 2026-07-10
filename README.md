# Classificação de Arritmias em ECG com Rede Neural Convolucional

*Pipeline completo de processamento de biosinais: do ECG bruto do MIT-BIH à
classificação de batimentos, com detector de QRS (Pan-Tompkins) implementado
do zero em NumPy.*

> **Projeto acadêmico e demonstrativo.** Não é um dispositivo médico e não
> deve ser utilizado para diagnóstico ou qualquer decisão clínica.

Projeto pessoal desenvolvido para consolidar competências em Inteligência
Artificial e Processamento Digital de Sinais. O pipeline está organizado em
sete etapas:

1. Aquisição dos dados
2. Pré-processamento
3. Detecção de QRS
4. Segmentação de batimentos
5. Representação do batimento
6. Classificação
7. Avaliação

O detalhamento visual de cada etapa, com os gráficos intermediários do sinal,
está no notebook [`notebooks/01_pipeline_completo.ipynb`](notebooks/).

---

## Resultados

<!-- TODO: tabela de F1 por classe AAMI + matriz de confusão -->
<!-- Registrar aqui: split inter-paciente, DS1/DS2 (de Chazal et al., 2004) -->

---

## Estrutura do projeto