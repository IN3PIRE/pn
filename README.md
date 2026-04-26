# PN Bot

Welcome to **PN**, a beginner‑friendly Discord bot built with the latest `discord.py`! This repository provides a simple yet powerful foundation for creating Discord bots using **prefix commands**, **slash commands**, and **event handlers**.

---

## ✨ Features
- **Prefix Commands** – Classic `!ping` style commands for quick testing.
- **Slash Commands** – Modern, discoverable commands powered by Discord's Interaction API.
- **Event Handlers** – React to events like `on_message`, `on_ready`, and more.
- **Fully Typed** – Utilises type hints for better IDE support and readability.
- **Ready‑to‑Deploy** – Includes a minimal Dockerfile and a GitHub Actions workflow for CI.

---

## 📦 Getting Started
1. **Clone the repo**
   ```bash
   git clone https://github.com/IN3PIRE/pn.git
   cd pn
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -U discord.py
   ```
4. **Add your bot token**
   - Rename `.env.example` to `.env` and replace `YOUR_BOT_TOKEN` with your token.
5. **Run the bot**
   ```bash
   python bot.py
   ```

---

## 🛠️ Commands & Events
### Prefix Commands
```python
@bot.command()
async def ping(ctx):
    """Simple ping command"""
    await ctx.send('Pong!')
```

### Slash Commands
```python
@bot.tree.command(name='hello', description='Say hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello, world!')
```

### Event Handlers
```python
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests. Please follow the standard GitHub flow:
1. Fork the repo.
2. Create a feature branch (`git checkout -b feat/your-feature`).
3. Commit your changes (`git commit -m "feat: add xyz"`).
4. Push and open a PR.

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀
