# Contributing to PN Bot

Thank you for your interest in contributing to PN Bot! This guide will help you get started and ensure your contributions meet our standards.

## 🌟 Star Requirement

**Before we merge your pull request, you must star this repository.**

This requirement serves two important purposes:
1. **Verification**: Confirms you're a human contributor, not a bot or spam account
2. **Support**: Shows your appreciation for the work and helps grow our community

We consider stargazers as part of our team helping shape this repository's future.

## 📝 How to Contribute

### 1. Find an Issue

- Browse our [Issues](https://github.com/IN3PIRE/pn/issues) tab
- Look for issues labeled `good first issue` if you're new to open source
- Comment "I would like to work on this" on the issue you'd like to tackle
- Wait for assignment before starting work

### 2. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/pn.git
cd pn
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 4. Make Your Changes

- Follow our code standards (see below)
- Test your changes thoroughly
- Update documentation if needed
- Ensure no console errors or warnings

### 5. Star the Repository

**Before submitting your PR:**
- Go to the main repository: https://github.com/IN3PIRE/pn
- Click the ⭐ "Star" button at the top right
- This is **mandatory** for PR consideration

### 6. Submit Pull Request

```bash
git add .
git commit -m "feat: add amazing new feature"
git push origin feature/your-feature-name
```

Then create a pull request on GitHub. Our team will review it promptly.

## ✅ Code Standards

### General Requirements

- **Use discord.py v2.3.2+ patterns** - No deprecated methods
- **Follow existing code style** - Match indentation and formatting (4 spaces)
- **Add type hints** - All functions must have proper type annotations
- **Add docstrings** - Follow Google style or reStructuredText format
- **Test your code** - No errors in console, commands work as expected
- **Handle errors gracefully** - Try/except blocks where appropriate

### Command Structure

**Prefix Commands:**
```python
import discord
from discord.ext import commands

class CommandName(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name='commandname')
    async def command_name(self, ctx: commands.Context) -> None:
        """Brief description here."""
        # Command logic here
        await ctx.send('Response')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandName(bot))
```

**Slash Commands:**
```python
@bot.tree.command(name='commandname', description='Description here')
async def command_name(interaction: discord.Interaction) -> None:
    """Brief description here."""
    # Command logic here
    await interaction.response.send_message('Response')
```

### Type Hints Required

All functions must include type hints:
```python
async def command(self, ctx: commands.Context, argument: str) -> None:
    pass
```

## 🚫 What Not to Do

- ❌ Don't submit PRs for issues you weren't assigned
- ❌ Don't include unrelated changes in a single PR
- ❌ Don't commit `__pycache__`, `.venv`, `.env`, or IDE files
- ❌ Don't use blocking operations (use async/await)
- ❌ Don't ignore error handling
- ❌ Don't use `print()` for logging (use `logging` module)

## 🏷️ Issue Labels

- `good first issue` - Perfect for newcomers
- `help wanted` - Extra attention needed
- `enhancement` - New features or improvements
- `bug` - Something isn't working
- `documentation` - Improvements to docs

## ❓ Questions?

If you need help:
1. Comment on the issue you're working on
2. Check existing PRs for examples
3. Review the [discord.py Guide](https://discordpy.readthedocs.io/)

## 🎉 Recognition

Contributors who actively participate and star the repo will be recognized in our README and release notes. We value every contribution, from code to documentation to bug reports.

Thank you for helping make this project better! ⭐