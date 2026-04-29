<div align="center">
  <br>
  <p>
    <img src="https://raw.githubusercontent.com/python-discord/branding/main/logos/logo_python/python-logo.png" alt="Python" width="150" />
  </p>
  <h1>🤖 PN Bot</h1>
  <p>Beginner-friendly Discord bot built with the latest <strong>discord.py</strong> — featuring prefix commands, slash commands, and event handlers</p>
  <br>
  <p>
    <img src="https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python" alt="Python Version" />
    <img src="https://img.shields.io/badge/discord.py-2.3+-7289DA?style=flat-square&logo=discord" alt="Discord.py Version" />
    <img src="https://img.shields.io/github/license/IN3PIRE/pn?style=flat-square&color=green" alt="License" />
    <img src="https://img.shields.io/github/stars/IN3PIRE/pn?style=flat-square&color=yellow" alt="Stars" />
  </p>
  <p>
    <a href="#-quick-start">⚡ Quick Start</a> •
    <a href="#-commands--events">🎯 Commands</a> •
    <a href="#-contributing">🤝 Contribute</a> •
    <a href="#-license">📜 License</a>
  </p>
</div>

---

## ✨ Features

- 🎮 **Prefix Commands** – Classic `!ping` style commands for quick testing and familiar usage
- ⚡ **Slash Commands** – Modern, discoverable commands powered by Discord's Interaction API
- 📡 **Event Handlers** – React to Discord events like `on_message`, `on_ready`, `on_member_join`, and more
- 📝 **Fully Typed** – Utilizes Python type hints for better IDE support, autocomplete, and code readability
- 🐳 **Docker Ready** – Includes a minimal Dockerfile for containerized deployment
- 🔄 **GitHub Actions CI** – Automated testing and deployment workflow included
- 🚀 **Production-Ready** – Robust error handling and logging built-in
- 📦 **Minimal Dependencies** – Lightweight with only essential packages

## 🛠️ Tech Stack

- [Python](https://www.python.org/) 3.8+ - Programming language
- [discord.py](https://discordpy.readthedocs.io/) 2.3+ - Discord API wrapper
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- [Docker](https://www.docker.com/) - Containerization (optional)

---

## ⚡ Quick Start

### 📋 Prerequisites

- Python 3.8 or higher
- A Discord bot token ([Create one here](https://discord.com/developers/applications))
- Git (for cloning the repository)

### 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/IN3PIRE/pn.git
cd pn

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Linux/macOS:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install discord.py
pip install -U discord.py python-dotenv
```

### 🔧 Configuration

1. Rename `.env.example` to `.env`
2. Replace `YOUR_BOT_TOKEN` with your bot token
3. (Optional) Configure other variables as needed

```bash
# On Linux/macOS:
cp .env.example .env

# On Windows:
copy .env.example .env
```

### ▶️ Run the Bot

```bash
python bot.py
```

---

## 🎯 Commands & Events

### 🎮 Prefix Commands

Classic command style using `!` prefix:

```python
@bot.command()
async def ping(ctx):
    """Simple ping command to check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! {latency}ms')
```

### ⚡ Slash Commands

Modern Discord interactions:

```python
@bot.tree.command(name='hello', description='Say hello to someone')
async def hello(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'Hello, {name}! 👋')
```

### 📡 Event Handlers

Respond to Discord events:

```python
@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')
    print(f'📊 Connected to {len(bot.guilds)} guilds')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'hello' in message.content.lower():
        await message.reply('Hello there! 👋')
    
    await bot.process_commands(message)
```

---

## 📁 Project Structure

```
pn/
├── bot.py                      # Main bot file
├── cogs/                       # Command modules (optional)
│   └── example.py
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Docker configuration
├── LICENSE                    # MIT License
├── README.md                  # Documentation
├── requirements.txt           # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml             # GitHub Actions workflow
```

---

## 🤝 Contributing

We welcome contributions! Please see our detailed [Contributing Guide](CONTRIBUTING.md) for:

- 🌟 **Star Requirement**: Must star repo before PR merge
- 📝 Step-by-step contribution process
- ✅ Code standards and best practices
- 🏷️ Issue labels and assignment process
- 🧪 Testing guidelines

### 🚀 Quick Contributing Steps

1. **⭐ Star the repository** (click the star button at the top-right) - **Required for PR merge**
2. **Find an issue**: Look for `good first issue` or `help wanted` labels
3. **Comment**: Say "I would like to work on this" on the issue
4. **Wait for assignment**: Don't start until officially assigned
5. **Fork & branch**: Create a feature branch (`feature/amazing-feature`)
6. **Code & test**: Follow our coding standards
7. **Submit PR**: Fill out the PR template completely

### 🏷️ Issue Labels

- `good first issue` - Perfect for newcomers
- `help wanted` - Extra attention needed
- `bug` - Something isn't working correctly
- `enhancement` - New feature or improvement
- `documentation` - Docs need updating
- `high priority` - Needs immediate attention

### 🌟 Why Star?

**⚠️ IMPORTANT**: You must star this repository before your PR can be merged.

Starring:
- ✨ Shows support for the project
- 👤 Verifies you're a human contributor
- 🫂 Makes you part of our contributor team
- 📈 Helps the project grow and gain visibility
- 🏆 Recognizes you as an active community member

We consider all stargazers as part of our contributor team!

### ❓ Need Help?

1. Comment on any issue you're interested in
2. Check existing PRs for implementation examples
3. Read the [discord.py Guide](https://discordpy.readthedocs.io/)
4. Join our discussions or create a new issue

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Support

If you find this project helpful, please consider giving it a ⭐ star on GitHub!

<div align="center">
  <br>
  <p>Made with ❤️ and ☕ by the IN3PIRE Team</p>
  <p>
    <a href="https://github.com/IN3PIRE">View our other projects</a> •
    <a href="https://discord.gg">Join our Discord community</a>
  </p>
  <p>
    <strong>Happy coding! 🚀</strong>
  </p>
</div>
