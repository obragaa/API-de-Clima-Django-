# Projeto de Previsão do Tempo

Este é um projeto simples de previsão do tempo usando Django e a API do OpenWeatherMap.

## Instalação

1. Clone este repositório.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências com `pip install -r requirements.txt`.
4. Execute as migrações com `python manage.py migrate`.
5. Crie uma chave gratuita em https://home.openweathermap.org/api_keys e defina a variável de ambiente `OPENWEATHER_API_KEY` com ela (no Windows: `set OPENWEATHER_API_KEY=sua_chave`; no Linux/macOS: `export OPENWEATHER_API_KEY=sua_chave`).

## Uso

1. Inicie o servidor com `python manage.py runserver`.
2. Abra o seu navegador e acesse `http://localhost:8000`.
3. Digite o nome de uma cidade no campo de texto e clique em "Buscar".

## Funcionalidades

- Buscar a previsão do tempo para uma cidade específica.
- Exibir a temperatura, a descrição do clima e um ícone representativo.

## Contribuição

Se você quiser contribuir para este projeto, por favor, faça um fork do repositório, crie uma branch para a sua funcionalidade ou correção de bug, faça as suas alterações e envie um pull request.