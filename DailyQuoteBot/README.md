# DailyQuoteBot

Um pequeno bot em Python que obtém uma citação inspiradora aleatória e opcionalmente envia para o Telegram.

## Pré-requisitos

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/) instalado

## Instalação

1. Clone este repositório e acesse a pasta `DailyQuoteBot`.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal para exibir a citação e registrá-la em `quotes.json`:

```bash
python daily_quote_bot.py
```

Cada execução salva a citação obtida junto com data e hora no arquivo `quotes.json`.

### Envio para Telegram (opcional)

Para que o bot envie a citação para um canal ou chat do Telegram, defina duas variáveis de ambiente:

- `DAILY_QUOTE_BOT_TOKEN` – token do bot criado no BotFather.
- `DAILY_QUOTE_CHAT_ID` – ID do chat ou canal que receberá a mensagem.

Exemplo em Linux/macOS:

```bash
export DAILY_QUOTE_BOT_TOKEN="<seu_token>"
export DAILY_QUOTE_CHAT_ID="<chat_id>"
python daily_quote_bot.py
```

Se as variáveis não estiverem configuradas, o bot apenas exibirá a citação no terminal e a salvará no arquivo.

## Licença

Distribuído sob a licença MIT.
