#  Modelo de Classificação de Galáxias
 
Este repositório contém um modelo de classificação de galáxias em contêiner Docker como forma de avaliação da matéria IC-007 Tópicos de Banco de Dados. O modelo é desenvolvido usando a biblioteca Scikit-learn e é empacotado em um contêiner Docker para facilitar a implantação e o uso.

## Pré-requisitos

Antes de usar este modelo, certifique-se de ter os seguintes requisitos instalados:

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)

## Como usar

Siga as etapas abaixo para executar o modelo de classificação de galáxias:

1. Clone este repositório em sua máquina local:

```
git clone https://github.com/RodrigoAB93/Classificador_Galaxias
```

2. Navegue até o diretório raiz do projeto:

```
cd Classificador_Galaxias
```

3. Carregue a imagem Docker do modelo a partir do link:
   
    [Imagem Docker](https://drive.google.com/drive/folders/1RLyJjzxzCSs93SyesDY4iJbOtZocP6Ix)
```
docker load -i path/to/classificador-galaxias-docker.tar

```

4. Execute o contêiner Docker:

```
docker run -p 8000:8000 classificador-galaxias-docker 
```

5. Acesse a API em ferramentas como o Postman ou o Insomnia:

```
http://localhost:8000/classify
```

6. Envie uma solicitação POST contendo os dados da galáxia a ser classificada no formato JSON. Exemplo:

```json
{
  "u": 17.8,
  "r": 0.956,
  "g": 625.4,
  "i": 42.7,
  "z": 68.9,
  "deVAB_u": 115.2,
  "deVAB_g": 0.191,
  "deVAB_r": 105.7,
  "deVAB_i": 83.5,
  "deVAB_z": 581.3,
  "mCr4_u": 106,
  "mCr4_g": 956,
  "mCr4_r": 16.9,
  "mCr4_i": 36.1,
  "mCr4_z": 67.9,
  "petroR50_r": 6.9,
  "petroR90_r": 7.3,
  "petroR50_u": 1.8,
  "petroR90_u": 9.2,
  "petroR50_z": 7.31,
  "petroR90_z": 6.64
}
```
- Existe um arquivo chamado: modelo-requisição que possui formato txt neste repositório com mais dois exemplos.

7. O modelo classificará a galáxia com base nos dados fornecidos e retornará o resultado da classificação.


## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.


Agradecemos seu interesse e contribuição!
