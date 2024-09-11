# BANCO DE DADOS VETORIAL SIMPLES

<p>Este código cria um banco de dados vetorial simples usando python, com as bibliotecas NumPy para manipulação de vetores e FAISS (Facebook AI Similarity Search) para busca rápida de vetores.<br></p>

<p>Foram criados vetores aletórios, preenchidos com dados do tipo float, utilizando o módulo random.<br></p>

<h3>Como funciona um banco de dados vetorial?</h3>
<h4>Vetorização dos dados:</h4>

O primeiro passo é transformar os dados (como texto, imagens ou áudio) em vetores. Isso é feito por meio de modelos de machine learning (como BERT ou Word2Vec para texto, ResNet para imagens, etc.), que codificam as informações em vetores de alta dimensão. <br>

<h4>Armazenamento de vetores:</h4>

Cada vetor gerado é armazenado junto com um identificador (ID) que representa o dado original. Isso permite a recuperação dos dados quando for realizada uma busca.<br>
<h4>Busca por similaridade:</h4>

As consultas no banco de dados vetorial são feitas utilizando a similaridade entre vetores. Uma métrica comum para isso é a distância de cosseno ou a distância euclidiana, que mede quão similares dois vetores são. Quanto mais próximos dois vetores estiverem no espaço vetorial, mais similares os dados correspondentes são.<br>
<h4>Indexação vetorial:</h4>

Para otimizar a busca em grandes conjuntos de vetores, são usadas técnicas de indexação, como HNSW (Hierarchical Navigable Small World) ou FAISS (Facebook AI Similarity Search), que tornam a recuperação de vetores muito mais rápida em grandes volumes de dados.<br>

<h4>Passo 1: Instalar bibliotecas necessárias</h4>
<p>pip install numpy faiss-cpu</p>

<h4>Passo 2: Download do código e execução</h4>
<p> Baixe o código em sua máquina local ou em um ambiente remoto, e execute-o. Lembre-se de ter todas as dependências instaladas previamente.</p>