<img width="1640" height="856" alt="deckullt" src="https://github.com/user-attachments/assets/71a33800-87c0-4979-9b4d-1784d7401284" />

https://github.com/user-attachments/assets/74320509-d19a-4ed7-be41-8271e4e61914

# DeckU - Server

Parte do projeto **DeckU**: transformar um Steam Deck em um controle e uma segunda tela estilo WiiU GamePad para o PC.

Este repositório contém o **servidor**, que roda no PC (Windows). Ele recebe os dados enviados pelo [DeckU-Client](https://github.com/luizDiasDev/DeckU-Client) (rodando no Steam Deck) e os traduz para um controle virtual reconhecido pelo Windows.

> O repositório do cliente (parte que roda no Deck) está aqui: **[DeckU-Client](https://github.com/luizDiasDev/DeckU-Client)**

---

## 💡 Sobre o projeto

A ideia surgiu como um desafio pessoal de aprendizado para sair da zona de conforto e aprender programação na prática — sockets, POO, boas práticas, tudo isso construído do zero, sem tutorial pronto pra seguir.

---

## ⚙️ O que esse servidor faz hoje

- Recebe pacotes via **socket UDP** enviados pelo cliente no Deck.
- Desserializa o JSON recebido de volta para um dicionário Python com o estado do controle.
- Repassa esse estado para a classe `VirtualGamepad`, que usa a biblioteca **vgamepad** para criar um controle Xbox virtual reconhecido nativamente pelo Windows.
- Atualiza em tempo real os analógicos e botões do controle virtual conforme os dados chegam — permitindo, por exemplo, jogar jogos no PC usando o Steam Deck como controle físico.

## 🚧 O que ainda falta / limitações conhecidas

- **Perda ocasional de pacotes**: por usar UDP (escolha intencional, priorizando baixa latência sobre garantia de entrega), às vezes um pacote se perde e o controle demora um instante para "voltar ao normal". É um ponto que pretendo melhorar.
- Nem todos os botões (ex: press/release de botões como A/B/X/Y) estão 100% finalizados — o mapeamento básico funciona, mas ainda há ajustes pendentes.
- A parte de **transmissão de tela** (o Deck funcionando como uma segunda tela, ao estilo WiiU) ainda **não está integrada no código**. Hoje, essa parte é validada manualmente com ferramentas externas:
  - Um **Virtual Display Driver** cria um monitor virtual no Windows.
  - O **ffmpeg** é executado manualmente (fora do Python) para capturar esse monitor virtual e transmitir via UDP para o Deck.
  - Existe lag perceptível nesse processo atual, além de depender de comandos rodados manualmente em vez de estar automatizado no projeto.
  - Automatizar esse pipeline dentro do próprio código Python é a próxima grande etapa do projeto.

---

## 🏗️ Arquitetura

O projeto é organizado em classes com responsabilidades separadas:

- **`Receiver`**: escuta a porta UDP, recebe os pacotes e desserializa o JSON de volta para dicionário. Não sabe nada sobre controles virtuais.
- **`VirtualGamepad`**: recebe o dicionário de estado e traduz isso em comandos para a biblioteca `vgamepad`. Não sabe nada sobre rede.
- **`main.py`**: orquestra as duas classes através de um **callback** — o `Receiver` avisa quando novos dados chegam, e o `main.py` repassa isso pro `VirtualGamepad`.

Essa separação segue o princípio de responsabilidade única: cada classe faz uma coisa só, e pode evoluir/ser substituída sem afetar as outras.

---

## 🔧 Tecnologias

- **Python 3.13**
- [`vgamepad`](https://github.com/yannbouteiller/vgamepad) — criação de controle virtual Xbox reconhecido pelo Windows (via ViGEmBus)
- `socket` (biblioteca padrão) — comunicação via UDP
- `json` (biblioteca padrão) — desserialização dos dados
- `python-dotenv` — gerenciamento de configuração via variáveis de ambiente
- **ffmpeg** (ferramenta externa, ainda não integrada ao código) — captura e streaming de tela
- **Virtual Display Driver** (ferramenta externa) — criação de monitor virtual no Windows

---

## ▶️ Como rodar

1. Instale o **ViGEmBus** (driver necessário para o `vgamepad` funcionar): [ViGEmBus Releases](https://github.com/ViGEm/ViGEmBus/releases)

2. Clone o repositório:
   ```bash
   git clone https://github.com/luizDiasDev/DeckU-Server.git
   cd DeckU-Server
   ```

3. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com as configurações (veja `.env.example`):
   ```
   PC_IP=0.0.0.0
   PORT=5005
   ```

5. Rode:
   ```bash
   python main.py
   ```

6. No Steam Deck, rode o [DeckU-Client](https://github.com/luizDiasDev/DeckU-Client) correspondente.

---

## 📌 Status

🟡 **MVP funcional** — o PC já reconhece o Deck como controle Xbox virtual e é possível jogar normalmente. A parte de segunda tela ainda depende de ferramentas externas rodadas manualmente.

---

## 🗺️ Próximos passos

- [ ] Finalizar mapeamento de todos os botões (press/release)
- [ ] Melhorar estabilidade da conexão (lidar com perda de pacotes)
- [ ] Automatizar a captura e o streaming de tela dentro do próprio código Python (hoje depende de ffmpeg rodado manualmente)
- [ ] Reduzir a latência da transmissão de tela
- [ ] Implementar recepção de toques do Deck para controlar o mouse/tela do PC

---

## 👤 Autor

**Luiz Dias**
Projeto pessoal de aprendizado em Python, redes e programação orientada a objetos.

