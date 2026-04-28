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
 source .venv/bin/activate # On Windows: .venv\Scripts\activate
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

We welcome contributions! Please see our detailed [Contributing Guide](CONTRIBUTING.md) for:

- 🌟 **Star Requirement**: Must star repo before PR merge
- 📝 Step-by-step contribution process
- ✅ Code standards and best practices
- 🏷️ Issue labels and assignment process

### Quick Contributing Steps:

1. **Find an Issue**: Look for `good first issue` labels
2. **Comment**: Say "I would like to work on this" on the issue
3. **Wait for Assignment**: Don't start until assigned
4. **Star the Repository** ⭐ (Click the star button at the top right)
5. **Make Changes & Submit PR**: Follow our guidelines

### 🌟 Why Star?

**Before your PR can be merged, you must star this repository.**

This requirement:
- Verifies you're a human contributor (not a bot/spam account)
- Shows your support for the project
- Makes you part of our team shaping this repo's future
- Helps us grow and maintain the project

**We consider stargazers as part of our contributor team!**

### Need Help?

If you need help getting started:
1. Comment on the issue you're interested in
2. Check existing PRs for examples
3. Read the [discord.py Guide](https://discordpy.readthedocs.io/)

---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀