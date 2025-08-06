const venom = require('venom-bot');
const express = require('express');
const app = express();

app.use(express.json());

// Inicia sessão do WhatsApp
venom
  .create({
    session: 'minha-sessao', // nome da sessão
    multidevice: true, // compatível com multi-dispositivo
  })
  .then((client) => start(client))
  .catch((erro) => {
    console.log(erro);
  });

function start(client) {
  console.log('✅ WhatsApp conectado!');

  // Receber mensagens
  client.onMessage((message) => {
    console.log(`Mensagem recebida de ${message.from}: ${message.body}`);

    if (message.body.toLowerCase() === 'oi') {
      client.sendText(message.from, 'Olá! Seja bem-vindo ao nosso atendimento 🤖');
    }
  });

  // Enviar mensagem via API HTTP
  app.post('/send', (req, res) => {
    const { number, text } = req.body;
    client
      .sendText(`${number}@c.us`, text)
      .then(() => res.send({ status: 'ok' }))
      .catch((err) => res.status(500).send(err));
  });

  app.listen(3000, () => {
    console.log('🚀 API rodando na porta 3000');
  });
}
